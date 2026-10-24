"""Own selected-provider dispatch, complete physical roles and fresh invoices.

This is a parameterized numeric realization, not a replay of full Gaussian
phase semantics. Every selected finite program, PLAN and OWNERS is separately
bound to its own immutable source. No earlier invoice is reused.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import gzip,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;C=R/'early-mixed-provider-source'
checks={};used={}
def hs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,v):assert v,n;checks[n]=True
def rd(p):
    used[p.relative_to(R).as_posix()]=hs(p)
    return json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_bytes())
def ident(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [enc(v)for v in o]
    return o
manifest=rd(C/'own-packages-manifest.json')
def own(pr,path):
    x=next(x for x in manifest if x['pr']==pr and x['logical_path']==path)
    p=C/x['file'];ck(str(pr)+'_own_primary_'+path,hs(p)==x['sha256']);return p
comp=rd(R/'early-mixed-native-components.json')
ck('actual_selected_components',comp['script_sha256']==hs(R/'early_mixed_native_components.py')and all(comp['checks'].values())and len(comp['rows'])==9)
for key in ['source_sha256','derived_selected_bytes_sha256','dependency_hashes']:
    for p,h in comp[key].items():ck('native_'+key+'_'+p,hs(R/p)==h)
components={(z['pr'],z['provider']):z for z in comp['rows']}
s=importlib.util.spec_from_file_location('own_actual_roles',R/'finite_actual_owner_census.py');mod=importlib.util.module_from_spec(s);s.loader.exec_module(mod)
old=rd(R/'older-reviewed-source/535-manifest.json')
proto=rd(R/'older-reviewed-source'/next(x['file']for x in old if x['path']=='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz'))
datam=rd(R/'t21-t37-cost-source/manifest.json')
def data(suffix):return R/'t21-t37-cost-source'/next(x['file']for x in datam if x.get('path','').endswith(suffix)and'error'not in x)
phasepath=data('/work/complex-nine-native/DATA-PHASES.json');phases=rd(phasepath)
baseword=rd(data('/split-centres/CANONICAL-WORD.json.gz'))
ck('primary_parent_data_phase',proto['exact_data_phase_recipe_sha256']==hs(phasepath))
group=2**(36*36)
for i in range(1,37):group*=2**(2*i)-1
compiler=64*74**3;rows=[];plans={};invoices={}
for pr in [588,596,617,626]:
    tag=str(pr)+'_';sp=own(pr,'data/SPEC.json');spec=rd(sp);pp=own(pr,'data/PLAN.json');op=own(pr,'data/OWNERS.json.gz')
    ck(tag+'own_historical_PLAN_and_OWNERS',hs(pp)==spec['data']['plan_sha256']and hs(op)==spec['data']['owners_sha256'])
    plan=rd(pp);roles=rd(op);dispatch={(s,r):pid for s,r,pid in spec['dispatch']}
    ck(tag+'own_complete_dispatch_and_order',len(dispatch)==72 and plan['order']==spec['call_order']and set(dispatch.values())==set(spec['providers']))
    providers={};nativecost={}
    for pid,p in spec['providers'].items():
        c=components[pr,pid];local=c['selected_local_census'];f=local['forward'];reg=plan['provider_registry'][pid]
        ck(tag+pid+'_own_native_geometry',c['ports']==baseword['ports']and all(mod.basis(a)==mod.basis(b)for a,b in zip(c['centre_frames'],[baseword['frames'][z]for z in baseword['center_frames']])))
        ck(tag+pid+'_actual_registry_binding',reg['ports']==c['ports']and reg['widths']==f['widths']and reg['actual_paid_profile']==p['expected_profile']and reg['orientation_program_sha256']==p['program_hashes']and reg['artifact_semantic_sha256']==p['artifact_semantic_sha256'])
        ck(tag+pid+'_scalar_scope_and_actual_frames',all(x['scalar_specialization_columns_checked']and not x['operator_valued_endpoint_proved_by_this_census']and x['native_canonical_frame_catalog_checked']and x['native_monotone_frame_checks']>0 for x in local.values()))
        providers[pid]=dict(columns=f['columns'],helpers=f['helpers'],widths=f['widths'],paid_profile={int(k):v for k,v in f['paid_profile'].items()},prefix_bits=max(z['prefix_bits']for z in local.values()))
        adapter=16*(max(z['scalar_macros']for z in local.values())+sum(providers[pid]['paid_profile'].values())+f['columns']+8)+64*73
        ck(tag+pid+'_actual_adapter_tariff',adapter==p['complete_contract']['local_adapters'])
        nativecost[pid]=dict(local=local,adapters=adapter)
    stageorient={c['stage']:c['orientation']for c in proto['calls']}
    ck(tag+'own_every_selected_call_program',plan['provider_calls']==[dict(time=t,stage=s,replica=r,provider=dispatch[s,r],orientation=stageorient[s],local_program_sha256=spec['providers'][dispatch[s,r]]['program_hashes'][stageorient[s]])for t,(s,r)in enumerate(plan['order'])])
    ck(tag+'own_every_whole_call_width',plan['per_call_widths']==[dict(stage=s,replica=r,widths=providers[dispatch[s,r]]['widths'])for s,r in plan['order']])
    ctx=mod.context(proto,phases,baseword['ports'],plan,roles,dispatch,providers)
    role=mod.audit(ctx,roles);bad=mod.controls(ctx,roles);ex=spec['expected']
    ck(tag+'six_whole_role_negative_controls',len(bad)==6)
    for actual,k in [('live','live'),('physical','physical'),('roles','hosted_residuals'),('rank_mass','rank_mass'),('rank_surplus','deficit'),('cross_replica_helpers','cross_replica_helper_roles'),('entering_helpers','entering_helper_roles'),('actual_73_axis_charts','actual_73column_sigmas')]:ck(tag+'own_'+k,role[actual]==ex[k])
    ck(tag+'own_fresh_global_profile_and_idle',role['profile']=={int(k):v for k,v in ex['global_profile'].items()}=={int(k):v for k,v in plan['profile'].items()}and role['idle']=={int(k):v for k,v in ex['idle_remainder_profile'].items()})
    T=plan['T'];calls=role['calls'];live=role['live'];physical=role['physical'];helpers=role['helpers_max']
    ck(tag+'literal_T8_parent_inventory',T==8 and proto['live']==11704 and proto['physical']==12218 and len(proto['calls'])==72)
    # Own source assemble.py and invoice_allcold.py explicitly specify these
    # same physical operations. We independently sum from the selected calls.
    ap=own(pr,'code/assemble.py');ip=own(pr,'code/invoice_allcold.py');used[ap.relative_to(R).as_posix()]=hs(ap);used[ip.relative_to(R).as_posix()]=hs(ip)
    parentlive=proto['live'];parentphysical=proto['physical'];banks,rem=divmod(parentlive-live,9);idle=sum(z['replicas']for z in proto['idle_children'])
    ck(tag+'parent_full_banks_and_idle',not rem and banks==504 and idle==16128)
    scalar=work=wrapperfactors=0;selectedcalls=[]
    for t,(s,r)in enumerate(plan['order']):
        pid=dispatch[s,r];o=stageorient[s];z=nativecost[pid]['local'][o]
        scalar+=z['real_component_primitives'];work+=z['coefficient_work_primitives'];wrapperfactors+=(z['pre_wrappers']+z['post_wrappers'])*144
        selectedcalls.append(dict(time=t,stage=s,replica=r,provider=pid,orientation=o,program_sha256=z['sha256'],real=z['real_component_primitives'],coefficient_work=z['coefficient_work_primitives'],pre_wrappers=z['pre_wrappers'],post_wrappers=z['post_wrappers']))
    adapters=max(z['adapters']for z in nativecost.values());bridges=2*112*role['bridges'];shifts=4*112*T;moves=2*shifts
    items=4*112*T*9+2*112*T*9+2*calls*helpers+idle+9*banks+bridges+shifts+moves+parentlive+parentphysical+wrapperfactors
    outside=8*items+64*73;pervertex=scalar+bridges+shifts+moves+parentlive+(calls*adapters+outside)*compiler+64*parentphysical
    rebased=pervertex+65*(physical-parentphysical)+(live-parentlive);usedwork=max(pervertex,rebased)
    stock=group*physical;streamed=group*role['rank_mass'];logical=group*usedwork+64;router=compiler*(logical+1)*(stock+1)**2
    literal=2*2**30000*stock**2+8*streamed+4*stock+4+32*73
    ck(tag+'fresh_finite_router_and_literal',logical<2**6050 and router<2**30000 and literal<2**100000 and usedwork<2**64)
    ck(tag+'allsize_semantic_height_reserve',32*73*(streamed+2**100000)**2<2**210000 and 2*(streamed+2**100000)+18<2**210000)
    ck(tag+'source_prefix_and_physical_row',role['prefix_bits']<role['charged_prefix_bits']==512 and role['physical_row_coefficient']<20161)
    np=dict(schema='own_mixed_numeric_realization/1',pr=pr,own_head=components[pr,next(iter(providers))]['own_head'],historical_PLAN_sha256=hs(pp),OWNERS_sha256=hs(op),owners_content_sha256=ident(roles),order=plan['order'],windows=plan['windows'],profile=role['profile'],selected_calls=selectedcalls,parent_fixture_content_sha256=ident(proto),historical_parent_provenance_byte_identity_claimed=False,scope='Fresh physical numeric parent realization with exact own PLAN/order/windows/OWNERS/provider dispatch; no historical parent metadata byte identity is asserted.')
    np=json.loads(json.dumps(np))
    invoice=dict(schema='own_mixed_complete_invoice/1',pr=pr,own_head=np['own_head'],live=live,physical=physical,calls=calls,helpers=helpers,provider_counts=dict(Counter(dispatch.values())),parent_live=parentlive,parent_physical=parentphysical,parent_banks=banks,source_idle=idle,bridge_sweeps=role['bridges'],selected_real_component_primitives=scalar,selected_coefficient_work_primitives=work,local_adapters=adapters,wrapper_elementary_factors=wrapperfactors,compiler=compiler,nonlocal_items=items,outside=outside,unhosted_pervertex=pervertex,hosted_rebased_pervertex=rebased,complete_pervertex_used=usedwork,retained_previous_invoice=None,source_G_upper='2^30000',source_E_upper='2^100000',source_C0='2^210000',physical_stock_bits=stock.bit_length(),paid_profile=role['profile'],paid_rank_mass=role['rank_mass'],rank_surplus=role['rank_surplus'],prefix_bits=role['prefix_bits'],charged_prefix_bits=512,row_prefix_extra=1024,physical_row_coefficient=role['physical_row_coefficient'],numeric_plan_sha256=ident(np),own_record_kappa=ex['kappa'],own_complex_lower=ex['complex_lower'])
    plans[pr]=np;invoices[pr]=invoice;rows.append(dict(pr=pr,own_head=np['own_head'],own_SPEC_file=sp.relative_to(R).as_posix(),own_SPEC_sha256=hs(sp),own_PLAN_sha256=hs(pp),own_OWNERS_sha256=hs(op),role_receipt=role,negative_controls=bad,invoice=invoice))
    print('PASS own mixed selected owner/invoice',pr,flush=True)
out=dict(schema='own_mixed_owner_invoice_census/1',status='own_source_numeric_role_invoice_checked',rows=rows,checks_passed=len(checks),checks=checks,source_sha256=used,dependency_hashes={p:hs(R/p)for p in ['early_mixed_native_components.py','early-mixed-native-components.json','finite_selected_program_census.py','finite_actual_owner_census.py']},script_sha256=hs(Path(__file__)),whole_integer_upper=None,meaningful_lower=None,retained_hypotheses=['Full operator-valued native phase and normalized-wrapper contract for the own selected bytes','Ascending typed helper endpoints and monomial normalized wrappers','Arbitrary-input common-label, mutable-source, owner restoration and all-size occupied-row interfaces'])
(R/'early-mixed-owner-invoice.json').write_text(json.dumps(enc(out),indent=2)+'\n')
for pr in plans:
    (R/f'pr{pr}-mixed-own-numeric-plan.json').write_text(json.dumps(enc(plans[pr]),indent=2)+'\n')
    (R/f'pr{pr}-mixed-own-finite-invoice.json').write_text(json.dumps(enc(invoices[pr]),indent=2)+'\n')
print(json.dumps(dict(status=out['status'],checks=len(checks),prs=list(plans)),indent=2))
