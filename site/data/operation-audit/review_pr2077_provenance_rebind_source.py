"""Narrow PR2077 provenance rebind after the separately authorized V16 repair."""
from pathlib import Path
from hashlib import sha256
import json, os, subprocess, sys, tempfile

sys.set_int_max_str_digits(0)
R = Path(__file__).resolve().parent
P = 'pr2077-v16-document-provenance-rebind/previous/'
OLD_DOC = 'cabb3bb2ac6b276aa685d7caf9f3c04a1c4cc8a70bb28824180b57e92776ae7c'
NEW_DOC = '76cf5c7b662126affdffa484a9ff046abeddf1eceeee27f5598bf20ec3c77f98'
certs = [f'pr2077-vacancy-chain-finite-{k}.json' for k in ['native', 'early-upper', 'record-upper']]
old_hashes = dict(zip(certs, ['36d6cf3bdf4d4537e729d036bc5642afb74cbadef26afa0dc12ee8fa794b2f85', '63652ad8ba0d36697594d3dad736e115856d5b3952920d074b3f93580e11ac6a', 'c156d927c0be3fa56889654e36fe3b9c04de3b7c925d5b5c2e14666c665dadb2']))
old_peer = 'pr2077-vacancy-chain-finite-source-peer-review.json'
checks = {}
def ck(n, v):
    assert v, n
    checks[n] = True
def hs(f): return sha256((R / f).read_bytes()).hexdigest()
def rd(f): return json.loads((R / f).read_bytes())
def differences(a, b, path=()):
    if type(a) is not type(b): return [(path, a, b)]
    if isinstance(a, dict):
        return [d for k in sorted(a.keys() | b.keys()) for d in differences(a.get(k, '<absent>'), b.get(k, '<absent>'), path + (k,))]
    if isinstance(a, list):
        if len(a) != len(b): return [(path + ('length',), len(a), len(b))]
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, path + (i,))]
    return [] if a == b else [(path, a, b)]

previous_peer = rd(P + old_peer)
ck('previous_peer_exact_frozen_bytes', hs(P + old_peer) == '223f0bd89e13c03a0a32b68a3aab3bdfbb80ba4f7c2f8afde6a1c2f2fdfe10d4')
ck('repaired_V16_document_exact_current_bytes', hs('selected-provider-v16-whole-upper.md') == NEW_DOC)
allowed_changes = []
for f in certs:
    ck('preserved_previous_' + f, hs(P + f) == old_hashes[f] == previous_peer['reviewed_sha256'][f])
    old, new = rd(P + f), rd(f)
    expected = [(('dependency_hashes', 'selected-provider-v16-whole-upper.md'), OLD_DOC, NEW_DOC)]
    if f.endswith('early-upper.json'):
        expected += [(('record_tail_certificate_sha256',), old_hashes[certs[2]], hs(certs[2]))]
    ds = differences(old, new)
    ck('only_explicit_provenance_leaves_' + f, sorted(ds, key=lambda x: str(x[0])) == sorted(expected, key=lambda x: str(x[0])))
    ck('same_own_source_head_and_complete_source_map_' + f, old['own_head'] == new['own_head'] == '407712103b605a662a89a56f9c42b93dca69126b' and old['source_sha256'] == new['source_sha256'])
    allowed_changes += [dict(file=f, json_path=list(p), previous=a, current=b) for p, a, b in ds]
ck('exactly_four_provenance_leaves_total', len(allowed_changes) == 4)
changed_previous_peer_inputs = []
for f, h in previous_peer['reviewed_sha256'].items():
    if hs(f) != h: changed_previous_peer_inputs.append(f)
    else: ck('unchanged_original_source_and_cost_input_' + f, True)
ck('only_three_certificates_and_V16_document_rebound', sorted(changed_previous_peer_inputs) == sorted(certs + ['selected-provider-v16-whole-upper.md']))
before = {f: hs(f) for f in previous_peer['reviewed_sha256']}
runs = []
with tempfile.TemporaryDirectory(prefix='pr2077-provenance-offline-') as td:
    Path(td, 'sitecustomize.py').write_text('import socket\ndef blocked(*a,**k): raise RuntimeError("Network disabled for provenance replay")\nsocket.create_connection=blocked\nsocket.socket.connect=blocked\nsocket.socket.connect_ex=blocked\nsocket.getaddrinfo=blocked\n', encoding='utf8')
    env = dict(os.environ, PYTHONPATH=td, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
    for i, script in enumerate(['selected_provider_v18_whole_bounds.py', 'selected_provider_v18_whole_bounds.py', 'review_selected_provider_v18_source.py']):
        result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(R / script)], cwd=R, env=env, capture_output=True, text=True, encoding='utf8', timeout=180)
        ck('network_disabled_replay_' + str(i), result.returncode == 0)
        ck('all_current_source_and_cost_bytes_stable_' + str(i), all(hs(f) == h for f, h in before.items()))
        runs.append(dict(script=script, returncode=result.returncode, stdout=result.stdout.strip()))
current_peer = rd(old_peer)
for f, h in before.items(): ck('refreshed_source_peer_binds_current_' + f, current_peer['reviewed_sha256'][f] == h)
ck('no_source_peer_material_findings', current_peer['material_findings_remaining'] == [] and all(current_peer['checks'].values()))
pins = dict(before)
pins.update({P + f: hs(P + f) for f in certs + [old_peer]})
pins.update({f: hs(f) for f in [old_peer, 'review_selected_provider_v18_source.py', Path(__file__).name, 'pr2077-v16-document-provenance-rebind.md']})
out = dict(schema='own2077-V16-document-provenance-rebind-source-audit/1', pr=2077, own_head='407712103b605a662a89a56f9c42b93dca69126b', review_status='PASS', correction='After the separately authorized V16 wallclock-portability document repair, the PR2077 evaluator correctly consumed the repaired document but the three frozen PR2077 certificates still stored its previous digest. This audit permits exactly that document-hash leaf in all three certificates and the consequential early-certificate reference to the rebound record certificate. It permits no other leaf change.', exact_changed_leaves=allowed_changes, all_mathematical_values_contracts_sources_native_invoices_and_endpoints_unchanged=True, all_original_producer_and_source_selection_bytes_unchanged=True, previous_snapshots_are_comparison_evidence_only_not_active_aliases=True, original_conditions_and_limitations_unchanged=True, network_disabled=True, fresh_reproduction_jobs=runs, reviewed_sha256=pins, checks_passed=len(checks), checks=checks, material_findings_remaining=[], reproducer_sha256=hs(Path(__file__).name))
(R / 'pr2077-v16-document-provenance-rebind-source-audit.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf8')
print('PASS', len(checks), 'narrow PR2077 provenance-rebind source checks; exactly4 allowed leaves; two stable whole replays plus source-peer replay')
