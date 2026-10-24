"""Fresh own-source T21/T37 role, geometry, finite-invoice workbench.

Original source modules are loaded read-only from pinned flat caches. Common
I/O is injected so their constructors/checkers can consume verified primary
inputs and freshly generated objects without rebuilding unrelated ancestry.
"""
from pathlib import Path
from types import SimpleNamespace
from fractions import Fraction as F
from collections import Counter
import ast,copy,gzip,hashlib,json,sys
import io,tokenize
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'t21-t37-cost-source';O=R/'older-reviewed-source'
checks={}
def ck(n,v):assert v,n;checks[n]=True
def hs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def identity(o):return hashlib.sha256(canonical(o)).hexdigest()
def portable(o):
    b=bytearray(gzip.compress(canonical(o),mtime=0));b[9]=255;return bytes(b)
manifest=json.loads((S/'manifest.json').read_text())
source={x['path']:S/x['file'] for x in manifest if 'error' not in x}
for x in manifest:
    if 'error' not in x:ck('source_'+x['path'],hs(S/x['file'])==x['sha256'])
for pr in [535,799,890,942]:
    for x in json.loads((O/f'{pr}-manifest.json').read_text()):source.setdefault(x['path'],O/x['file'])
VIRTUAL={};VBYTES={};modules={};used_primary={}
def key(p):return Path(p).as_posix().lstrip('./')
def read(p):
    k=key(p)
    if k in VIRTUAL:return copy.deepcopy(VIRTUAL[k])
    q=source[k] if k in source else Path(p)
    if q.is_relative_to(R):used_primary[q.relative_to(R).as_posix()]=hs(q)
    b=q.read_bytes();return json.loads(gzip.decompress(b) if q.suffix=='.gz' else b)
def sha(p):
    k=key(p)
    if k in VBYTES:return hashlib.sha256(VBYTES[k]).hexdigest()
    return hs(source[k] if k in source else Path(p))
def require(v,n):
    if not v:raise ValueError(n)
def register(p,obj,compress=False):
    k=key(p);VIRTUAL[k]=copy.deepcopy(obj)
    VBYTES[k]=portable(obj) if compress else (json.dumps(obj,indent=2)+'\n').encode()
def dump(p,obj):register(p,obj)
def write_gzip(p,obj):register(p,obj,True)
def load(p,name='source_module'):
    k=key(p)
    if k in modules:return modules[k]
    q=source[k];tree=ast.parse(q.read_text(encoding='utf8'))
    used_primary[q.relative_to(R).as_posix()]=hs(q)
    # Original relative-file I/O resolves against this source package's logical
    # namespace. Mathematical constructors and assertions are unchanged.
    tree.body=[n for n in tree.body if not(isinstance(n,ast.ImportFrom) and n.module=='common')]
    package=Path('research/complex-t21-owners') if k.startswith('research/complex-t21-owners/') else Path('research/complex-t37-owners')
    ns=dict(__name__=name,__file__=str(q),HERE=package,ROOT=Path('.'),P=package,T21=Path('research/complex-t21-owners'),read=read,sha=sha,require=require,identity=identity,dump=dump,write_gzip=write_gzip,load=load)
    exec(compile(tree,str(q),'exec'),ns)
    m=SimpleNamespace(**ns);modules[k]=m;return m

# Capture the actual canonical native object inside the already authenticated
# frozen U8 reconstruction. No old certificate outputs are executed/written.
u8=R/'u8_selected_native_recovery.py';nodes=[]
for n in ast.parse(u8.read_text()).body:
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='deps' for t in n.targets):break
    if isinstance(n,ast.With) and any(isinstance(i.context_expr,ast.Call) and isinstance(i.context_expr.func,ast.Attribute) and i.context_expr.func.attr=='TemporaryDirectory' for i in n.items):
        n.body+=ast.parse("captured_canonical=read(out/'CANONICAL-WORD.json.gz')").body
    nodes.append(n)
native={'__name__':'own_u8_numeric_input','__file__':str(u8)}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(u8),'exec'),native)
print('PASS selected U8 source recovery',flush=True)
word=native['captured_canonical'];programs=native['programs'];localchecks=native['local']
spec21=read('research/complex-t21-owners/data/SPEC.json');claim21=read('research/complex-t21-owners/data/CLAIM.json')
contract=spec21['providers']['gauge44']['complete_contract']
ck('own_selected_u8_input',identity(programs)==spec21['providers']['gauge44']['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz'])

