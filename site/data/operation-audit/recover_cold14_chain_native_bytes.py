"""Exact own604 typed-chain intermediate native byte recovery (no phase/cost transfer)."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from fractions import Fraction as Q
import ast,gzip,json,os,shutil,subprocess,sys,tempfile,time
R=Path(__file__).resolve().parent;D=R/'cold14-chain-native-bytes';D.mkdir(exist_ok=True)
hs=lambda p:sha256(p.read_bytes()).hexdigest()
rd=lambda p:json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_bytes())
ident=lambda o:sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
m=rd(R/'cold14-source-reconstruction/source-closure-manifest.json');seeds=rd(R/'cold14-retained-baseline-seeds/manifest.json');assert seeds['source_closure_sha256']==hs(R/'cold14-source-reconstruction/source-closure-manifest.json');spec=rd(R/m['SPEC_file']);steps=[];outputs=[]
with tempfile.TemporaryDirectory(prefix='c604bytes-')as temp:
 T=Path(temp);dirs={p['key']:T/('complex-571-cold14'if p['key']=='package'else spec['build']['sources'][p['key']]['dir'])for p in m['packages']}
 for a in m['objects']:
  raw=(R/a['file']).read_bytes();assert sha256(raw).hexdigest()==a['sha256'];p=dirs[a['package']]/a['relative'];assert p.resolve().is_relative_to(dirs[a['package']].resolve());p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
 P=dirs['package'];S=dirs['multicold'];B=S/'vendor/pr558';F=B/'vendor/pr552';V=F/'complex-global/vendor531';GK=F/'complex-local/static44/gk';baseline=T/'retained-source-baseline'
 for a in seeds['objects']:
  raw=(R/a['file']).read_bytes();assert sha256(raw).hexdigest()==a['sha256'];p=baseline/a['relative'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
 RAW=baseline/'reconstruction/promoted/FULL-WORD.json.gz';SEL=baseline/'reconstruction/static44/SELECTION.json';assert sha256(gzip.decompress(RAW.read_bytes())).hexdigest()==seeds['raw_content_sha256'];O=T/'constructors';O.mkdir();env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(S),GAIN_PR564_SOURCE=str(S),WITNESS_SPEC=str(P/'data/SPEC.json'));env.pop('PYTHONOPTIMIZE',None)
 def run(name,script,*args):
  cmd=[sys.executable,'-B',str(S/'code/run_portable.py'),str(script),*map(str,args)];r=subprocess.run(cmd,cwd=T,env=env,capture_output=True,text=True,encoding='utf8');steps.append(dict(name=name,exit_code=r.returncode));
  if r.returncode:raise RuntimeError(name+'\n'+r.stdout[-6000:]+'\n'+r.stderr[-6000:])
 source=(P/'verify.py').read_text();tree=ast.parse(source);fnames={'read','sha','content','dump','pinned','ref','omissions','cold_kernel','finalize','multicut','frame_only','promote','joint_prefix','frame_coalesce','gate_move_coalesce','hyperplane_end','cold_end','build_word'};constants={'PROMOTER','JOINT','COAL','STEPS'};nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in fnames or isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id in constants for t in n.targets)]
 assert {n.name for n in nodes if isinstance(n,ast.FunctionDef)}==fnames
 ns=dict(Path=Path,Q=Q,Counter=Counter,json=json,gzip=gzip,hashlib=__import__('hashlib'),subprocess=subprocess,sys=sys,os=os,shutil=shutil,time=time,P=P,SPEC=spec,BUILD=spec['build'],SRC=dirs,S=S,B=B,F=F,V=V,GK=GK,O=O,RAW=RAW,SEL=SEL,DISCOVER=False,discovered={},env=env,run=run)
 exec(compile(ast.Module(body=nodes,type_ignores=[]),str(P/'verify.py'),'exec'),ns)
 for pid in sorted(spec['build']['providers']):
  ns['build_word'](pid,spec['build']['providers'][pid]);print('typedrawchainPASS',pid,flush=True)
 expected={v['base']['content_sha256']for v in spec['build']['providers'].values()}|{x[k]for v in spec['build']['providers'].values()for x in v['steps']for k in ['input_content_sha256','output_content_sha256']if k in x};rawfiles={}
 for p in [RAW,*O.rglob('FULL-WORD.json.gz'),*dirs['structural_gain'].rglob('FULL-WORD.json.gz')]:
  h=sha256(gzip.decompress(p.read_bytes())).hexdigest()
  if h in expected:rawfiles[h]=p
 assert expected<=set(rawfiles),(len(expected),len(rawfiles))
 for ix,(content,word)in enumerate(sorted(rawfiles.items()),1):
  local=T/('native-'+content[:12]);hp='helper_final'in rd(word);NC=(lambda name:P/'code'/('hpe_'+name))if hp else(lambda name:V/'code'/name)
  for name,args in [('audit_and_transport.py',['--raw',word,'--routing',F/'complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz','--out',local]),('emit_local.py',[local]),('audit_local.py',[local]),('adapters_local.py',[local/'CANONICAL-WORD.json.gz',local/'RESIDUAL-ADAPTERS.json',local/'WRAPPER-CHECKS.json'])]:run(content[:12]+'_'+name,NC(name),*args)
  for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','RESIDUAL-ADAPTERS.json','LOCAL-CHECKS.json']:
   p=local/name;raw=p.read_bytes();o=rd(p);dest=D/content/name;dest.parent.mkdir(exist_ok=True);dest.write_bytes(raw);outputs.append(dict(raw_content_sha256=content,artifact=name,file=dest.relative_to(R).as_posix(),sha256=hs(dest),semantic_sha256=ident(o),orientation_sha256={k:ident(v)for k,v in o.items()}if name.startswith('LOCAL-PROGRAMS')else None))
  print('nativebyteobjectPASS',ix,'/',len(rawfiles),content[:12],flush=True)
# Actual own SPEC commitment matching only; selectedness/whole cost separate.
snap=rd(R/'selected-provider-dispatch-inputs.json');pair={a['raw_content_sha256']:{}for a in outputs}
for a in outputs:pair[a['raw_content_sha256']][a['artifact']]=a
matches=[]
for own in snap['cohort_rows']:
 for a in own['verified_components']:
  if not a.get('path','').endswith('/SPEC.json'):continue
  s=rd(R/a['file'])
  for pid,p in s.get('providers',{}).items():
   sem=p.get('artifact_semantic_sha256',{})
   for h,obj in pair.items():
    if sem.get('CANONICAL-WORD.json.gz')==obj['CANONICAL-WORD.json.gz']['semantic_sha256']and sem.get('LOCAL-PROGRAMS.json.gz')==obj['LOCAL-PROGRAMS.json.gz']['semantic_sha256']and p.get('program_hashes')==obj['LOCAL-PROGRAMS.json.gz']['orientation_sha256']:matches.append(dict(pr=own['pr'],own_head=own['own_head'],provider=pid,SPEC_file=a['file'],SPEC_sha256=a['sha256'],raw_content_sha256=h))
out=dict(schema='own604-exact-typed-chain-native-byte-recovery/1',status='passed_actual_typed_constructors_scalar_native_wrappers',pr=604,own_head=m['own_head'],outputs=outputs,steps=steps,exact_own_SPEC_commitment_matches=matches,phase_engine_executed_for_intermediate_words=False,full_native_endpoint_proved=False,source_sha256={a['file']:a['sha256']for a in m['objects']},dependency_hashes={p:hs(R/p)for p in ['cold14-source-reconstruction/source-closure-manifest.json','cold14-retained-baseline-seeds/manifest.json',m['SPEC_file'],'selected-provider-dispatch-inputs.json']},retained_base_sha256={a['file']:a['sha256']for a in seeds['objects']},script_sha256=hs(Path(__file__)),scope='AST-extracted actual own604 allowlisted typed constructors/paired controls are unmodified; only source-pinned recipes and committed before/after raw words are accepted. Actual source scalar/native/frame transport and wrappers produce full bytes. Full phase/operator contracts remain explicit for intermediate words. Exact canonical/program/orientation matches discover byteobjects; each own selected source/PLAN/OWNERS/full invoice/moment/whole cost still separate, no profile or cutoff transfer.')
(R/'cold14-typed-chain-native-byte-recovery.json').write_text(json.dumps(out,indent=2)+'\n');print('PASSactualtypednativeobjects',len(pair),'ownSPECmatches',len(matches))
