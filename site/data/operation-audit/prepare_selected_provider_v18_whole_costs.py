"""Versioned same-model proof with actual own2077 selected target and data."""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parent;COST_REVIEW_CLOSED=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
assert hs('selected_provider_v16_whole_bounds.py')=='eae7c2b0f6cbb0761d77dd9133cb2a6f72a09b154f131c6bd7f77c1c42c02819'
s=(R/'selected_provider_v16_whole_bounds.py').read_text().replace('REVIEW_CLOSED=True','REVIEW_CLOSED='+str(COST_REVIEW_CLOSED))
for a,b in[('selected-provider-v16','selected-provider-v18'),('selected_provider_v16','selected_provider_v18'),('selected-provider-dispatch-v16','selected-provider-dispatch-v18'),('selected_provider_dispatch_v16','selected_provider_dispatch_v18'),('u8-selected-finite','vacancy-chain-finite'),('u8-descriptive-counter','vacancy-chain-descriptive-counter'),('u8_descriptive_counter','vacancy_chain_descriptive_counter')]:s=s.replace(a,b)
s=s.replace('ADMITTED={869,870}','ADMITTED={2077}').replace('Own two selected U8 finite Gaussian uppers','Own2077 selected vacancy-chain finite Gaussian upper').replace('exact_two_own_selected_U8_packages','exact_one_own_selected_vacancy_chain_package')
start=s.index("    selector_file=f'selected-provider-dispatch-v18-source/");end=s.index("    ck('own_MANIFEST_actual_PLAN_OWNERS'",start)
new="""    selector_file=f'selected-provider-dispatch-v18-source/{pr}/actual-own-selector.json';selector=rd(selector_file);ownM=selector['MANIFEST_file'];ownV=selector['verifier_file'];M=rd(ownM);v=(R/ownV).read_text();builder=(R/selector['builder_file']).read_text();candidate=rd('pr2077-vacancy-chain-source/CANDIDATE.json')
    ck('actual_own_MANIFEST_literal_verifier_builder_selector',selector['own_head']==cr['own_head']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and hs(ownM)==selector['MANIFEST_sha256']and M['verify.py']==hs(ownV)==selector['verifier_sha256']and M['build.py']==hs(selector['builder_file'])==selector['builder_sha256']and \"blobs=mod.derive(main)\"in v and\"source/'verify_t16.py'\"in v and\"for name in ('OWNERS.json.gz','PLAN.json','SPEC.json')\"in v)
    recovery=rd(selector['source_recovery_file']);ck('entire_own_data_reconstruction_not_profile',all(recovery['checks'].values())and recovery['checks_passed']==35 and recovery['script_sha256']==hs('recover_pr2077_selected_data.py')and selector['source_recovery_sha256']==hs(selector['source_recovery_file'])and recovery['own_head']==cr['own_head'])
    ck('actual_source_target_separate_from_frozen_baseline',candidate['expected_updates']['kappa']==ownspec['expected']['kappa']==cr['kappa_record']==selector['actual_own_kappa']and candidate['baseline_kappa']==selector['frozen_metadata_kappa']=='836330098538459/500000000000000000'and cr['kappa_record']=='418166011373521/250000000000000000')
    chronology=rd(selector['chronology_file']);ck('actual_source_version_chronology',hs(selector['chronology_file'])==selector['chronology_sha256']and chronology['own_head']==cr['own_head']and cr['own_head']in chronology['merge_parents']and chronology['source_committed_at']<=chronology['merged_at']and chronology['source_included_at_actual_merge']and chronology['merge_parent_number']==16)
    primary.update({selector_file:hs(selector_file),ownM:hs(ownM),selector['chronology_file']:selector['chronology_sha256']})
    for receipt in chronology['primary_receipts']:ck('chronology_primary_'+receipt['file'],hs(receipt['file'])==receipt['sha256']);primary[receipt['file']]=receipt['sha256']
    for a in selector['whole_source_inventory']:ck('actual_own_primary_'+a['file'],a['own_head']==cr['own_head']and hs(a['file'])==a['sha256']==M[a['relative']]);primary[a['file']]=a['sha256']
    for f,h in recovery['source_sha256'].items():ck('own_reconstruction_input_'+f,hs(f)==h);primary[f]=h
"""
s=s[:start]+new+s[end:]
start=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'");end=s.index('\n    dep=',start)
s=s[:start]+"    deps+=['gaussian-only-parameter-ledger-peer-review.json','pr2077-vacancy-chain-source/source-receipt.json','prepare_selected_provider_v18.py','prepare_selected_provider_v18_whole_costs.py','selected_provider_v16_whole_bounds.py','selected-provider-v16-whole-upper.md','pr2077-exact-selected-data-recovery.json','recover_pr2077_selected_data.py','r480-selected-native-recovery.json','pr2077-source-chronology/chronology.json','vacancy-chain-descriptive-counter-audit.md','vacancy-chain-descriptive-counter-audit.json','vacancy_chain_descriptive_counter_audit.py']"+s[end:]
needle="        if kind=='early-upper':"
extra="""        o.update(source_selected_kappa_correction=True,frozen_metadata_kappa=selector['frozen_metadata_kappa'],actual_own_selected_kappa=cr['kappa_record'],source_selected_kappa_correction_basis='Own immutable MANIFEST/verify/build reconstruct all3complete data bytes; own SPEC and CANDIDATE.expected_updates select actual target, while CANDIDATE baseline is the preserved frozen parser quote.',source_kappa_correction_primary_receipt=selector['chronology_file'],source_revision_included_at_merge=chronology['merged_at'],source_revision_merge_commit=chronology['merge_commit_sha'],source_revision_committed_at=chronology['source_committed_at'])
"""
assert needle in s;s=s.replace(needle,extra+needle)
(R/'selected_provider_v18_whole_bounds.py').write_text(s,encoding='utf8')
a=(R/'u8_descriptive_counter_audit.py').read_text().replace('selected_provider_dispatch_v16','selected_provider_dispatch_v18').replace('selected-provider-dispatch-v16','selected-provider-dispatch-v18').replace('u8-descriptive-counter','vacancy-chain-descriptive-counter').replace('own-selected-U8-descriptive-meter-noninterference/1','own-selected-vacancy-chain-descriptive-meter-noninterference/1')
(R/'vacancy_chain_descriptive_counter_audit.py').write_text(a,encoding='utf8')
(R/'vacancy-chain-descriptive-counter-audit.md').write_text('''# Own2077 descriptive entry-meter independence

The complete actual canonical initial/final ranks and own whole role widths are
mandatory. No global source entering meter is fabricated. The AST and exact
full invoice block checks plus0/2^100 noninterference execution establish that
the descriptive counter enters no work/stock/router/tape arithmetic. This
does not waive a physical or operator invariant or claim a historical verifier
PASS. It is applied to the actual own four-placement complete controller.
''',encoding='utf8');print('PASS own2077 actual-source whole-cost evaluator preparation')
