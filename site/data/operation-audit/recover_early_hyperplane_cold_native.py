"""Execute own591/608/615 typed constructors and selected native engines.

Only actual source constructor functions/constants are AST-loaded. The driver
does not execute or claim the original full global, phase or assembly pipeline.
"""
from pathlib import Path
from hashlib import sha256,sha1
from collections import Counter
from fractions import Fraction as Q
import ast,gzip,json,os,shutil,subprocess,sys,tempfile,time
R=Path(__file__).resolve().parent;D=R/'early-hyperplane-cold-selected-native';D.mkdir(exist_ok=True);checks={};steps=[];outputs=[];selected=[]
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(k,v):assert v,k;checks[k]=True
mf='early-hyperplane-cold-own-source/source-manifest.json';own=rd(R/mf)
cf='cold14-source-reconstruction/source-closure-manifest.json';closure=rd(R/cf);oldspec=rd(R/closure['SPEC_file'])
sf='cold14-retained-baseline-seeds/manifest.json';seeds=rd(R/sf);ck('same_bound_retained_source_baseline',seeds['source_closure_sha256']==hs(R/cf))
for row in own['rows']:
 pr=row['pr'];files={a['relative']:a for a in row['files']};spec=rd(R/row['SPEC_file']);M=rd(R/row['MANIFEST_file'])
 ck(f'{pr}_own_complete_external_source_declarations',spec['build']['sources']==oldspec['build']['sources'])
 ck(f'{pr}_complete_own_MANIFEST_inventory',M=={k:a['sha256']for k,a in files.items()if k!='MANIFEST.json'})
 for a in files.values():
  b=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  ck(f'{pr}_primary_'+a['relative'],hs(R/a['file'])==a['sha256']and a['own_head']==row['own_head']and blob==a['git_blob_sha1']==a['own_API_git_blob_sha1'])
 with tempfile.TemporaryDirectory(prefix=f'early-{pr}-')as temp:
  T=Path(temp);dirs={p['key']:T/('own-package'if p['key']=='package'else spec['build']['sources'][p['key']]['dir'])for p in closure['packages']}
  for a in closure['objects']:
   if a['package']=='package':continue
   ck(f'{pr}_external_'+a['file'],hs(R/a['file'])==a['sha256']);p=dirs[a['package']]/a['relative'];ck(f'{pr}_safe_external_'+a['relative'],p.resolve().is_relative_to(T.resolve()));p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/a['file']).read_bytes())
  P=dirs['package'];P.mkdir()
  for a in files.values():
   p=P/a['relative'];ck(f'{pr}_safe_own_'+a['relative'],p.resolve().is_relative_to(P.resolve()));p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/a['file']).read_bytes())
  S=dirs['multicold'];B=S/'vendor/pr558';F=B/'vendor/pr552';V=F/'complex-global/vendor531';GK=F/'complex-local/static44/gk';baseline=T/'retained-source-baseline'
  for a in seeds['objects']:
   ck(f'{pr}_retained_base_'+a['relative'],hs(R/a['file'])==a['sha256']);p=baseline/a['relative'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/a['file']).read_bytes())
  RAW=baseline/'reconstruction/promoted/FULL-WORD.json.gz';SEL=baseline/'reconstruction/static44/SELECTION.json';ck(f'{pr}_actual_baseline_RAW',sha256(gzip.decompress(RAW.read_bytes())).hexdigest()==seeds['raw_content_sha256'])
  # Some unchanged own constructors prepend a historical absolute GK path.
  # Supply only the exact same hash-bound GK import directory as a portable
  # fallback. No constructor text, scalar guard or operation is changed.
  gkfile=GK/'gk_common.py'
  ck(f'{pr}_exact_bound_GK_module',any(a['package']!='package' and hs(R/a['file'])==hs(gkfile) and a['relative'].endswith('/gk/gk_common.py')for a in closure['objects']))
  O=T/'constructors';O.mkdir();env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',PYTHONPATH=str(GK),MULTICOLD_SOURCE=str(S),GAIN_PR564_SOURCE=str(S),WITNESS_SPEC=str(P/'data/SPEC.json'));env.pop('PYTHONOPTIMIZE',None)
  preflight=subprocess.run([sys.executable,'-B','-c','import importlib.util,pathlib,sys; assert pathlib.Path(importlib.util.find_spec("gk_common").origin).resolve()==pathlib.Path(sys.argv[1]).resolve()',str(gkfile)],cwd=T,env=env,capture_output=True,text=True,encoding='utf8')
  ck(f'{pr}_portable_GK_import_resolves_only_exact_materialized_module',preflight.returncode==0)
  def run(name,script,*args):
   p=subprocess.run([sys.executable,'-B',str(S/'code/run_portable.py'),str(script),*map(str,args)],cwd=T,env=env,capture_output=True,text=True,encoding='utf8')
   if p.returncode:raise RuntimeError(name+'\n'+p.stdout[-6000:]+'\n'+p.stderr[-6000:])
   ck(f'{pr}_executed_'+name,p.returncode==0);steps.append(dict(pr=pr,name=name,exit_code=p.returncode));print('PASS own',pr,name,flush=True)
  source=(P/'verify.py').read_text();tree=ast.parse(source);excluded={'tree','run','localize','provider'};names={n.name for n in tree.body if isinstance(n,ast.FunctionDef)and n.name not in excluded};constants={'PROMOTER','JOINT','COAL','STEPS'}
  nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in names or isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id in constants for t in n.targets)]
  ck(f'{pr}_exact_unmodified_function_AST_selection',{n.name for n in nodes if isinstance(n,ast.FunctionDef)}==names and {'read','sha','content','dump','pinned','ref','build_word'}<=names)
  ns=dict(Path=Path,Q=Q,Counter=Counter,json=json,gzip=gzip,hashlib=__import__('hashlib'),subprocess=subprocess,sys=sys,os=os,shutil=shutil,time=time,P=P,SPEC=spec,BUILD=spec['build'],SRC=dirs,S=S,B=B,F=F,V=V,GK=GK,O=O,RAW=RAW,SEL=SEL,DISCOVER=False,discovered={},env=env,run=run)
  exec(compile(ast.Module(body=nodes,type_ignores=[]),str(P/'verify.py'),'exec'),ns)
  ck(f'{pr}_literal_native_four_stage_paths',"NC('audit_and_transport.py')"in source and"NC('emit_local.py')"in source and"NC('audit_local.py')"in source and"NC('adapters_local.py')"in source)
  for pid,p in sorted(spec['build']['providers'].items()):
   word=ns['build_word'](pid,p);rawhash=sha256(gzip.decompress(word.read_bytes())).hexdigest();ck(f'{pr}_{pid}_own_selected_whole_RAW',rawhash==p['word_content_sha256'])
   out=D/str(pr)/pid;out.mkdir(parents=True,exist_ok=True);(out/'FULL-WORD.json.gz').write_bytes(gzip.compress(gzip.decompress(word.read_bytes()),mtime=0))
   local=T/('native-'+pid);hp='helper_final'in rd(word);NC=(lambda name:P/'code'/('hpe_'+name))if hp else(lambda name:V/'code'/name)
   for name,args in [('audit_and_transport.py',['--raw',word,'--routing',F/'complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz','--out',local]),('emit_local.py',[local]),('audit_local.py',[local]),('adapters_local.py',[local/'CANONICAL-WORD.json.gz',local/'RESIDUAL-ADAPTERS.json',local/'WRAPPER-CHECKS.json'])]:run(pid+'-native-'+name,NC(name),*args)
   objs={}
   for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','LOCAL-CHECKS.json','RESIDUAL-ADAPTERS.json','WRAPPER-CHECKS.json']:
    pth=local/name;b=pth.read_bytes();o=rd(pth);dest=out/name;dest.write_bytes(gzip.compress(gzip.decompress(b),mtime=0)if b[:2]==b'\x1f\x8b'else b);a=dict(pr=pr,own_head=row['own_head'],provider=pid,raw_content_sha256=rawhash,artifact=name,file=dest.relative_to(R).as_posix(),sha256=hs(dest),semantic_sha256=ident(o),orientation_sha256={k:ident(v)for k,v in o.items()}if name=='LOCAL-PROGRAMS.json.gz'else None);outputs.append(a);objs[name]=a
   provider=spec['providers'][pid];ck(f'{pr}_{pid}_entire_own_selected_native',objs['CANONICAL-WORD.json.gz']['semantic_sha256']==provider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and objs['LOCAL-PROGRAMS.json.gz']['semantic_sha256']==provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and objs['LOCAL-PROGRAMS.json.gz']['orientation_sha256']==provider['program_hashes'])
   selected.append(dict(pr=pr,own_head=row['own_head'],provider=pid,own_SPEC_file=row['SPEC_file'],own_SPEC_sha256=row['SPEC_sha256'],RAW_file=(out/'FULL-WORD.json.gz').relative_to(R).as_posix(),RAW_sha256=hs(out/'FULL-WORD.json.gz'),RAW_content_sha256=rawhash,canonical_file=objs['CANONICAL-WORD.json.gz']['file'],program_file=objs['LOCAL-PROGRAMS.json.gz']['file']));print('PASS whole own selected provider',pr,pid,flush=True)
