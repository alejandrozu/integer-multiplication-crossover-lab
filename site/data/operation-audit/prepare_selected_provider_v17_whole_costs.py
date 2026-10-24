"""Versioned mathematical implementation; own V17 inputs are checked afresh."""
from pathlib import Path
A=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
src=(A/'selected_provider_v12_whole_bounds.py').read_text()
src=src.replace('Own ten cold14-related','Own six K492 mixed').replace('REVIEW_CLOSED=True',f'REVIEW_CLOSED={COST_REVIEW_CLOSED}')
src=src.replace('ADMITTED={586,601,603,604,607,609,610,614,616,618}','ADMITTED={636,638,639,640,642,644}')
src=src.replace('v12','v17').replace('cold14-typed-finite','k492-mixed-finite')
src=src.replace('cold14-descriptive-counter-audit','late-cold-mixed-descriptive-counter-audit').replace('cold14_descriptive_counter_audit','late_cold_mixed_descriptive_counter_audit')
anchor="review=rd('selected-provider-review-evidence-screen.json');"
src=src.replace(anchor,"""fast=rd('late-cold-mixed-native-fast-offline-verification.json')
ck('native_fast_receipt_complete',fast['status']=='passed'and fast['script_sha256']==hs('verify_late_cold_mixed_native_recovery.py')and fast['checks_passed']==1333 and all(fast['checks'].values())and {x['pr']for x in fast['selected_own_providers']}==ADMITTED)
for f,h in fast['source_recovery_receipts'].items():ck('native_recovery_receipt_'+f,hs(f)==h)
"""+anchor)
start=src.index("    selector_file=f'selected-provider-dispatch-v17-source/")
end=src.index("    for kind,a in cr['own_physical_artifacts'].items():",start)
src=src[:start]+'''    selector_file=f'selected-provider-dispatch-v17-source/{pr}/actual-own-selector.json';selector=rd(selector_file);ownM=selector['MANIFEST_file'];ownV=selector['verifier_file'];v=(R/ownV).read_text();M=rd(ownM)
    ck('own_actual_entrypoint_MANIFEST_selects_SPEC',selector['own_head']==cr['own_head']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and hs(ownM)==selector['MANIFEST_sha256']and M['verify.py']==hs(ownV)==selector['verifier_sha256']and "default=P/'data/SPEC.json'"in v and "SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v and "P/'data/PLAN.json'"in v and "P/'data/OWNERS.json.gz'"in v and selector['actual_literal_spec_driven_native_and_global_data_selection']and F(ownspec['expected']['kappa'])==F(cr['kappa_record']))
    primary[selector_file]=hs(selector_file)
    for a in selector['verified_primary']:
        payload=(R/a['file']).read_bytes();blob=hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\\0'+payload).hexdigest()
        ck('own_primary_'+a['file'],a['own_head']==entry['own_head']and hs(a['file'])==a['sha256']and blob==a['git_blob_sha1']==a.get('own_API_git_blob_sha1',blob)and entry['own_head']in a['primary_url']and(a['relative']=='MANIFEST.json'or M[a['relative']]==a['sha256']));primary[a['file']]=a['sha256']
    ck('own_MANIFEST_API_authority',any(a['relative']=='MANIFEST.json'and(a.get('own_MANIFEST_authenticated_by_API_blob')is True or a.get('own_API_git_blob_sha1')==a['git_blob_sha1'])for a in selector['verified_primary']))
    ck('own_selected_native_recovery_receipt',hs(selector['own_selected_native_recovery_file'])==selector['own_selected_native_recovery_sha256']and all(rd(selector['own_selected_native_recovery_file'])['checks'].values())and not selector['complete_historical_package_replay_claimed'])
    ck('each_own_selected_provider_covered_by_actual_recovery',{x['provider']for x in fast['selected_own_providers']if x['pr']==pr}=={n['provider']for n in cr['selected_native_censuses']})
    primary[selector['own_selected_native_recovery_file']]=selector['own_selected_native_recovery_sha256']
    ck('own_MANIFEST_actual_PLAN_OWNERS',M['data/PLAN.json']==hs(cr['own_physical_artifacts']['PLAN']['file'])==ownspec['data']['plan_sha256']and M['data/OWNERS.json.gz']==hs(cr['own_physical_artifacts']['OWNERS']['file'])==ownspec['data']['owners_sha256'])
'''+src[end:]
# All six own taxed interior endpoints are tested, not inferred from the native
# byte identity or from another source's profile. Failure remains early-only.
src=src.replace('record_quantified=True','record_quantified=recordiv[1]<1 and 1-recordiv[1]>F(1,2**100)')
src=src.replace("deps+=['gaussian-only-parameter-ledger-peer-review.json','cold14-own-selection-source/manifest.json','prepare_selected_provider_v17.py','cold14-typed-chain-native-byte-recovery.json','recover_cold14_chain_native_bytes.py','cold14-source-reconstruction/source-closure-manifest.json','cold14-retained-baseline-seeds/manifest.json','late-cold-mixed-descriptive-counter-audit.md','late-cold-mixed-descriptive-counter-audit.json','late_cold_mixed_descriptive_counter_audit.py']", "deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v17.py','prepare_selected_provider_v17_whole_costs.py','selected_provider_v12_whole_bounds.py','selected-provider-v12-whole-upper.md','late-cold-mixed-selected-native-recovery.md','late-cold-mixed-source/native-source-closure-638.json','late-cold-mixed-source/variant-own-source-manifest.json','late-cold-mixed-native-byte-recovery-638.json','late-cold-mixed-native-variant-recovery.json','late-cold-mixed-native-fast-offline-verification.json','recover_late_cold_mixed_native_bytes.py','recover_late_cold_variants_native_bytes.py','verify_late_cold_mixed_native_recovery.py','late-cold-mixed-descriptive-counter-audit.md','late-cold-mixed-descriptive-counter-audit.json','late_cold_mixed_descriptive_counter_audit.py']")
src=src.replace("ck('exact_ten_own_typed_cold14_packages'","ck('exact_six_own_selected_K492_packages'")
assert 'cold14'not in src
(A/'selected_provider_v17_whole_bounds.py').write_text(src,encoding='utf8')

# Reuse the already-reviewed mechanical noninterference algorithm on the actual
# V17 dispatcher block, all six own physical roles, and their unmodified specs.
audit=(A/'vacancy_chain_descriptive_counter_audit.py').read_text().replace('v18','v17').replace('vacancy-chain','late-cold-mixed').replace('vacancy_chain','late_cold_mixed')
audit=audit.replace('These four own SPECs do not declare a global entering meter; the absence is preserved while actual initial-frame and width meters are separately computed.','The actual global source counters are preserved, including legacy width-meter matches and unreproduced copied values; actual initial-frame and width meters are separately computed.')
(A/'late_cold_mixed_descriptive_counter_audit.py').write_text(audit,encoding='utf8')
print('Prepared own V17 six whole-cost implementation and counter audit; closed=',COST_REVIEW_CLOSED)