T21=Path('research/complex-t21-owners');T37=Path('research/complex-t37-owners')
ownersmod=load(T21/'build_owners.py','own_t21_owner_constructor')
planpath=Path('research/gauge44-frames-x/data/PLAN.json');ownerpath=Path('research/gauge44-frames-x/data/OWNERS.json.gz')
roles21,order21,details21=ownersmod.construct(planpath,ownerpath)
print('PASS T21 exact owner constructor',flush=True)
ck('own_t21_owner_semantic_pin',identity(roles21)==spec21['data']['owners_content_sha256'])
ck('own_t21_owner_compressed_pin',hashlib.sha256(portable(roles21)).hexdigest()==spec21['data']['owners_sha256'])
ck('own_t21_call_order',order21==spec21['call_order'] and len(roles21)==95256)

# This primary immutable template is a geometry fixture. Its literal schedule
# is independently checked against the selected PR799 PLAN's physical windows.
proto=read('research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz')
basecanonical=read('research/community-k492-audit/pr622/replay/baseline558/complex-global/base/split-centres/CANONICAL-WORD.json.gz')
phases=read('research/community-k492-audit/pr622/replay/baseline558/complex-global/base/work/complex-nine-native/DATA-PHASES.json')
windowmod=load(T21/'vendor/pr870/t16/build_parent.py','own_actual_source_windows')
plan8=read(planpath)
ck('geometry_fixture_matches_selected_t8_windows',windowmod.actual_windows(proto,plan8['order'])[0]==plan8['windows'])
ck('native_source_port_order',word['ports']==basecanonical['ports'])
ck('geometry_fixture_stock_and_schedule',proto['m']==73 and proto['live']==11704 and proto['physical']==12218 and len(proto['execution_schedule'])==32)
ck('geometry_fixture_exact_data_phase_source',proto['exact_data_phase_recipe_sha256']==sha('research/community-k492-audit/pr622/replay/baseline558/complex-global/base/work/complex-nine-native/DATA-PHASES.json'))
liftmod=load(T21/'build_parent.py','own_t21_bank_constructor')
parent21=liftmod.lift(proto)
parentcheck=load(T21/'check_parent.py','independent_t21_bank_checker')
bank21=parentcheck.audit(proto,parent21)
bank_controls21=parentcheck.controls(proto,parent21)
print('PASS T21 partial bank envelope and controls',flush=True)
ck('own_t21_partial_bank_checks',bank21['calls']==189 and bank21['bank_families']==13608 and len(bank_controls21)==8)
windows21,schedule21=windowmod.actual_windows(parent21,order21)
ck('own_t21_source_window_membership',all(r['time'] in windows21[f"{r['owner_replica']},{r['child']}"][1] for r in roles21))

# Reconstruct a new numeric projection of the native endpoint/prefix evidence.
# It is explicitly not an impersonation of a historical phase replay receipt.
numeric_replay={'paid_profiles':{k:v['paid_profile'] for k,v in localchecks.items()},'local':{k:{'prefix_bits_upper':v['prefix_bits'],'prefix_l1_upper':v['prefix_l1']} for k,v in contract['local'].items()}}
independent=load(T21/'independent_check.py','independent_t21_whole_roles')
ck('native_and_baseline_ordered_centre_interface',len(word['center_frames'])==len(basecanonical['center_frames'])==8 and [independent.basis(word['frames'][f]) for f in word['center_frames']]==[independent.basis(basecanonical['frames'][f]) for f in basecanonical['center_frames']])
independent.EXPECTED_IDLE={48:6292,3:1,1:3}
# Functions retain their module global namespace, so modify that namespace too.
independent.make_context.__globals__['EXPECTED_IDLE']=independent.EXPECTED_IDLE
context21=independent.make_context(proto,phases,basecanonical['ports'],word,numeric_replay,roles21)
role21=independent.check_roles(context21,roles21)
controls21=independent.controls(context21,roles21)
omitted21=[]
index21={(r['time'],r['helper']):i for i,r in enumerate(roles21)}
for edit in read(T21/'data/EDITS.json'):
    bad=roles21.copy();i=index21[tuple(edit['role'])];r=dict(roles21[i]);r.update(edit['before'])
    owner,child,port=r['owner_replica'],r['child'],r['port']
    r.update(copy=112*owner+port,family=896*owner+112*(2*context21['child_pair'][child]+context21['side'][child])+port);bad[i]=r
    try:independent.check_roles(context21,bad)
    except ValueError as e:omitted21.append(dict(role=edit['role'],reason=str(e)))
    else:raise AssertionError('T21 omitted edit accepted')
