"""Versioned source-explicit adaptation of only the closed finite cost implementation."""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
assert hs('selected_provider_v12_whole_bounds.py')=='bc76ec8c9cd1baa6c0f225b5c049cf4c55bc0e76ce17e961804b991821e154ed'
s=(R/'selected_provider_v12_whole_bounds.py').read_text()
s=s.replace('REVIEW_CLOSED=True','REVIEW_CLOSED='+str(COST_REVIEW_CLOSED))
s=s.replace('selected-provider-v12','selected-provider-v13').replace('selected_provider_v12','selected_provider_v13').replace('selected-provider-dispatch-v12','selected-provider-dispatch-v13').replace('selected_provider_dispatch_v12','selected_provider_dispatch_v13').replace('cold14-typed-finite','ends7-selected-finite').replace('cold14-descriptive-counter','ends7-descriptive-counter').replace('cold14_descriptive_counter','ends7_descriptive_counter')
s=s.replace('ADMITTED={586,601,603,604,607,609,610,614,616,618}','ADMITTED={1104,1107,1117,1121}')
before="M['verify.py']==hs(ownV)and(\"default=P/'data/SPEC.json'\"in v or \"SPECFILE=P/'data/SPEC.json';SPEC=\"in v)and \"SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']\"in v"
after="M['verify_t16.py']==hs(ownV)and \"SPEC8, SPEC16 = PKG / 'data/SPEC-T8.json', PKG / 'data/SPEC.json'\"in v and 'spec=SPEC16'in v and \"'--plan', PKG / 'data/PLAN.json'\"in v and \"'--owners', PKG / 'data/OWNERS.json.gz'\"in v"
assert s.count(before)==1;s=s.replace(before,after)
before="deps+=['gaussian-only-parameter-ledger-peer-review.json','cold14-own-selection-source/manifest.json','prepare_selected_provider_v13.py','cold14-typed-chain-native-byte-recovery.json','recover_cold14_chain_native_bytes.py','cold14-source-reconstruction/source-closure-manifest.json','cold14-retained-baseline-seeds/manifest.json','ends7-descriptive-counter-audit.md','ends7-descriptive-counter-audit.json','ends7_descriptive_counter_audit.py']"
after="deps+=['gaussian-only-parameter-ledger-peer-review.json','ends7-own-selection-source/source-fetch-manifest.json','prepare_selected_provider_v13.py','prepare_selected_provider_v13_whole_costs.py','selected_provider_v12_whole_bounds.py','selected-provider-v12-whole-upper.md','pr1104-exact-selected-ends7-native-recovery.json','recover_pr1104_ends7_selected_native.py','ends7-descriptive-counter-audit.md','ends7-descriptive-counter-audit.json','ends7_descriptive_counter_audit.py']"
assert s.count(before)==1;s=s.replace(before,after)
s=s.replace("exact_ten_own_typed_cold14_packages","exact_four_own_selected_ends7_packages").replace('Own ten cold14-related finite Gaussian uppers','Own four selected ends7 finite Gaussian uppers')
(R/'selected_provider_v13_whole_bounds.py').write_text(s,encoding='utf8')
audit=(R/'cold14_descriptive_counter_audit.py').read_text().replace('selected_provider_dispatch_v12','selected_provider_dispatch_v13').replace('selected-provider-dispatch-v12','selected-provider-dispatch-v13').replace('cold14-descriptive-counter','ends7-descriptive-counter')
audit=audit.replace("spec['expected']['entering_helper_roles']","spec['expected'].get('entering_helper_roles')")
audit=audit.replace('Cases610/618 retain a source counter unequal to both actual initial and below-nine-width counts.','These four own SPECs do not declare a global entering meter; the absence is preserved while actual initial-frame and width meters are separately computed.')
audit=audit.replace('own-selected-cold14-descriptive-meter-noninterference/1','own-selected-ends7-descriptive-meter-noninterference/1')
(R/'ends7_descriptive_counter_audit.py').write_text(audit,encoding='utf8')
print('PASS built four-source own-selector finite evaluator and descriptive noninterference audit')
