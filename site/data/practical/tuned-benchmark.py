"""Pinned Windows GMP measurements, including native preallocated batch loops.

Run only on Windows x64. No installed binary is changed. CPU-vector overrides,
affinity and every allocated GMP value are restored/released in this process.
The explicit x64 wrappers do no arithmetic: they repeatedly call a passed GMP
function, eliminating Python/ctypes transitions inside a timed native batch.
"""
from __future__ import annotations
import csv, ctypes as C, gc, hashlib, json, math, os, platform, random, re
import statistics as st, struct, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
DEPS=HERE.parent/'benchmark-deps'
sys.path.insert(0,str(DEPS))
import gmpy2

BITS=[256,1024,4096,16384,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216]
PAIRS=3; ROUNDS=7; TARGET=0.020; SEED=10944702026
DLLPATH=DEPS/'gmpy2.libs/libgmp-10.dll'
assert os.name=='nt' and C.sizeof(C.c_void_p)==8
gmp=C.CDLL(str(DLLPATH))
kernel=C.WinDLL('kernel32',use_last_error=True)
u64=C.c_uint64; sz=C.c_size_t; void=C.c_void_p

class MPZ(C.Structure):
    _fields_=[('alloc',C.c_int),('size',C.c_int),('limbs',C.POINTER(u64))]
ZP=C.POINTER(MPZ)
def bind(name,args,ret=None):
    f=getattr(gmp,name);f.argtypes=args;f.restype=ret;return f
init=bind('__gmpz_init2',[ZP,C.c_ulong])
clear=bind('__gmpz_clear',[ZP])
imp=bind('__gmpz_import',[ZP,sz,C.c_int,sz,C.c_int,sz,void])
mulz=bind('__gmpz_mul',[ZP,ZP,ZP])
muln=bind('__gmpn_mul_n',[void,void,void,C.c_long])
addn=bind('__gmpn_add_n',[void,void,void,C.c_long],u64)
mul1=bind('__gmpn_mul_1',[void,void,C.c_long,u64],u64)

# Windows x64 ABI. repeat3(fn,out,a,b,count): preserve five nonvolatile
# registers; 32-byte caller shadow space; stack 16-byte aligned at each CALL.
# count is loaded from original [rsp+40] before changing the stack.
REPEAT3_ASM='''mov rax,[rsp+40]; push rbx; push rbp; push rsi; push rdi;
push r12; sub rsp,32; mov rbx,rax; mov r12,rcx; mov rdi,rdx;
mov rsi,r8; mov rbp,r9; loop: mov rcx,rdi; mov rdx,rsi;
mov r8,rbp; call r12; dec rbx; jnz loop; add rsp,32;
pop r12; pop rdi; pop rsi; pop rbp; pop rbx; ret'''
REPEAT3=bytes.fromhex('488b4424285355565741544883ec204889c34989cc4889d74c89c64c89cd4889f94889f24989e841ffd448ffcb75ef4883c420415c5f5e5d5bc3')
# repeat4(fn,out,a,b,n,count), n from original [rsp+40], count [rsp+48].
# Six saved registers require 40 bytes (shadow + alignment) before CALL.
REPEAT4_ASM='''mov r10,[rsp+40]; mov r11,[rsp+48]; push rbx; push rbp;
push rsi; push rdi; push r12; push r13; sub rsp,40; mov rbx,r11;
mov r13,r10; mov r12,rcx; mov rdi,rdx; mov rsi,r8; mov rbp,r9;
loop: mov rcx,rdi; mov rdx,rsi; mov r8,rbp; mov r9,r13;
call r12; dec rbx; jnz loop; add rsp,40; pop r13; pop r12;
pop rdi; pop rsi; pop rbp; pop rbx; ret'''
REPEAT4=bytes.fromhex('4c8b5424284c8b5c243053555657415441554883ec284c89db4d89d54989cc4889d74c89c64c89cd4889f94889f24989e84d89e941ffd448ffcb75ec4883c428415d415c5f5e5d5bc3')
kernel.VirtualAlloc.argtypes=[void,sz,C.c_ulong,C.c_ulong];kernel.VirtualAlloc.restype=void
kernel.VirtualProtect.argtypes=[void,sz,C.c_ulong,C.POINTER(C.c_ulong)];kernel.VirtualProtect.restype=C.c_int
kernel.VirtualFree.argtypes=[void,sz,C.c_ulong];kernel.VirtualFree.restype=C.c_int
blocks=[]
def executable(code,signature):
    address=kernel.VirtualAlloc(None,len(code),0x3000,4)
    if not address:raise C.WinError(C.get_last_error())
    blocks.append(address); C.memmove(address,code,len(code));old=C.c_ulong()
    if not kernel.VirtualProtect(address,len(code),0x20,C.byref(old)):raise C.WinError(C.get_last_error())
    return signature(address)