ck('own_t21_nine_omitted_edit_controls',len(omitted21)==9)
print('PASS T21 independent whole-role/window/chart audit',flush=True)
ck('own_t21_whole_role_chart_window_recount',role21['roles']==95256 and role21['calls']==189 and role21['prefix_bits']==491 and role21['physical_row_coefficient']==16469 and len(controls21)==6)

# T37's frozen roles are own primary inputs. Check every role directly against
# the physical event windows; constructor provenance is an additional audit,
# not a replacement for the whole-role correctness check.
roles37=read(T37/'OWNERS.json.gz');order37=read(T37/'ORDER.json');claim37=read(T37/'CLAIM.json')
text=source['research/complex-t21-owners/independent_check.py'].read_text()
for a,b,count in [('2 * 512','2 * 1024',1),('prefix < 512','prefix < 1024',1),('charged_prefix_bits=512','charged_prefix_bits=1024',1),('1 <= T <= 22','1 <= T <= 50',1)]:
    ck('own_t37_exact_checker_adaptation_'+a,text.count(a)==count);text=text.replace(a,b)
ns={'__name__':'independent_t37_whole_roles','__file__':str(source['research/complex-t21-owners/independent_check.py'])}
exec(compile(text,'source_T37_1024_adaptation','exec'),ns);ns['T']=37;ns['EXPECTED_IDLE']={48:11086,1:6}
context37=ns['make_context'](proto,phases,basecanonical['ports'],word,numeric_replay,roles37)
role37=ns['check_roles'](context37,roles37);controls37=ns['controls'](context37,roles37)
omitted37=[];index37={(r['stage'],r['replica'],r['helper']):i for i,r in enumerate(roles37)}
for edit in read(T37/'EDITS.json')['edits']:
    bad=roles37.copy();i=index37[tuple(edit['role'])];r=dict(roles37[i]);r.update(edit['before'])
    owner,child,port=r['owner_replica'],r['child'],r['port']
    r.update(copy=112*owner+port,family=896*owner+112*(2*context37['child_pair'][child]+context37['side'][child])+port);bad[i]=r
    try:ns['check_roles'](context37,bad)
    except ValueError as e:omitted37.append(dict(role=edit['role'],reason=str(e)))
    else:raise AssertionError('T37 omitted edit accepted')
ck('own_t37_eight_omitted_edit_controls',len(omitted37)==8)
ck('own_t37_whole_role_chart_window_recount',role37['roles']==167832 and role37['calls']==333 and role37['prefix_bits']==779 and role37['charged_prefix_bits']==1024 and role37['physical_row_coefficient']==17495 and len(controls37)==6)
ck('own_t37_frozen_call_order',[[s,r] for s,r in context37['order']]==order37)

# Exact source-prescribed T37 adaptation of the T21 bank constructor/checker.
# Only numeric token replacements and the documented group tuple change.
prepare=load(T37/'prepare.py','own_t37_literal_adapter')
adapted={}
for filename in ['build_parent.py','check_parent.py']:
    text=source[key(T21/filename)].read_text()
    text=prepare.transform(text)
    if filename=='build_parent.py':
        require(text.count('((48, 11086), (3, 1), (1, 3))')==1,'T37 idle exact adaptation')
        text=text.replace('((48, 11086), (3, 1), (1, 3))','((48, 11086), (1, 6))')
    tree=ast.parse(text);tree.body=[n for n in tree.body if not(isinstance(n,ast.ImportFrom) and n.module=='common')]
    a=dict(__name__='own_t37_'+filename,__file__=str(source[key(T21/filename)]),HERE=T21,ROOT=Path('.'),read=read,sha=sha,require=require,identity=identity,dump=dump,write_gzip=write_gzip,load=load)
    exec(compile(tree,'source_prescribed_T37_'+filename,'exec'),a);adapted[filename]=a
parent37=adapted['build_parent.py']['lift'](proto)
bank37=adapted['check_parent.py']['audit'](proto,parent37)
bank_controls37=adapted['check_parent.py']['controls'](proto,parent37)
ck('own_t37_partial_bank_checks',bank37['calls']==333 and bank37['bank_families']==22680 and len(bank_controls37)==8)
print('PASS T37 five-group bank envelope and controls',flush=True)

