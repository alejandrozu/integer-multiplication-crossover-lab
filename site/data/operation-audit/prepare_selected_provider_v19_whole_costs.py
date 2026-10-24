"""Own962/991 whole costs from exact source-generated semantic data."""
from pathlib import Path
A=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
s=(A/'selected_provider_v17_whole_bounds.py').read_text().replace('Own six K492 mixed','Own two source-generated U8/T37').replace('REVIEW_CLOSED=True',f'REVIEW_CLOSED={COST_REVIEW_CLOSED}')
s=s.replace('ADMITTED={636,638,639,640,642,644}','ADMITTED={962,991}').replace('v17','v19').replace('k492-mixed-finite','generated-U8-t37-finite')
start=s.index("fast=rd('late-cold-mixed-native-fast-offline-verification.json')")
end=s.index("review=rd('selected-provider-review-evidence-screen.json');",start)
s=s[:start]+'''recovery=rd('u8-t37-generated-data-recovery.json');recovered={x['pr']:x for x in recovery['rows']}
ck('exact_source_generated_semantic_recovery',recovery['status']=='checked_exact_own_source_generated_PLAN_OWNER_semantics'and recovery['script_sha256']==hs('recover_u8_t37_generated_data.py')and all(recovery['checks'].values())and set(recovered)==ADMITTED and not recovery['opaque_parent_hint_used'])
for k in ['source_sha256','dependency_hashes']:
    for f,h in recovery[k].items():ck('source_generated_data_'+f,hs(f)==h)
'''+s[end:]
s=s.replace('late-cold-mixed-descriptive-counter-audit','generated-U8-t37-descriptive-counter-audit').replace('late_cold_mixed_descriptive_counter_audit','generated_u8_t37_descriptive_counter_audit')
start=s.index("    selector_file=f'selected-provider-dispatch-v19-source/")
end=s.index("    for kind,a in cr['own_physical_artifacts'].items():",start)
s=s[:start]+'''    selector_file=f'selected-provider-dispatch-v19-source/{pr}/actual-own-selector.json';selector=rd(selector_file);z=recovered[pr];ownM=selector['MANIFEST_file'];M=rd(ownM);original=rd(selector['original_SPEC_file']);ownV=selector['verifier_file'];v=(R/ownV).read_text()
    ck('actual_own_MANIFEST_verifier_and_generated_data_selector',selector['own_head']==cr['own_head']and hs(ownM)==selector['MANIFEST_sha256']and hs(selector['original_SPEC_file'])==M['data/SPEC.json']==selector['original_SPEC_sha256']and M['verify.py']==hs(ownV)and "def runtime_spec(plan_path, owner_path):"in v and "Frozen owner/plan semantic identity"in v and "work/'lift/PLAN.json'"in v and M['build_owners.py']==hs(selector['owner_constructor_file'])and M['build_parent.py']==hs(selector['parent_constructor_file']))
    expected=rd(selector['original_SPEC_file']);expected['data']['plan_sha256']=selector['PLAN_sha256'];expected['data']['owners_sha256']=selector['OWNERS_sha256']
    ck('only_own_authorized_raw_portability_fields_rebound',ownspec==expected and hs(selector['runtime_SPEC_file'])==cr['own_SPEC_sha256']==selector['runtime_SPEC_sha256']and z['PLAN_semantic_sha256']==original['data']['plan_semantic_sha256']and z['owners_content_sha256']==original['data']['owners_content_sha256']and z['only_own_authorized_raw_portability_fields_rebound'])
    primary.update({selector_file:hs(selector_file),ownM:hs(ownM),selector['original_SPEC_file']:selector['original_SPEC_sha256']})
    for a in selector['verified_primary']:
        ck('own_primary_'+a['file'],a['own_head']==entry['own_head']and hs(a['file'])==a['sha256']==M[a['relative']]);primary[a['file']]=a['sha256']
    ck('own_generated_PLAN_OWNERS_raw_runtime_commitments',hs(cr['own_physical_artifacts']['PLAN']['file'])==ownspec['data']['plan_sha256']==selector['PLAN_sha256']and hs(cr['own_physical_artifacts']['OWNERS']['file'])==ownspec['data']['owners_sha256']==selector['OWNERS_sha256'])
'''+s[end:]
start=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'")
end=s.index("    dep={p:hs(p)for p in deps};dep.update(cached)",start)
s=s[:start]+'''    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v19.py','prepare_selected_provider_v19_whole_costs.py','selected_provider_v17_whole_bounds.py','selected-provider-v17-whole-upper.md','u8-t37-generated-data-recovery.md','u8-t37-generated-data-recovery.json','recover_u8_t37_generated_data.py','u8-t37-generated-source/manifest.json','u8-t37-generated-parent-inputs/manifest.json','u8-exact-earlier-selected-byte-recovery.json','recover_u8_selected_archive_bytes.py','generated-U8-t37-descriptive-counter-audit.md','generated-U8-t37-descriptive-counter-audit.json','generated_u8_t37_descriptive_counter_audit.py']
'''+s[end:]
s=s.replace("    fallback=32*m*m*sum(P.values());", "    ck('own_actual_T37_payload_and_complete_inventory',role['roles']==167832 and role['calls']==333 and role['prefix_bits']==779 and role['charged_prefix_bits']==1024 and role['row_prefix_extra']==2048 and role['physical_row_coefficient']==17495)\n    fallback=32*m*m*sum(P.values());")
s=s.replace("ck('exact_six_own_selected_K492_packages'","ck('exact_two_own_source_generated_U8_T37_packages'")
assert 'late-cold-mixed'not in s and 'fast['not in s
(A/'selected_provider_v19_whole_bounds.py').write_text(s,encoding='utf8')
a=(A/'vacancy_chain_descriptive_counter_audit.py').read_text().replace('v18','v19').replace('vacancy-chain','generated-U8-t37').replace('vacancy_chain','generated_u8_t37')
a=a.replace('These four own SPECs','These two own SPECs')
(A/'generated_u8_t37_descriptive_counter_audit.py').write_text(a,encoding='utf8')
print('Prepared own two exact U8/T37 generated-data cost instances; closed=',COST_REVIEW_CLOSED)