repeat3=executable(REPEAT3,C.CFUNCTYPE(None,void,void,void,void,u64))
repeat4=executable(REPEAT4,C.CFUNCTYPE(None,void,void,void,void,u64,u64))

# Test wrapper argument passing and exact call count independently of GMP.
counter=C.c_uint64(); seen=[]
@C.CFUNCTYPE(None,void,void,void)
def callback3(a,b,c):
    counter.value+=1;seen.append((a,b,c))
repeat3(callback3,11,22,33,17)
assert counter.value==17 and set(seen)=={(11,22,33)}
seen.clear();counter.value=0
@C.CFUNCTYPE(None,void,void,void,u64)
def callback4(a,b,c,n):
    counter.value+=1;seen.append((a,b,c,n))
repeat4(callback4,11,22,33,44,19)
assert counter.value==19 and set(seen)=={(11,22,33,44)}

names=json.loads((HERE/'tuned-gmp-exports.json').read_text())['exports']
addr={}
for name in names:
    try:addr.setdefault(C.cast(getattr(gmp,name),void).value,[]).append(name)
    except AttributeError:pass
source=(HERE/'tuned-sources/gmp-impl.h').read_text()
source=source[source.index('struct cpuvec_t {'):];source=source[:source.index('};')]
fields=re.findall(r'\(\*([a-zA-Z_0-9]+)\)',source)
thresholds=['mul_toom22_threshold','mul_toom33_threshold','sqr_toom2_threshold','sqr_toom3_threshold','bmod_1_to_mod_1_threshold']
# GMP's Win64 mp_size_t is signed long (32 bits), unlike its 64-bit limbs.
class CPUVec(C.Structure):
    _fields_=[(f,void) for f in fields]+[(f,C.c_long) for f in thresholds]
assert len(fields)==37 and C.sizeof(C.c_long)==4
gmp.__gmpn_cpuvec_init()
vector=CPUVec.in_dll(gmp,'__gmpn_cpuvec')
original=C.string_at(C.addressof(vector),C.sizeof(vector))
def capture():
    return {'selected_function_symbols':{f:addr.get(getattr(vector,f),['unmatched']) for f in fields},
            'dynamic_thresholds_limbs':{f:getattr(vector,f) for f in thresholds}}
default=capture()
# A deliberately labelled compatible profile, not an upstream Tiger-Lake build.
# Match the source's core2 -> Nehalem -> Sandy Bridge -> Haswell -> Broadwell
# setup order. Only exported routine implementations are used, and threshold
# values come from the supplied GMP 6.3.0 Broadwell machine header.
for suffix in ['core2','coreinhm','coreisbr','coreihwl','coreibwl']:
    for field in fields:
        name='__gmpn_'+field+'_'+suffix
        if name in names:setattr(vector,field,C.cast(getattr(gmp,name),void).value)
header=(HERE/'tuned-sources/mpn/x86_64/coreibwl/gmp-mparam.h').read_text()
for field in thresholds:
    m=re.search(r'^#define\s+'+field.upper()+r'\s+(\d+)\s*$',header,re.M)
    if m:setattr(vector,field,int(m[1]))
