"""Versioned explicit-source-selected core applications; exact own targets only."""
from pathlib import Path
from hashlib import sha1,sha256
from fractions import Fraction as F
import ast,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;ADMITTED={1673};checks={};prefix=''
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(k,v):assert v,prefix+k;checks[prefix+k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def at(o,p):
 for k in p:o=o[k]
 return o
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
inputs_file='source-selected-core-application-inputs-v1.json';snap=rd(inputs_file);ck('exact_versioned_whitelist',snap['schema']=='explicit-source-selected-core-cost-inputs/1'and set(snap['exact_admitted_PRs'])==ADMITTED=={a['pr']for a in snap['rows']}and len(snap['rows'])==len(ADMITTED))
component=rd('gaussian-only-parameter-ledger.json');ck('closed_reduced_Gaussian_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed'])
for p,h in component['dependency_hashes'].items():ck('component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('own_core_application_Gaussian_arithmetic',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
names={'divup','series_log_ratio','logint','expint','powint','moment'};defs=[a for a in ast.parse((R/'pr531_finite_controller_upper.py').read_bytes()).body if isinstance(a,ast.FunctionDef)and a.name in names];ck('frozen_pure_interval_engine',{a.name for a in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),'core_application_exact_interval','exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
rows=[]
for case in snap['rows']:
 pr=case['pr'];prefix=str(pr)+'_';start=set(checks);M=rd(case['own_source_manifest']);ownfiles={a['relative_package_path']:a for a in M['source_manifest']};source={}
 ck('actual_own_head_and_primary_manifest',M['pr']==pr and M['own_head']==case['own_head']and not M['original_source_verifier_executed']and M['script_sha256']==hs('fetch_pr1673_core_selection.py'))
 for rel,a in ownfiles.items():
  raw=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
  ck('actual_own_primary_'+rel,a['pr']==pr and a['own_head']==case['own_head']and '/'+case['own_head']+'/'in a['primary_url']and sha256(raw).hexdigest()==a['sha256']and blob==a['git_blob_sha1']and(a['expected_own_changed_Git_blob']is None or a['expected_own_changed_Git_blob']==blob));source[a['file']]=a['sha256']
 pkg=rd(ownfiles[case['authority_manifest_relative']]['file'])
 for rel,a in ownfiles.items():
  if rel!=case['authority_manifest_relative']:ck('authoritative_own_package_commitment_'+rel,pkg[rel]==a['sha256'])
 nativefile=case['native_certificate_file'];native=rd(nativefile);cr=rd(native['own_complete_census_file']);selection=next(a for a in rd(case['native_selection_inputs_file'])['selection_receipts']if a['pr']==case['native_selection_pr'])
 ck('named_native_component_closed_and_exact',native['pr']==case['native_selection_pr']==1661 and native['status']=='closed_conditional_upper_only'and native['native_coordinate_rank']==73 and native['own_head']==selection['own_head']and native['own_complete_census_sha256']==hs(native['own_complete_census_file']))
 for key in ['native_math_peer_file','native_source_peer_file']:
  pf=case[key];peer=rd(pf);passed=(peer.get('review_status','').startswith('PASS')if key=='native_math_peer_file'else peer.get('status')=='passed_independent_AI_source_selection_scope_review')
  ck('closed_native_peer_'+pf,passed and peer['pr']==native['pr']and peer['own_head']==native['own_head']and peer['reviewed_sha256'][nativefile]==hs(nativefile))
 for key in ['source_sha256','dependency_hashes']:
  for p,h in native[key].items():ck('named_native_'+p,hs(p)==h)
 declared=rd(ownfiles[case['supplier_declaration_relative']]['file'])['supplier'];binding=rd(ownfiles[case['native_binding_relative']]['file']);nativeprefix=case['native_package_relative'];own_mf=ownfiles[nativeprefix+'/MANIFEST.json'];own_spec=ownfiles[nativeprefix+'/new/SPEC.json'];sm=rd(own_mf['file']);spec=rd(own_spec['file'])
 ck('explicit_named_original_supplier_commit',declared['pr']==binding['source_pr']==native['pr']and declared['commit']==binding['source_head']==native['own_head']and declared['manifest_sha256']==binding['source_manifest_sha256']==own_mf['sha256']==selection['manifest_sha256'])
 ck('exact_original_manifest_and_selected_SPEC',sm['new/SPEC.json']==own_spec['sha256']==selection['authority_sha256']==cr['own_SPEC_sha256']and hs(cr['own_SPEC_file'])==own_spec['sha256']and hs(selection['manifest_file'])==own_mf['sha256'])
 vr=(R/ownfiles[case['own_verifier_relative']]['file']).read_text(encoding='utf8');tree=ast.parse(vr);assigns=[a for a in tree.body if isinstance(a,ast.Assign)and any(isinstance(t,ast.Name)and t.id in['PIN','SOURCE_REL','EXPECTED_KAPPA']for t in a.targets)];env={'Q':F,'Path':Path};exec(compile(ast.Module(body=assigns,type_ignores=[]),'own_exact_selection_declarations','exec'),env)
 ck('literal_actual_own_verifier_selects_named_source',env['PIN']==native['own_head']and env['SOURCE_REL'].as_posix()==nativeprefix and "b['source_head']==PIN"in vr and "b['source_manifest_sha256']==sha(source/'MANIFEST.json')"in vr and "Q(b['recomposed_final_kappa']['strassen'])==EXPECTED_KAPPA"in vr)
 arithmetic=rd(ownfiles[case['own_record_source_relative']]['file']);kappa=F(at(arithmetic,case['own_record_json_pointer']));native_endpoint=F(at(arithmetic,case['own_native_endpoint_json_pointer']))
 ck('actual_own_record_pointer_and_verifier',kappa==env['EXPECTED_KAPPA']==F(binding['recomposed_final_kappa']['strassen'])==F(case['quoted_kappa_fraction'])and kappa==F('1677160151714381/1000000000000000000'))
 ck('explicit_original_outer_not_claimed_costed',case['source_selection_kind']=='explicit_original_commit_manifest_and_copied_selected_SPEC'and case['original_outer_algorithm_costed']is False)
 P={int(k):v for k,v in native['own_role_receipt']['profile'].items()};inv=native['own_invoice'];role=native['own_role_receipt'];m=73;Wlive=inv['live'];mass=sum(k*v for k,v in P.items())
 ck('own_selected_complete_profile_not_selection_rule',{str(k):v for k,v in P.items()}==arithmetic['profile']==binding['native_profile']==spec['expected']['global_profile']and arithmetic['m']==m and arithmetic['W']==Wlive==66304 and 73*Wlive-mass==role['rank_surplus']>0 and 73**2>2*max(P)**2)
 ck('complete_native_invoice_reattached',inv['retained_previous_invoice']is None and inv['router_bits']<30000 and inv['literal_bits']<100000 and role['physical_row_coefficient']==19545<20161 and role['prefix_bits']==1441<role['charged_prefix_bits']==2048 and len(cr['negative_controls'])==6)
 ck('own_admitted_endpoint_inside_selected_native',kappa<native_endpoint<=F(cr['complex_lower'])and native_endpoint==F(binding['complex_lower_used']))
 fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(kappa+native_endpoint)/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
 ck('fresh_early_taxed_moment',earlyiv[1]<F(1695000,1696009)<1);ck('fresh_own_record_taxed_moment',recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
 group=2**(36*36)
 for j in range(1,37):group*=2**(2*j)-1
 stock=group*inv['physical'];streamed=group*mass;Esource=2**100000
 ck('complete_semantic_guard',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
 for tag,iv in [('early',earlyiv),('record',recordiv)]:
  reciprocal=ceil(1/(1-iv[1]));coefficient=2**32*m**4*(Esource+stock+streamed+1)**2*(1+reciprocal)**2*20162**2;ck(tag+'_fresh_whole_allsize_coefficient',reciprocal<2**100 and coefficient<2**220000)
 early=G.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001);record=G.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)
 for tag,o in [('early',early),('record',record)]:ck(tag+'_fresh_complete32_runtime_checks',len(o['checks'])==32 and all(o['checks'].values())and not o['ordinary_BIT_supplier_consumed']and'bit_saving'not in o['new_outer_parameters'])
 contracts=native['retained_contracts']+['This is a new direct Gaussian/Fermat realization of the explicitly selected1661 core, not a cost proof or validation of every theorem of the original capped phase-cell fusion outer algorithm. No optional matrix9/4 premise or original BIT supplier is consumed.','Concrete normalized Gaussian/finite-LDU/narrow-gap/cyclic-border/fine-prime/recovery and repaired reference correctness/finite-kernel halting remain the closed component interfaces; no arbitrary-scale accretive theorem is used.']
 deps=['source-selected-core-applications-v1.md',inputs_file,case['own_source_manifest'],'fetch_pr1673_core_selection.py',nativefile,case['native_math_peer_file'],case['native_source_peer_file'],case['native_selection_inputs_file'],native['own_complete_census_file'],'gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
 dep={p:hs(p)for p in deps};dep.update(native['dependency_hashes']);source.update(native['source_sha256'])
 base=dict(pr=pr,own_head=case['own_head'],source_head=case['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(kappa),native_coordinate_rank=73,not_uniform_2_to_H=True,source_selected_core_reuse=True,original_outer_algorithm_costed=False,original_outer_contribution=case['source_contribution'],optional_matrix_9_4_premise_used=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,native_engine_independently_rerun_here=False,source_selection_kind=case['source_selection_kind'],named_native_theorem_file=nativefile,named_native_theorem_sha256=hs(nativefile),retained_contracts=contracts,source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks={k:v for k,v in checks.items()if k not in start})
 rf=f'pr{pr}-explicit-core-gaussian-record-upper.json';ro=dict(base,**record,schema='own-explicit-core-Gaussian-record-upper/1');(R/rf).write_text(json.dumps(enc(ro),indent=2)+'\n',encoding='utf8')
 ef=f'pr{pr}-explicit-core-gaussian-early-upper.json';eo=dict(base,**early,schema='own-explicit-core-Gaussian-early-upper/1',early_effective_kappa='1/5000',record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Freshly counted own source-selected1661 Gaussian realization at the exact own1673 exponent target; original capped phase-fusion outer schedule not costed.',piecewise_description='Identical repaired reference below sufficient gate, then counted source-core early and quantified own-record circuits. Chosen switches are not natural lower bounds.');(R/ef).write_text(json.dumps(enc(eo),indent=2)+'\n',encoding='utf8')
 nf=f'pr{pr}-explicit-core-gaussian-native.json';no=dict(base,schema='own-explicit-core-Gaussian-native-parameters/1',own_source_authorities=case,selected_core_finite_profile=P,named_core_invoice=inv,coarse_moment_interval=[str(v)for v in earlyiv],native_record_saving=str(eta_record),record_moment_interval=[str(v)for v in recordiv],inherited_fallback_tax_denominator='10000000000000000',inherited_fallback_tax_removed=False);(R/nf).write_text(json.dumps(enc(no),indent=2)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=case['own_head'],kappa_record=str(kappa),native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None,source_selected_core_reuse=True,original_outer_algorithm_costed=False))
prefix='';out=dict(schema='explicit-own-source-selected-core-cost-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',exact_admitted_PRs=sorted(ADMITTED),rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'source-selected-core-applications-v1.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'exact-authority own selected-core fresh whole costs',sorted(ADMITTED))
