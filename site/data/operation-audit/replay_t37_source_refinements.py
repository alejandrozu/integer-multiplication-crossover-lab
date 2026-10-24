"""Portable own1009 bootstrap replay and scoped own1019 rational-grid arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,importlib.util,json,os,subprocess,sys,tempfile
R=Path(__file__).resolve().parent;D=R/'t37-source-refinement-cases'
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
for pr in [1009,1019]:
 own=rd(f't37-source-refinement-cases/{pr}-manifest.json');decl=rd(f't37-source-refinement-cases/{pr}-declared-inputs.json');pins={};head=own[0]['own_head'];paths={}
 with tempfile.TemporaryDirectory(prefix=f't37-{pr}-')as folder:
  T=Path(folder)
  for a in [x for x in own if x.get('file')]+decl:
   raw=(R/a['file']).read_bytes();assert sha256(raw).hexdigest()==a['sha256'];p=T/a['path'];assert p.resolve().is_relative_to(T.resolve());p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw);pins[a['file']]=a['sha256'];paths[a['path']]=a['file']
  if pr==1009:
   env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0');env.pop('PYTHONOPTIMIZE',None);command=['research/t37-bootstrap-depth-seed60/verify.py'];run=subprocess.run([sys.executable,'-B',*command],cwd=T,env=env,capture_output=True,text=True,encoding='utf8');assert run.returncode==0,run.stdout+run.stderr
   result=dict(returncode=0,stdout=run.stdout,stderr=run.stderr,unchanged_original_source_executed=True,full_native_or_supplier_replayed=False,scope='Complete unchanged own six-vs-seven bootstrap/47-constraint finite arithmetic verifier; selected physical/native supplier and its moments remain inherited. No native engine or complete integer execution is rerun.')
  else:
   sf=paths['research/t37-rational-refinement/verify.py'];tree=ast.parse((R/sf).read_bytes());defs=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in {'bridge','refined_point'}];assert {n.name for n in defs}=={'bridge','refined_point'};env={'Q':F};assign=[n for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(a,ast.Name)and a.id=='GRID'for a in n.targets)];assert len(assign)==1;exec(compile(ast.Module(body=assign+defs,type_ignores=[]),'own1019_original_grid_functions','exec'),env)
   engine='research/e8-bit-carrier-skeleton/code/pricing/outer.py';module=importlib.util.module_from_spec(importlib.util.spec_from_file_location('own1019_outer',T/engine));module.__spec__.loader.exec_module(module);baseline=rd(paths['research/community-frontier942-audit/ASSEMBLY.json']);fresh=env['refined_point'](module,baseline);ownsource=rd(paths['research/t37-rational-refinement/SOURCES.json']);committed=rd(paths['research/t37-rational-refinement/ASSEMBLY.json']);assert fresh==F(ownsource['refined_kappa'])==F(committed['kappa']);a=F(baseline['bootstrap'][-1]['exponent']);b=F(baseline['complex_lower']);o=module.assembly(a,b,env['bridge'](),fresh,eta=F(1,10**24),beta=F(1,10**24));assert len(o['strict_constraints'])==47 and all(v>0 for v in o['strict_constraints'].values())
   result=dict(returncode=0,original_functions_executed_unmodified=['bridge','refined_point'],own_objective_GRID=str(env['GRID']),refined_kappa=str(fresh),all47_strict_constraints_pass=True,full_original_verifier_executed=False,full_876_source_inventory_replayed=False,full_native_or_supplier_replayed=False,scope='Scoped exact own original rational-grid functions and47-constraint outer arithmetic using own bound baseline. Does not execute the full876-source inventory/assembly/native replay.')
  result.update(schema='own-T37-source-refinement-replay/1',pr=pr,own_head=head,source_sha256=pins,source_manifests={f't37-source-refinement-cases/{pr}-manifest.json':hs(f't37-source-refinement-cases/{pr}-manifest.json'),f't37-source-refinement-cases/{pr}-declared-inputs.json':hs(f't37-source-refinement-cases/{pr}-declared-inputs.json')},script_sha256=hs(Path(__file__).name));(D/f'{pr}-fresh-source-arithmetic.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print('PASS scoped original T37 source arithmetic',pr,flush=True)
