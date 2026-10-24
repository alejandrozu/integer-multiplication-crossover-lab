"""Fresh exact native/owner/invoice replay for the frozen fifteen admitted PRs.

This scoped reproducer needs only the fifteen own source/input sets, not every
unpriced discovery artifact in the144-entry source inventory. It does not change
or regenerate any frozen mathematical certificate.
"""
from pathlib import Path
from collections import Counter
import gzip,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;checks={}
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def rd(p):
    q=R/p;return json.loads(gzip.decompress(q.read_bytes())if q.suffix=='.gz'else q.read_bytes())
def ck(k,v):assert v,k;checks[k]=True
def norm(o):return json.loads(json.dumps(o))
def mod(name):
    s=importlib.util.spec_from_file_location(name,R/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
nc=mod('finite_selected_program_census');oc=mod('finite_actual_owner_census')
old=rd('older-reviewed-source/535-manifest.json');proto=rd('older-reviewed-source/'+next(x['file']for x in old if x['path']=='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz'))
dm=rd('t21-t37-cost-source/manifest.json')
def data(suffix):return 't21-t37-cost-source/'+next(x['file']for x in dm if x.get('path','').endswith(suffix)and'error'not in x)
phases=rd(data('/work/complex-nine-native/DATA-PHASES.json'));base=rd(data('/split-centres/CANONICAL-WORD.json.gz'))
bundle=rd('selected-provider-batch-upper.json');points=[r for r in bundle['rows']if r.get('numeric_bound_completed')]
ck('exact_frozen_fifteen',len(points)==15 and set(r['pr']for r in points)=={592,600,622,623,624,625,1018,1082,1063,1297,1319,1130,1124,3338,3413})
nativecache={};owncache={};sourcepins={};replayed=[]
for row in points:
    pr=row['pr'];tag=str(pr)+'_';n=rd(row['native_certificate']);cp=n['own_complete_census_file'];c=rd(cp);ck(tag+'frozen_census_hash',hs(cp)==n['own_complete_census_sha256'])
    spec=rd(c['own_SPEC_file']);ck(tag+'own_SPEC',hs(c['own_SPEC_file'])==c['own_SPEC_sha256']);sourcepins[c['own_SPEC_file']]=c['own_SPEC_sha256']
    providers={};cost={}
    for z in c['selected_native_censuses']:
        pid=z['provider'];key=z['program_file_sha256'],z['canonical_file_sha256'];ck(tag+pid+'_actual_program_hash',hs(z['program_file'])==z['program_file_sha256']);sourcepins[z['program_file']]=z['program_file_sha256']
        if z['canonical_file']:ck(tag+pid+'_actual_canonical_hash',hs(z['canonical_file'])==z['canonical_file_sha256']);sourcepins[z['canonical_file']]=z['canonical_file_sha256']
        if key not in nativecache:nativecache[key]=norm(nc.census(rd(z['program_file']),canonical=rd(z['canonical_file'])if z['canonical_file']else None))
        fresh=nativecache[key];ck(tag+pid+'_fresh_exact_scalar_frame_cost_census',fresh==rd(z['census_file'])and hs(z['census_file'])==z['census_sha256'])
        ck(tag+pid+'_own_orientation_pair',{o:v['sha256']for o,v in fresh.items()}==spec['providers'][pid]['program_hashes'])
        f=fresh['forward'];providers[pid]=dict(columns=f['columns'],helpers=f['helpers'],widths=f['widths'],paid_profile={int(k):v for k,v in f['paid_profile'].items()},prefix_bits=max(v['prefix_bits']for v in fresh.values()))
        cost[pid]=dict(local=fresh,adapters=16*(max(v['scalar_macros']for v in fresh.values())+sum(providers[pid]['paid_profile'].values())+f['columns']+8)+64*73)
    art=c['own_physical_artifacts'];plan=rd(art['PLAN']['file']);roles=rd(art['OWNERS']['file'])
    for k,a in art.items():ck(tag+'own_'+k,hs(a['file'])==a['sha256']==a['own_SPEC_expected_sha256']);sourcepins[a['file']]=a['sha256']
    dispatch={(a,b):p for a,b,p in spec['dispatch']};key=(art['PLAN']['sha256'],art['OWNERS']['sha256'],json.dumps(providers,sort_keys=True))
    if key not in owncache:
        ctx=oc.context(proto,phases,base['ports'],plan,roles,dispatch,providers);owncache[key]=(norm(oc.audit(ctx,roles)),oc.controls(ctx,roles))
    role,neg=owncache[key];ck(tag+'fresh_complete_owner_and_six_controls',role==c['role_receipt']and neg==c['negative_controls']and len(neg)==6)
    inv=c['invoice'];T=plan['T'];groups=(T+7)//8;parentlive=11704*groups-896*(8*groups-T);parentphysical=parentlive+514;banks=504*groups;idle=16128*groups
    orient={z['stage']:z['orientation']for z in proto['calls']};scalar=wrappers=0
    for a,b in plan['order']:
        z=cost[dispatch[a,b]]['local'][orient[a]];scalar+=z['real_component_primitives'];wrappers+=(z['pre_wrappers']+z['post_wrappers'])*144
    calls=role['calls'];helpers=role['helpers_max'];bridges=2*112*role['bridges'];shifts=4*112*T;moves=2*shifts;adapters=max(v['adapters']for v in cost.values());compiler=64*74**3
    items=4*112*T*9+2*112*T*9+2*calls*helpers+idle+9*banks+bridges+shifts+moves+parentlive+parentphysical+wrappers;outside=8*items+64*73
    work=scalar+bridges+shifts+moves+parentlive+(calls*adapters+outside)*compiler+64*parentphysical;used=max(work,work+65*(role['physical']-parentphysical)+(role['live']-parentlive))
    expected=dict(selected_real=scalar,wrapper_factors=wrappers,adapters=adapters,parent_live=parentlive,parent_physical=parentphysical,parent_banks=banks,parent_idle=idle,nonlocal_items=items,outside=outside,unhosted_work=work,complete_work=used,retained_previous_invoice=None,physical=role['physical'],live=role['live'])
    ck(tag+'fresh_no_prior_complete_invoice',all(inv[k]==v for k,v in expected.items()))
    replayed.append(pr);print('PASS admitted own source replay',pr,flush=True)
out=dict(schema='frozen-fifteen-admitted-source-replay/1',status='fresh_selected_scalar_owner_invoice_replay_passed',prs=replayed,checks_passed=len(checks),checks=checks,actual_distinct_native_pairs_recounted=len(nativecache),actual_distinct_owner_components_replayed=len(owncache),operator_valued_phase_replayed=False,scope='Fresh exact numeric scalar/frame-if-catalogue-present, complete whole-owner/control and invoice reproduction. Full required physical endpoint, phase/typed-width and all-size contracts remain explicit; missing catalogue is not repaired by scalar specialization.',source_sha256=sourcepins,dependency_hashes={p:hs(p)for p in ['selected-provider-batch-upper.json','finite_selected_program_census.py','finite_actual_owner_census.py']},script_sha256=hs(Path(__file__).name))
(R/'selected-provider-admitted-replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(status=out['status'],checks=len(checks),prs=replayed),indent=2))
