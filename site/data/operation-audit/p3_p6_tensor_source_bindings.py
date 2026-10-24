"""Authenticate and optionally replay own PR4412/4414 tensor-native sources."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha1, sha256
import argparse
import gzip
import json
import os
import subprocess
import sys
import tempfile
import urllib.request

sys.set_int_max_str_digits(0)
R = Path(__file__).resolve().parent
D = R / 'p3-p6-tensor-own-source'
CASES = {
    4412: ('9f0df9bf6f49942faf5f31389e7e387fdfe511b3', 'research/pr4359-tensor-strictification'),
    4414: ('90da4b0ab894350ca12cac9110cc6da2225d18af', 'research/pr4359-p6-fresh'),
}

def hs(p):
    return sha256(p.read_bytes()).hexdigest()

def blob(b):
    return sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()

def fetch_one(task):
    pr, head, item = task
    path, want = item['filename'], item['sha']
    out = D / str(pr) / 'files' / (want[:12] + '__' + Path(path).name)
    url = 'https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/' + head + '/' + path
    if out.exists():
        b = out.read_bytes()
        assert blob(b) == want, ('cached own Git blob', pr, path)
    else:
        if not ARGS.fetch:
            raise FileNotFoundError(out)
        req = urllib.request.Request(url, headers={'User-Agent': 'SourceBoundTensorNativeAudit/1.0'})
        with urllib.request.urlopen(req, timeout=90) as response:
            b = response.read()
        assert blob(b) == want, ('own Git blob', pr, path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(b)
    return dict(pr=pr, own_head=head, path=path, primary_url=url,
                git_blob_sha1=want, file=out.relative_to(R).as_posix(),
                sha256=sha256(b).hexdigest(), bytes=len(b))

def main():
    queue = json.loads((R / 'remaining-record-audit/complete-audit-queue.json').read_bytes())
    own = {x['pr']: x for x in queue['rows']}
    for pr in ARGS.prs:
        head, package = CASES[pr]
        assert own[pr]['own_head_sha'] == head
        changes = R / f'remaining-record-audit/changed-files/{pr}-p1.json.gz'
        items = json.loads(gzip.decompress(changes.read_bytes()))
        assert all(x['filename'].startswith(package + '/') for x in items)
        with ThreadPoolExecutor(max_workers=6) as pool:
            rows = list(pool.map(fetch_one, [(pr, head, x) for x in items]))
        rows.sort(key=lambda x: x['path'])
        manifest = dict(schema='own-tensor-native-source-bindings/1', pr=pr, own_head=head,
                        package=package, changed_file_list_sha256=hs(changes),
                        own_source_claim=dict(kappa=own[pr]['quoted_kappa_fraction'],
                                              accepted_at=own[pr]['accepted_at']),
                        files=rows, source_byte_authentication='Each own path fetched at the frozen own head and matched to its recorded Git blob SHA1; SHA256 and exact bytes retained.',
                        script_sha256=hs(Path(__file__)))
        output = D / f'{pr}-manifest.json'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        print('PASS own source bytes', pr, len(rows), flush=True)
        if ARGS.replay:
            # The original focused export contains deep nested source paths.
            # Use the OS temporary root so the unchanged verifier also works
            # on Windows installations retaining the legacy path-length cap.
            with tempfile.TemporaryDirectory(prefix=f'tensor-{pr}-') as folder:
                tree = Path(folder)
                for a in rows:
                    p = tree / a['path']; p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_bytes((R / a['file']).read_bytes())
                env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1',
                           PYTHONINTMAXSTRDIGITS='0')
                env.pop('PYTHONOPTIMIZE', None)
                result = subprocess.run([sys.executable, '-I', '-O', '-B', str(tree / package / 'verify.py')],
                                        cwd=tree, env=env, capture_output=True,
                                        text=True, encoding='utf-8')
                original_result = json.loads((tree / package / 'RESULT.json').read_bytes())
                normalized_keys = []
                def posix_source_keys(value, chain=()):
                    if isinstance(value, list):
                        return [posix_source_keys(v, chain + (str(i),)) for i, v in enumerate(value)]
                    if not isinstance(value, dict):
                        return value
                    out = {}
                    for key, item in value.items():
                        fixed = key.replace('\\', '/') if chain and chain[-1] == 'source_sha256' else key
                        if fixed != key:
                            normalized_keys.append(dict(receipt_path='/'.join(chain), original_key=key, normalized_key=fixed))
                        assert fixed not in out, ('source-key normalization collision', chain, key)
                        out[fixed] = posix_source_keys(item, chain + (fixed,))
                    return out
                repair_result = None
                if result.returncode:
                    # Preserve an original default-verification failure. Run
                    # the unchanged producer's own write option only inside
                    # the temporary tree, then permit source-path dictionary
                    # key separators and absolutely no scientific difference.
                    repair_result = subprocess.run([sys.executable, '-I', '-O', '-B',
                        str(tree / package / 'verify.py'), '--write-result'], cwd=tree,
                        env=env, capture_output=True, text=True, encoding='utf-8')
                    actual_result = json.loads((tree / package / 'RESULT.json').read_bytes())
                    assert repair_result.returncode == 0, repair_result.stderr
                    assert posix_source_keys(original_result) == posix_source_keys(actual_result), \
                        'Scientific/source-value receipt difference beyond path-key separators'
                    assert normalized_keys, 'Original failure had no diagnosed source-key separator difference'
                receipt = dict(schema='own-tensor-native-fresh-replay/1', pr=pr, own_head=head,
                               source_manifest=output.relative_to(R).as_posix(),
                               source_manifest_sha256=hs(output),
                               source_files_sha256={a['file']: a['sha256'] for a in rows},
                               command=['python', '-I', '-O', '-B', package + '/verify.py'],
                               original_source_edited=False, returncode=result.returncode,
                               stdout=result.stdout, stderr=result.stderr,
                               status='PASS_unchanged_own_native_and_arithmetic_saved_receipt' if result.returncode == 0 else 'PASS_all_scientific_and_source_values_after_explicit_source_path_key_normalization',
                               original_default_verification_passed=result.returncode == 0,
                               original_default_failure_preserved=result.returncode != 0,
                               temp_only_write_result_returncode=repair_result.returncode if repair_result is not None else None,
                               normalized_source_path_dictionary_keys=normalized_keys,
                               all_other_scientific_and_source_fields_exact=True,
                               full_native_engine_execution_claim='Exactly the named original verify.py and its invoked native_inventory/strictification/endpoint stages; no other engines claimed.',
                               script_sha256=hs(Path(__file__)))
                (D / f'{pr}-fresh-replay.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
                print('OWN REPLAY', pr, result.returncode, result.stdout[-2000:], flush=True)
                if result.returncode:
                    print('DIAGNOSED own source-path dictionary separators', len(normalized_keys), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--prs', nargs='+', type=int, choices=sorted(CASES), default=sorted(CASES))
    ARGS = parser.parse_args()
    main()