profile_bytes=C.string_at(C.addressof(vector),C.sizeof(vector));profile=capture()
def select(which):C.memmove(C.addressof(vector),original if which=='default' else profile_bytes,len(original))
select('default')

cpuid=bind('__gmpn_cpuid',[void,C.c_int],C.c_long)
buf=C.create_string_buffer(49); fms=cpuid(buf,1)&0xffffffff
buf7=C.create_string_buffer(49); cpuid(buf7,7)
ebx=int.from_bytes(buf7.raw[:4],'little')
assert all(ebx&(1<<bit) for bit in [5,8,19]),'Broadwell profile requires AVX2, BMI2 and ADX'
cpuid_data={'family':(fms>>8)&15,'model':((fms>>4)&15)|((fms>>12)&240),'stepping':fms&15,
            'leaf1_eax_hex':hex(fms),'leaf7_ebx_hex':hex(ebx),'AVX2':bool(ebx&(1<<5)),'BMI2':bool(ebx&(1<<8)),'ADX':bool(ebx&(1<<19))}

kernel.GetCurrentProcess.restype=void
kernel.GetProcessAffinityMask.argtypes=[void,C.POINTER(sz),C.POINTER(sz)];kernel.GetProcessAffinityMask.restype=C.c_int
kernel.SetProcessAffinityMask.argtypes=[void,sz];kernel.SetProcessAffinityMask.restype=C.c_int
proc=kernel.GetCurrentProcess(); oldaff=sz();sysaff=sz()
if not kernel.GetProcessAffinityMask(proc,C.byref(oldaff),C.byref(sysaff)):raise C.WinError(C.get_last_error())
# Logical CPU2 avoids choosing the first logical CPU by default. No assumption
# is made that this is an otherwise idle core or that frequency is fixed.
choices=[i for i in range(64) if oldaff.value&(1<<i)]
chosen=choices[min(2,len(choices)-1)]; pinned=1<<chosen
if not kernel.SetProcessAffinityMask(proc,pinned):raise C.WinError(C.get_last_error())

