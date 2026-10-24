"""Reproduce DLL export/build/dispatch and installed-ABI evidence; no file edits to GMP."""
import ctypes as C, hashlib, json, re, struct, tarfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
DLL=HERE.parent/'benchmark-deps/gmpy2.libs/libgmp-10.dll'
ARCHIVE=HERE.parent/'operation-audit/gmp-6.3.0.tar.xz'
def sha(b):return hashlib.sha256(b).hexdigest()

# Extract only explicitly named source members, with no archive path traversal.
members=['gmp-impl.h','gmp-h.in','configure.ac','mpz/mul.c',
         'mpn/generic/mul_n.c','mpn/x86_64/fat/fat.c','mpn/x86_64/fat/fat_entry.asm',
         'mpn/x86_64/fat/gmp-mparam.h','mpn/x86_64/coreihwl/gmp-mparam.h',
         'mpn/x86_64/coreibwl/gmp-mparam.h','mpn/x86_64/skylake/gmp-mparam.h']
with tarfile.open(ARCHIVE) as archive:
    for member in members:
        data=archive.extractfile('gmp-6.3.0/'+member).read()
        dest=HERE/'tuned-sources'/member;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)

data=DLL.read_bytes();pe=struct.unpack_from('<I',data,0x3c)[0]
nsections=struct.unpack_from('<H',data,pe+6)[0];optsize=struct.unpack_from('<H',data,pe+20)[0]
opt=pe+24;magic=struct.unpack_from('<H',data,opt)[0]
export_rva,export_size=struct.unpack_from('<II',data,opt+(112 if magic==0x20b else 96))
sections=[]
for i in range(nsections):
    off=opt+optsize+40*i;name=data[off:off+8].split(b'\0')[0].decode()
    vsize,va,rsize,rpos=struct.unpack_from('<IIII',data,off+8)
    sections.append((name,va,vsize,rpos,rsize))
def offset(rva):
    for name,va,vsize,rpos,rsize in sections:
        if va<=rva<va+max(vsize,rsize):return rpos+rva-va
    raise ValueError(rva)
def cstring(rva):
    off=offset(rva);return data[off:data.index(0,off)].decode()
export=offset(export_rva)
nfunc,nnames,func_rva,name_rva,ord_rva=struct.unpack_from('<IIIII',data,export+20)
names=[cstring(struct.unpack_from('<I',data,offset(name_rva)+4*i)[0]) for i in range(nnames)]
(HERE/'tuned-gmp-exports.json').write_text(json.dumps({'exports':names,'sections':sections},indent=2)+'\n')
gmp=C.CDLL(str(DLL));gmp.__gmpn_cpuvec_init()
addresses={}
for name in names:
    addresses.setdefault(C.cast(getattr(gmp,name),C.c_void_p).value,[]).append(name)
source=(HERE/'tuned-sources/gmp-impl.h').read_text()
source=source[source.index('struct cpuvec_t {'):];source=source[:source.index('};')]
fields=re.findall(r'\(\*([a-zA-Z_0-9]+)\)',source)
thresholds=['mul_toom22_threshold','mul_toom33_threshold','sqr_toom2_threshold','sqr_toom3_threshold','bmod_1_to_mod_1_threshold']
class CPUVec(C.Structure):_fields_=[(name,C.c_void_p) for name in fields]+[(name,C.c_long) for name in thresholds]
vector=CPUVec.in_dll(gmp,'__gmpn_cpuvec')
dispatch={'selected_function_symbols':{name:addresses.get(getattr(vector,name),['unmatched']) for name in fields},
          'dynamic_thresholds_limbs':{name:getattr(vector,name) for name in thresholds},
          'mp_size_t_bits':32,'source_struct_field_count':len(fields)}
assert dispatch['dynamic_thresholds_limbs']==dict(zip(thresholds,[20,130,30,200,20]))
(HERE/'tuned-dispatch.json').write_text(json.dumps(dispatch,indent=2)+'\n')

class MPZ(C.Structure):_fields_=[('alloc',C.c_int),('size',C.c_int),('limbs',C.POINTER(C.c_uint64))]
gmp.__gmpz_init2.argtypes=[C.POINTER(MPZ),C.c_ulong]
gmp.__gmpz_import.argtypes=[C.POINTER(MPZ),C.c_size_t,C.c_int,C.c_size_t,C.c_int,C.c_size_t,C.c_void_p]
gmp.__gmpz_clear.argtypes=[C.POINTER(MPZ)]
abi_checks=[]
for bits in [1,65,1024]:
    z=MPZ();gmp.__gmpz_init2(C.byref(z),bits)
    value=(1<<(bits-1))+int(bits>1);b=value.to_bytes((bits+7)//8,'little');buf=C.create_string_buffer(b)
    gmp.__gmpz_import(C.byref(z),len(b),-1,1,0,0,buf)
    actual=int.from_bytes(C.string_at(z.limbs,z.size*8),'little')
    assert actual==value and z.size==(bits+63)//64
    abi_checks.append({'input_bits':bits,'observed_alloc_limbs':z.alloc,'observed_size_limbs':z.size,'full_value_matches':actual==value})
    gmp.__gmpz_clear(C.byref(z))
cap=64*((1<<31)-1)
result={'gmp_dll_sha256':sha(data),'gmp_version':C.c_char_p.in_dll(gmp,'__gmp_version').value.decode(),
        'official_source_archive_sha256':sha(ARCHIVE.read_bytes()),
        'official_archive_url':'https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz',
        'sources_sha256':{member:sha((HERE/'tuned-sources'/member).read_bytes()) for member in members},
        'embedded_compiler_strings':sorted(set(s.decode() for s in re.findall(rb'[ -~]{7,}',data) if s.startswith(b'GCC: '))),
        'full_compiler_flags':'Not distributed with wheel; unavailable from __gmp_cc/__gmp_cflags exports.',
        'fat_dispatch_present':all(name in names for name in ['__gmpn_cpuvec','__gmpn_cpuvec_init','__gmpn_add_n_coreihwl']),
        'default_dispatch':dispatch,
        'abi':{'mp_limb_t_bits':64,'C_int_bits':C.sizeof(C.c_int)*8,'C_long_bits':C.sizeof(C.c_long)*8,
               'pointer_bits':C.sizeof(C.c_void_p)*8,'mp_size_t_bits':32,'mp_bitcnt_t_bits':32,
               'mpz_struct_bytes':C.sizeof(MPZ),'mpz_alloc_offset':MPZ.alloc.offset,'mpz_size_offset':MPZ.size.offset,'mpz_limb_pointer_offset':MPZ.limbs.offset,
               'positive_mpz_representation_ceiling_bits':cap,'equal_input_bits_necessary_output_size_ceiling':(cap+1)//2,
               'ceiling_interpretation':'Necessary representation ceiling only, not a guaranteed allocatable or supported size; installation/ABI-specific. Full product output must also fit. mpn length is Windows long32 here, not universal ptrdiff_t64.',
               'runtime_struct_checks':abi_checks}}
(HERE/'tuned-installation-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'version':result['gmp_version'],'ABI':result['abi'],'dispatch_thresholds':dispatch['dynamic_thresholds_limbs']},indent=2))
