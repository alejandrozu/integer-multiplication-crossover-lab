"""Own punctured112 native/owner/invoice and direct-Gaussian cost instantiation."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import ast,copy,gzip,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):
 b=(R/p).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ck(n,v):assert v,n;checks[n]=True
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
manifest='pr523-punctured112-source/523-manifest.json';M=rd(manifest);head='a900f98be8ff2c09d3292b5112d4731dbd0c8438';pre='research/punctured112-global/';by={x['path'][len(pre):]:x for x in M};get=lambda p:by[p]['file']
for x in M:
 b=(R/x['file']).read_bytes();ck('own_primary_'+x['path'],x['pr']==523 and x['own_head']==head and sha256(b).hexdigest()==x['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['expected_api_blob'])
internal=rd(get('MANIFEST.json'));ck('all124_declared_inputs',internal['format']=='sha256-lf-text-v1'and len(internal['files'])==124 and set(internal['files'])<=set(by))
for p,x in internal['files'].items():
 b=(R/get(p)).read_bytes();ck('own_internal_'+p,sha256(b.replace(b'\r\n',b'\n')if x['mode']=='lf-text'else b).hexdigest()==x['sha256'])
expected=rd(get('EXPECTED.json'));invoice=rd(get('evidence/PREFIX-AND-INVOICE.json'));hosted=rd(get('evidence/hosted/HOSTED.json'));template=rd(get('evidence/hosted/GLOBAL-TEMPLATE.json.gz'));local=rd(get('evidence/local/CANONICAL-WORD.json.gz'));program=rd(get('evidence/local/LOCAL-PROGRAMS.json.gz'));owner=rd(get('inputs/OWNERS112.json.gz'));plan=rd(get('inputs/ASYNC112-PLAN.json'));owneraudit=rd(get('evidence/OWNERS-AND-PROFILE.json'));assembly=rd(get('evidence/EXACT-ASSEMBLY.json'))
m=73;Wlive=expected['live'];P={int(k):v for k,v in expected['global_profile'].items()};mass=sum(k*v for k,v in P.items());kap=F(expected['kappa']);complex_lower=F(expected['complex_lower'])
ck('own_selected_kappa',kap==F(182243220215421,125000000000000000)==F(assembly['kappa']))
ck('own_selected_whole_template_hash',sha256(gzip.decompress((R/get('evidence/hosted/GLOBAL-TEMPLATE.json.gz')).read_bytes())).hexdigest()==expected['complex_template_sha256']==hosted['template_sha256']==invoice['template_sha256']==owneraudit['template_sha256'])
ck('own_native_shape',(local['v'],local['R'],local['h'],len(local['start']))==(112,560,9,784)and set(program)=={'forward','backward'}and all(len(p)==25242 for p in program.values()))
phasefile='vendor/pr514/inputs/work/complex-nine-native/DATA-PHASES.json';ph0=rd(get(phasefile));mapping=rd(get('evidence/local/PORT-MAPPING.json'))['new_to_old'];ph=copy.deepcopy(ph0);ph['ports']=112;ph['recipes']=[copy.deepcopy(ph0['recipes'][i])for i in mapping]
for i,z in enumerate(ph['recipes']):ck('own_restricted_phase_'+str(i),z['port']==mapping[i]and z['q']==local['ports'][i]);z['port']=i
ph['nonzero_stage_alignment_translations']=sum(bool(v)for z in ph['recipes']for e in z['stage_alignment']for v in e.values());ph['terminal_omission_controls_rejected']=112;ph['inherited_parent_exact_phase_polynomial_evaluations']=ph.pop('exact_phase_polynomial_evaluations');ph['restriction_method']='Each complete recipe is unchanged except its port index; the retained parent polynomial checks establish every selected equality.';ph['source_parent_sha256']=hs(get(phasefile));phasebytes=json.dumps(ph,sort_keys=True,separators=(',',':')).encode()+b'\n';phasepath='pr523-reconstructed-phase-recipe.json';(R/phasepath).write_bytes(phasebytes)
for p,h in hosted['source_artifacts'].items():
 rel='evidence/local/'+p.split('split-centres/',1)[1]if p.startswith('split-centres/')else None
 ck('own_hosted_selected_'+p,(hs(get(rel))if rel else hs(phasepath))==h)
ck('own_complete_profile_stock',(Wlive,expected['physical'],mass,m*Wlive-mass,max(P))==(7168,7738,520704,2560,48)and m*m>2*max(P)**2 and hosted['global_profile']==expected['global_profile']==owneraudit['paid_profile'])
ck('own_literal_owner_and_plan',len(owner)==40320 and len(template['calls'])==72 and len(plan['order'])==72 and template['hosting']['pooled_slots']==owner and template['hosting']['owner_map_sha256']==hs(get('inputs/OWNERS112.json.gz'))and template['async_schedule']['order']==plan['order'])
ck('own_retained_no_banks',template['bank_padding']['families']==[] and template['private_namespace']=={'centers':[7168,7176],'reserved_tableau':[7176,7736],'coefficient':[7736,7738]})
ck('own_source_invoice',all(invoice['strict_checks'].values())and invoice['conservative_pervertex_used']==1516291843612800 and invoice['finite']['physical_row_coefficient']==16467 and invoice['global_prefix_bits']==206<invoice['charged_prefix_bits']==512 and invoice['local_primitive_bound']<2**48)
for ori in program:ck('own_local_receipt_'+ori,invoice['local'][ori]['all_exact_columns']==784 and invoice['local'][ori]['all_560_dirty_helper_columns_restored']and invoice['local'][ori]['private_centres_and_coefficient_work_cleared'])
fullfile='pr523-full-fresh-replay.json';fresh=rd(fullfile)if(R/fullfile).exists()else None
if fresh:
 ck('fresh_unmodified_full_source_reconstruction',fresh['status']=='passed_unchanged_full_own_source_reconstruction'and fresh['exit_code']==0 and fresh['own_head']==head and fresh['source_manifest_sha256']==hs(manifest)and fresh['source_code_modified']is False)
 derived={x['original_work_path']:x for x in fresh['derived_artifacts']}
 for x in fresh['derived_artifacts']:ck('fresh_retained_payload_'+x['original_work_path'],hs(x['file'])==x['sha256'])
 for rel,primary in [('local112/LOCAL-PROGRAMS.json.gz','evidence/local/LOCAL-PROGRAMS.json.gz'),('local112/CANONICAL-WORD.json.gz','evidence/local/CANONICAL-WORD.json.gz')]:ck('fresh_selected_native_semantics_'+rel,gzip.decompress((R/derived[rel]['file']).read_bytes())==gzip.decompress((R/get(primary)).read_bytes()))
 ck('fresh_selected_phase_payload',hs(derived['base112/work/complex-nine-native/DATA-PHASES.json']['file'])==hs(phasepath))
 for key in ['RESULT.json','STEPS.json','audit/PREFIX-AND-INVOICE.json','audit/OWNERS-AND-PROFILE.json','audit/INDEPENDENT112-RAW-AUDIT.json','audit/ASYNC-AUDIT.json','audit/EXACT-ASSEMBLY.json']:
  x=derived[key];ck('fresh_artifact_'+key,hs(x['file'])==x['sha256'])
 result=rd(derived['RESULT.json']['file']);ck('all14_own_and13_predecessor_stages',result['all_own_stages']==14 and result['pinned_predecessor_stages']==13 and all(x['exit']==0 for x in result['steps'])and F(result['kappa'])==kap)
 finv=rd(derived['audit/PREFIX-AND-INVOICE.json']['file']);ck('fresh_complete_invoice_exact',finv==invoice)
 fowner=rd(derived['audit/OWNERS-AND-PROFILE.json']['file']);ck('fresh_complete_owner_values',all(fowner[k]==owneraudit[k]for k in ['paid_profile','live','physical','rank_mass','deficit','hosted_residuals','banked_residuals','all_784_owners_per_call_distinct','actual_helper_owner_charts','actual_73column_sigmas','cross_replica_helper_roles','explicit_idle_remainder_children','source_idle_children_charged']))
ck('closure_requires_full_own_replay',not REVIEW_CLOSED or fresh is not None)
component=rd('gaussian-only-parameter-ledger.json');ck('closed_noBIT_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and component['ordinary_BIT_supplier_consumed']is False and component['invented_BIT_saving']is None)
for p,h in component['dependency_hashes'].items():ck('component_'+p,hs(p)==h)
spec=importlib.util.spec_from_file_location('own523_reduced_gaussian',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(spec);spec.loader.exec_module(G)
names={'divup','series_log_ratio','logint','expint','powint','moment'};source=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(source.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names];ck('independent_directed_functions',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(source),'exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(kap+complex_lower)/2;iv_early=moment(eta_early);iv_record=moment(eta_record)
ck('own_positive_coarse_moment',0<iv_early[0]<=iv_early[1]<1 and 1-iv_early[1]>F(1,2000))
ck('own_interior_record_moment',kap<eta_record<complex_lower and iv_record[1]<1 and 1-iv_record[1]>F(1,2**100))
group=2**(36*36)
for j in range(1,37):group*=2**(2*j)-1
stock=group*expected['physical'];streamed=group*mass;Esource=2**100000
ck('own_semantic_height',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
for kind,iv in [('early',iv_early),('record',iv_record)]:
 bound=-(-(1/(1-iv[1])).numerator//(1/(1-iv[1])).denominator);coefficient=2**32*m**4*(Esource+stock+streamed+1)**2*(1+bound)**2*20162**2
 ck(kind+'_own_complete_work_coefficient',bound<2**100 and coefficient<2**220000)
early=G.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001);record=G.finite_branch(kap,eta_record,10**8,400000001,2**59,record=True)
for kind,o in [('early',early),('record',record)]:ck(kind+'_fresh_reduced_runtime',len(o['checks'])==32 and all(o['checks'].values())and o['ordinary_BIT_supplier_consumed']is False and 'bit_saving'not in json.dumps(o['new_outer_parameters']))
contracts=['Own exact required-entry/output all-column native phase realizations, complete row covers/common-label mutable-basis interfaces, owned erasure and all-size compiler semantics. Fresh14-stage replay checks finite native/frame/phase/owner/invoice/outer source implementations; universal analytic/physical interfaces remain hypotheses.','Concrete normalized Gaussian/finite-LDU/narrow-gap/cyclic-border/fine-prime/exact-recovery and fixed repaired optimized-GMP correctness/halting contracts.','New direct Gaussian/Fermat circuit realization of the exact selected punctured112 source core. Original optional493ordinaryBIT construction is not consumed or asserted freshly replayed.']
deps=['pr523-punctured-gaussian-upper.md',manifest,phasepath,'replay_pr523_full_source.py','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','pr531_finite_controller_upper.py','pr531-finite-controller-upper.md','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
if fresh:deps.append(fullfile);deps.extend(x['file']for x in fresh['derived_artifacts'])
common=dict(pr=523,own_head=head,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(kap),ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,source_equivalent_numeric_realization=True,retained_contracts=contracts,source_sha256={x['file']:x['sha256']for x in M},dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks.copy(),original_full_own_source_replay_completed=fresh is not None,fresh_selected_gzip_raw_containers_identical={rel:hs(derived[rel]['file'])==hs(get(primary))for rel,primary in [('local112/LOCAL-PROGRAMS.json.gz','evidence/local/LOCAL-PROGRAMS.json.gz'),('local112/CANONICAL-WORD.json.gz','evidence/local/CANONICAL-WORD.json.gz')]}if fresh else None,source_gzip_comparison_scope='Own source PORTABILITY/README permits regenerated compression/header differences; complete decompressed selected native objects and actual orientation/template commitments must agree exactly.')
native=dict(native_coordinate_rank=73,own_live_fields=Wlive,own_physical_fields=expected['physical'],own_paid_profile=P,own_rank_mass=mass,own_rank_surplus=2560,source_finite_invoice=invoice,source_template_sha256=expected['complex_template_sha256'],selected_program_file=get('evidence/local/LOCAL-PROGRAMS.json.gz'),selected_canonical_file=get('evidence/local/CANONICAL-WORD.json.gz'),selected_whole_template_file=get('evidence/hosted/GLOBAL-TEMPLATE.json.gz'),literal_owner_file=get('inputs/OWNERS112.json.gz'),literal_plan_file=get('inputs/ASYNC112-PLAN.json'),coarse_moment_interval=iv_early,record_moment_interval=iv_record)
for kind,o in [('native',native),('record-upper',record),('early-upper',early)]:
 o.update(common);o['schema']='own-pr523-punctured112-'+kind+'/1'
 if kind=='early-upper':o.update(early_effective_kappa='1/5000',record_tail_quantified=True,record_tail_certificate='pr523-punctured-gaussian-record-upper.json',record_tail_certificate_sha256=hs('pr523-punctured-gaussian-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='New counted directGaussian realization of same selected punctured112 core, not literal historical dual-supplier replay.',piecewise_description='Existence witness uses repairedGMP below sufficient early gate, counted own directGaussian early branch, then counted own same-core record tail; switches are not necessary lower bounds.')
 (R/f'pr523-punctured-gaussian-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
print('PASS',len(checks),'own523 source/finite/runtime checks; fullreplay',fresh is not None)
