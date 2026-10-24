"""Exact own18/24 finite arithmetic; giant C++ producers are not invoked."""
from pathlib import Path
from hashlib import sha256
import json,subprocess,sys,tempfile,os
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'partial-swap-endpoint-source'
def hs(p):return sha256(p.read_bytes()).hexdigest()
for pr,name,cert in[(18,'partial_swap_network.py','partial-swap-network.json'),(24,'endpoint_gauge_network.py','endpoint-gauge-network.json')]:
 M=json.loads((D/f'{pr}-manifest.json').read_bytes())+json.loads((D/f'{pr}-additional-module-manifest.json').read_bytes());files={a['path']:a for a in M}
 for a in M:assert hs(R/a['file'])==a['sha256']and a['own_head']==M[0]['own_head']
 src=D/str(pr);env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0');env.pop('PYTHONOPTIMIZE',None)
 with tempfile.TemporaryDirectory(prefix='finite18-24-')as temporary:
  target=Path(temporary)/'certificate.json';run=subprocess.run([sys.executable,'-X','utf8','-B',str(src/'scripts'/name),'--output',str(target)],cwd=src,env=env,text=True,encoding='utf8',capture_output=True)
  if run.returncode:raise RuntimeError(str(pr)+'\n'+run.stdout+'\n'+run.stderr)
  actual=json.loads(target.read_bytes());saved=json.loads((src/'certificates'/cert).read_bytes())
  # The original producer serializes str(Path.relative_to(...)), hence Windows
  # backslashes versus the committed POSIX path keys. Only this source-map key
  # encoding is translated; mathematical objects and every source digest stay exact.
  assert {k:v for k,v in actual.items()if k!='source_sha256'}=={k:v for k,v in saved.items()if k!='source_sha256'},(pr,[k for k in actual if k!='source_sha256'and actual[k]!=saved.get(k)])
  actual_paths={p.replace('\\','/'):h for p,h in actual['source_sha256'].items()}
  assert len(actual_paths)==len(actual['source_sha256'])and actual_paths==saved['source_sha256']
  for p,h in actual_paths.items():assert p in files and files[p]['sha256']==h
 receipt=dict(schema='own-partial-swap-endpoint-finite-arithmetic-replay/1',pr=pr,own_head=M[0]['own_head'],status='passed_own_original_finite_arithmetic_with_explicit_path_key_encoding_translation',source_code_modified=False,own_source_cpp_producer_or_full_native_replayed=False,returncode=run.returncode,kappa=actual['kappa'],native_coordinate_rank=actual['complex']['counts']['m'],own_complex_saving=actual['complex']['saving'],own_complete_finite_guard=actual['guard'],own_recorded_certificate_file=files['certificates/'+cert]['file'],own_recorded_certificate_sha256=files['certificates/'+cert]['sha256'],source_path_key_encoding=dict(original_producer_expression='str(p.relative_to(ROOT))',host_backslash_to_committed_POSIX_keys_only=True,key_mapping_bijective=True,every_source_digest_exact=True,all_other_certificate_values_exact=True),all29_original_constraints_pass=len(actual['assembly']['constraints'])==29 and all(__import__('fractions').Fraction(v)>0 for v in actual['assembly']['constraints'].values()),source_sha256={a['file']:a['sha256']for a in M},dependency_hashes={str((D/f'{pr}-manifest.json').relative_to(R)).replace('\\','/'):hs(D/f'{pr}-manifest.json'),str((D/f'{pr}-additional-module-manifest.json').relative_to(R)).replace('\\','/'):hs(D/f'{pr}-additional-module-manifest.json')},stdout=run.stdout,stderr=run.stderr,script_sha256=hs(Path(__file__)),scope='Original exact finite histogram/count/moment/dependency-path/assembly arithmetic certificate only. Every mathematical and invoice object is exact after JSON parsing; only source-map path separators differ by the original platform-dependent str(Path) serialization, with a checked bijection and identical source digests. CPP producers/matching, simultaneous physical/native/all-column/phase, common-label, arbitrary dirty/full compiler and analytic/tape contracts are NOT independently replayed by this job.')
 (D/f'{pr}-fresh-finite-arithmetic.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8');print('PASS own',pr,'complete finite arithmetic reproduced; source path keys translated explicitly',flush=True)
