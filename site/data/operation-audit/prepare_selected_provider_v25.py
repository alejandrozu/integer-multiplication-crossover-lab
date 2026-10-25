"""Own PR619 fine-grid application: exact source selection, never a kappa join."""
from pathlib import Path
from hashlib import sha256, sha1
from fractions import Fraction as F
import base64, copy, gzip, json

R = Path(__file__).resolve().parent
D = R / 'selected-provider-dispatch-v25-source/619'
D.mkdir(parents=True, exist_ok=True)
def hs(f): return sha256((R / f).read_bytes()).hexdigest()
def rd(f):
    b = (R / f).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2] == b'\x1f\x8b' else b)
def ident(o): return sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
def differences(a, b, p=()):
    if type(a) is not type(b): return [(p, a, b)]
    if isinstance(a, dict): return [d for k in sorted(a.keys() | b.keys()) for d in differences(a.get(k, '<absent>'), b.get(k, '<absent>'), p + (k,))]
    if isinstance(a, list):
        if len(a) != len(b): return [(p + ('length',), len(a), len(b))]
        return [d for i, (v, w) in enumerate(zip(a, b)) for d in differences(v, w, p + (i,))]
    return [] if a == b else [(p, a, b)]
mf = 'pr619-selected-complex-source/source-manifest.json'
own = rd(mf)
assert own['pr'] == 619 and own['own_head'] == '9879380b4e9fd922842a35cb3edefd712debfdac'
M = rd(own['MANIFEST_file'])
files = {a['relative']: dict(a, own_API_git_blob_sha1=a['own_changed_file_API_blob_sha1']) for a in own['files']}
assert set(M) == set(files) and len(M) == 289
api = rd(own['actual_own_MANIFEST_API_file'])
raw = (R / own['MANIFEST_file']).read_bytes()
assert base64.b64decode(api['content']) == raw and hs(own['MANIFEST_file']) == own['MANIFEST_sha256']
assert api['path'] == own['selected_package'] + '/MANIFEST.json' and sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == api['sha'] == own['actual_own_MANIFEST_Git_blob_sha1']
for rel, a in files.items():
    raw = (R / a['file']).read_bytes()
    assert hs(a['file']) == M[rel] == a['sha256'] and a['own_head'] == own['own_head']
    assert sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == a['git_blob_sha1'] == a['own_API_git_blob_sha1']
ownspec = files['data/SPEC.json']
s = rd(ownspec['file'])
old = rd('selected-provider-dispatch-v10-inputs.json')
row = copy.deepcopy(next(a for a in old['cohort_rows'] if a['pr'] == 619))
claim = copy.deepcopy(next(a for a in old['claim_metadata'] if a['pr'] == 619))
assert row['own_head'] == own['own_head'] and F(s['expected']['kappa']) == F(claim['quoted_kappa_fraction'])
for a in row['verified_components']:
    if a.get('path') == own['selected_package'] + '/data/SPEC.json':
        assert a['sha256'] == ownspec['sha256']
        a['file'] = ownspec['file']
v = (R / files['verify.py']['file']).read_text()
assert "SPECFILE=a.spec.resolve();SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']" in v
assert "default=P/'data/SPEC.json'" in v and "'--plan',P/'data/PLAN.json'" in v and "'--owners',P/'data/OWNERS.json.gz'" in v
base_mf = rd('early-hyperplane-cold-own-source/source-manifest.json')
base = next(a for a in base_mf['rows'] if a['pr'] == 615)
t = rd(base['SPEC_file'])
ds = differences(t, s)
allowed = {('build', 'sources', k, 'dir') for k in ['frame_coalescing', 'joint_prefix', 'larger_gain', 'multicold', 'structural_gain']} | {('expected', k) for k in ['conservative_kappa_decimal', 'kappa', 'kappa_decimal']}
assert len(ds) == 8 and {p for p, a, b in ds} == allowed
assert s['providers'] == t['providers'] and s['dispatch'] == t['dispatch'] and s['data'] == t['data']
recfile = 'early-hyperplane-cold-selected-native-recovery.json'
rec = rd(recfile)
assert rec['checks_passed'] == 1645 and all(rec['checks'].values()) and rec['script_sha256'] == hs('recover_early_hyperplane_cold_native.py')
sources, bindings = {}, {}
for pid, provider in s['providers'].items():
    raw_hash = s['build']['providers'][pid]['word_content_sha256']
    selected = [a for a in rec['selected_own_providers'] if a['pr'] == 615 and a['provider'] == pid]
    assert len(selected) == 1 and selected[0]['own_head'] == base['own_head'] and selected[0]['RAW_content_sha256'] == raw_hash
    matches = [a for a in rec['outputs'] if a['pr'] == 615 and a['provider'] == pid and a['raw_content_sha256'] == raw_hash]
    assert all(sum(a['artifact'] == name for a in matches) == 1 for name in ['CANONICAL-WORD.json.gz', 'LOCAL-PROGRAMS.json.gz'])
    aa = {a['artifact']: a for a in matches}
    can, program = aa['CANONICAL-WORD.json.gz'], aa['LOCAL-PROGRAMS.json.gz']
    assert ident(rd(can['file'])) == can['semantic_sha256'] == provider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']
    assert ident(rd(program['file'])) == program['semantic_sha256'] == provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']
    assert program['orientation_sha256'] == provider['program_hashes']
    for a in [can, program]:
        assert hs(a['file']) == a['sha256']
        sources[a['file']] = dict(file=a['file'], sha256=a['sha256'], origin='actual_derived_byte_object_matching_own619_direct_SPEC_commitments', primary=dict(recovery_file=recfile, recovery_sha256=hs(recfile), predecessor_pr=615, payload=a))
    bindings[pid] = dict(own_RAW_content_sha256=raw_hash, canonical_file=can['file'], program_file=program['file'], canonical_sha256=can['semantic_sha256'], program_sha256=program['semantic_sha256'], orientation_sha256=provider['program_hashes'])
