"""Fresh own r480 T16 role, stock and complete literal invoices."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import ast,copy,gzip,hashlib,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;O=R/'older-reviewed-source';S=R/'r480-t16-cost-source'
checks={};used={}
def ck(n,v):assert v,n;checks[n]=True
def hs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):
    used[p.relative_to(R).as_posix()]=hs(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def canonical(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def ident(o):return hashlib.sha256(canonical(o)).hexdigest()
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v) for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [enc(v) for v in o]
    return o
manifest=rd(S/'manifest.json')
for x in manifest:
    if 'error' not in x:
        ck('own1042_source_'+x['path'],hs(S/x['file'])==x['sha256'] and x['head']=='7e8ef087c02a77038a28a337a7ee3a77039cac0d')
        used['r480-t16-cost-source/'+x['file']]=x['sha256']
paths={x['path']:S/x['file'] for x in manifest if 'error'not in x}
def own1042(suffix):return next(p for k,p in paths.items() if k.endswith('/'+suffix))
old1042=rd(O/'1042-manifest.json')
spec1042path=O/next(x['file'] for x in old1042 if x['path']=='research/gauge44-slots-t16/data/SPEC.json')
specs={1042:rd(spec1042path)}
manifest1094=rd(R/'pr1094-source/manifest.json');P1094=R/'pr1094-source/files/research/complex-t16-rare-pattern-exchanges'
ownhash1094=rd(P1094/'MANIFEST.json')
for p in ['data/SPEC.json','data/PLAN.json','OWNERS.json.gz','PROFILE.json']:
    ck('own1094_primary_'+p,hs(P1094/p)==ownhash1094[p])
specs[1094]=rd(P1094/'data/SPEC.json')

native=rd(R/'r480-selected-native-recovery.json')
ck('fresh_own_selected_native_recovery',native['script_sha256']==hs(R/'r480_selected_native_recovery.py') and native['checks_passed']>=37 and all(native['checks'].values()))
for p,h in native['source_sha256'].items():ck('native_primary_'+p,hs(R/p)==h)
for p,h in native['dependency_hashes'].items():ck('native_dependency_'+p,hs(R/p)==h)
recovery_manifest=rd(R/'r480-selected-recovery-source/manifest.json')
word=rd(R/'r480-selected-recovery-source'/next(x['file']for x in recovery_manifest if x['path'].endswith('/CANONICAL-WORD.json.gz')))
contract=specs[1042]['providers']['gauge44']['complete_contract'];recount=native['selected_local_recount']
numeric_replay={'paid_profiles':{o:specs[1042]['providers']['gauge44']['expected_profile']for o in recount},'local':{o:{'prefix_bits_upper':v['prefix_bits'],'prefix_l1_upper':v['prefix_l1']}for o,v in contract['local'].items()}}

# Pure source modules. Only external input configuration is injected; their
# constructors, inequalities, role checker and mutation controls are unchanged.
bankpath=own1042('t16/build_parent.py');used[bankpath.relative_to(R).as_posix()]=hs(bankpath)
bank={'__name__':'own_r480_t16_parent','__file__':str(bankpath)};exec(compile(bankpath.read_bytes(),str(bankpath),'exec'),bank)
indpath=own1042('t16/indep16.py');used[indpath.relative_to(R).as_posix()]=hs(indpath)
tree=ast.parse(indpath.read_text());tree.body=[n for n in tree.body if not(isinstance(n,ast.Assign) and any(isinstance(t,ast.Name)and t.id in ['EXPECTED_IDLE','EXPECTED_WIDTHS']for t in n.targets))]
ind={'__name__':'own_r480_t16_roles','__file__':str(indpath)};exec(compile(tree,str(indpath),'exec'),ind)
fixture=O/next(x['file']for x in rd(O/'535-manifest.json')if x['path']=='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz')
proto=rd(fixture)
data_manifest=rd(R/'t21-t37-cost-source/manifest.json')
data=lambda suffix:R/'t21-t37-cost-source'/next(x['file']for x in data_manifest if x.get('path','').endswith(suffix)and'error'not in x)
phasespath=data('/work/complex-nine-native/DATA-PHASES.json');phases=rd(phasespath)
baseword=rd(data('/split-centres/CANONICAL-WORD.json.gz'))
plan8=rd(own1042('data/T8/PLAN.json'))
ck('own_T8_complete_physical_windows',bank['actual_windows'](proto,plan8['order'])[0]==plan8['windows'])
ck('geometry_data_phase_source_binding',proto['exact_data_phase_recipe_sha256']==hs(phasespath))
ck('selected_native_same_ordered_port_centres',word['ports']==baseword['ports'] and [ind['basis'](word['frames'][f])for f in word['center_frames']]==[ind['basis'](baseword['frames'][f])for f in baseword['center_frames']])
ck('source_T8_identity_parent',bank['lift_parent'](proto,1)==proto)
parent=bank['lift_parent'](proto)
ck('own_two_group_parent_stock',parent['live']==23408 and parent['physical']==23922 and len(parent['calls'])==144)

group=2**(36*36)
for i in range(1,37):group*=2**(2*i)-1
compiler=64*74**3;invoices={};plans={};role_receipts={};controls={}
for pr in [1042,1094]:
    spec=specs[pr];provider=spec['providers']['gauge44'];localP={int(k):v for k,v in provider['expected_profile'].items()}
    planpath=own1042('data/PLAN.json')if pr==1042 else P1094/'data/PLAN.json'
    rolepath=own1042('data/OWNERS.json.gz')if pr==1042 else P1094/'OWNERS.json.gz'
    ck(str(pr)+'_own_PLAN_primary_binding',hs(planpath)==spec['data']['plan_sha256'])
    ck(str(pr)+'_own_OWNERS_primary_binding',hs(rolepath)==spec['data']['owners_sha256'])
    plan=rd(planpath);roles=rd(rolepath)
    ck(str(pr)+'_own_selected_provider_hash',provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']==native['selected_program_semantic_sha256'])
    ind['EXPECTED_IDLE']={int(k):v for k,v in spec['expected']['idle_remainder_profile'].items()}
    ind['EXPECTED_WIDTHS']={int(k):v for k,v in provider['inventory'].items()}
    context=ind['make_context'](proto,phases,baseword['ports'],word,numeric_replay,roles)
    role=ind['check_roles'](context,roles);bad=ind['controls'](context,roles)
    ck(str(pr)+'_full_whole_role_and_six_controls',role['roles']==69120 and role['calls']==144 and len(bad)==6)
    order=[list(z)for z in context['order']];windows,schedule=bank['actual_windows'](parent,order)
    ck(str(pr)+'_own_order_and_windows',order==spec['call_order']==plan['order'] and windows==plan['windows'])
    P={int(k):v for k,v in role['profile'].items()};mass=sum(r*n for r,n in P.items())
    ck(str(pr)+'_fresh_complete_profile',P=={int(k):v for k,v in spec['expected']['global_profile'].items()}=={int(k):v for k,v in plan['profile'].items()} and mass==1041408 and 73*14336-mass==5120)
    calls=144;live=14336;physical=14850;helpers=480
    stageorient={c['stage']:c['orientation']for c in proto['calls']};orient=Counter(stageorient[s]for s,r in order)
    scalar=sum(n*recount[o]['real_component_primitives']for o,n in orient.items())
    work=sum(n*recount[o]['coefficient_work_primitives']for o,n in orient.items())
    wrappers=sum(n*(contract['local'][o]['pre_wrappers']+contract['local'][o]['post_wrappers'])*144 for o,n in orient.items())
    adapters=16*(max(v['scalar_macros']for v in recount.values())+sum(localP.values())+704+8)+64*73
    ck(str(pr)+'_actual_own_local_adapters',adapters==contract['local_adapters']==native['local_complete_adapters'])
    banks,rem=divmod(parent['live']-live,9);idle=sum(c['replicas']for c in parent['idle_children'])
    bridge_sweeps=sum(e['kind']=='bridge'for e in schedule);bridges=2*112*bridge_sweeps;shifts=4*112*16;moves=2*shifts
    items=4*112*16*9+2*112*16*9+2*calls*helpers+idle+9*banks+bridges+shifts+moves+parent['live']+parent['physical']+wrappers
    outside=8*items+64*73
    pervertex=scalar+bridges+shifts+moves+parent['live']+(calls*adapters+outside)*compiler+64*parent['physical']
    rebased=pervertex+65*(physical-parent['physical'])+(live-parent['live']);usedwork=max(pervertex,rebased)
    stock=group*physical;streamed=group*mass;logical=group*usedwork+64;router=compiler*(logical+1)*(stock+1)**2
    literal=2*2**30000*stock**2+8*streamed+4*stock+4+32*73;row=2*stock.bit_length()+9909+252+1024
    ck(str(pr)+'_complete_source_sweeps_and_parent_banks',not rem and banks==1008 and bridge_sweeps==144 and idle==32256 and sum(orient.values())==144)
    ck(str(pr)+'_all_own_finite_work_and_stock',logical<2**6050 and router<2**30000 and literal<2**100000 and usedwork<2**64)
    ck(str(pr)+'_own_semantic_C0_inequalities',32*73*(streamed+2**100000)**2<2**210000 and 2*(streamed+2**100000)+18<2**210000)
    ck(str(pr)+'_own_global_prefix_payload_and_row',role['prefix_bits']==397<512 and row==role['physical_row_coefficient']==16469<20161)
    ck(str(pr)+'_own_selected_child_halving',73**2>2*max(P)**2)
    head={1042:'7e8ef087c02a77038a28a337a7ee3a77039cac0d',1094:'0fc329d0bec93ca7cd288eaea1295172e8789810'}[pr]
    np=dict(schema='own_r480_t16_numeric_realization/1',pr=pr,own_head=head,selected_program_semantic_sha256=native['selected_program_semantic_sha256'],own_historical_PLAN_sha256=hs(planpath),owners_sha256=hs(rolepath),owners_content_sha256=ident(roles),order=order,windows=windows,profile=P,complete_calls=[dict(time=t,stage=s,replica=r,orientation=stageorient[s],helpers=480,columns=704,program_sha256=provider['program_hashes'][stageorient[s]])for t,(s,r)in enumerate(order)],parent_geometry_content_sha256=ident(parent),historical_parent_provenance_byte_identity_claimed=False,scope='Fresh source-equivalent numeric parent from independently window-matched primary fixture; own historical PLAN/order/windows/profile/OWNERS remain exactly bound, but parent metadata byte identity is not claimed.')
    np=json.loads(json.dumps(np));plans[pr]=np
    invoices[pr]=dict(schema='own_r480_t16_complete_invoice/1',pr=pr,own_head=head,live=live,physical=physical,calls=calls,helpers=helpers,parent_live=parent['live'],parent_physical=parent['physical'],parent_banks=banks,source_idle=idle,bridge_sweeps=bridge_sweeps,orientation_counts=dict(orient),actual_selected_real_primitives=scalar,actual_coefficient_work_primitives=work,local_adapters=adapters,wrapper_factors=wrappers,compiler=compiler,nonlocal_items=items,outside=outside,unhosted_pervertex=pervertex,hosted_rebased_pervertex=rebased,complete_pervertex_used=usedwork,retained_previous_invoice=None,router_bits=router.bit_length(),literal_bits=literal.bit_length(),source_G_upper='2^30000',source_E_upper='2^100000',source_C0='2^210000',physical_stock_bits=stock.bit_length(),paid_profile=P,paid_rank_mass=mass,rank_surplus=5120,prefix_bits=397,charged_prefix_bits=512,row_prefix_extra=1024,physical_row_coefficient=row,numeric_plan_sha256=ident(np),own_record_kappa=spec['expected']['kappa'],own_complex_lower=spec['expected']['complex_lower'])
    role_receipts[pr]=role;controls[pr]=bad
    print('PASS own r480 T16 roles/invoice',pr,flush=True)
out=dict(schema='r480-t16-own-owner-invoice-census/1',status='own_source_numeric_role_invoice_checked',checks_passed=len(checks),checks=checks,role_receipts=role_receipts,controls=controls,invoices=invoices,source_sha256=used,dependency_hashes={p:hs(R/p)for p in ['r480_selected_native_recovery.py','r480-selected-native-recovery.json','r480-selected-native-recovery.md']},script_sha256=hs(Path(__file__)),whole_integer_upper=None,meaningful_lower=None)
(R/'r480-t16-owner-invoice.json').write_text(json.dumps(enc(out),indent=2)+'\n')
for pr in [1042,1094]:
    (R/f'pr{pr}-r480-own-numeric-plan.json').write_text(json.dumps(enc(plans[pr]),indent=2)+'\n')
    (R/f'pr{pr}-r480-own-finite-invoice.json').write_text(json.dumps(enc(invoices[pr]),indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks)},indent=2))
