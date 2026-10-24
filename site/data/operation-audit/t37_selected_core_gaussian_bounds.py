"""Fresh own1009/1019 direct-Gaussian costs from exact selected T37 inputs."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
REVIEW_CLOSED=True
checks={};prefix=''
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(k,v):assert v,prefix+k;checks[prefix+k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
component=rd('gaussian-only-parameter-ledger.json')
ck('closed_reduced_Gaussian_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed'])
for p,h in component['dependency_hashes'].items():ck('component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('own_T37_reduced_Gaussian',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
binding_file='t37-refinement-source-bindings.json';binding=rd(binding_file)
ck('own_source_binding_builder',binding['schema']=='own-T37-refinement-native-source-bindings/1'and binding['status']=='passed_own_source_selection_and_complete_component_identity'and binding['script_sha256']==hs('t37_refinement_source_bindings.py')and all(binding['checks'].values()))
ck('exact_two_source_cases',{x['pr']for x in binding['rows']}=={1009,1019}and len(binding['rows'])==2)
names={'divup','series_log_ratio','logint','expint','powint','moment'}
defs=[x for x in ast.parse((R/'pr531_finite_controller_upper.py').read_bytes()).body if isinstance(x,ast.FunctionDef)and x.name in names]
ck('frozen_pure_directed_interval_engine',{x.name for x in defs}==names)
exec(compile(ast.Module(body=defs,type_ignores=[]),'own_T37_exact_interval_engine','exec'),globals())
SCALE=1<<384;ln2=series_log_ratio(2,1);rows=[]
for own in binding['rows']:
 pr=own['pr'];prefix=str(pr)+'_';start=set(checks)
 for group in ['source_sha256','dependency_hashes']:
  for p,h in own[group].items():ck('own_bound_'+p,hs(p)==h)
 nativefile=own['same_own_source_native_theorem_file'];native=rd(nativefile);invoice=rd(own['same_source_finite_invoice_file']);plan=rd(own['same_source_numeric_plan_file'])
 ck('exact_closed_native_identity',hs(nativefile)==own['same_own_source_native_theorem_sha256']and native['pr']==942 and native['status']=='closed_conditional_upper_only'and own['native_same_complete_source_inputs']and not own['numerical_cutoff_transferred'])
 ck('exact_complete_profile_and_invoice',own['native_coordinate_rank']==native['native_coordinate_rank']==73 and invoice==native['invoice']and own['paid_profile']==invoice['paid_profile']and own['productive_live']==invoice['live']==33152 and own['physical_families']==invoice['physical']==33666)
 ck('selected_program_and_physical_owners',own['selected_program_semantic_sha256']==native['selected_program_semantic_sha256']==plan['selected_program_semantic_sha256']and own['own_owner_content_sha256']==native['owners_content_sha256']==plan['owners_content_sha256'])
 ck('complete_T37_payload_and_row',invoice['calls']==333 and invoice['global_prefix_bits']==779 and invoice['charged_prefix_bits']==1024 and invoice['row_prefix_extra']==2048 and invoice['physical_row_coefficient']==17495<20161 and invoice['retained_previous_invoice']is None)
 ck('complete_G_E_C0_envelopes',invoice['router_bits']<30000 and invoice['literal_bits']<100000 and invoice['source_G_upper']=='2^30000'and invoice['source_E_upper']=='2^100000'and invoice['source_C0']=='2^210000')
 m=73;Wlive=invoice['live'];P={int(k):v for k,v in invoice['paid_profile'].items()};mass=sum(r*n for r,n in P.items())
 ck('own_raw_surplus_and_halving',mass==invoice['paid_rank_mass']==2408256 and m*Wlive-mass==invoice['rank_surplus']==11840 and max(P)==48 and m*m>2*max(P)**2)
 declared=rd(f't37-source-refinement-cases/{pr}-declared-inputs.json');baseline_file=next(a['file']for a in declared if a['path']=='research/community-frontier942-audit/ASSEMBLY.json');baseline=rd(baseline_file)
 kappa=F(own['kappa_record']);native_lower=F(baseline['complex_lower'])
 ck('own_source_moment_endpoint',baseline['complex_profile']==own['paid_profile']and native_lower==F('416181814685169713943/250000000000000000000000')and 0<kappa<native_lower)
 replay=rd(own['source_arithmetic_replay_file'])
 ck('own_source_replay_scope_retained',replay['pr']==pr and replay['own_head']==own['own_head']and replay['returncode']==0 and not replay['full_native_or_supplier_replayed'])
 if pr==1009:ck('own_bootstrap_contribution_not_discarded',replay['unchanged_original_source_executed']and kappa==F('1661960547713947/1000000000000000000'))
 else:ck('own_finer_record_target',not replay['full_original_verifier_executed']and not replay['full_876_source_inventory_replayed']and replay['all47_strict_constraints_pass']and kappa==F('1661960547713947858091/1000000000000000000000000'))
 fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(kappa+native_lower)/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
 ck('fresh_early_taxed_moment',earlyiv[1]<F(1695000,1696009)<1)
 ck('fresh_own_record_taxed_moment',kappa<eta_record<native_lower and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
 group=2**(36*36)
 for j in range(1,37):group*=2**(2*j)-1
 stock=group*invoice['physical'];streamed=group*mass;Esource=2**100000
 ck('same_complete_semantic_guard',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
 for tag,iv in [('early',earlyiv),('record',recordiv)]:
  reciprocal=ceil(1/(1-iv[1]));coefficient=2**32*m**4*(Esource+stock+streamed+1)**2*(1+reciprocal)**2*20162**2
  ck(tag+'_fresh_allsize_coefficient',reciprocal<2**100 and coefficient<2**220000)
 early=G.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001)
 record=G.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)
 for tag,o in [('early',early),('record',record)]:
  ck(tag+'_fresh_all32_runtime_guards',len(o['checks'])==32 and all(o['checks'].values()))
  ck(tag+'_no_unused_BIT_supplier',not o['ordinary_BIT_supplier_consumed']and'bit_saving'not in o['new_outer_parameters'])
  ck(tag+'_own_input_width_mapping',int(o['upper_log2log2_integer'])==int(o['A'])*int(o['E'])-8)
 contracts=own['retained_contracts']+component['component_source_interfaces_required']+['This new direct Gaussian/Fermat realization uses the exact own explicitly selected942 T37 core. It does not execute or quantify the original six-/seven-level affine bootstrap algorithm; no cost benefit of the source bootstrap-depth improvement is inferred.','Exact identity imports the named native/owner/invoice component only; own source arithmetic replay scope remains as recorded, with no new full native/phase or876-source verifier execution.']
 deps=['t37-selected-core-gaussian-bounds.md',binding_file,'t37_refinement_source_bindings.py','replay_t37_source_refinements.py',own['source_arithmetic_replay_file'],'gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','t21-t37-finite-controller-upper.md','t21_t37_finite_controller_upper.py',nativefile,own['same_source_finite_invoice_file'],own['same_source_numeric_plan_file'],'pr942-finite-controller-peer-review.json','pr942-finite-controller-source-peer-review.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
 dep={p:hs(p)for p in deps};dep.update(own['dependency_hashes'])
 base=dict(pr=pr,own_head=own['own_head'],source_head=own['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(kappa),native_coordinate_rank=73,not_uniform_2_to_H=True,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,source_selected_core_reuse=True,source_contribution_preserved=True,original_bootstrap_cost_realized_by_this_certificate=False,selected_native_theorem=nativefile,selected_native_theorem_sha256=hs(nativefile),original_source_arithmetic_scope=own['source_arithmetic_scope'],native_engine_independently_rerun_here=False,full_phase_engine_rerun=False,retained_contracts=contracts,source_sha256=own['source_sha256'],dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks={k:v for k,v in checks.items()if k not in start})
 rf=f'pr{pr}-selected-t37-gaussian-record-upper.json';ro=dict(base,**record,schema='own-selected-T37-Gaussian-record-upper/1');(R/rf).write_text(json.dumps(enc(ro),indent=2)+'\n',encoding='utf8')
 ef=f'pr{pr}-selected-t37-gaussian-early-upper.json';eo=dict(base,**early,schema='own-selected-T37-Gaussian-early-upper/1',early_effective_kappa='1/5000',record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Freshly counted own-source-selected T37 direct Gaussian realization at that own record kappa; not a quantitative threshold for the historical affine bootstrap.',piecewise_description='Identical repaired reference below the sufficient early gate, then counted selected-core early circuit and quantified own-record circuit after its sufficient gate. No switch is a natural crossover lower bound.');(R/ef).write_text(json.dumps(enc(eo),indent=2)+'\n',encoding='utf8')
 nf=f'pr{pr}-selected-t37-gaussian-native.json';no=dict(base,schema='own-selected-T37-Gaussian-native-parameters/1',source_binding=own,own_complete_invoice=invoice,coarse_moment_interval=[str(x)for x in earlyiv],native_record_saving=str(eta_record),record_moment_interval=[str(x)for x in recordiv],inherited_fallback_tax_denominator='10000000000000000',inherited_fallback_tax_removed=False);(R/nf).write_text(json.dumps(enc(no),indent=2)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=own['own_head'],kappa_record=str(kappa),native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None,source_selected_core_reuse=True,original_bootstrap_cost_realized_by_this_certificate=False))
prefix=''
out=dict(schema='own-selected-T37-Gaussian-cost-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'t37-selected-core-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8')
print('PASS',len(checks),'fresh own1009/1019 selected-core Gaussian cost checks')
