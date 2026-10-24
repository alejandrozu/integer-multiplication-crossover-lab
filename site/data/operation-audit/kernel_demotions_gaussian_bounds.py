"""Own dynamic1154/1176 counted Gaussian uppers; no prior invoice/cutoff."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={};prefix=''
def hs(f):return hashlib.sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(n,v):assert v,prefix+n;checks[prefix+n]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return{str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return[enc(v)for v in o]
 return o
component=rd('gaussian-only-parameter-ledger.json');ck('closed_reduced_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed'])
for f,h in component['dependency_hashes'].items():ck('component_'+f,hs(f)==h)
s=importlib.util.spec_from_file_location('closed_reduced_gaussian',R/'gaussian_only_parameter_ledger.py');reduced=importlib.util.module_from_spec(s);s.loader.exec_module(reduced)
names={'divup','series_log_ratio','logint','expint','powint','moment'};fp=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(fp.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names];ck('pure_exact_interval_functions',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(fp),'exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
batch=rd('kernel-demotions-counted-source-censuses.json');ck('complete_dynamic_own_censuses',batch['script_sha256']==hs('kernel_demotions_native_owner_invoice.py')and all(batch['checks'].values())and{r['pr']for r in batch['rows']}=={1154,1176})
review=rd('selected-provider-review-evidence-screen.json');rm={r['pr']:r for r in review['rows']};scope=rd('selected-provider-canonical-contradiction-scope-read.json');scm={r['pr']:r for r in scope['rows']};ck('counterexample_scope_screen',scope['source_screen_sha256']==hs('selected-provider-review-evidence-screen.json')and scope['summary']['exhibited_selected_native_frame_phase_counterexamples_found']==0)
observed=rd('kernel-demotions-original-full-replay.json')
ck('observed_original_full_source_replay',observed['status']=='passed_actual_original_native_owner_invoice_assembly'and{r['pr']for r in observed['runs']}=={1154,1176}and observed['script_sha256']==hs('run_kernel_demotions_original.py')and observed['execution_timeout_wrapper_sha256']==hs('kernel_demotions_timeout_bootstrap.py'))
for z in observed['runs']:
 ck(str(z['pr'])+'_observed_source_manifest',z['source_manifest_sha256']==hs(z['source_manifest_file'])and z['unchanged_original_verifier_exit_code']==0)
rows=[]
for entry in batch['rows']:
 pr=entry['pr'];prefix=str(pr)+'_';cr=rd(entry['own_census_file']);ck('own_census_binding',hs(entry['own_census_file'])==entry['own_census_sha256']and cr['own_head']==entry['own_head']and cr['script_sha256']==hs('kernel_demotions_native_owner_invoice.py'))
 primary=dict(cr['source_sha256']);cached={}
 for f,h in primary.items():ck('actual_own_primary_'+f,hs(f)==h)
 for f,h in cr['dependency_hashes'].items():ck('pure_module_'+f,hs(f)==h)
 ck('complete_source_manifest',cr['source_manifest_sha256']==hs(cr['source_manifest_file']))
 ck('fresh_numeric_PLAN',hs(cr['numeric_PLAN_file'])==cr['numeric_PLAN_sha256']and not cr['historical_complete_PLAN_byte_identity_claimed'])
 for n in cr['selected_native_censuses']:
  ck(n['provider']+'_complete_actual_native_census',hs(n['census_file'])==n['census_sha256']and hs(n['program_file'])==n['program_file_sha256']and hs(n['canonical_file'])==n['canonical_file_sha256']);cached[n['census_file']]=n['census_sha256']
  c=rd(n['census_file']);ck(n['provider']+'_own_partial_entry_and_final_widths',[b-a for a,b in zip(n['initial_helper_ranks'],n['final_helper_ranks'])]==c['forward']['widths']and n['entering_flags']==[bool(x)for x in n['initial_helper_ranks']])
 rev=rm[pr];ck('own_source_contradiction_scope',rev['own_head']==cr['own_head']and pr not in scope['summary']['shared_analytic_qualification_entries'])
 for x in rev['matched_review_rows']:ck('review_primary_'+x['source_file'],hs(x['source_file'])==x['source_sha256']);primary[x['source_file']]=x['source_sha256']
 if any(x['literal_potential_contradiction_anchors']for x in rev['matched_review_rows']):ck('flagged_review_individually_read',pr in scm and scm[pr]['manual_scope_read'])
 inv=cr['invoice'];role=cr['role_receipt'];m=73;Wlive=inv['live'];P={int(k):v for k,v in role['profile'].items()};mass=sum(r*n for r,n in P.items());group=2**(36*36)
 for i in range(1,37):group*=2**(2*i)-1
 stock=group*inv['physical'];streamed=group*mass;Esource=2**100000
 ck('positive_surplus_and_halving',mass==role['rank_mass']and m*Wlive-mass==role['rank_surplus']>0 and max(P)<m and m*m>2*max(P)**2)
 ck('full_owned_work_stock_and_row',len(cr['negative_controls'])==6 and inv['retained_previous_invoice']is None and inv['router_bits']<30000 and inv['literal_bits']<100000 and role['physical_row_coefficient']<20161 and role['prefix_bits']<role['charged_prefix_bits'])
 ck('full_semantic_height',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
 fallback=32*m*m*sum(P.values());kappa=F(cr['kappa_record']);eta_early=F(1,1000);eta_record=(kappa+F(cr['complex_lower']))/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
 ck('own_early_taxed_moment',earlyiv[1]<F(1695000,1696009)<1)
 ck('own_record_taxed_interior_moment',kappa<eta_record<F(cr['complex_lower'])and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
 for kind,iv in [('early',earlyiv),('record',recordiv)]:
  reciprocal=ceil(1/(1-iv[1]));C=2**32*m**4*(Esource+stock+streamed+1)**2*(1+reciprocal)**2*20162**2;ck(kind+'_own_complete_finite_work_constant',reciprocal<2**100 and C<2**220000)
 early=reduced.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001);record=reduced.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)
 for kind,b in [('early',early),('record',record)]:ck(kind+'_fresh_all_32_outer_and_runtime_checks',len(b['checks'])==32 and all(b['checks'].values())and not b['ordinary_BIT_supplier_consumed']and 'bit_saving'not in json.dumps(b['new_outer_parameters']))
 contracts=component['component_source_interfaces_required']+['Own required physical partial initial/output Gaussian operators, identity on spectators, absolute phases, bounded73-axis affine/even-Z4 monomial grammar and normalized completed-child identities remain explicit; scalar/rank checks alone do not prove them.','Own arbitrary dirty restoration, common-label, whole-call/all-column/all-size hosting and fixed group/compiler interfaces.','A new complete numeric parent and full operation invoice are priced; no historical full PLAN byte identity or old billed amount is claimed.','The original optional BIT supplier is not consumed by this direct Gaussian realization.']
 native=dict(native_coordinate_rank=73,own_complete_census_file=entry['own_census_file'],own_complete_census_sha256=entry['own_census_sha256'],selected_native_censuses=cr['selected_native_censuses'],own_invoice=inv,own_role_receipt=role,coarse_moment_interval=[str(x)for x in earlyiv],record_moment_interval=[str(x)for x in recordiv],native_record_saving=str(eta_record),record_tail_quantified=True,inherited_fallback_tax_denominator='10000000000000000',inherited_fallback_tax_removed=False,original_global_verifier_full_PASS_claimed=False,actual_original_components_observed_with_external_timeout_wrapper=True,source_equivalent_numeric_realization=True)
 deps=['kernel-demotions-gaussian-bounds.md','kernel-demotions-counted-source-censuses.json','kernel_demotions_native_owner_invoice.py','kernel-demotions-source/manifest.json','kernel-demotions-original-full-replay.json','run_kernel_demotions_original.py','kernel_demotions_timeout_bootstrap.py',cr['numeric_PLAN_file'],entry['own_census_file'],'gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','finite_selected_program_census.py','finite_actual_owner_census_v2.py','selected-provider-review-evidence-screen.json','selected-provider-canonical-contradiction-scope-read.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json'];dep={f:hs(f)for f in deps};dep.update(cached)
 for kind,b in [('native',native),('record-upper',record),('early-upper',early)]:
  b.update(schema='own-dynamic-kernel-demotions-Gaussian-'+kind+'/1',pr=pr,own_head=cr['own_head'],source_head=cr['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=cr['kappa_record'],early_effective_kappa='1/5000'if kind=='early-upper'else None,source_equivalent_numeric_realization=True,historical_complete_PLAN_byte_identity_claimed=False,original_global_verifier_full_PASS_claimed=False,literal_original_timeout_command_PASS_claimed=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,retained_contracts=contracts,source_sha256=primary,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks=checks.copy(),whole_instance_checks_passed=len(checks))
  if kind=='early-upper':b.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-dynamic-kernel-finite-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-dynamic-kernel-finite-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],piecewise_description='Own separately quantified source-core record tail; this sufficient domain is not an actual or natural first crossing.')
  (R/f'pr{pr}-dynamic-kernel-finite-{kind}.json').write_text(json.dumps(enc(b),indent=2)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=cr['own_head'],kappa_record=cr['kappa_record'],native_certificate=f'pr{pr}-dynamic-kernel-finite-native.json',early_upper_certificate=f'pr{pr}-dynamic-kernel-finite-early-upper.json',record_upper_certificate=f'pr{pr}-dynamic-kernel-finite-record-upper.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_quantified=True,meaningful_lower=None));print('PASS own dynamic kernel whole bound',pr,flush=True)
out=dict(schema='own-dynamic-kernel-demotions-Gaussian-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__).name));(R/'kernel-demotions-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'whole checks')
