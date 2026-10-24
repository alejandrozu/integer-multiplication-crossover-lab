"""Two separately selected exact generated-PLAN sources; no prior numeric bound."""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parent;COST_REVIEW_CLOSED=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
assert hs('selected_provider_v13_whole_bounds.py')=='abdec9f98bf7074004c9be40350af97d8ff22e4548b343c632b687f73ace4fb0'
s=(R/'selected_provider_v13_whole_bounds.py').read_text().replace('REVIEW_CLOSED=True','REVIEW_CLOSED='+str(COST_REVIEW_CLOSED))
for before,after in[('selected-provider-v13','selected-provider-v14'),('selected_provider_v13','selected_provider_v14'),('selected-provider-dispatch-v13','selected-provider-dispatch-v14'),('selected_provider_dispatch_v13','selected_provider_dispatch_v14'),('ends7-selected-finite','generated-t37-finite'),('ends7-descriptive-counter','generated-t37-descriptive-counter'),('ends7_descriptive_counter','generated_t37_descriptive_counter')]:s=s.replace(before,after)
s=s.replace('ADMITTED={1104,1107,1117,1121}','ADMITTED={1131,1152}')
start=s.index("    selector_file=f'selected-provider-dispatch-v14-source/");end=s.index("    ck('own_MANIFEST_actual_PLAN_OWNERS'",start)
new="""    selector_file=cr['own_source_selector_file'];selector=rd(selector_file);ownM=selector['MANIFEST_file'];M=rd(ownM);prepfile=selector['prepare_file'];controllerfile=selector['controller_file'];prep=(R/prepfile).read_text();ctrl=(R/controllerfile).read_text()
    recoveryfile=selector['source_recovery_receipt'];recovery=rd(recoveryfile);rr=next(a for a in recovery['rows']if a['pr']==pr)
    ck('exact_own_generated_PLAN_recovery',recovery['status']=='closed_exact_own_SPEC_PLAN_byte_recovery'and recovery['checks_passed']==203 and all(recovery['checks'].values())and recovery['script_sha256']==hs('recover_t37_generated_selected_plans.py')and hs(recoveryfile)==selector['source_recovery_receipt_sha256']and rr['own_head']==cr['own_head']and rr['own_SPEC_sha256']==cr['own_SPEC_sha256']and rr['PLAN_sha256']==selector['PLAN_sha256']==ownspec['data']['plan_sha256']and not recovery['historical_parent_template_byte_identity_claimed']and not recovery['original_full_global_verifier_PASS_claimed'])
    ck('own_actual_prepare_controller_MANIFEST_select_SPEC_PLAN_OWNERS',selector['own_head']==cr['own_head']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and M['prepare.py']==hs(prepfile)==selector['prepare_sha256']and M['controller.py']==hs(controllerfile)==selector['controller_sha256']and \"spec=read(P/'data/SPEC.json')\"in prep and \"'plan_sha256':sha(lift/'PLAN.json')\"in prep and \"--plan',work/'lift/PLAN.json'\"in ctrl and F(ownspec['expected']['kappa'])==F(cr['kappa_record']))
    primary[selector_file]=hs(selector_file)
    for f,h in selector['full_source_binding'].items():ck('own_primary_'+f,hs(f)==h);primary[f]=h
    for f,h in recovery['dependency_hashes'].items():ck('exact_PLAN_dependency_'+f,hs(f)==h);cached[f]=h
"""
s=s[:start]+new+s[end:]
s=s.replace("M['data/PLAN.json']==hs(cr['own_physical_artifacts']['PLAN']['file'])", "selector['PLAN_sha256']==hs(cr['own_physical_artifacts']['PLAN']['file'])")
needle="    inv=cr['invoice'];role=cr['role_receipt'];"
extra="""    physical=(R/'finite_actual_owner_census_v2.py').read_text();dispatchsrc=(R/'selected_provider_dispatch_v14.py').read_text();ia=dispatchsrc.index(\"        T=plan['T'];groups=\");ib=dispatchsrc.index(\"        out=dict(schema=\",ia)
    ck('opaque_parent_provenance_not_used_by_new_physical_or_invoice',all(t not in physical and t not in dispatchsrc[ia:ib]for t in['parent_template_content_sha256','replica_lift']))
"""
assert s.count(needle)==1;s=s.replace(needle,extra+needle)
needle="deps+=['gaussian-only-parameter-ledger-peer-review.json','ends7-own-selection-source/source-fetch-manifest.json','prepare_selected_provider_v14.py','prepare_selected_provider_v14_whole_costs.py','selected_provider_v12_whole_bounds.py','selected-provider-v12-whole-upper.md','pr1104-exact-selected-ends7-native-recovery.json','recover_pr1104_ends7_selected_native.py','generated-t37-descriptive-counter-audit.md','generated-t37-descriptive-counter-audit.json','generated_t37_descriptive_counter_audit.py']"
replacement="deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v14.py','prepare_selected_provider_v14_whole_costs.py','selected_provider_v13_whole_bounds.py','selected-provider-v13-whole-upper.md','pr1104-ends7-selected-finite-peer-review.json','t37-generated-selected-plan-recovery.json','t37-generated-selected-plan-recovery.md','recover_t37_generated_selected_plans.py','pr1104-exact-selected-ends7-native-recovery.json','r480-selected-native-recovery.json','generated-t37-descriptive-counter-audit.md','generated-t37-descriptive-counter-audit.json','generated_t37_descriptive_counter_audit.py']"
assert s.count(needle)==1;s=s.replace(needle,replacement)
s=s.replace('exact_four_own_selected_ends7_packages','exact_two_own_generated_T37_packages').replace('Own four selected ends7 finite Gaussian uppers','Own two exact generated-PLAN T37 finite Gaussian uppers')
(R/'selected_provider_v14_whole_bounds.py').write_text(s,encoding='utf8')
audit=(R/'ends7_descriptive_counter_audit.py').read_text().replace('selected_provider_dispatch_v13','selected_provider_dispatch_v14').replace('selected-provider-dispatch-v13','selected-provider-dispatch-v14').replace('ends7-descriptive-counter','generated-t37-descriptive-counter').replace('own-selected-ends7-descriptive-meter-noninterference/1','own-selected-generated-T37-descriptive-meter-noninterference/1').replace('These four own SPECs','These two own SPECs')
(R/'generated_t37_descriptive_counter_audit.py').write_text(audit,encoding='utf8')
print('PASS prepared two-source exact generated-PLAN whole evaluator')
