"""Durable exact U8 byte recovery for four earlier own SPEC commitments.

This is programme recovery, not own-provider selectedness, a complete source
invoice, an operator phase theorem or a numerical crossover.
"""
from pathlib import Path
import ast,gzip,hashlib,json,math
R=Path(__file__).resolve().parent
def hs(f):return hashlib.sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 p=R/f;b=p.read_bytes();return json.loads(gzip.decompress(b)if p.suffix=='.gz'else b)
def ident(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
checks={}
def ck(k,v):assert v,k;checks[k]=True
source='u8_selected_native_recovery.py';tree=ast.parse((R/source).read_text());nodes=[]
for node in tree.body:
 if isinstance(node,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='deps'for t in node.targets):break
 if isinstance(node,ast.With)and any(isinstance(t.context_expr,ast.Call)and isinstance(t.context_expr.func,ast.Attribute)and t.context_expr.func.attr=='TemporaryDirectory'for t in node.items):
  node.body+=ast.parse("durable={n:(out/n).read_bytes()for n in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','LOCAL-CHECKS.json','SCALAR-FRAME-AUDIT.json']}").body
 nodes.append(node)
g={'__name__':'exact_u8_archive_recovery','__file__':str(R/source)};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(R/source),'exec'),g)
ck('closed_source_arithmetic_native_checks',all(g['checks'].values()))
D=R/'u8-recovered-selected-native';D.mkdir(exist_ok=True);outputs=[]
historical='u8-recovered-selected-native/SCALAR-FRAME-AUDIT.historical-observed.json'
historical_sha='276bb56e2b79fcef35f2adbc0eb61afa1c5a279ffc6c051ae6d9db4099be9c83'
ck('preserved_original_observed_scalar_audit',hs(historical)==historical_sha)
fresh=json.loads(g['durable']['SCALAR-FRAME-AUDIT.json']);observed=rd(historical)
ck('only_named_wallclock_field_is_excluded',all(type(o['seconds'])in(int,float)and math.isfinite(o['seconds'])and o['seconds']>=0 for o in(fresh,observed)))
fresh_projection={k:v for k,v in fresh.items()if k!='seconds'}
observed_projection={k:v for k,v in observed.items()if k!='seconds'}
ck('every_other_scalar_frame_audit_field_exact',fresh_projection==observed_projection)
g['durable']['SCALAR-FRAME-AUDIT.json']=(json.dumps(fresh_projection,sort_keys=True,indent=2)+'\n').encode('utf8')
for n,b in g['durable'].items():
 p=D/n;p.write_bytes(b);o=rd(p.relative_to(R));outputs.append(dict(file=p.relative_to(R).as_posix(),sha256=hs(p.relative_to(R)),semantic_sha256=ident(o)))
canonical=rd('u8-recovered-selected-native/CANONICAL-WORD.json.gz');programs=rd('u8-recovered-selected-native/LOCAL-PROGRAMS.json.gz');orient={o:ident(v)for o,v in programs.items()};rows=[]
ledger=rd('remaining-record-audit/cost-coverage-ledger.json');lm={r['pr']:r for r in ledger['rows']}
for pr,specfile in [(869,'remaining-record-audit/artifacts/869/635d7237f8ab__SPEC.json'),(870,'remaining-record-audit/artifacts/870/7cb726737824__SPEC.json'),(962,'remaining-record-audit/artifacts/962/9dbaac104382__SPEC.json'),(991,'remaining-record-audit/artifacts/991/5adbe4872ae9__SPEC.json')]:
 spec=rd(specfile);provider=spec['providers']['gauge44'];ck(str(pr)+'_own_primary_SPEC',any(a.get('file')==specfile and a.get('sha256')==hs(specfile)for a in lm[pr]['verified_components']))
 ck(str(pr)+'_complete_canonical_program_and_orientations',ident(canonical)==provider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and ident(programs)==provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and orient==provider['program_hashes'])
 rows.append(dict(pr=pr,own_head=lm[pr]['own_head'],own_SPEC_file=specfile,own_SPEC_sha256=hs(specfile),canonical_semantic_sha256=ident(canonical),program_semantic_sha256=ident(programs),orientation_sha256=orient,own_actual_verifier_selection_adjudicated=False,whole_cost_admitted=False))
deps={source:hs(source),'u8-selected-native-recovery.json':hs('u8-selected-native-recovery.json'),'u8-selected-native-recovery.md':hs('u8-selected-native-recovery.md'),'pr799_recovered_finite_controller.py':hs('pr799_recovered_finite_controller.py')};deps.update({f:hs(f)for f in g.get('paths799',{}).values()if isinstance(f,str)and(R/f).is_file()})
parent=rd('u8-selected-native-recovery.json')
deps[historical]=historical_sha
for f,h in parent['source_sha256'].items():ck('source_'+f,hs(f)==h)
out=dict(schema='exact-U8-durable-native-byte-recovery/1',status='actual_exact_own_commitments_recovered_no_bound',rows=rows,outputs=outputs,source_sha256=parent['source_sha256'],dependency_hashes=deps,checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__).name),scope='The already source-bound actual U8 recipe/transport/emitter/scalar checks recover durable byteobjects matching each earlier own SPEC full canonical/program/two-orientation digest. Later source archives supply exact bytes only. Own actual provider selection, complete PLAN/OWNERS/invoice, phase/operator contracts and any runtime bound remain separate. No performance equivalence is inferred.')
out['observational_normalization']=dict(artifact='SCALAR-FRAME-AUDIT.json',excluded_fields=['seconds'],retained_original_observed_file=historical,retained_original_observed_sha256=historical_sha,every_other_field_compared_exactly=True,canonical_program_orientation_and_LOCAL_CHECKS_bytes_changed=False,reason='Elapsed wall-clock seconds are observational metadata, not a scalar/frame check or numerical cost input. Only this top-level field is omitted from the deterministic reproduced audit; the complete originally observed audit is retained verbatim.')
(R/'u8-exact-earlier-selected-byte-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'exact U8 own-byte joins',len(rows),'no cost admission')
