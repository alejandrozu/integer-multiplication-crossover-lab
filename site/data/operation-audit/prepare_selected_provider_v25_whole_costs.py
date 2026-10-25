"""Build own619 fine-grid selected-core costs; no inherited invoice or cutoff."""
from pathlib import Path
R = Path(__file__).resolve().parent
COST_REVIEW_CLOSED = True
s = (R / 'selected_provider_v23_whole_bounds.py').read_text()
s = s.replace('Own two hyperplane/cold-end', 'Own619 fine-grid selected-core').replace('ADMITTED={591,615}', 'ADMITTED={619}').replace('REVIEW_CLOSED=True', f'REVIEW_CLOSED={COST_REVIEW_CLOSED}').replace('v23', 'v25').replace('hyperplane-cold-finite', 'ceiling-refined-finite')
s = s.replace('import ast,hashlib,importlib.util,json,sys', 'import ast,base64,hashlib,importlib.util,json,sys')
a = s.index("ck('own_actual_typed_native_recovery'")
b = s.index("for key in ['source_sha256'", a)
s = s[:a] + "ck('actual_predecessor_selected_byte_recovery',native_recovery['status']=='passed_actual_own_typed_constructor_and_native_scalar_frame_wrapper_engines'and 615 in native_recovery['prs'] and native_recovery['checks_passed']==1645 and all(native_recovery['checks'].values())and native_recovery['script_sha256']==hs('recover_early_hyperplane_cold_native.py')and not native_recovery['original_full_global_or_phase_verifier_PASS_claimed'])\n" + s[b:]
s = s.replace('hyperplane-cold-descriptive-counter-audit', 'ceiling-refinement-descriptive-counter-audit').replace('hyperplane_cold_descriptive_counter_audit', 'ceiling_refinement_descriptive_counter_audit')
s = s.replace("{x['provider']for x in native_recovery['selected_own_providers']if x['pr']==pr}", "set(selector['exact_own_selected_native_bindings'])")
s = s.replace("ck('actual_own_native_execution_heads',all(x['own_head']==entry['own_head']for x in native_recovery['selected_own_providers']if x['pr']==pr))", "ck('own_direct_native_commitments_not_predecessor_kappa_join',selector['native_commitments_directly_bound_by_own_SPEC']and selector['native_recovery_reused_only_as_exact_byte_object']and not selector['previous_invoice_or_cutoff_consumed']and len(selector['actual_own_SPEC_vs_PR615_differences'])==8)\n    api=rd(selector['actual_own_MANIFEST_API_file']);ck('actual_own_HEAD_MANIFEST_API_authority',hs(selector['actual_own_MANIFEST_API_file'])==selector['actual_own_MANIFEST_API_sha256']and base64.b64decode(api['content'])==(R/ownM).read_bytes()and api['sha']==next(a['git_blob_sha1']for a in selector['verified_primary']if a['relative']=='MANIFEST.json')and api['path']=='research/complex-pr615-ceiling/MANIFEST.json');primary[selector['actual_own_MANIFEST_API_file']]=selector['actual_own_MANIFEST_API_sha256']")
s = s.replace("a['pr']==pr and a['provider']==pid and a['raw_content_sha256']==raw", "a['pr']==615 and a['provider']==pid and a['raw_content_sha256']==raw")
a = s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'")
b = s.index('    dep={p:hs(p)for p in deps}', a)
s = s[:a] + "    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v25.py','prepare_selected_provider_v25_whole_costs.py','selected_provider_v17_whole_bounds.py','selected-provider-v17-whole-upper.md','pr619-selected-complex-source/source-manifest.json','fetch_pr619_selected_complex_sources.py','early-hyperplane-cold-selected-native-recovery.json','recover_early_hyperplane_cold_native.py','ceiling-refinement-descriptive-counter-audit.md','ceiling-refinement-descriptive-counter-audit.json','ceiling_refinement_descriptive_counter_audit.py']\n" + s[b:]
s = s.replace('exact_two_own_selected_hyperplane_cold_packages', 'exact_own619_fine_grid_selected_core')
(R / 'selected_provider_v25_whole_bounds.py').write_text(s, encoding='utf8')
a = (R / 'signed_root_K480_descriptive_counter_audit.py').read_text().replace('v20', 'v25').replace('signed-root-K480', 'ceiling-refinement').replace('signed_root_K480', 'ceiling_refinement')
(R / 'ceiling_refinement_descriptive_counter_audit.py').write_text(a, encoding='utf8')
print('Prepared own619 fresh Gaussian realization; closed=', COST_REVIEW_CLOSED)
