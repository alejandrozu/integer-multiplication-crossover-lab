"""Source-bound compact compiler, Apache-2.0; substantial Codex assistance."""
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
def need(x,m):
 if not x:raise ValueError(m)
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);sys.modules[n]=m;spec.loader.exec_module(m);return m
def authenticate():
 for row in json.loads((HERE/'SOURCES.json').read_bytes())['files']:
  if row['usage']=='input':need(hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()==row['sha256'],'Changed source '+row['path'])
def run(part):
 authenticate();source=ROOT/'research/joint-helper-lattice';sys.path.insert(0,str(source));parent=load(source/'verify.py','frozen4470_parent')
 if part=='dependencies':parent.replay_dependencies()
 elif part=='native':
  parent.authenticate();local=parent.J.run();need(json.loads(json.dumps(local))==parent.read(source/'NATIVE.json.gz'),'Fresh two-interpreter/native/absolute-phase receipt')
  a=load(HERE/'arithmetic/verify.py','compact_arithmetic_native_binding');result=a.run(local)
  need(result==json.loads((HERE/'arithmetic/RESULT.json').read_bytes()),'Native profile bound to compact arithmetic')
 elif part=='arithmetic':
  previous=parent.run(execute_sources=False);need(previous==parent.read(source/'RESULT.json'),'Fresh complete source arithmetic/controller')
  a=load(HERE/'arithmetic/verify.py','compact_arithmetic');result=a.run()
  need(result==json.loads((HERE/'arithmetic/RESULT.json').read_bytes()),'Frozen compact receipt')
  need((HERE/'arithmetic/controller.json').read_bytes()==(source/'CONTROLLER.json').read_bytes(),'Unchanged literal p16 controller')
  for key in ('targets','paid','local_helpers','local_paid','ordinary_BIT','productive_fields','paid_calls'):
   need(result[key]==previous[key],'Unchanged complete source bill '+key)
  need(int(result['compiler']['H'])==558100005581<int(previous['compiler']['H']),'Strictly smaller sufficient local compiler rank')
 else:raise ValueError(part)
 print('PASS_COMPACT_JOINT_COMPILER_'+part.upper())
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--part',choices=['dependencies','native','arithmetic'],required=True);run(p.parse_args().part)
