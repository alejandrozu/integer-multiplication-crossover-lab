"""New whole costs for two independently source-selected owner exchanges."""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parent;COST_REVIEW_CLOSED=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
assert hs('selected_provider_v13_whole_bounds.py')=='abdec9f98bf7074004c9be40350af97d8ff22e4548b343c632b687f73ace4fb0'
s=(R/'selected_provider_v13_whole_bounds.py').read_text().replace('REVIEW_CLOSED=True','REVIEW_CLOSED='+str(COST_REVIEW_CLOSED))
for before,after in [('selected-provider-v13','selected-provider-v15'),('selected_provider_v13','selected_provider_v15'),('selected-provider-dispatch-v13','selected-provider-dispatch-v15'),('selected_provider_dispatch_v13','selected_provider_dispatch_v15'),('ends7-selected-finite','ends7-exchange-finite'),('ends7-descriptive-counter','ends7-exchange-descriptive-counter'),('ends7_descriptive_counter','ends7_exchange_descriptive_counter')]:s=s.replace(before,after)
s=s.replace('ADMITTED={1104,1107,1117,1121}','ADMITTED={1150,1172}')
start=s.index("    selector_file=f'selected-provider-dispatch-v15-source/");end=s.index("    ck('own_MANIFEST_actual_PLAN_OWNERS'",start)
new="""    selector_file=cr['own_source_selector_file'];selector=rd(selector_file);ownM=selector['MANIFEST']['file'];M=rd(ownM);authority=selector['own_source_authority']
    ck('own_MANIFEST_selected_SPEC_and_target',selector['own_head']==cr['own_head']and hs(selector_file)==cr['own_source_selector_sha256']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and F(ownspec['expected']['kappa'])==F(cr['kappa_record']))
    if pr==1150:
        sourcefile=authority['source_file'];up=rd(sourcefile);parentM=authority['parent_manifest_file'];parentV=authority['parent_verifier_file'];v=(R/parentV).read_text();ownV=next(a['file']for a in selector['verified_primary']if a['path'].endswith('/verify.py'));ov=(R/ownV).read_text()
        ck('own_SOURCE_exact_1104_manifest_and_unchanged_selector',authority['kind']=='own_verified_SOURCE_exact_manifest_to_unchanged1104_strict_selector_then_own_three_data_overlays'and hs(sourcefile)==authority['source_sha256']==M['SOURCE.json']and up['pr']==1104 and up['head']=='d8982686afd7ef6ce52ddeaa17011ccda558d666'and up['manifest_sha256']==hs(parentM)==authority['parent_manifest_sha256']and up['files']==rd(parentM)and up['files']['verify_t16.py']==hs(parentV)==authority['parent_verifier_sha256']and len(up['files'])==195)
        ck('own_actual_verifier_three_data_overlays',M['verify.py']==hs(ownV)and \"for name in ('OWNERS.json.gz','PLAN.json','SPEC.json'):\"in ov and \"shutil.copyfile(P/'data'/name,source/'data'/name)\"in ov and \"source/'verify_t16.py'\"in ov)
        primary.update({sourcefile:hs(sourcefile),parentM:hs(parentM),parentV:hs(parentV)})
    else:
        ownV=authority['verifier']['file'];v=(R/ownV).read_text();ck('own_actual_strict_selector',authority['kind']=='own_manifest_and_literal_strict_selector'and M['verify_t16.py']==hs(ownV)==authority['verifier']['sha256'])
    ck('literal_strict_selector_consumes_selected_own_data',\"SPEC8, SPEC16 = PKG / 'data/SPEC-T8.json', PKG / 'data/SPEC.json'\"in v and 'spec=SPEC16'in v and \"'--plan', PKG / 'data/PLAN.json'\"in v and \"'--owners', PKG / 'data/OWNERS.json.gz'\"in v)
    primary[selector_file]=hs(selector_file)
    for a in selector['verified_primary']:ck('own_primary_'+a['file'],a['own_head']==entry['own_head']and hs(a['file'])==a['sha256']);primary[a['file']]=a['sha256']
"""
s=s[:start]+new+s[end:]
old="deps+=['gaussian-only-parameter-ledger-peer-review.json','ends7-own-selection-source/source-fetch-manifest.json','prepare_selected_provider_v15.py','prepare_selected_provider_v15_whole_costs.py','selected_provider_v12_whole_bounds.py','selected-provider-v12-whole-upper.md','pr1104-exact-selected-ends7-native-recovery.json','recover_pr1104_ends7_selected_native.py','ends7-exchange-descriptive-counter-audit.md','ends7-exchange-descriptive-counter-audit.json','ends7_exchange_descriptive_counter_audit.py']"
newdep="deps+=['gaussian-only-parameter-ledger-peer-review.json','ends7-exchange-own-selection-source/source-fetch-manifest.json','prepare_selected_provider_v15.py','prepare_selected_provider_v15_whole_costs.py','selected_provider_v13_whole_bounds.py','selected-provider-v13-whole-upper.md','pr1104-ends7-selected-finite-peer-review.json','pr1104-exact-selected-ends7-native-recovery.json','recover_pr1104_ends7_selected_native.py','ends7-exchange-descriptive-counter-audit.md','ends7-exchange-descriptive-counter-audit.json','ends7_exchange_descriptive_counter_audit.py']"
assert s.count(old)==1;s=s.replace(old,newdep)
s=s.replace('exact_four_own_selected_ends7_packages','exact_two_own_selected_ends7_exchanges').replace('Own four selected ends7 finite Gaussian uppers','Own two selected ends7 owner-exchange Gaussian uppers')
(R/'selected_provider_v15_whole_bounds.py').write_text(s,encoding='utf8')
audit=(R/'ends7_descriptive_counter_audit.py').read_text().replace('selected_provider_dispatch_v13','selected_provider_dispatch_v15').replace('selected-provider-dispatch-v13','selected-provider-dispatch-v15').replace('ends7-descriptive-counter','ends7-exchange-descriptive-counter').replace('These four own SPECs','These two own SPECs')
(R/'ends7_exchange_descriptive_counter_audit.py').write_text(audit,encoding='utf8')
print('PASS prepared two own selected ends7 exchange cost instantiations')