# Independently recount the *actual selected* native scalar/Horner/prefix word.
# The full frame/column engines were executed in the U8 recovery above.
counter=ast.parse((R/'pr799_recovered_finite_controller.py').read_text())
counter=next(n for n in counter.body if isinstance(n,ast.For) and isinstance(n.target,ast.Tuple) and [t.id for t in n.target.elts]==['orientation','events'])
provider=spec21['providers']['gauge44'];recount={}
primary_mapping=source
exec(compile(ast.Module(body=[counter],type_ignores=[]),'source_selected_u8_scalar_recount','exec'),globals())
source=primary_mapping
ck('own_u8_scalar_prefix_recount',max(F(r['prefix_l1']) for r in recount.values())<2**72)

group=2**(36*36)
for i in range(1,37):group*=2**(2*i)-1
compiler=64*74**3
localP={int(k):v for k,v in localchecks['forward']['paid_profile'].items()}
children=sum(localP.values());macros=max(r['scalar_macros'] for r in recount.values())
adapters=16*(macros+children+728+8)+64*73
primitive=max(r['real_component_primitives'] for r in recount.values())+adapters*compiler
ck('own_u8_complete_adapter_count',adapters==contract['local_adapters'] and primitive==contract['local_primitive_bound'] and primitive<2**48)
invoices={};numericplans={};rolechecks={890:role21,942:role37}
for pr,T,roles,order,parent,role,claim,payload in [(890,21,roles21,order21,parent21,role21,claim21,512),(942,37,roles37,order37,parent37,role37,claim37,1024)]:
    calls=len(order);live=896*T;physical=live+514
    bystage={c['stage']:c['orientation'] for c in proto['calls']}
    orientation_counts=Counter(bystage[s] for s,r in order)
    selected_real=sum(n*recount[o]['real_component_primitives'] for o,n in orientation_counts.items())
    selected_work=sum(n*recount[o]['coefficient_work_primitives'] for o,n in orientation_counts.items())
    selected_macros=sum(n*recount[o]['scalar_macros'] for o,n in orientation_counts.items())
    wrapper_factors=sum(n*(contract['local'][o]['pre_wrappers']+contract['local'][o]['post_wrappers'])*144 for o,n in orientation_counts.items())
    banks,rem=divmod(parent['live']-live,9)
    parent_idle=sum(c['replicas'] for c in parent['idle_children'])
    windows,schedule=windowmod.actual_windows(parent,order)
    bridges=sum(e['kind']=='bridge' for e in schedule)
    bridge_additions=2*112*bridges;shifts=4*112*T;moves=2*shifts
    nonlocal_items=(4*112*T*9+2*112*T*9+2*calls*504+parent_idle+9*banks+bridge_additions+shifts+moves+parent['live']+parent['physical']+wrapper_factors)
    outside=8*nonlocal_items+64*73
    pervertex=selected_real+bridge_additions+shifts+moves+parent['live']+(calls*adapters+outside)*compiler+64*parent['physical']
    rebased=pervertex+65*(physical-parent['physical'])+(live-parent['live'])
    used=max(pervertex,rebased)
    P={int(k):v for k,v in role['profile'].items()};mass=sum(r*n for r,n in P.items())
    stock=group*physical;streamed=group*mass
    logical=group*used+64;router=compiler*(logical+1)*(stock+1)**2
    literal=2*2**30000*stock**2+8*streamed+4*stock+4+32*73
    row=2*stock.bit_length()+9909+252+2*payload
    ck(str(pr)+'_own_parent_and_final_stock',not rem and banks==504*((T+7)//8) and physical==role['physical'] and live==role['live'] and parent['physical']==parent['live']+514)
    ck(str(pr)+'_actual_complete_calls',calls==9*T and bridges==9*T and sum(orientation_counts.values())==calls)
    ck(str(pr)+'_actual_selected_primitive_and_wrapper_counts',selected_real>0 and wrapper_factors==calls*576*144 and used>0 and used<2**64)
    ck(str(pr)+'_own_profile_binding',P=={int(k):v for k,v in (claim.get('profile') or spec21['expected']['global_profile']).items()} and mass==73*live-320*T)
    ck(str(pr)+'_all_own_finite_constants',logical<2**6050 and router<2**30000 and literal<2**100000 and 32*73*(streamed+2**100000)**2<2**210000 and 2*(streamed+2**100000)+18<2**210000)
    ck(str(pr)+'_own_prefix_and_row_charges',role['prefix_bits']<payload and row==role['physical_row_coefficient']<20161 and role['charged_prefix_bits']==payload)
    ck(str(pr)+'_selected_rank_halving',73**2>2*max(P)**2)
    callledger=[dict(time=t,stage=s,replica=r,orientation=bystage[s],selected_program_sha256=localchecks[bystage[s]]['sha256'],helper_roles=504,local_columns=728) for t,(s,r) in enumerate(order)]
    head={890:'4b3bd8cbe8e3e81c44161017c9b72c905a8040a8',942:'1960cfa919a0945d0ca4cb14ea96237000037903'}[pr]
    numericplans[pr]=dict(schema='own_numeric_realization_plan/1',pr=pr,own_head=head,replicas=T,live=live,physical=physical,order=order,windows=windows,selected_program_semantic_sha256=identity(programs),owners_content_sha256=identity(roles),profile=P,complete_calls=callledger,parent_geometry_content_sha256=identity(parent),historical_PLAN_byte_identity_claimed=False,parent_geometry_scope='Fresh source-constructed numeric envelope from independently window-matched primary geometry fixture; not a claim of historical parent/PLAN metadata byte identity.')
    # JSON objects have string keys. Canonicalize the public receipt in its
    # serialized type system before hashing it, so offline parse/hash agrees.
    numericplans[pr]=json.loads(json.dumps(numericplans[pr]))
    invoices[pr]=dict(schema='own_complete_finite_invoice/1',pr=pr,replicas=T,calls=calls,live=live,physical=physical,parent_live=parent['live'],parent_physical=parent['physical'],parent_banks_per_stage=banks,source_idle_children_charged=parent_idle,actual_bridge_sweeps=bridges,orientation_counts=dict(orientation_counts),selected_real_component_primitives=selected_real,selected_coefficient_work_primitives=selected_work,selected_scalar_macros=selected_macros,wrapper_elementary_factors=wrapper_factors,local_adapters=adapters,local_primitive_bound=primitive,compiler=compiler,nonlocal_items=nonlocal_items,outside=outside,unhosted_pervertex=pervertex,hosted_rebased_pervertex=rebased,conservative_pervertex_used=used,retained_previous_invoice=None,physical_stock_bits=stock.bit_length(),router_bits=router.bit_length(),literal_bits=literal.bit_length(),source_G_upper='2^30000',source_E_upper='2^100000',source_C0='2^210000',global_prefix_bits=role['prefix_bits'],charged_prefix_bits=payload,row_prefix_extra=2*payload,physical_row_coefficient=row,retained_row_coefficient=20161,paid_profile=P,paid_rank_mass=mass,rank_surplus=320*T,numeric_plan_sha256=identity(numericplans[pr]),actual_selected_native_recount=recount)

def encode(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):encode(v) for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [encode(v) for v in o]
    return o
used_primary.update(json.loads((R/'u8-selected-native-recovery.json').read_text())['source_sha256'])
for x in manifest:
    if 'error' not in x:used_primary['t21-t37-cost-source/'+x['file']]=x['sha256']
deps=['u8_selected_native_recovery.py','u8-selected-native-recovery.json','pr799_recovered_finite_controller.py']
out=dict(schema='t21-t37-own-owner-geometry-census/1',status='source_numeric_and_whole_role_checks_verified',checks_passed=len(checks),checks=checks,source_geometry_fixture='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz',geometry_fixture_scope='Only geometry/schedule, independently window-matched to selected799PLAN; not selected U8 native program or historical T21 parent-template byte identity.',native_allcolumn_scalar_frame_replayed=True,full_phase_engine_rerun=False,owner21_semantic_sha256=identity(roles21),owner21_byte_hash_matches_SPEC=True,bank21=bank21,bank_controls21=bank_controls21,role21=role21,owner_controls21=controls21,omitted_edit_controls21=omitted21,bank37=bank37,bank_controls37=bank_controls37,role37=role37,owner_controls37=controls37,omitted_edit_controls37=omitted37,invoices=invoices,complete_runtime_bound=None,source_sha256=used_primary,dependency_hashes={p:hs(R/p) for p in deps},script_sha256=hs(Path(__file__)))
(R/'t21-t37-owner-invoice-workbench.json').write_text(json.dumps(encode(out),indent=2)+'\n')
for pr in [890,942]:
    (R/f'pr{pr}-own-numeric-plan.json').write_text(json.dumps(encode(numericplans[pr]),indent=2)+'\n')
    (R/f'pr{pr}-own-finite-invoice.json').write_text(json.dumps(encode(invoices[pr]),indent=2)+'\n')
print(json.dumps({'checks':len(checks),'t21':{k:role21[k] for k in ['roles','calls','prefix_bits','physical_row_coefficient']},'t37':{k:role37[k] for k in ['roles','calls','prefix_bits','physical_row_coefficient']}},indent=2))
