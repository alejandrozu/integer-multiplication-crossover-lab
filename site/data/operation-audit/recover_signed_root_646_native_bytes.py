"""Exact own646 K-triangle mixed native recovery; no phase/cost transfer.

The original allowlisted native constructor function bodies and paired controls
are executed unchanged. A short temp tree avoids Windows path-length effects.
Only derived gzip containers are made deterministic; their decompressed byte
strings and every own raw/semantic/orientation commitment remain exact.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction as Q
import ast,gzip,hashlib,json,os,shutil,subprocess,sys,tempfile,threading,time
R=Path(__file__).resolve().parent;D=R/'late-cold-mixed-native-outputs';D.mkdir(exist_ok=True)
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_bytes())
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
m=rd(R/'late-cold-mixed-source/native-source-closure-646.json');seeds=rd(R/'cold14-retained-baseline-seeds/manifest.json');spec=rd(R/m['SPEC_file']);steps=[];outputs=[];checks={}
def ck(n,v):assert v,n;checks[n]=True
ck('own_source_SPEC_manifest',hs(R/m['SPEC_file'])==m['SPEC_sha256'])
with tempfile.TemporaryDirectory(prefix='mix646-')as temp:
 T=Path(temp);dirs={x['key']:T/('own646'if x['key']=='package'else spec['build']['sources'][x['key']]['dir'])for x in m['packages']}
 for a in m['objects']:
  raw=(R/a['file']).read_bytes();ck('source_'+a['file'],sha256(raw).hexdigest()==a['sha256']);p=dirs[a['package']]/a['relative'];assert p.resolve().is_relative_to(dirs[a['package']].resolve());p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
 P=dirs['package'];S=dirs['multicold'];B=S/'vendor/pr558';F=B/'vendor/pr552';V=F/'complex-global/vendor531';GK=F/'complex-local/static44/gk';baseline=T/'baseline'
 for a in seeds['objects']:
  raw=(R/a['file']).read_bytes();ck('retained_seed_'+a['file'],sha256(raw).hexdigest()==a['sha256']);p=baseline/a['relative'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
 RAW=baseline/'reconstruction/promoted/FULL-WORD.json.gz';SEL=baseline/'reconstruction/static44/SELECTION.json';ck('retained_exact_raw_seed',sha256(gzip.decompress(RAW.read_bytes())).hexdigest()==seeds['raw_content_sha256'])
 for key,src in spec['build']['sources'].items():
  own=dirs[key];manifest=rd(own/'MANIFEST.json');ck('source_manifest_'+key,hs(own/'MANIFEST.json')==src['manifest_sha256']);items=manifest.get('sha256',manifest.get('files',manifest))
  for rel,want in src['files'].items():ck('declared_source_'+key+'_'+rel,hs(own/rel)==want==items[rel])
 O=T/'constructors';O.mkdir();env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(S),GAIN_PR564_SOURCE=str(S),WITNESS_SPEC=str(P/'data/SPEC.json'));env.pop('PYTHONOPTIMIZE',None);env.pop('WITNESS_DISCOVER',None)
 def run(name,script,*args):
  r=subprocess.run([sys.executable,'-B',str(S/'code/run_portable.py'),str(script),*map(str,args)],cwd=T,env=env,capture_output=True,text=True,encoding='utf8');steps.append(dict(name=name,exit_code=r.returncode))
  if r.returncode:raise RuntimeError(name+'\n'+r.stdout[-8000:]+'\n'+r.stderr[-8000:])
  print('PASS',name,flush=True)
 fnames={'read','sha','content','dump','pinned','ref','omissions','cold_kernel','finalize','multicut','frame_only','promote','joint_prefix','frame_coalesce','gate_move_coalesce','hyperplane_end','cold_end','k_triangle','stage_word','port_stage','frame_regroup','build_word'};constants={'PROMOTER','JOINT','COAL','STEPS','KT','KT_LOCK','STAGEWORDS','KMAP'}
 tree=ast.parse((P/'verify.py').read_text());nodes=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name in fnames or isinstance(x,ast.Assign)and any(isinstance(t,ast.Name)and t.id in constants for t in x.targets)]
 ck('exact_native_constructor_AST_allowlist',{x.name for x in nodes if isinstance(x,ast.FunctionDef)}==fnames)
 ns=dict(Path=Path,Q=Q,Counter=Counter,json=json,gzip=gzip,hashlib=hashlib,subprocess=subprocess,sys=sys,os=os,shutil=shutil,time=time,threading=threading,P=P,SPEC=spec,BUILD=spec['build'],SRC=dirs,S=S,B=B,F=F,V=V,GK=GK,O=O,RAW=RAW,SEL=SEL,DISCOVER=False,discovered={},env=env,run=run)
 exec(compile(ast.Module(body=nodes,type_ignores=[]),str(P/'verify.py'),'exec'),ns)
 # Reuse complete actual RAW shadow inputs only at every own full digest.
 # Their unchanged constructors and controls were executed by the bound638
 # recovery; this replay executes the distinct own646 K480 chain and controls.
 recovered=rd(R/'late-cold-mixed-native-byte-recovery-638.json')
 ck('actual_source_shadow_recovery',all(recovered['checks'].values())and recovered['script_sha256']==hs(R/'recover_late_cold_mixed_native_bytes.py'))
 rawmap={a['decompressed_sha256']:R/a['file'] for a in recovered['raw_intermediates']}
 for a in recovered['raw_intermediates']:ck('retained_shadow_container_'+a['decompressed_sha256'],hs(R/a['file'])==a['sha256'])
 refspec=rd(R/'late-cold-mixed-source/638/data/SPEC.json')
 ck('own_exact_shadow_recipes',spec['build']['shadows']==refspec['build']['shadows'])
 for pid,d in sorted(spec['build'].get('shadows',{}).items()):
  h=d['base']['content_sha256'];seq={'base':h}
  bp=RAW if d['base']['kind']=='frozen558_promoted'else ns['ref'](d['base']['file'])
  ck('own_shadow_primary_base_'+pid,sha256(gzip.decompress(bp.read_bytes())).hexdigest()==h);rawmap[h]=bp
  for i,z in enumerate(d['steps']):h=z.get('output_content_sha256',h);seq[str(i)]=h
  ns['STAGEWORDS'][pid]={}
  for key,h in seq.items():
   path=rawmap[h];ck('exact_own_shadow_'+pid+'_'+key,sha256(gzip.decompress(path.read_bytes())).hexdigest()==h)
   ns['STAGEWORDS'][pid][key]=path
  ck('exact_own_shadow_final_'+pid,h==d['word_content_sha256'])
  print('PASS exact source-bound RAW shadow inputs',pid,flush=True)
 with ThreadPoolExecutor(max_workers=2)as pool:
  jobs={pid:pool.submit(ns['build_word'],pid,d)for pid,d in sorted(spec['build']['providers'].items())};selected={pid:f.result()for pid,f in jobs.items()}
 # Keep every exact raw intermediate for subsequent independently selected cases.
 rawobjects={}
 for p in[RAW,*O.rglob('FULL-WORD.json.gz')]:
  raw=gzip.decompress(p.read_bytes());h=sha256(raw).hexdigest();dest=D/h/'FULL-WORD.json.gz';dest.parent.mkdir(exist_ok=True);saved=gzip.compress(raw,mtime=0)
  if dest.exists():ck('retained_exact_raw_'+h,dest.read_bytes()==saved)
  else:dest.write_bytes(saved)
  rawobjects[h]=dict(file=dest.relative_to(R).as_posix(),sha256=hs(dest),decompressed_sha256=h)
 for pid,word in selected.items():
  rawhash=sha256(gzip.decompress(word.read_bytes())).hexdigest();ck('own_selected_final_raw_'+pid,rawhash==spec['build']['providers'][pid]['word_content_sha256']);local=T/('native-'+pid);hp='helper_final'in rd(word);NC=(lambda n:P/'code'/('hpe_'+n))if hp else(lambda n:V/'code'/n)
  for name,args in [('audit_and_transport.py',['--raw',word,'--routing',F/'complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz','--out',local]),('emit_local.py',[local]),('audit_local.py',[local]),('adapters_local.py',[local/'CANONICAL-WORD.json.gz',local/'RESIDUAL-ADAPTERS.json',local/'WRAPPER-CHECKS.json'])]:run(pid+'_'+name,NC(name),*args)
  for name in['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','LOCAL-CHECKS.json','RESIDUAL-ADAPTERS.json','WRAPPER-CHECKS.json']:
   p=local/name;b=p.read_bytes();o=rd(p);dest=D/rawhash/name;dest.write_bytes(gzip.compress(gzip.decompress(b),mtime=0)if name.endswith('.gz')else b);outputs.append(dict(provider=pid,raw_content_sha256=rawhash,artifact=name,file=dest.relative_to(R).as_posix(),sha256=hs(dest),semantic_sha256=ident(o),orientation_sha256={k:ident(v)for k,v in o.items()}if name.startswith('LOCAL-PROGRAMS')else None,derived_gzip_container_deterministic=True))
  own=spec['providers'][pid];can=next(a for a in outputs if a['provider']==pid and a['artifact']=='CANONICAL-WORD.json.gz');prog=next(a for a in outputs if a['provider']==pid and a['artifact']=='LOCAL-PROGRAMS.json.gz')
  ck('own_complete_canonical_'+pid,can['semantic_sha256']==own['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']);ck('own_complete_program_'+pid,prog['semantic_sha256']==own['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']);ck('own_both_orientation_words_'+pid,prog['orientation_sha256']==own['program_hashes'])
out=dict(schema='own646-typed-K-triangle-native-byte-recovery/1',status='passed_actual_source_constructors_scalar_frame_wrapper_engines',pr=m['pr'],own_head=m['own_head'],checks=dict(sorted(checks.items())),checks_passed=len(checks),steps=sorted(steps,key=lambda a:a['name']),raw_intermediates=sorted(rawobjects.values(),key=lambda a:a['decompressed_sha256']),outputs=outputs,source_sha256={a['file']:a['sha256']for a in m['objects']},retained_base_sha256={a['file']:a['sha256']for a in seeds['objects']},dependency_hashes={f:hs(R/f)for f in ['late-cold-mixed-source/native-source-closure-646.json','late-cold-mixed-source/signed-root-646-source-manifest.json','late-cold-mixed-native-byte-recovery-638.json','recover_late_cold_mixed_native_bytes.py','cold14-retained-baseline-seeds/manifest.json']},exact_shadow_RAW_byte_reuse=True,original_complete_source_package_replay_claimed=False,full_phase_or_operator_engine_replayed=False,whole_owner_or_cost_proved=False,scope='Actual own646 unmodified allowlisted K480/native constructors and paired controls are executed, using exact whole source-bound shadow RAW byte inputs from the independently executed638 recovery from immutable own/source-pinned recipes. Raw input/output commitments, full canonical/program semantic hashes and both orientations are checked. Temporary materialization/source-native scalar/frame/wrapper stages do not prove universal operator/absolute-phase/all-size contracts. All raw intermediates are retained exactly for future per-own selection checks. No global profile, invoice or bound is transferred.',script_sha256=hs(Path(__file__)))
(R/'late-cold-mixed-native-byte-recovery-646.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'source/native checks;',len(outputs),'selected outputs;',len(rawobjects),'exact raw intermediates')
