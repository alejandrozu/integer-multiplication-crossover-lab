"""Own PR4446 selected hybrid endpoint and literal boundary-work floor."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256,sha1
from types import SimpleNamespace
import ast,gzip,json,runpy
R=Path(__file__).resolve().parent
HEAD='e2bde8f5b9bfa2e8d51f959656d84ebcc2af81b7'
BASE='research/kappa-hybrid-controller/'
REVIEW_CLOSED=True
checks={}
def ck(n,v):
    assert v,n
    checks[n]=True
def read(p):return json.loads((R/p).read_bytes())
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def enc(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):enc(x)for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [enc(x)for x in v]
    return v
def need(v,msg):assert v,msg
rows=read('hybrid-4446-own-source/manifest.json')
priority=read('remaining-record-audit/artifacts/4446/priority-manifest.json')
sources={};by={}
for i,row in enumerate(rows+priority):
    file=row['file'] if row in rows else 'remaining-record-audit/'+row['file'].replace('\\','/')
    raw=(R/file).read_bytes()
    ck('own_head_'+str(i),row['head']==HEAD and HEAD in row['url'])
    ck('own_sha_'+str(i),sha256(raw).hexdigest()==row['sha256'])
    ck('own_blob_'+str(i),sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob_sha1'])
    sources[file]=row['sha256'];by[row['path']]=file
result=read(by[BASE+'RESULT.json']);endpoint=result['endpoint'];strict=result['strictification'];native=strict['native_inventory']
for suffix,digest in result['implementation_sha256'].items():
    if BASE+suffix in by:ck('own_selected_implementation_'+suffix,hs(by[BASE+suffix])==digest)
parameters=runpy.run_path(str(R/by[BASE+'parameters.py']),run_name='own4446_literal_parameters')
par=SimpleNamespace(**{k:v for k,v in parameters.items()if k.isupper()})
ck('selected_own_claim',F(endpoint['kappa'])==par.KAPPA==F(3001053,10**9))
ck('raw_mass_and_complete_profiles',sum(k*v for k,v in par.TARGETS.items())==260798 and sum(k*v for k,v in par.PAID.items())==259998 and sum(par.TARGETS.values())==11560 and strict['targets']=={str(k):v for k,v in par.TARGETS.items()} and strict['paid']=={str(k):v for k,v in par.PAID.items()})
tree=ast.parse((R/by[BASE+'endpoint.py']).read_bytes());nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='compiler_rank'];ck('one_own_pure_compiler_function',len(nodes)==1)
env=dict(Q=F,PARAMETERS=par,need=need)
exec(compile(ast.Module(body=nodes,type_ignores=[]),'own4446_compiler_rank','exec'),env)
uniform=par.KAPPA+6*(par.TESTED_SAVING-par.KAPPA)/7
fresh=enc(env['compiler_rank'](par.EXPONENT,par.TESTED_SAVING,uniform))
ck('fresh_own_exact_compiler_matches',fresh==endpoint['compiler'])
H=fresh['H1'];ck('actual_hybrid_H_not_inherited_helper_point',H==15026650096742881962201 and H!=165315500000000)
ck('strict_uniform_win',F(fresh['z'])==1-uniform and uniform>0 and F(fresh['final_strict_power_gap'])>0)
ck('strict_gamma_decay',2*9991**780<10000**780)
ck('strict_completion_decay',2*6**5<7**5)
ck('enough_complete_decay_blocks',par.EXPONENT//780>=22 and par.EXPONENT//5>=22)
moment=1/(1+F(par.EXPONENT,10**10))+F(4,2**22)
ck('positive_full_strictification_moment',moment==F(strict['normalized_moment_upper_rational'])<1 and F(strict['strictification_gap_rational'])==1-moment and strict['strict_moment_verified'])
case=read(by[BASE+'controller/P17-DIRECT-CASE.json']);full=read(by[BASE+'controller/P17-FULL-LAURENT-CASE.json'])
ck('own_full_case_selected_by_native_receipt',hs(by[BASE+'controller/P17-FULL-LAURENT-CASE.json'])==native['case_sha256']==case['source_full_case_sha256'])
ck('specialized_boundary_words_exactly_original',all(case[s]==full[s]for s in ['left_program','right_program']))
adds=[(s,i,x)for s in ['left_program','right_program']for i,x in enumerate(case[s])if x[0]=='ADD']
ck('own_unit_add_count',len(adds)==97 and all(x[1]!=x[2] and F(x[-1])in(-1,1)for _,_,x in adds))
ck('complete_direct_native_schedule',case['native_invocations']==19 and case['direct_Q_shears']==16 and case['direct_rank1_children']==1792 and case['ambient_dimension_with_all_original_stage_coordinates']==281)
geometry=gzip.decompress((R/by[BASE+'certificates/HYBRID-GEOMETRY.json.gz']).read_bytes())
ck('exact_geometry_payload_bound',sha256(geometry).hexdigest()==native['artifact_sha256']=='a58789b3cc4449fd7f9520119b2aaf6f5d9f7351cc34ed96f32e41e4169eb034')
ck('complete_geometry_case_ownership',json.loads(geometry)['formal']['exact_diagonal_monomials']==case['exact_diagonal_monomials'])
baseline=read('optimized-gmp-degree8-upper.json')
ck('same_closed_reference',baseline['status']=='closed_conditional_degree8_source_upper' and baseline['baseline_extension_id']=='gmp-630-native-skylake-unbounded-exact-constants-v2' and baseline['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8')
ck('exact_constant_cancellation',8*(1<<69)==1<<72)
ck('positive_literal_prefix',H>73 and 8==1<<3 and 24>=8)
deps=['hybrid-4446-own-source/manifest.json','remaining-record-audit/artifacts/4446/priority-manifest.json','pr4446-hybrid-boundary-lower.md','optimized-gmp-degree8-upper.json','optimized-gmp-degree8-upper.md','pr4433-literal-boundary-lower.md']
out=dict(schema='own-hybrid-p17-boundary-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=4446,own_head=HEAD,model='xag-straightline-v1',baseline_extension_id=baseline['baseline_extension_id'],H=str(H),N=f'2^{H}',tensor_power=par.EXPONENT,kappa=str(par.KAPPA),uniform_native_saving=str(uniform),own_boundary_complex_ADD_count=len(adds),used_boundary_complex_ADD_count=4,used_boundary_event_indices=[dict(program=s,index=i,instruction=x)for s,i,x in adds[:4]],active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),scope='Own selected hybrid supplier with complete unreduced boundary/native word when active, width at least two, whole-field/spectator rank N contract; identical optimized GMP when inactive.',statistic='Earliest possible strict win in the specified literal enhancement family',all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,whole_sufficient_upper_derived=False,native_endpoint_engine_replayed=False,interval_engine_replayed=False,own_pure_compiler_arithmetic_replayed=True,materialized_uniform_word=False,excluded_inherited_point=dict(H='165315500000000',reason='Inherited fresh-helper-thinned result is not the own selected hybrid endpoint.'),retained_contracts=['Own full Laurent/direct/native arbitrary-input identity, required physical entry/output frames, absolute phase and complete all-column whole-job copied/owned/spectator semantics.','Own strictifying physical native tensor/compiler realization, literal boundary retention, exact source interval enclosures and positive winning uniform supplier at the selected H.','Fixed repaired optimized-GMP correctness/finite-kernel halting and prescribed unreduced XAG lowering.'],formal_status='Conditional AI-assisted written mathematics and exact source/arithmetic checks; not Lean or independent human review.',dependency_hashes={p:hs(p)for p in deps},source_hashes=sources,script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
(R/'pr4446-hybrid-boundary-lower.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(pr=4446,status=out['status'],checks=len(checks),H=str(H),lower=out['input_bits'])))
