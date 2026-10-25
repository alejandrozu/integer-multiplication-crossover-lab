"""Own646 distinct K480 cost instance; actual source recovery remains mandatory."""
from pathlib import Path
A=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
s=(A/'selected_provider_v17_whole_bounds.py').read_text().replace('Own six K492 mixed','Own distinct signed-root K480').replace('REVIEW_CLOSED=True',f'REVIEW_CLOSED={COST_REVIEW_CLOSED}')
s=s.replace('ADMITTED={636,638,639,640,642,644}','ADMITTED={646}').replace('v17','v20').replace('k492-mixed-finite','signed-root-K480-finite')
a=s.index("fast=rd('late-cold-mixed-native-fast-offline-verification.json')");b=s.index("review=rd('selected-provider-review-evidence-screen.json');",a)
s=s[:a]+'''native_recovery=rd('late-cold-mixed-native-byte-recovery-646.json')
ck('own_actual_K480_native_recovery',native_recovery['pr']==646 and native_recovery['checks_passed']==334 and all(native_recovery['checks'].values())and native_recovery['script_sha256']==hs('recover_signed_root_646_native_bytes.py')and native_recovery['exact_shadow_RAW_byte_reuse']and not native_recovery['original_complete_source_package_replay_claimed'])
for key in ['source_sha256','retained_base_sha256','dependency_hashes']:
    for f,h in native_recovery[key].items():ck('own_actual_K480_native_source_'+f,hs(f)==h)
for a in native_recovery['outputs']:ck('own_actual_K480_native_output_'+a['file'],hs(a['file'])==a['sha256'])
'''+s[b:]
s=s.replace('late-cold-mixed-descriptive-counter-audit','signed-root-K480-descriptive-counter-audit').replace('late_cold_mixed_descriptive_counter_audit','signed_root_K480_descriptive_counter_audit')
s=s.replace("    cr=rd(entry['own_census_file']);", "    cr=rd(entry['own_census_file']);ck('exact_own_K480_native_head',native_recovery['own_head']==cr['own_head']=='cdfe8273bb5054e0a837a3594309c6262e995b1f');")
s=s.replace("    ck('each_own_selected_provider_covered_by_actual_recovery',{x['provider']for x in fast['selected_own_providers']if x['pr']==pr}=={n['provider']for n in cr['selected_native_censuses']})", "    ck('each_own_K480_selected_provider_actual_native_recovery',set(selector['exact_selected_K480_providers'])=={n['provider']for n in cr['selected_native_censuses']}==set(ownspec['providers']))\n    for pid,p in ownspec['providers'].items():\n        raw=ownspec['build']['providers'][pid]['word_content_sha256'];aa={a['artifact']:a for a in native_recovery['outputs']if a['provider']==pid and a['raw_content_sha256']==raw}\n        ck(pid+'_own_complete_K480_native_identity',aa['CANONICAL-WORD.json.gz']['semantic_sha256']==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and aa['LOCAL-PROGRAMS.json.gz']['semantic_sha256']==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and aa['LOCAL-PROGRAMS.json.gz']['orientation_sha256']==p['program_hashes'])")
a=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'");b=s.index("    dep={p:hs(p)for p in deps};dep.update(cached)",a)
s=s[:a]+'''    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v20.py','prepare_selected_provider_v20_whole_costs.py','selected_provider_v17_whole_bounds.py','selected-provider-v17-whole-upper.md','late-cold-mixed-source/signed-root-646-source-manifest.json','late-cold-mixed-source/native-source-closure-646.json','late-cold-mixed-native-byte-recovery-646.json','recover_signed_root_646_native_bytes.py','signed-root-K480-descriptive-counter-audit.md','signed-root-K480-descriptive-counter-audit.json','signed_root_K480_descriptive_counter_audit.py']
'''+s[b:]
s=s.replace("ck('exact_six_own_selected_K492_packages'","ck('exact_one_own_selected_distinct_K480_package'")
assert 'fast['not in s and 'late-cold-mixed-native-fast'not in s
(A/'selected_provider_v20_whole_bounds.py').write_text(s,encoding='utf8')
a=(A/'generated_u8_t37_descriptive_counter_audit.py').read_text().replace('v19','v20').replace('generated-U8-t37','signed-root-K480').replace('generated_u8_t37','signed_root_K480')
a=a.replace('These two own SPECs do not declare a global entering meter; the absence is preserved while actual initial-frame and width meters are separately computed.','The own source entering meter is preserved and compared with actual nonzero initial-frame and width-below-nine counts; neither value is used for cost.')
(A/'signed_root_K480_descriptive_counter_audit.py').write_text(a,encoding='utf8')
print('Prepared own distinct K480 whole evaluator; closed=',COST_REVIEW_CLOSED)