out=dict(schema='own-early-hyperplane-cold-three-native-recovery/1',status='passed_actual_own_typed_constructor_and_native_scalar_frame_wrapper_engines',prs=[591,608,615],checks=checks,checks_passed=len(checks),steps=steps,outputs=outputs,selected_own_providers=selected,source_sha256={a['file']:a['sha256']for r in own['rows']for a in r['files']},executed_external_source_sha256={a['file']:a['sha256']for a in closure['objects']if a['package']!='package'},retained_base_sha256={a['file']:a['sha256']for a in seeds['objects']},dependency_hashes={f:hs(R/f)for f in [mf,cf,sf]},script_sha256=hs(Path(__file__)),portable_import_adapter='External PYTHONPATH contains only the exact materialized hash-bound GK directory; a fresh child-process import-resolution guard checks gk_common resolves to that exact file. This supplies a fallback for unchanged source constructors with a historical absolute GK path; constructor text and all mathematical guards are unchanged.',original_full_global_or_phase_verifier_PASS_claimed=False,whole_integer_cost_proved=False,scope='Each own immutable MANIFEST and full own SPEC selects exact typed constructor AST bodies, recipes and RAW endpoints. Complete own external source declarations equal the materialized hash-bound closure. Each own selected constructor/control chain and actual four native engines execute; complete canonical/program/both-orientation commitments must match every own provider. Exact retained baseline RAW is a checked source byte input, not claimed freshly rebuilt here. Full operator/absolute-phase/owned/allsize contracts remain explicit. No global invoice, cutoff or original full CLI/phase PASS transfers.')
(R/'early-hyperplane-cold-selected-native-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own591/608/615 typed/native checks',len(selected),'selected providers')
