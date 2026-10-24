"""Recover the exact earlier selected r480 word; no whole-runtime claim."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import ast,contextlib,gzip,hashlib,io,json,sys,tempfile
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'r480-selected-recovery-source';O=R/'older-reviewed-source'
checks={}
def ck(n,v):assert v,n;checks[n]=True
def hs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def identity(o):return hashlib.sha256(canon(o)).hexdigest()
manifest=read(S/'manifest.json');source_hashes={}
for x in manifest:
    ck('recovered_primary_'+x['path'],hs(S/x['file'])==x['sha256'] and x['head']=='a007dc2e1cc7ae7e8f7ec1343e8883fe43259f21')
    source_hashes['r480-selected-recovery-source/'+x['file']]=x['sha256']
def recovered(name):return S/next(x['file'] for x in manifest if x['path'].endswith('/'+name))
canonical=read(recovered('CANONICAL-WORD.json.gz'));programs=read(recovered('LOCAL-PROGRAMS.json.gz'))
providers={};heads={1042:'7e8ef087c02a77038a28a337a7ee3a77039cac0d',1094:'0fc329d0bec93ca7cd288eaea1295172e8789810'}
for pr in [1042,1094]:
    wanted='research/gauge44-slots-t16/data/SPEC.json' if pr==1042 else 'research/complex-t16-rare-pattern-exchanges/data/SPEC.json'
    if pr==1042:
        rows=read(O/f'{pr}-manifest.json');base=O
    else:
        ownmanifest=read(R/'pr1094-source/manifest.json');rows=[dict(x,head=ownmanifest['head']) for x in ownmanifest['files']];base=R/'pr1094-source'
    x=next(x for x in rows if x['path']==wanted)
    ck(str(pr)+'_own_authority_head',x['head']==heads[pr] and hs(base/x['file'])==x['sha256'])
    source_hashes[str((base/x['file']).relative_to(R)).replace('\\','/')]=x['sha256']
    spec=read(base/x['file']);provider=spec['providers']['gauge44'];providers[pr]=provider
    ck(str(pr)+'_earlier_own_selected_canonical',identity(canonical)==provider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']=='4ddb29fb9bc6f27e0c0fbfcf19a2a93a3496ad900d0f6d89059d0305c9576c0c')
    ck(str(pr)+'_earlier_own_selected_programs',identity(programs)==provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']=='9f41d53659e9be84e20c661560c5687abbf5cd0660cdecbe01ad5eb29e6b8ee3')
    ck(str(pr)+'_own_two_orientation_hashes',all(identity(events)==provider['program_hashes'][o] for o,events in programs.items()))
    ck(str(pr)+'_own_dimension',provider['complete_contract']['helpers']==480 and provider['complete_contract']['n']==704 and canonical['R']==480 and 2*canonical['v']+canonical['R']==704)
    for name in ['CLIFFORD-RECIPES.json','RESIDUAL-ADAPTERS.json']:
        ck(str(pr)+'_own_selected_'+name,identity(read(recovered(name)))==provider['artifact_semantic_sha256'][name])

# This older generic emitter is a mathematical replay, not a later algorithm.
# It regenerates the exact earlier selected program hashes and checks all704
# formal input columns with rational coefficients in both orientations.
rows799=read(O/'799-manifest.json');e=next(x for x in rows799 if x['path'].endswith('/hpe_emit_local.py'));engine=O/e['file']
ck('pinned_generic_native_engine',hs(engine)==e['sha256'])
source_hashes['older-reviewed-source/'+e['file']]=e['sha256']
with tempfile.TemporaryDirectory(prefix='r480-selected-native-') as td:
    td=Path(td);(td/'CANONICAL-WORD.json.gz').write_bytes(recovered('CANONICAL-WORD.json.gz').read_bytes())
    argv=sys.argv[:];sys.argv=[str(engine),str(td)]
    try:
        ns={'__name__':'r480_exact_generic_emission','__file__':str(engine)}
        with contextlib.redirect_stdout(io.StringIO()):exec(compile(engine.read_bytes(),str(engine),'exec'),ns)
    finally:sys.argv=argv
    fresh=read(td/'LOCAL-PROGRAMS.json.gz');localchecks=read(td/'LOCAL-CHECKS.json')
    ck('fresh_both_selected_programs_identical',fresh==programs and identity(fresh)==identity(programs))
    ck('fresh_all_native_columns_and_private_clears',all(v['all_columns']==704 and v['private_centers_cleared'] and v['private_coefficient_stream_cleared_after_each_macro'] for v in localchecks.values()))
    ck('fresh_dimension_and_profile',all(v['events']==24767 and v['paid_profile']==providers[1042]['expected_profile'] for v in localchecks.values()))

# Reuse only the exact Horner/prefix counting block, with its literal native
# dimension changed from728 to this own704. No earlier invoice is executed.
tree=ast.parse((R/'pr799_recovered_finite_controller.py').read_text())
counter=next(n for n in tree.body if isinstance(n,ast.For) and isinstance(n.target,ast.Tuple) and [t.id for t in n.target.elts]==['orientation','events'])
class Dimension(ast.NodeTransformer):
    def visit_Constant(self,node):return ast.copy_location(ast.Constant(704),node) if node.value==728 else node
counter=Dimension().visit(counter);ast.fix_missing_locations(counter)
provider=providers[1042];contract=provider['complete_contract'];recount={}
exec(compile(ast.Module(body=[counter],type_ignores=[]),'r480_exact_horner_prefix','exec'),globals())
for pr,provider in providers.items():
    ck(str(pr)+'_same_own_complete_contract',provider['complete_contract']==contract)
    ck(str(pr)+'_own_counts_match_regenerated_native',all(recount[o]['real_component_primitives']==provider['complete_contract']['local'][o]['real_component_primitives'] for o in programs))
ck('actual_pre_post_wrapper_sweeps',all(sum(e[0]=='residual_adapter' and e[1]=='pre' for e in events)==contract['local'][o]['pre_wrappers']==240 and sum(e[0]=='residual_adapter' and e[1]=='post' for e in events)==contract['local'][o]['post_wrappers']==240 for o,events in programs.items()))
ck('own_local_prefix_guard',max(F(v['prefix_l1']) for v in recount.values())<2**68)
children=sum(int(v) for v in provider['expected_profile'].values());macros=max(v['scalar_macros'] for v in recount.values())
adapters=16*(macros+children+704+8)+64*73
primitive=max(v['real_component_primitives'] for v in recount.values())+adapters*64*74**3
ck('own_local_complete_invoice',adapters==contract['local_adapters']==387056 and primitive==contract['local_primitive_bound']==10038040553630 and primitive<2**48)
deps=['r480-selected-native-recovery.md','pr799_recovered_finite_controller.py','r480-selected-recovery-source/manifest.json']
out=dict(schema='r480-earlier-selected-native-recovery/1',status='fresh_source_native_recovery_only_no_whole_runtime_bound',prs=[1042,1094],earlier_own_heads=heads,recovery_artifact_head=manifest[0]['head'],recovery_artifact_pr=1129,recovery_scope='The later archive supplies bytes whose exact semantic and orientation hashes were already selected by each earlier own SPEC. No later owner profile, word modification, rank supplier or runtime estimate is transferred.',selected_canonical_semantic_sha256=identity(canonical),selected_program_semantic_sha256=identity(programs),orientation_hashes={k:identity(v) for k,v in programs.items()},native_coordinate_rank=73,helpers=480,columns=704,selected_local_recount=recount,local_complete_adapters=adapters,local_primitive_bound=primitive,native_scalar_allcolumn_replayed=True,full_phase_or_normalized_wrapper_engine_rerun=False,whole_owner_or_whole_integer_upper=None,meaningful_lower=None,remaining_obligations=['Bind each own selected owner map, complete call order, parent geometry and bridge-aware windows.','Freshly assemble each own global profile, full literal invoice, finite stock/C0 and source-specific prefix reserve.','Apply the corrected stopped-reserve unequal-child recurrence and fresh seven-row early/own-record schedules, with independent review.'],checks_passed=len(checks),checks=checks,source_sha256=source_hashes,dependency_hashes={p:hs(R/p) for p in deps},script_sha256=hs(Path(__file__)))
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v) for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [enc(v) for v in o]
    return o
(R/'r480-selected-native-recovery.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks_passed':len(checks),'selected_program_semantic_sha256':identity(programs),'recount':recount},indent=2))
