"""Reconstruct the two own1672 k554 native objects used by exact later selectors."""
from pathlib import Path
from hashlib import sha256
import gzip,json,os,subprocess,sys,tempfile,tarfile
R=Path(__file__).resolve().parent;S=R/'pr1672-native-recovery-source';D=R/'pr1672-recovered-native';D.mkdir(exist_ok=True)
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
checks={}
def ck(n,v):assert v,n;checks[n]=True
head='b8ab040dbb7638e79249e763c60e877765d9d3b7';base='research/gmx-t74-k554-signed-001/'
M=rd(S/'408001d452bd__MANIFEST.json');inputs=rd(S/'native-input-manifest.json');by={a['path'][len(base):]:a for a in inputs}
for a in inputs:ck('own_manifest_'+a['path'],a['own_head']==head and hs(R/a['file'])==a['sha256']==M[a['path'][len(base):]])
specfile=R/'remaining-record-audit/artifacts/1672/41d7bd51c18e__SPEC.json';spec=rd(specfile);ck('own_selected_SPEC',hs(specfile)==M['new/SPEC.json'])
outputs=[];steps=[];logs=[];source_manifest={}
with tempfile.TemporaryDirectory(prefix='p1672-')as temporary:
 T=Path(temporary)
 with tarfile.open(R/by['vendor/pr1297/upstream-layout.tar.gz']['file'])as archive:
  for a in archive:
   rel=Path(a.name);ck('archive_path_'+a.name,a.isfile()and not rel.is_absolute()and'..'not in rel.parts)
   out=T/rel;assert out.resolve().is_relative_to(T.resolve());out.parent.mkdir(parents=True,exist_ok=True);raw=archive.extractfile(a).read();out.write_bytes(raw);source_manifest[a.name]=sha256(raw).hexdigest()
 root=T/'joint1148-round45/source';src=root/'research/complex-k492-owner-repair/vendor/multicold';up=root/'research/complex-sw4-frame8/vendor/pr635/research/complex-571-cold14-st2/code';portable=src/'code/run_portable.py';routing=src/'vendor/pr558/vendor/pr552/complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz'
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(src),GAIN_PR564_SOURCE=str(src));env.pop('PYTHONOPTIMIZE',None)
 for key in ['extra','gauge44']:
  raw=R/by['new/'+key+'-word-566.json.gz']['file'];local=T/('native-'+key);provider=spec['providers'][key]
  jobs=[('allcolumn_transport',[str(up/'hpe_audit_and_transport.py'),'--raw',str(raw),'--routing',str(routing),'--out',str(local)]),('native_emitter',[str(up/'hpe_emit_local.py'),str(local)]),('scalar_replay',[str(up/'hpe_audit_local.py'),str(local)]),('normalized_wrappers',[str(up/'hpe_adapters_local.py'),str(local/'CANONICAL-WORD.json.gz'),str(local/'RESIDUAL-ADAPTERS.json'),str(local/'WRAPPER-CHECKS.json')])]
  for label,args in jobs:
   result=subprocess.run([sys.executable,'-B',str(portable),*args],cwd=root,env=env,capture_output=True,text=True,encoding='utf8')
   steps.append(dict(provider=key,name=label,exit_code=result.returncode));logs.append(dict(provider=key,name=label,stdout=result.stdout,stderr=result.stderr));(R/'pr1672-native-recovery-execution-log.json').write_text(json.dumps(logs,indent=2)+'\n')
   if result.returncode:raise RuntimeError(key+' '+label+'\n'+result.stdout[-6000:]+'\n'+result.stderr[-6000:])
   ck(key+'_'+label,result.returncode==0)
  for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','RESIDUAL-ADAPTERS.json','LOCAL-CHECKS.json']:
   data=(local/name).read_bytes();obj=rd(local/name)
   if name in provider['artifact_semantic_sha256']:ck(key+'_semantic_'+name,ident(obj)==provider['artifact_semantic_sha256'][name])
   if name.startswith('LOCAL-PROGRAMS'):ck(key+'_both_orientations',{o:ident(v)for o,v in obj.items()}==provider['program_hashes'])
   if name in provider['artifacts']:ck(key+'_raw_'+name,sha256(data).hexdigest()==provider['artifacts'][name])
   target=D/key/name;target.parent.mkdir(exist_ok=True);target.write_bytes(data);outputs.append(dict(provider=key,artifact=name,file=target.relative_to(R).as_posix(),sha256=hs(target),semantic_sha256=ident(obj),raw_own_commitment=provider['artifacts'].get(name),origin='unchanged_own_pinned_raw_word_transport_emitter'))
out=dict(schema='own1672-selected-native-recovery/1',pr=1672,own_head=head,status='passed_exact_selected_semantic_and_orientation_reconstruction',outputs=outputs,steps=steps,checks=checks,checks_passed=len(checks),source_archive_members=source_manifest,source_sha256={a['file']:a['sha256']for a in inputs},dependency_hashes={str(p.relative_to(R)):hs(p)for p in [S/'408001d452bd__MANIFEST.json',S/'native-input-manifest.json',specfile]},script_sha256=hs(Path(__file__)),scope='Actual own committed raw full words and own MANIFEST-bound source archive are used. Original all-column scalar/frame transport, native emitter, scalar replay and normalized wrapper check execute unchanged for both orientations. Complete selected semantic/orientation and declared raw artifact hashes must match. Full operator-valued phase, global owner, all-size compiler and whole integer costs remain separate.')
(R/'pr1672-exact-selected-native-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('PASS',len(checks),'own1672 exact selected native recovery checks')
