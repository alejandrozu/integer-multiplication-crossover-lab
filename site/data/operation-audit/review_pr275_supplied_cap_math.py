"""Independent source-selection, chronology and finite-cost review of own275."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json, subprocess, sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
names=[f'pr275-supplied-cap-gaussian-{k}.json'for k in ['native','early-upper','record-upper']]
allfiles=['pr275-supplied-cap-gaussian-bounds.json']+names
before={p:hs(p)for p in allfiles}
r=subprocess.run([sys.executable,'-X','utf8',str(R/'pr275_supplied_cap_gaussian_bounds.py')],cwd=R,capture_output=True,text=True,encoding='utf8',timeout=90)
assert r.returncode==0,r.stderr
assert all(hs(p)==h for p,h in before.items())
bundle=rd(allfiles[0]);assert bundle['status']=='closed_conditional_case'and bundle['checks_passed']==79 and all(bundle['checks'].values())and bundle['pr']==275
native,early,record=[rd(p)for p in names]
assert all(x['pr']==275 and x['own_head']==native['own_head']and x['status']=='closed_conditional_upper_only'and not x['ordinary_BIT_supplier_consumed']and x['invented_BIT_saving']is None for x in[native,early,record])
assert early['record_tail_quantified']and early['record_tail_certificate_sha256']==hs(names[2])
assert all(x['source_selected_kappa_correction']and x['kappa_record']!=x['frozen_metadata_kappa']and x['source_revision_included_at_merge']=='2026-10-16T15:51:16Z'for x in[native,early,record])
assert F(native['kappa_record'])==F(207704331708695884480429,125000000000000000000000000)
assert all(x['meaningful_lower']is None and not x['actual_first_crossing_known']for x in[native,early,record])
pins={p:hs(p)for p in ['pr275-supplied-cap-gaussian-bounds.md','pr275_supplied_cap_gaussian_bounds.py',Path(__file__).name]+allfiles}
for x in[native,early,record,native['own_native_theorem_facts']]:
    for group in['source_sha256','dependency_hashes']:
        for p,h in x[group].items():assert hs(p)==h,p;pins[p]=h
out=dict(schema='independent-ai-mathematical-review/1',pr=275,own_head=native['own_head'],review_status='PASS_under_explicit_retained_source_and_analytic_contracts',reviewed_sha256=pins,material_findings=[],fresh_evaluator_result=dict(checks=79,whole_output_files_byte_identical=4),source_selected_kappa_correction=True,source_selected_kappa=native['kappa_record'],preserved_historical_parser_kappa=native['frozen_metadata_kappa'],checked_mathematical_interfaces=[
    'Actual own MANIFEST/EXPECTED/UPSTREAM and verifier select the799 application at explicit immutable parent revision. Exact selected SPEC/PLAN/OWNERS bytes equal the independently checked799 native theorem inputs; neither matching kappa nor paid profile establishes selection.',
    'The historical595 parser selected an older433 fixture. The actual own merged-head EXPECTED target is independently bound and separately preserved. API primary objects prove the actual source head is the second parent of the named merge; its source commit date precedes the actual October16 merge. No application is backdated to PR creation.',
    'Selected native theorem rejects stale evidence and explicitly preserves the mismatching historical RESULT.spec_sha as unused selection authority. Both actual reconstructed program orientations and canonical commitments are bound to the exact own selected SPEC.',
    'Fresh positive rank surplus/paid halving, exact complete profile and G/E/C0/row inputs support newly enclosed taxed early/interior-record moments and coefficient below2^220000.',
    'Reduced50strict/2functional/7margin Gaussian-only ledger, full1000000Q stopped reserve and all7 actual cost rows are freshly evaluated. No BIT supplier, invented saving, inherited numerical cutoff or complete original dual-supplier replay is consumed.',
    'The own same-core record exponent is separately quantified after its explicit gate; this is a sufficient eventual bound for the new source-equivalent circuit, not an actual natural crossing or hardware timing.'
],limitations=[
    'The overlay must visibly retain the source-selection correction and original parser value and use actual accepted chronology; it must not silently rewrite frozen historical metadata.',
    'Full native required entry/output/absolute-phase/all-column endpoint, clean ownership/common-label/all-size and concrete normalized analytic/recovery/reference contracts remain explicit. This reviewer freshly executes the79-check whole evaluator, not the earlier expensive native engine.',
    'No input-size lower, universal implementation claim, formal-kernel or independent-human review is provided.'
],reproduction_command=['review_pr275_supplied_cap_math.py'])
(R/'pr275-supplied-cap-gaussian-peer-review.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('PASS own275 source-selection/math peer;79 checks;4 frozen outputs byte-identical')
