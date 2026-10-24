"""Own two exact generated-PLAN T37 finite Gaussian uppers with actual selected typed native words and complete own physical inputs."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
ADMITTED={1131,1152}
checks={};prefix=''
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(n,v):assert v,prefix+n;checks[prefix+n]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [enc(v)for v in o]
    return o
component=rd('gaussian-only-parameter-ledger.json')
ck('closed_reduced_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed']and component['invented_BIT_saving']is None)
for p,h in component['dependency_hashes'].items():ck('reduced_component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('frozen_gaussian_reduced_component',R/'gaussian_only_parameter_ledger.py');reduced=importlib.util.module_from_spec(sp);sp.loader.exec_module(reduced)
names={'divup','series_log_ratio','logint','expint','powint','moment'};source=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(source.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names];ck('pure_exact_interval_functions',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(source),'exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
screen=rd('selected-provider-dispatch-v14.json');sm={r['pr']:r for r in screen['rows']};ck('frozen_source_dispatcher',screen['script_sha256']==hs('selected_provider_dispatch_v14.py'))
for p,h in screen['source_sha256'].items():ck('frozen_source_input_'+p,hs(p)==h)
for p,h in screen['dependency_hashes'].items():ck('source_module_'+p,hs(p)==h)
review=rd('selected-provider-review-evidence-screen.json');rm={r['pr']:r for r in review['rows']};scope=rd('selected-provider-canonical-contradiction-scope-read.json');scm={r['pr']:r for r in scope['rows']}
ck('canonical_semantic_scope_review',scope['source_screen_sha256']==hs('selected-provider-review-evidence-screen.json')and scope['summary']['exhibited_selected_native_frame_phase_counterexamples_found']==0)
meter_audit=rd('generated-t37-descriptive-counter-audit.json');meter_by={r['pr']:r for r in meter_audit['rows']}
ck('complete_cost_noninterference',meter_audit['status']=='checked_cost_noninterference_component'and meter_audit['script_sha256']==hs('generated_t37_descriptive_counter_audit.py')and all(meter_audit['checks'].values()))
for p,h in meter_audit['dependency_hashes'].items():ck('meter_component_'+p,hs(p)==h)
rows=[]
for pr in sorted(ADMITTED):
    prefix=str(pr)+'_';entry=sm[pr];ck('complete_own_numeric_inputs',entry['status']=='source_numeric_inputs_checked_not_yet_whole_cost_certificate')
    cr=rd(entry['own_census_file']);ck('own_census_and_SPEC',hs(entry['own_census_file'])==entry['own_census_sha256']and hs(cr['own_SPEC_file'])==cr['own_SPEC_sha256']and cr['own_head']==entry['own_head'])
    ownspec=rd(cr['own_SPEC_file']);primary={cr['own_SPEC_file']:cr['own_SPEC_sha256']};cached={}
    ck('actual_entry_meter_source_value_and_cost_noninterference',meter_by[pr]['own_census_sha256']==entry['own_census_sha256']and meter_by[pr]['source_declared_entering_helper_roles']==cr['descriptive_entering_counter']['source_declared_entering_helper_roles']and not meter_by[pr]['used_by_new_cost_stock_or_precision'])
    selector_file=cr['own_source_selector_file'];selector=rd(selector_file);ownM=selector['MANIFEST_file'];M=rd(ownM);prepfile=selector['prepare_file'];controllerfile=selector['controller_file'];prep=(R/prepfile).read_text();ctrl=(R/controllerfile).read_text()
    recoveryfile=selector['source_recovery_receipt'];recovery=rd(recoveryfile);rr=next(a for a in recovery['rows']if a['pr']==pr)
    ck('exact_own_generated_PLAN_recovery',recovery['status']=='closed_exact_own_SPEC_PLAN_byte_recovery'and recovery['checks_passed']==203 and all(recovery['checks'].values())and recovery['script_sha256']==hs('recover_t37_generated_selected_plans.py')and hs(recoveryfile)==selector['source_recovery_receipt_sha256']and rr['own_head']==cr['own_head']and rr['own_SPEC_sha256']==cr['own_SPEC_sha256']and rr['PLAN_sha256']==selector['PLAN_sha256']==ownspec['data']['plan_sha256']and not recovery['historical_parent_template_byte_identity_claimed']and not recovery['original_full_global_verifier_PASS_claimed'])
    ck('own_actual_prepare_controller_MANIFEST_select_SPEC_PLAN_OWNERS',selector['own_head']==cr['own_head']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and M['prepare.py']==hs(prepfile)==selector['prepare_sha256']and M['controller.py']==hs(controllerfile)==selector['controller_sha256']and "spec=read(P/'data/SPEC.json')"in prep and "'plan_sha256':sha(lift/'PLAN.json')"in prep and "--plan',work/'lift/PLAN.json'"in ctrl and F(ownspec['expected']['kappa'])==F(cr['kappa_record']))
    primary[selector_file]=hs(selector_file)
    for f,h in selector['full_source_binding'].items():ck('own_primary_'+f,hs(f)==h);primary[f]=h
    for f,h in recovery['dependency_hashes'].items():ck('exact_PLAN_dependency_'+f,hs(f)==h);cached[f]=h
    ck('own_MANIFEST_actual_PLAN_OWNERS',selector['PLAN_sha256']==hs(cr['own_physical_artifacts']['PLAN']['file'])==ownspec['data']['plan_sha256']and M['data/OWNERS.json.gz']==hs(cr['own_physical_artifacts']['OWNERS']['file'])==ownspec['data']['owners_sha256'])
    for kind,a in cr['own_physical_artifacts'].items():ck('own_'+kind,hs(a['file'])==a['sha256']==a['own_SPEC_expected_sha256']);primary[a['file']]=a['sha256']
    for n in cr['selected_native_censuses']:
        ck(n['provider']+'_selected_program_census',hs(n['program_file'])==n['program_file_sha256']and hs(n['census_file'])==n['census_sha256']);primary[n['program_file']]=n['program_file_sha256'];cached[n['census_file']]=n['census_sha256']
        ck(n['provider']+'_actual_canonical_required',n['canonical_file'] is not None and hs(n['canonical_file'])==n['canonical_file_sha256']);primary[n['canonical_file']]=n['canonical_file_sha256']
        ck(n['provider']+'_actual_initial_final_helper_dimensions',len(n['initial_helper_ranks'])==len(n['final_helper_ranks'])==len(n['entering_flags']) and [b-a for a,b in zip(n['initial_helper_ranks'],n['final_helper_ranks'])]==ownspec['providers'][n['provider']]['complete_contract']['widths'] and n['entering_flags']==[bool(a)for a in n['initial_helper_ranks']] and sum(n['entering_flags'])==ownspec['providers'][n['provider']]['entering'])
    rev=rm[pr];ck('own_canonical_review_scope_bound',rev['own_head']==entry['own_head'])
    for x in rev['matched_review_rows']:ck('canonical_primary_'+x['source_file'],hs(x['source_file'])==x['source_sha256']);primary[x['source_file']]=x['source_sha256']
    if any(x['literal_potential_contradiction_anchors']for x in rev['matched_review_rows']):ck('flagged_review_individually_read',pr in scm and scm[pr]['manual_scope_read'])
    ck('shared_historical_false_general_theorem_not_imported',pr not in scope['summary']['shared_analytic_qualification_entries']and not component['bounded_schur_lemma']['arbitrary_scale_free_H_theorem_used'])
    physical=(R/'finite_actual_owner_census_v2.py').read_text();dispatchsrc=(R/'selected_provider_dispatch_v14.py').read_text();ia=dispatchsrc.index("        T=plan['T'];groups=");ib=dispatchsrc.index("        out=dict(schema=",ia)
    ck('opaque_parent_provenance_not_used_by_new_physical_or_invoice',all(t not in physical and t not in dispatchsrc[ia:ib]for t in['parent_template_content_sha256','replica_lift']))
    inv=cr['invoice'];role=cr['role_receipt'];m=73;Wlive=inv['live'];P={int(k):v for k,v in role['profile'].items()};mass=sum(k*v for k,v in P.items())
    group=2**(36*36)
    for i in range(1,37):group*=2**(2*i)-1
    stock=group*inv['physical'];streamed=group*mass;Esource=2**100000
    ck('positive_raw_surplus_and_halving',mass==role['rank_mass']and m*Wlive-mass==role['rank_surplus']>0 and max(P)<m and m*m>2*max(P)**2)
    ck('own_complete_work_stock_and_row',len(cr['negative_controls'])==6 and inv['retained_previous_invoice']is None and inv['router_bits']<30000 and inv['literal_bits']<100000 and role['physical_row_coefficient']<20161 and role['prefix_bits']<role['charged_prefix_bits'])
    ck('own_semantic_height',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
    fallback=32*m*m*sum(P.values());eta_early=F(1,1000);kappa=F(cr['kappa_record']);eta_record=(kappa+F(cr['complex_lower']))/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
    ck('own_early_moment',earlyiv[1]<F(1695000,1696009)<1)
    record_quantified=True
    if record_quantified:ck('own_record_interior_moment',kappa<eta_record<F(cr['complex_lower'])and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
    else:ck('record_tail_tax_limitation_preserved',recordiv[0]>1 and kappa<eta_record<F(cr['complex_lower']))
    for kind,iv in [('early',earlyiv)]+([('record',recordiv)]if record_quantified else[]):
        bound=ceil(1/(1-iv[1]));coeff=2**32*m**4*(Esource+stock+streamed+1)**2*(1+bound)**2*20162**2
        ck(kind+'_own_allsize_work_coefficient',bound<2**100 and coeff<2**220000)
    early=reduced.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001)
    record=reduced.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)if record_quantified else None
    for kind,o in [('early',early)]+([('record',record)]if record_quantified else[]):
        ck(kind+'_fresh_all_reduced_and_runtime_checks',len(o['checks'])==32 and all(o['checks'].values()))
        ck(kind+'_no_BIT_parameter_or_operation',not o['ordinary_BIT_supplier_consumed']and'bit_saving'not in json.dumps(o['new_outer_parameters']))
    contracts=cr['retained_interfaces']+component['component_source_interfaces_required']+['The exact own selected source core is realized by this new direct Gaussian/Fermat circuit; original optional BIT admission is neither assumed nor executed. Full partial initial/final Gaussian-subspace operator identities, tensor identity on spectators, required absolute phases and normalized completed-child interfaces remain explicit; scalar specialization or frame dimensions alone do not prove them. Actual canonical initial/final nesting and rank differences are checked, and actual nonzero initial frames, not width<9, determine entering counts.']
    ownnative=dict(pr=pr,own_head=cr['own_head'],native_coordinate_rank=73,own_complete_census_file=entry['own_census_file'],own_complete_census_sha256=entry['own_census_sha256'],selected_native_censuses=cr['selected_native_censuses'],canonical_catalogue_absent_for=cr['canonical_catalogue_absent_for'],operator_phase_proved=False,descriptive_entering_counter=cr['descriptive_entering_counter'],original_global_verifier_full_PASS_claimed=False,own_invoice=inv,own_role_receipt=role,coarse_moment_interval=[str(x)for x in earlyiv],record_moment_interval=[str(x)for x in recordiv],attempted_record_saving=str(eta_record),native_record_saving=str(eta_record)if record_quantified else None,record_tail_quantified=record_quantified,original_record_tail_status='quantified_new_source_core_realization'if record_quantified else'unquantified_inherited_tax_exceeds_own_tight_record_endpoint',inherited_fallback_tax_denominator='10000000000000000',inherited_fallback_tax_removed=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,retained_contracts=contracts)
    deps=['selected-provider-v14-whole-upper.md','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-source-peer-review.json','selected-provider-dispatch-v14.json','selected-provider-dispatch-v14-inputs.json','selected_provider_dispatch_v14.py','finite_selected_program_census.py','finite_actual_owner_census_v2.py','selected-provider-review-evidence-screen.json','selected-provider-canonical-contradiction-scope-read.json',entry['own_census_file'],'pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v14.py','prepare_selected_provider_v14_whole_costs.py','selected_provider_v13_whole_bounds.py','selected-provider-v13-whole-upper.md','pr1104-ends7-selected-finite-peer-review.json','t37-generated-selected-plan-recovery.json','t37-generated-selected-plan-recovery.md','recover_t37_generated_selected_plans.py','pr1104-exact-selected-ends7-native-recovery.json','r480-selected-native-recovery.json','generated-t37-descriptive-counter-audit.md','generated-t37-descriptive-counter-audit.json','generated_t37_descriptive_counter_audit.py']
    dep={p:hs(p)for p in deps};dep.update(cached)
    for kind,o in [('native',ownnative)]+([('record-upper',record)]if record_quantified else[])+[('early-upper',early)]:
        o.update(schema='own-selected-direct-gaussian-'+kind+'/1',pr=pr,own_head=cr['own_head'],source_head=cr['own_head'],descriptive_entering_counter=cr['descriptive_entering_counter'],original_global_verifier_full_PASS_claimed=False,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=cr['kappa_record'],early_effective_kappa='1/5000'if kind=='early-upper'else None,source_equivalent_numeric_realization=True,historical_parent_provenance_byte_identity_claimed=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,retained_contracts=contracts,source_sha256=primary,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks=checks.copy(),whole_instance_checks_passed=len(checks))
        if kind=='early-upper':
            o.update(record_tail_quantified=record_quantified,record_tail_scope='Own original record exponent is separately quantified by this new direct Gaussian circuit.'if record_quantified else'Own historical record kappa is provenance only. This certificate proves only the explicitly weaker early exponent1/5000; its inherited finite-envelope tax is NOT removed and no same-XAG record tail is quantified.',piecewise_description='The counted early circuit is compared against the repaired reference only on its sufficient domain; a chosen wrapper switch is not a natural lower bound.')
            if record_quantified:o.update(record_tail_certificate=f'pr{pr}-generated-t37-finite-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-generated-t37-finite-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'])
            else:o.update(record_tail_certificate=None,record_tail_upper_log2log2_integer=None,unquantified_original_record_tail=True,original_record_exponent_not_proved_by_this_cost_certificate=True)
        (R/f'pr{pr}-generated-t37-finite-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
    rows.append(dict(pr=pr,own_head=cr['own_head'],kappa_record=cr['kappa_record'],native_certificate=f'pr{pr}-generated-t37-finite-native.json',early_upper_certificate=f'pr{pr}-generated-t37-finite-early-upper.json',record_upper_certificate=f'pr{pr}-generated-t37-finite-record-upper.json'if record_quantified else None,upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_quantified=record_quantified,record_tail_upper_log2log2_integer=record['upper_log2log2_integer']if record_quantified else None,canonical_catalogue_absent_for=cr['canonical_catalogue_absent_for'],meaningful_lower=None))
    print('PASS own direct Gaussian whole bound',pr,flush=True)
ck('exact_two_own_generated_T37_packages',set(r['pr']for r in rows)==ADMITTED)
out=dict(schema='own-selected-direct-gaussian-upper-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,script_sha256=hs(Path(__file__).name))
(R/'selected-provider-v14-whole-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n');print(json.dumps(dict(status=out['status'],checks=len(checks),points=len(rows)),indent=2))
