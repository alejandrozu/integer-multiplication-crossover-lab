"""Reconstruct own937 immutable source paths and execute its untouched finite checker."""
from pathlib import Path
from hashlib import sha256,sha1
import json,subprocess,sys,tempfile
R=Path(__file__).resolve().parent
mf='pr937-finite-source/source-manifest.json';raw=(R/mf).read_bytes();m=json.loads(raw)
assert m['pr']==937 and m['own_head']=='b303fed6dfe2066dcd78c0d8ed74d2a3b153ba72'
bound={};checks={}
with tempfile.TemporaryDirectory(prefix='own937-')as tmp:
 t=Path(tmp)
 for i,a in enumerate(m['source_manifest']):
  p=Path(a['path']);assert not p.is_absolute()and '..'not in p.parts
  b=(R/a['file']).read_bytes();h=sha256(b).hexdigest();git=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  assert h==a['sha256']and git==a['git_blob_sha1'];assert a['expected_api_blob_sha1']is None or git==a['expected_api_blob_sha1'];assert a['own_declared_sha256']is None or h==a['own_declared_sha256']
  dest=t/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b);bound[a['file']]=h;checks[f'own_source_{i}_{p.as_posix()}']=True
 cmd=[sys.executable,'-I','-B',str(t/'research/dyadic-center-two-shear/verify.py')]
 r=subprocess.run(cmd,cwd=t,capture_output=True,text=True,encoding='utf8',timeout=900)
 assert r.returncode==0,(r.returncode,r.stdout[-3000:],r.stderr[-3000:])
 assert r.stdout.strip().endswith('PASS_DYADIC_CENTER_TWO_SHEAR h=26 G+H=45381->42600 saved=112797360000 no_new_kappa')
 checks['untouched_own_finite_verifier_returncode_zero']=True
 checks['exact_saved_expected_receipt_passed_without_rewrite']=True
out=dict(schema='own937-untouched-finite-replay/1',status='PASS_original_finite_verifier_and_exact_saved_receipt',pr=937,own_head=m['own_head'],source_manifest_sha256=sha256(raw).hexdigest(),source_sha256=bound,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),original_own_finite_verifier_executed=True,full_integer_algorithm_or_universal_phase_proved=False,checks=checks,checks_passed=len(checks),returncode=0,stdout=r.stdout.strip())
f=R/'pr937-finite-source/fresh-finite-verification.json';f.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS own937 untouched finite source',len(checks),'checks')
