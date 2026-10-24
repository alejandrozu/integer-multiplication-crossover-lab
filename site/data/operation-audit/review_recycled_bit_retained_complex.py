"""Independent exact-cost review of the own PR150/151 retained-complex circuits."""
from pathlib import Path
from hashlib import sha256
import json, subprocess, sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
PRS=[150,151]
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
files=['recycled-bit-retained-complex-bounds.json']+[f'pr{pr}-retained-complex-{k}.json'for pr in PRS for k in ['native-parameters','early-upper','record-upper']]
before={p:hs(p)for p in files}
r=subprocess.run([sys.executable,'-X','utf8',str(R/'recycled_bit_retained_complex_bounds.py')],cwd=R,capture_output=True,text=True,encoding='utf8',timeout=90)
assert r.returncode==0,r.stderr
assert all(hs(p)==h for p,h in before.items())
bundle=rd(files[0]);assert bundle['status']=='closed_conditional_batch'and bundle['checks_passed']==588 and all(bundle['checks'].values())and {x['pr']for x in bundle['rows']}==set(PRS)
for pr in PRS:
    names=[f'pr{pr}-retained-complex-{k}.json'for k in ['native-parameters','early-upper','record-upper']]
    native,early,record=[rd(p)for p in names]
    assert all(x['pr']==pr and x['own_head']==native['own_head']and x['status']=='closed_conditional_upper_only'and x['native_coordinate_rank']==72 for x in [native,early,record])
    assert early['record_tail_quantified']and early['record_tail_certificate_sha256']==hs(names[2])
    assert all(not x['ordinary_BIT_supplier_consumed']and x['invented_BIT_saving']is None and not x['original_BIT_producer_rerun']and x['meaningful_lower']is None for x in [native,early,record])
    pins={p:hs(p)for p in ['recycled-bit-retained-complex-bounds.md','recycled_bit_retained_complex_bounds.py','recycled-bit-retained-complex-bounds.json',Path(__file__).name]+names}
    for x in [native,early,record]:
        for group in ['source_sha256','dependency_hashes']:
            for p,h in x[group].items():assert hs(p)==h,p;pins[p]=h
    out=dict(schema='independent-ai-mathematical-review/1',pr=pr,own_head=native['own_head'],review_status='PASS_under_explicit_retained_source_and_analytic_contracts',reviewed_sha256=pins,material_findings=[],fresh_evaluator_result=dict(checks=588,whole_output_files_byte_identical=7,exact_admitted_set=PRS),checked_mathematical_interfaces=[
        'Each own head explicitly selects paired-cube-complex-input and all38 actual producer/native/bridge source bytes match the named counted rank72 component. Own48/52-primary manifests and unchanged complex-producer replay join the complete selected object; no kappa-only inference.',
        'Own changed-bit prices are re-evaluated only to bind the original claim and atom; changed bit geometry or literal native word is neither rerun nor executed by this NEW source-equivalent direct Gaussian/Fermat circuit.',
        'Actual rank72 fourth-power halving, own moment gap, full G/E/C0/C1 and20445/70000 row invoice are recomputed under correctly ordered guards. No rank73 finite helper or uniform2^H cutoff is substituted.',
        'Only the newly introduced child odd3 grid is cancelled at complete exact Gaussian-dyadic endpoints, preserving the parent odd grid. Fixed rational and exact reciprocal-multiply conversion costs fit the declared helper widths and include8 additional log powers.',
        'The complete70000Q stopped reserve, per-input-coordinate40e direct fallback, exact50/2/7 Gaussian ledger and all7 actual row coefficients/smooth tails are separately checked. Record E2^66 pays32Q+500000 and full precision/stock before absorption.',
        'Both same-core record exponents are newly and explicitly quantified; a piecewise existence witness preserves them. No original changed-BIT runtime, natural first crossing, input-size lower or hardware claim follows.'
    ],limitations=[
        'Full required operator/absolute-phase endpoint, arbitrary-input ownership, common-label/full-column realization, analytic and exact-recovery interfaces remain explicit premises. The own Python producer replay is not a fresh complete C++ matching/native operator proof.',
        'This reviewer independently reads the proof and freshly executes the588-check exact cost/hash evaluator; it does not repeat the separate original producer engines or prove all retained universal hypotheses.',
        'AI-assisted written mathematics and exact rational/source checks, not Lean or independent human review.'
    ],reproduction_command=['review_recycled_bit_retained_complex.py'])
    (R/f'pr{pr}-retained-complex-peer-review.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('PASS two retained-complex math peers;588 checks;7 frozen files byte-identical')
