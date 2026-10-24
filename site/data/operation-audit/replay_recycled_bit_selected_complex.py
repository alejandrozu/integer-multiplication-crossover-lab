"""Portable own150/151 selected-complex replay and source-selected bit-row arithmetic.

The changed bit geometry/whole word is not rerun by this job. It independently
rebuilds only the retained complex core, plus prices each committed bit row.
"""
from pathlib import Path
from hashlib import sha256
from concurrent.futures import ThreadPoolExecutor
import json,os,subprocess,sys,tempfile
R=Path(__file__).resolve().parent
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def job(pr):
 mf=f'recycled-bit-complex-source/{pr}-manifest.json';m=json.loads((R/mf).read_bytes());head=m[0]['head'];src={}
 with tempfile.TemporaryDirectory(prefix=f'p{pr}-complex-')as tmp:
  T=Path(tmp)
  for a in m:
   assert a['pr']==pr and a['head']==head and a['status']=='authenticated_own_head_primary_bytes'and hs(a['file'])==a['sha256'];p=T/a['path'];assert p.resolve().is_relative_to(T.resolve());p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/a['file']).read_bytes());src[a['file']]=a['sha256']
  env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0');env.pop('PYTHONOPTIMIZE',None)
  command=['scripts/paired_cube_producer.py'];run=subprocess.run([sys.executable,'-B',*command],cwd=T,env=env,capture_output=True,text=True,encoding='utf8');assert run.returncode==0,run.stderr
  native=json.loads(run.stdout);selected=json.loads((T/'certificates/paired-cube-complex-input.json').read_bytes());assert native['selected']==selected
  (R/f'recycled-bit-complex-source/{pr}-fresh-selected-complex-replay.json').write_text(json.dumps(dict(schema='own-selected-complex-producer-replay/1',pr=pr,own_head=head,status='passed_untouched_own_selected_complex_producer',returncode=run.returncode,stdout=run.stdout,stderr=run.stderr,command=['python','-B',*command],primary_code_changed=False,selected_matches_own_committed_object=True,changed_bit_geometry_or_wholeword_replayed=False,source_manifest=mf,source_manifest_sha256=hs(mf),source_sha256=src,script_sha256=hs(Path(__file__).name),scope='Fresh unchanged own selected complex scalar/frame/physical producer only. Changed original bit word and its geometry are not replayed; source-selected bit-row moment/assembly pricing is checked separately. Universal operator/all-size/analytic contracts remain retained.'),indent=2)+'\n',encoding='utf8')
  code="import sys,json;from pathlib import Path;from fractions import Fraction as Q;sys.path.insert(0,'research/bit-reuse-147');import price147;row=json.loads(Path('"+('research/bit-reuse-147/row.json'if pr==150 else'research/gauge-recycling/row.json')+"').read_bytes());print(json.dumps(price147.price(row,"+('None'if pr==150 else'Q(473,10**6)')+"),default=str,sort_keys=True))"
  run=subprocess.run([sys.executable,'-B','-c',code],cwd=T,env=env,capture_output=True,text=True,encoding='utf8');assert run.returncode==0,run.stderr;price=json.loads(run.stdout);assert price['kappa']==('471809569/1000000000000'if pr==150 else'472154791/1000000000000')
  (R/f'recycled-bit-complex-source/{pr}-fresh-price-replay.json').write_text(json.dumps(dict(schema='own-selected-bit-row-source-arithmetic-replay/1',pr=pr,own_head=head,status='passed_unchanged_own_price_functions_on_own_committed_row',returncode=run.returncode,price=price,command_python_code=code,primary_code_changed=False,original_bit_scalar_frame_or_geometric_replay_performed=False,source_manifest=mf,source_manifest_sha256=hs(mf),source_sha256=src,script_sha256=hs(Path(__file__).name),scope='Fresh source-row moment and original47-constraint assembly pricing only; does not establish that the changed physical bit word realizes this row.'),indent=2)+'\n',encoding='utf8')
 return(pr,price['kappa'])
with ThreadPoolExecutor(max_workers=2)as pool:
 for a in pool.map(job,[150,151]):print('PASS own native+price',*a,flush=True)