rng=random.Random(SEED); cases=[]; allocated=[]
def make_mpz(x,bits):
    z=MPZ();init(C.byref(z),bits);allocated.append(z)
    b=x.to_bytes((bits+7)//8,'little'); storage=C.create_string_buffer(b)
    imp(C.byref(z),len(b),-1,1,0,0,storage)
    assert z.size==(bits+63)//64
    return z
def check(case,method):
    z=case['r']; length=2*case['limbs']*8
    actual=C.string_at(z.limbs,length)
    assert actual==case['expected_bytes'],(case['bits'],method)
def invoke(case,method,count):
    assert count>0
    if method=='native_mpz_reuse':
        repeat3(mulz,C.byref(case['r']),C.byref(case['a']),C.byref(case['b']),count)
    elif method=='native_mpn_preallocated':
        repeat4(muln,case['r'].limbs,case['a'].limbs,case['b'].limbs,case['limbs'],count)
    else:
        a,b=case['ga'],case['gb'];out=None
        for _ in range(count):out=a*b
        case['last_gmpy2']=out
def timed(case,method,count):
    a=time.perf_counter_ns();c=time.process_time_ns()
    invoke(case,method,count)
    return time.perf_counter_ns()-a,time.process_time_ns()-c

started=datetime.now(timezone.utc).isoformat(); wall_start=time.perf_counter();cpu_start=time.process_time()
gc_on=gc.isenabled();gc.disable(); raw=[]
try:
    for bits in BITS:
        for pair in range(PAIRS):
            a=rng.getrandbits(bits)|(1<<(bits-1));b=rng.getrandbits(bits)|(1<<(bits-1))
            if a==b:b^=1
            expected=a*b # Python's independent multiplier, outside all timers.
            limbs=(bits+63)//64
            z=MPZ();init(C.byref(z),2*limbs*64);allocated.append(z)
            case={'bits':bits,'pair':pair,'limbs':limbs,'a':make_mpz(a,bits),'b':make_mpz(b,bits),'r':z,
                  'ga':gmpy2.mpz(a),'gb':gmpy2.mpz(b),'expected':expected,
                  'expected_bytes':expected.to_bytes(2*limbs*8,'little'),
                  'a_sha256':hashlib.sha256(a.to_bytes((bits+7)//8,'little')).hexdigest(),
                  'b_sha256':hashlib.sha256(b.to_bytes((bits+7)//8,'little')).hexdigest()}
            cases.append(case)
    methods=['native_mpz_reuse','native_mpn_preallocated','gmpy2_allocating']
    configs=[(profile_name,method,c) for profile_name in ['default','compatible_broadwell_profile'] for method in methods for c in cases]
    rng.shuffle(configs);counts={}
    for which,method,c in configs:
        select(which);invoke(c,method,1)
        if method=='gmpy2_allocating':assert int(c['last_gmpy2'])==c['expected']
        else:check(c,method)
        count=1
        while True:
            elapsed,unused=timed(c,method,count)
            if elapsed>=4_000_000 or count>=2_000_000:break
            count*=2
        counts[(which,method,c['bits'],c['pair'])]=max(1,min(2_000_000,int(TARGET*1e9/(elapsed/count))))
    for round_id in range(ROUNDS):
        rng.shuffle(configs)
        for which,method,c in configs:
            select(which);count=counts[(which,method,c['bits'],c['pair'])]
            wall,cpu=timed(c,method,count)
            if method=='gmpy2_allocating':assert int(c['last_gmpy2'])==c['expected']
            else:check(c,method)
            raw.append({'profile':which,'method':method,'input_bits_each':c['bits'],'operand_pair':c['pair'],
                        'round':round_id,'iterations':count,'wall_ns':wall,'process_cpu_ns':cpu,
                        'ns_per_multiplication':wall/count,'cpu_ns_per_multiplication':cpu/count})
        print(json.dumps({'round_complete':round_id+1,'of':ROUNDS,'wall_seconds':time.perf_counter()-wall_start}),flush=True)
finally:
    select('default')
    affinity_restored=bool(kernel.SetProcessAffinityMask(proc,oldaff.value))
    for z in allocated:clear(C.byref(z))
    for block in blocks:kernel.VirtualFree(block,0,0x8000)
    if gc_on:gc.enable()

rows=[]
for which in ['default','compatible_broadwell_profile']:
    for method in methods:
        for bits in BITS:
            samples=[s for s in raw if s['profile']==which and s['method']==method and s['input_bits_each']==bits]
            values=[s['ns_per_multiplication'] for s in samples];q=st.quantiles(values,n=4,method='inclusive')
            rows.append({'profile':which,'method':method,'input_bits_each':bits,'samples':len(values),
                         'independent_operand_pairs':PAIRS,'median_ns':st.median(values),'q25_ns':q[0],'q75_ns':q[2],
                         'min_ns':min(values),'max_ns':max(values),'median_cpu_ns':st.median(s['cpu_ns_per_multiplication'] for s in samples),
                         'observed_pair_medians_ns':{str(pair):st.median(s['ns_per_multiplication'] for s in samples if s['operand_pair']==pair) for pair in range(PAIRS)},
                         'median_ns_divided_by_n_log2_n':st.median(values)/(bits*math.log2(bits))})
compiler_strings=sorted(set(x.decode() for x in re.findall(rb'[ -~]{7,}',DLLPATH.read_bytes()) if x.startswith(b'GCC: ')))
cpu=json.loads(subprocess.run(['powershell','-NoProfile','-NonInteractive','-Command','Get-CimInstance Win32_Processor | Select-Object Name,Manufacturer,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed | ConvertTo-Json -Compress'],capture_output=True,text=True,check=True).stdout)
out={'schema_version':1,'kind':'measured_actual_GMP_baseline_not_crossover','recorded_at_utc':datetime.now(timezone.utc).isoformat(),
     'started_at_utc':started,'environment':{'python':sys.version,'platform':platform.platform(),'cpu':cpu,'cpuid':cpuid_data,
     'gmp_version':C.c_char_p.in_dll(gmp,'__gmp_version').value.decode(),'gmpy2_version':gmpy2.version(),'limb_bits':gmpy2.mp_limbsize(),
     'gmp_dll_path':str(DLLPATH),'gmp_dll_sha256':hashlib.sha256(DLLPATH.read_bytes()).hexdigest(),
     'embedded_compiler_strings':compiler_strings,'full_build_flags':'Not distributed in wheel; compiler string is evidence, not complete build provenance.',
     'original_process_affinity_mask':oldaff.value,'benchmark_logical_processor':chosen,'affinity_restored':affinity_restored,
     'process_priority':'default','power_frequency_thermals':'not controlled; no fixed-clock claim','background_work':'not controlled'},
     'profiles':{'default':default,'compatible_broadwell_profile':profile},
     'profile_interpretation':'Default is the actual installed DLL dispatch. Alternate is a process-local compatible exported-kernel/threshold profile, not a rebuilt or optimally tuned Tiger Lake library. No installed file changes.',
     'method':{'input_bits_each':BITS,'independent_operand_pairs_per_size':PAIRS,'rounds':ROUNDS,'seed':SEED,'target_seconds_per_batch':TARGET,
     'sampling_order':'Seeded shuffle of sizes, methods, profiles and operand pairs within every round; repeated hot operands inside each batch.',
     'validation':'Every operand pair independently multiplied by Python int outside timers; each timed batch final full product checked outside timer.',
     'native_mpz_reuse':'Native x64 loop calls __gmpz_mul into a preinitialized sufficiently allocated result. Inputs/import/conversion excluded. GMP internal scratch allocation remains included.',
     'native_mpn_preallocated':'Native x64 loop calls __gmpn_mul_n with preallocated result limbs. Inputs distinct, positive, exact stated bit length, not squaring. GMP internal scratch allocation remains included.',
     'gmpy2_allocating':'Serial Python loop a*b; includes Python iteration/binding and result allocation/release. Input conversion and correctness excluded.',
     'native_batch_overhead':'Includes one indirect call, loop decrement/branch and argument moves per GMP call; no per-product Python or ctypes crossing. No subtraction of estimated overhead.',
     'native_wrapper_tests':'repeat3 callback 17 calls and repeat4 callback 19 calls with exact arguments; full product validation on all cases/profiles/methods.',
     'native_wrapper_asm':{'repeat3':REPEAT3_ASM,'repeat4':REPEAT4_ASM,'repeat3_hex':REPEAT3.hex(),'repeat4_hex':REPEAT4.hex()},
     'gc':'disabled during benchmark; restored','cache':'hot repeated operands/code within batch; cache state between batches uncontrolled',
     'scope':'Finite machine/installation measurements, not rigorous runtime bounds, not an asymptotic fit, not an executable PR4470 comparison.'},
     'wall_seconds':time.perf_counter()-wall_start,'process_cpu_seconds':time.process_time()-cpu_start,
     'rows':rows,'raw_samples':raw,'operand_hashes':[{'bits':c['bits'],'pair':c['pair'],'a_sha256':c['a_sha256'],'b_sha256':c['b_sha256']} for c in cases],
     'official_sources':['https://gmplib.org/','https://gmplib.org/manual/Build-Options','https://gmplib.org/manual/FFT-Multiplication','https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz'],
     'PR4470_measured_runtime':None,'empirical_PR4470_crossover':None,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'tuned-practical-baseline.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
with (HERE/'tuned-practical-baseline.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=[k for k in rows[0] if k!='observed_pair_medians_ns']);writer.writeheader()
    writer.writerows({k:v for k,v in r.items() if k!='observed_pair_medians_ns'} for r in rows)
print(json.dumps({'output':'tuned-practical-baseline.json','rows':len(rows),'raw_samples':len(raw),'wall_seconds':out['wall_seconds'],'cpu_seconds':out['process_cpu_seconds']}),flush=True)
