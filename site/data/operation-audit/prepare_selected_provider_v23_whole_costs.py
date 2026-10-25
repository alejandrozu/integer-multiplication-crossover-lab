"""Two admitted own hyperplane/cold-end Gaussian instances; PR608 source mismatch remains open."""
from pathlib import Path
R=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
s=(R/'selected_provider_v17_whole_bounds.py').read_text()
s=s.replace('Own six K492 mixed','Own two hyperplane/cold-end').replace('ADMITTED={636,638,639,640,642,644}','ADMITTED={591,615}').replace('REVIEW_CLOSED=True',f'REVIEW_CLOSED={COST_REVIEW_CLOSED}').replace('v17','v23').replace('k492-mixed-finite','hyperplane-cold-finite')
a=s.index("fast=rd('late-cold-mixed-native-fast-offline-verification.json')");b=s.index("review=rd('selected-provider-review-evidence-screen.json');",a)
s=s[:a]+'''native_recovery=rd('early-hyperplane-cold-selected-native-recovery.json')
ck('own_actual_typed_native_recovery',native_recovery['status']=='passed_actual_own_typed_constructor_and_native_scalar_frame_wrapper_engines'and set(native_recovery['prs'])=={591,608,615} and ADMITTED<set(native_recovery['prs']) and all(native_recovery['checks'].values())and native_recovery['script_sha256']==hs('recover_early_hyperplane_cold_native.py')and not native_recovery['original_full_global_or_phase_verifier_PASS_claimed'])
for key in ['source_sha256','executed_external_source_sha256','retained_base_sha256','dependency_hashes']:
    for f,h in native_recovery[key].items():ck('actual_executed_source_'+f,hs(f)==h)
for a in native_recovery['outputs']:ck('actual_executed_output_'+a['file'],hs(a['file'])==a['sha256'])
'''+s[b:]
s=s.replace('late-cold-mixed-descriptive-counter-audit','hyperplane-cold-descriptive-counter-audit').replace('late_cold_mixed_descriptive_counter_audit','hyperplane_cold_descriptive_counter_audit')
s=s.replace("{x['provider']for x in fast['selected_own_providers']if x['pr']==pr}","{x['provider']for x in native_recovery['selected_own_providers']if x['pr']==pr}")
needle="    primary[selector['own_selected_native_recovery_file']]=selector['own_selected_native_recovery_sha256']"
s=s.replace(needle,needle+'''
    ck('actual_own_native_execution_heads',all(x['own_head']==entry['own_head']for x in native_recovery['selected_own_providers']if x['pr']==pr))
    for pid,p in ownspec['providers'].items():
        raw=ownspec['build']['providers'][pid]['word_content_sha256'];matches=[a for a in native_recovery['outputs']if a['pr']==pr and a['provider']==pid and a['raw_content_sha256']==raw]
        ck(pid+'_exactly_one_selected_canonical_and_program_artifact',all(sum(a['artifact']==name for a in matches)==1 for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']))
        aa={a['artifact']:a for a in matches}
        ck(pid+'_own_complete_RAW_canonical_program_and_orientations',aa['CANONICAL-WORD.json.gz']['semantic_sha256']==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and aa['LOCAL-PROGRAMS.json.gz']['semantic_sha256']==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and aa['LOCAL-PROGRAMS.json.gz']['orientation_sha256']==p['program_hashes'])
''')
a=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'");b=s.index('    dep={p:hs(p)for p in deps}',a)
s=s[:a]+'''    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v23.py','prepare_selected_provider_v23_whole_costs.py','selected_provider_v17_whole_bounds.py','selected-provider-v17-whole-upper.md','early-hyperplane-cold-own-source/source-manifest.json','early-hyperplane-cold-selected-native-recovery.json','recover_early_hyperplane_cold_native.py','hyperplane-cold-descriptive-counter-audit.md','hyperplane-cold-descriptive-counter-audit.json','hyperplane_cold_descriptive_counter_audit.py']
'''+s[b:]
s=s.replace("a['own_SPEC_expected_sha256']","ownspec['data']['plan_sha256'if kind=='PLAN'else'owners_sha256']")
s=s.replace("ck('exact_six_own_selected_K492_packages'","ck('exact_two_own_selected_hyperplane_cold_packages'")
assert 'fast['not in s and 'late-cold-mixed'not in s
(R/'selected_provider_v23_whole_bounds.py').write_text(s,encoding='utf8')
a=(R/'signed_root_K480_descriptive_counter_audit.py').read_text().replace('v20','v23').replace('signed-root-K480','hyperplane-cold').replace('signed_root_K480','hyperplane_cold')
a=a.replace(" pr=e['pr'];ck("," pr=e['pr']\n if pr not in {591,615}:continue\n ck(")
(R/'hyperplane_cold_descriptive_counter_audit.py').write_text(a,encoding='utf8')
print('Prepared own two hyperplane/cold-end whole costs; closed=',COST_REVIEW_CLOSED)
