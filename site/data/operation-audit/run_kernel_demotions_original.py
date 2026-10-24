"""Fresh unchanged own1154/1176 native/owner/invoice/assembly replays."""
from pathlib import Path
from hashlib import sha256
import json,os,subprocess,sys,tempfile
A=Path(__file__).resolve().parent;D=A/'kernel-demotions-fresh-replay';D.mkdir(exist_ok=True);manifest=json.loads((A/'kernel-demotions-source/manifest.json').read_bytes());hs=lambda p:sha256(p.read_bytes()).hexdigest();runs=[]
for key,root in manifest['packages'].items():
 pr=int(key);objects=[a for a in manifest['objects']if a['pr']==pr]
 with tempfile.TemporaryDirectory(prefix='kdem-'+key+'-')as td:
  T=Path(td);P=T/'package';P.mkdir();out=T/'result'
  for a in objects:
   raw=(A/a['file']).read_bytes();assert sha256(raw).hexdigest()==a['sha256'];path=P/a['relative'];assert path.resolve().is_relative_to(P.resolve());path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
  raw=(A/root['MANIFEST_file']).read_bytes();assert sha256(raw).hexdigest()==root['MANIFEST_sha256'];(P/'MANIFEST.json').write_bytes(raw)
  env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0');env.pop('PYTHONOPTIMIZE',None)
  logfile=D/(key+'-original-execution.log');print('RUNunchangedownfullsource',pr,flush=True)
  with logfile.open('w',encoding='utf8')as log:r=subprocess.run([sys.executable,'-I','-B',str(A/'kernel_demotions_timeout_bootstrap.py'),str(P/'verify.py'),'--out',str(out)],cwd=T,env=env,stdout=log,stderr=subprocess.STDOUT)
  if r.returncode:raise RuntimeError(str(pr)+' own source failed\n'+logfile.read_text()[-12000:])
  outputs=[]
  for path in sorted(out.rglob('*')):
   if not path.is_file()or path.suffix=='.log':continue
   raw=path.read_bytes();rel=path.relative_to(out);dest=D/key/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw);outputs.append(dict(relative=rel.as_posix(),file=dest.relative_to(A).as_posix(),sha256=hs(dest),bytes=len(raw)))
  runs.append(dict(pr=pr,own_head=root['own_head'],source_manifest_file=root['MANIFEST_file'],source_manifest_sha256=root['MANIFEST_sha256'],unchanged_original_verifier_exit_code=0,outputs=outputs,execution_control='Unmodified mathematical/source files and -I/-B isolation; explicit external bootstrap raises only subprocess wall deadlines below300seconds to300seconds and propagates that same rule to child Python jobs. Original20second invocation is not claimed passed.',scope='Actual unchanged mathematical source native/owner/finite-invoice/original dual-moment assembly replay under disclosed execution-only timeout wrapper. Original conditional compiler/native all-size/analytic contracts remain; no whole XAG crossover is inferred. Timing-bearing raw reports are observed execution artifacts, not yet advertised byte-stable reproduction inputs.'))
  print('PASSunchangedownfullsource',pr,'outputs',len(outputs),flush=True)
receipt=dict(schema='own-kernel-demotions-observed-full-replay/1',status='passed_actual_original_native_owner_invoice_assembly',runs=runs,source_closure_file='kernel-demotions-source/manifest.json',source_closure_sha256=hs(A/'kernel-demotions-source/manifest.json'),source_sha256={a['file']:a['sha256']for a in manifest['objects']},script_sha256=hs(Path(__file__)),not_yet_a_numeric_XAG_bound=True,raw_reports_may_contain_nondeterministic_timings=True,execution_timeout_wrapper_file='kernel_demotions_timeout_bootstrap.py',execution_timeout_wrapper_sha256=hs(A/'kernel_demotions_timeout_bootstrap.py'))
(A/'kernel-demotions-original-full-replay.json').write_text(json.dumps(receipt,indent=2)+'\n');print('PASSallactualkernel-demotionreplays')
