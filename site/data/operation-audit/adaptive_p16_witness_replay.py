from pathlib import Path
from hashlib import sha256
import importlib.util,sys,json,socket
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE/'adaptive-p16-upper-source'
rows=[]
for pr in [4483,4533]:
 base=ROOT/str(pr);moddir=base/'research/rank-convergence'
 sys.path.insert(0,str(moddir));sys.modules.pop('intervals',None)
 spec=importlib.util.spec_from_file_location('adaptive_source_'+str(pr),moddir/'compiler.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 profile=json.loads((base/'research/compact-joint-compiler/arithmetic/RESULT.json').read_text())
 witness=(next(c for c in json.loads((moddir/'BENCHMARKS.json').read_text())['cases']if c['name']=='p16')['witness'] if pr==4483 else json.loads((base/'research/adaptive-witness-retune/WITNESS-p16.json').read_text()))
 result=module.certify({'targets':profile['targets'],'paid':profile['paid']},witness)
 rows.append(dict(pr=pr,status='PASS',result=result,code_sha256=sha256((moddir/'compiler.py').read_bytes()).hexdigest(),intervals_sha256=sha256((moddir/'intervals.py').read_bytes()).hexdigest()))
result={'schema':'own-adaptive-p16-witness-replay/1','source_witness_only':True,'full_native_replayed':False,'rows':rows,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
p=HERE/'adaptive-p16-witness-replay.json';encoded=json.dumps(result,indent=2)+'\n'
if p.exists():assert p.read_text()==encoded,'Frozen witness replay bytes changed'
else:p.write_text(encoded,encoding='utf8')
print(json.dumps({'passed':True,'fresh_source_witnesses':len(rows),'full_native_replayed':False}))
