"""Execute unchanged own523 full offline reconstruction in a temporary tree."""
from pathlib import Path
from hashlib import sha256,sha1
import datetime,json,os,subprocess,sys,tempfile,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;O=R/'pr523-punctured112-source';m=json.loads((O/'523-manifest.json').read_bytes());pre='research/punctured112-global/';start=time.monotonic();D=R/'pr523-fresh-replay-outputs';D.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='punctured112-')as tmp:
 root=Path(tmp);by={x['path'][len(pre):]:x for x in m}
 for x in m:
  b=(R/x['file']).read_bytes();assert sha256(b).hexdigest()==x['sha256'];assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['expected_api_blob'];p=root/x['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 mf=json.loads((root/pre/'MANIFEST.json').read_bytes())
 for name,x in mf['files'].items():
  b=(root/pre/name).read_bytes();assert sha256(b.replace(b'\r\n',b'\n')if x['mode']=='lf-text'else b).hexdigest()==x['sha256'],name
 env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env['PYTHONUTF8']='1';env['PYTHONINTMAXSTRDIGITS']='0';env.pop('PYTHONOPTIMIZE',None)
 work=root/'freshwork';cmd=[sys.executable,'-X','utf8','-B',str(root/pre/'verify.py'),'--work',str(work)];print('RUN unchanged full523offline verifier;124sourceMANIFEST entries authenticated',flush=True)
 z=subprocess.run(cmd,cwd=root,env=env,capture_output=False,timeout=1800)
 derived=[]
 if work.exists():
  for p in work.rglob('*'):
   if p.is_file()and(p.suffix in ['.json','.gz','.log']):
    b=p.read_bytes();h=sha256(b).hexdigest();f=D/(h[:16]+'__'+p.name);f.write_bytes(b);derived.append(dict(original_work_path=p.relative_to(work).as_posix(),file=f.relative_to(R).as_posix(),sha256=h,bytes=len(b)))
 receipt=dict(schema='own-pr523-full-fresh-reconstruction/1',pr=523,own_head=m[0]['own_head'],status='passed_unchanged_full_own_source_reconstruction'if z.returncode==0 else'failed_unchanged_full_own_source_reconstruction',exit_code=z.returncode,elapsed_seconds=time.monotonic()-start,source_manifest='pr523-punctured112-source/523-manifest.json',source_manifest_sha256=sha256((O/'523-manifest.json').read_bytes()).hexdigest(),own_package_MANIFEST_entries=len(mf['files']),all_own_manifest_entries_checked=True,source_code_modified=False,arguments=['python','-X','utf8','-B',pre+'verify.py','--work','<newtempdir>'],executed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),derived_artifacts=derived,scope='Fresh unchanged source reconstruction includes predecessor/native/phase/physical/invoice/outer stages only if statusPASS; inherited all-size/analytic/operator interfaces remain conditional.')
 (R/'pr523-full-fresh-replay.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items()if k!='derived_artifacts'},indent=2),flush=True);assert z.returncode==0
