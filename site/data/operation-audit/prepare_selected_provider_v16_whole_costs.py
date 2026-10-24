"""Versioned mathematical implementation with own U8 source selection joins."""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parent;COST_REVIEW_CLOSED=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
assert hs('selected_provider_v13_whole_bounds.py')=='abdec9f98bf7074004c9be40350af97d8ff22e4548b343c632b687f73ace4fb0'
s=(R/'selected_provider_v13_whole_bounds.py').read_text().replace('REVIEW_CLOSED=True','REVIEW_CLOSED='+str(COST_REVIEW_CLOSED))
for a,b in[('selected-provider-v13','selected-provider-v16'),('selected_provider_v13','selected_provider_v16'),('selected-provider-dispatch-v13','selected-provider-dispatch-v16'),('selected_provider_dispatch_v13','selected_provider_dispatch_v16'),('ends7-selected-finite','u8-selected-finite'),('ends7-descriptive-counter','u8-descriptive-counter'),('ends7_descriptive_counter','u8_descriptive_counter')]:s=s.replace(a,b)
s=s.replace('ADMITTED={1104,1107,1117,1121}','ADMITTED={869,870}')
start=s.index("    selector_file=f'selected-provider-dispatch-v16-source/");end=s.index("    ck('own_MANIFEST_actual_PLAN_OWNERS'",start)
new="""    selector_file=f'selected-provider-dispatch-v16-source/{pr}/actual-own-selector.json';selector=rd(selector_file);ownM=selector['MANIFEST_file'];ownV=selector['verifier_file'];M=rd(ownM);v=(R/ownV).read_text()
    ck('actual_own_MANIFEST_and_literal_entrypoint_selection',selector['own_head']==cr['own_head']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and hs(ownM)==selector['MANIFEST_sha256']and M[selector['verifier_key']]==hs(ownV)==selector['verifier_sha256']and F(ownspec['expected']['kappa'])==F(cr['kappa_record']))
    if pr==869:ck('own_literal_T8_selector',\"WITNESS_SPEC=str(PACKAGE/'data/SPEC.json')\"in v and\"--plan', PACKAGE/'data/PLAN.json'\"in v and\"--owners', PACKAGE/'data/OWNERS.json.gz'\"in v)
    else:ck('own_literal_T16_selector',\"SPEC8, SPEC16 = PKG / 'data/SPEC-T8.json', PKG / 'data/SPEC.json'\"in v and\"--plan', PKG / 'data/PLAN.json'\"in v and\"--owners', PKG / 'data/OWNERS.json.gz'\"in v)
    recovery=rd('u8-exact-earlier-selected-byte-recovery.json');rr=next(a for a in recovery['rows']if a['pr']==pr)
    ck('own_exact_recovered_U8_commitments',all(recovery['checks'].values())and recovery['script_sha256']==hs('recover_u8_selected_archive_bytes.py')and rr['own_head']==cr['own_head']and rr['own_SPEC_sha256']==cr['own_SPEC_sha256']and rr['program_semantic_sha256']==ownspec['providers']['gauge44']['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and rr['orientation_sha256']==ownspec['providers']['gauge44']['program_hashes'])
    primary.update({selector_file:hs(selector_file),ownM:hs(ownM)})
    for a in selector['verified_primary']:ck('actual_own_primary_'+a['file'],a['own_head']==cr['own_head']and hs(a['file'])==a['sha256']);primary[a['file']]=a['sha256']
"""
s=s[:start]+new+s[end:]
start=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'");end=s.index('\n    dep=',start)
s=s[:start]+"    deps+=['gaussian-only-parameter-ledger-peer-review.json','u8-own-selection-source/manifest.json','prepare_selected_provider_v16.py','prepare_selected_provider_v16_whole_costs.py','selected_provider_v13_whole_bounds.py','selected-provider-v13-whole-upper.md','u8-exact-earlier-selected-byte-recovery.json','recover_u8_selected_archive_bytes.py','u8-selected-native-recovery.json','u8_selected_native_recovery.py','u8-descriptive-counter-audit.md','u8-descriptive-counter-audit.json','u8_descriptive_counter_audit.py']"+s[end:]
s=s.replace('exact_four_own_selected_ends7_packages','exact_two_own_selected_U8_packages').replace('Own four selected ends7 finite Gaussian uppers','Own two selected U8 finite Gaussian uppers')
(R/'selected_provider_v16_whole_bounds.py').write_text(s,encoding='utf8')
a=(R/'ends7_descriptive_counter_audit.py').read_text().replace('selected_provider_dispatch_v13','selected_provider_dispatch_v16').replace('selected-provider-dispatch-v13','selected-provider-dispatch-v16').replace('ends7-descriptive-counter','u8-descriptive-counter').replace('own-selected-ends7-descriptive-meter-noninterference/1','own-selected-U8-descriptive-meter-noninterference/1')
(R/'u8_descriptive_counter_audit.py').write_text(a,encoding='utf8')
(R/'u8-descriptive-counter-audit.md').write_text('''# Descriptive entry-meter independence for two own U8 controllers

The actual canonical start/end frames and complete role widths are mandatory.
The descriptive global entering counter is absent from each own expected object
and remains absent. The pure role output lists actual nonzero start flags and
widths below9 separately. This audit checks that only serialized descriptive
output reads the entering variable, while the exact whole-invoice block reads
none of these fields. Executing it for each complete own controller at0 and2^100
gives identical full work/stock/router/tape arithmetic. It does not waive any
physical or operator invariant and does not claim a historical verifier PASS.
''',encoding='utf8')
print('PASS prepared two own U8 whole-cost evaluators')