for kind in ['PLAN', 'OWNERS']:
    rel = 'data/PLAN.json' if kind == 'PLAN' else 'data/OWNERS.json.gz'
    a = files[rel]
    assert a['sha256'] == s['data'][kind.lower() + '_sha256']
    receipt = dict(pr=619, own_head=own['own_head'], path=a['path'], file=a['file'], sha256=a['sha256'], bytes=a['bytes'], own_SPEC_expected_sha256=a['sha256'], status='authenticated_own_SPEC_declared_bytes', primary=a)
    (D / (kind + '.json')).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf8')
ma = dict(pr=619, own_head=own['own_head'], path=own['selected_package'] + '/MANIFEST.json', relative='MANIFEST.json', file=own['MANIFEST_file'], sha256=own['MANIFEST_sha256'], bytes=len((R / own['MANIFEST_file']).read_bytes()), primary_url=f"https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/{own['own_head']}/{own['selected_package']}/MANIFEST.json", git_blob_sha1=api['sha'], own_API_git_blob_sha1=api['sha'], own_MANIFEST_authenticated_by_API_blob=True)
selector = dict(pr=619, own_head=own['own_head'], SPEC_file=ownspec['file'], SPEC_sha256=ownspec['sha256'], MANIFEST_file=own['MANIFEST_file'], MANIFEST_sha256=own['MANIFEST_sha256'], verifier_file=files['verify.py']['file'], verifier_sha256=files['verify.py']['sha256'], verified_primary=[ma, *files.values()], actual_own_MANIFEST_API_file=own['actual_own_MANIFEST_API_file'], actual_own_MANIFEST_API_sha256=own['actual_own_MANIFEST_API_sha256'], actual_literal_spec_driven_native_and_global_data_selection=True, exact_own_selected_native_bindings=bindings, own_selected_native_recovery_file=recfile, own_selected_native_recovery_sha256=hs(recfile), actual_own_SPEC_vs_PR615_differences=[dict(path=list(p), previous=a, own=b) for p, a, b in ds], native_commitments_directly_bound_by_own_SPEC=True, native_recovery_reused_only_as_exact_byte_object=True, previous_invoice_or_cutoff_consumed=False, complete_historical_package_replay_claimed=False, original_full_global_or_native_phase_PASS_claimed=False)
(D / 'actual-own-selector.json').write_text(json.dumps(selector, indent=2) + '\n', encoding='utf8')
deps = ['selected-provider-dispatch-v10-inputs.json', 'selected_provider_dispatch_v17.py', mf, 'fetch_pr619_selected_complex_sources.py', 'prepare_selected_provider_v25.py', recfile, 'recover_early_hyperplane_cold_native.py', 'early-hyperplane-cold-own-source/source-manifest.json']
snap = dict(schema='selected-provider-dispatch-frozen-inputs/25', cohort_rows=[row], claim_metadata=[claim], actual_native_archive_sources=list(sources.values()), original_input_sha256={f:hs(f) for f in deps}, scope='Own619 literal bundled source and exact native/PLAN/OWNERS commitments. The eight declared differences from615 are five source directory locators and three output-grid values. Native data equality is checked independently, not inferred from kappa or provider names. Fresh own complete physical census and new invoice are mandatory; no old cutoff or invoice is transferred.')
(R / 'selected-provider-dispatch-v25-inputs.json').write_text(json.dumps(snap, indent=2) + '\n', encoding='utf8')
source = (R / 'selected_provider_dispatch_v17.py').read_text().replace('selected-provider-dispatch-v17', 'selected-provider-dispatch-v25').replace('V17', 'V25')
(R / 'selected_provider_dispatch_v25.py').write_text(source, encoding='utf8')
print('PASS own619 exact fullM/literal-selector/native commitments; fresh physical census still required')
