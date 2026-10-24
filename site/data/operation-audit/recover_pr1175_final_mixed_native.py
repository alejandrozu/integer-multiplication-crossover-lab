"""Recover exact own final1175 mixed native byteobjects; no old fixture selection."""
from pathlib import Path
from hashlib import sha256
import gzip,json,os,subprocess,sys,tempfile,tarfile
R=Path(__file__).resolve().parent;S=R/'pr1175-final-mixed-source';D=R/'pr1175-final-mixed-native';D.mkdir(exist_ok=True);head='007a7c64280053e2ddabdb92e60b51bfd9105119';base='research/gauge44-slots-mixed-arcflow/'
def rd(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def hs(p):return sha256(p.read_bytes()).hexdigest()
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
checks={}
def ck(n,v):assert v,n;checks[n]=True
M=rd(S/'42bb252d3a60__MANIFEST.json');primary=rd(S/'initial-manifest.json')+rd(S/'construction-input-manifest.json');by={a['path'][len(base):]:a for a in primary}
for a in primary:
 ck('own_primary_'+a['path'],a['own_head']==head and hs(R/a['file'])==a['sha256'])
 if a['path']!=base+'MANIFEST.json':ck('own_MANIFEST_'+a['path'],M[a['path'][len(base):]]==a['sha256'])
spec=rd(R/by['data/SPEC.json']['file']);pins=rd(R/by['construction/mixed/MIXED-PINS-k8.json']['file']);claim=rd(R/by['CLAIM.json']['file']);result=rd(R/by['RESULT.json']['file']);ck('actual_final_head_selection',claim['head_kappa_package'].startswith('research/gauge44-slots-mixed-arcflow')and claim['head_kappa']==pins['kappa_decimal']==result['kappa_decimal']==spec['expected']['kappa_decimal']and result['spec_sha256']==hs(R/by['data/SPEC.json']['file']))
# Recover a byteobject already committed by this own base pin, never infer a
# native endpoint from its report/profile. Every before/after replacement and
# the entire resulting raw SHA are mandatory.
word_source=R/'pr1178-native-recovery-source/dependencies/d28c607df2bc__FULL-WORD.json.gz';inverse_source=R/'pr1178-native-recovery-source/dependencies/6a5d91b95bdb__RECIPE.json';inverse=rd(inverse_source);raw=gzip.decompress(word_source.read_bytes());w=json.loads(raw);ck('archived_recipe_output',sha256(raw).hexdigest()==inverse['output_content_sha256'])
for sec in ['A','B']:
 for i,before,after in inverse[sec]:ck('inverse_'+sec+'_'+str(i),w[sec][i][-1]==after);w[sec][i][-1]=before
for i,before,after in inverse['early_cleanup']:ck('inverse_early_'+str(i),w['early_cleanup'][i][1]==after);w['early_cleanup'][i][1]=before
for h,before,after in inverse['ends']:ck('inverse_end_'+str(h),w['helper_final'][str(h)]==after);w['helper_final'][str(h)]=before
old_spec=R/'remaining-record-audit/artifacts/1175/0f6fba7ee304__SPEC.json';old_manifest=R/'remaining-record-audit/artifacts/1175/bc4e809de8d8__MANIFEST.json';ck('older_report_source_bound',rd(old_manifest)['data/SPEC.json']==hs(old_spec));p=rd(old_spec)['providers']['gauge44'];w['report']['local_profile']=p['expected_profile'];w['report']['local_rank_mass']=sum(int(k)*v for k,v in p['expected_profile'].items());w['report']['width_inventory']=p['inventory'];basebytes=json.dumps(w,separators=(',',':')).encode();ck('whole_recovered_earlier_base_content',sha256(basebytes).hexdigest()==inverse['input_content_sha256']==pins['base_sha256'])
basefile=D/'exact-slot-base.json.gz';basefile.write_bytes(gzip.compress(basebytes,mtime=0));archive=R/'pr1672-native-recovery-source/a0cc229bb0fc__upstream-layout.tar.gz';archive_receipt=next(a for a in rd(R/'pr1672-native-recovery-source/native-input-manifest.json')if a['path'].endswith('/upstream-layout.tar.gz'));ck('published_source_archive',hs(archive)==archive_receipt['sha256']);pipeline=rd(S/'native-pipeline-own-primary.json');outputs=[];steps=[];logs=[];members={}
with tempfile.TemporaryDirectory(prefix='p1175-')as temporary:
 T=Path(temporary)
 with tarfile.open(archive)as tar:
  for a in tar:
   rel=Path(a.name);ck('archive_path_'+a.name,a.isfile()and not rel.is_absolute()and'..'not in rel.parts);target=T/rel;assert target.resolve().is_relative_to(T.resolve());target.parent.mkdir(parents=True,exist_ok=True);data=tar.extractfile(a).read();target.write_bytes(data);members[a.name]=sha256(data).hexdigest()
 root=T/'joint1148-round45/source';src=root/'research/complex-k492-owner-repair/vendor/multicold';up=root/'research/complex-sw4-frame8/vendor/pr635/research/complex-571-cold14-st2/code';portable=src/'code/run_portable.py';routing=src/'vendor/pr558/vendor/pr552/complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz'
 for a in pipeline:ck('own_pipeline_'+a['path'],a['own_head']==head and hs(R/a['file'])==a['sha256']==hs(root/a['path'])and a['own_primary_byte_equal_to_archive'])
 upstream=rd(R/by['data/UPSTREAM-PINS.json']['file'])
 for path,digest in upstream.items():ck('own_upstream_'+path,hs(root/path)==digest)
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(src),GAIN_PR564_SOURCE=str(src));env.pop('PYTHONOPTIMIZE',None)
 for key in ['gauge44r16','gauge44r12']:
  recipe=R/by['construction/mixed/RECIPE-'+key[-3:].upper()+'-k8.json']['file'];rawfile=T/(key+'.json.gz');local=T/('local-'+key);provider=spec['providers'][key]
  jobs=[('own_mixed_constructor',[str(R/by['construction/mixed/apply_mixed.py']['file']),str(basefile),str(recipe),str(rawfile)]),('native_transport',[str(portable),str(up/'hpe_audit_and_transport.py'),'--raw',str(rawfile),'--routing',str(routing),'--out',str(local)]),('native_emitter',[str(portable),str(up/'hpe_emit_local.py'),str(local)]),('native_scalar_replay',[str(portable),str(up/'hpe_audit_local.py'),str(local)]),('normalized_wrapper_check',[str(portable),str(up/'hpe_adapters_local.py'),str(local/'CANONICAL-WORD.json.gz'),str(local/'RESIDUAL-ADAPTERS.json'),str(local/'WRAPPER-CHECKS.json')])]
  for label,args in jobs:
   run=subprocess.run([sys.executable,'-B',*args],cwd=root,env=env,capture_output=True,text=True,encoding='utf8');steps.append(dict(provider=key,name=label,exit_code=run.returncode));logs.append(dict(provider=key,name=label,stdout=run.stdout,stderr=run.stderr));(R/'pr1175-final-mixed-recovery-execution-log.json').write_text(json.dumps(logs,indent=2)+'\n')
   if run.returncode:raise RuntimeError(key+' '+label+'\n'+run.stdout[-6000:]+'\n'+run.stderr[-6000:])
   ck(key+'_'+label,run.returncode==0)
  ck(key+'_actual_recipe_word',sha256(gzip.decompress(rawfile.read_bytes())).hexdigest()==pins['providers'][key]['word_sha256'])
  for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','RESIDUAL-ADAPTERS.json','LOCAL-CHECKS.json']:
   data=(local/name).read_bytes();o=rd(local/name);ck(key+'_own_full_semantic_'+name,ident(o)==provider['artifact_semantic_sha256'][name])
   if name.startswith('LOCAL-PROGRAMS'):ck(key+'_both_orientations',{k:ident(v)for k,v in o.items()}==provider['program_hashes']==pins['providers'][key]['program_sha256'])
   if name in provider['artifacts']:ck(key+'_own_raw_'+name,sha256(data).hexdigest()==provider['artifacts'][name])
   target=D/key/name;target.parent.mkdir(exist_ok=True);target.write_bytes(data);outputs.append(dict(provider=key,artifact=name,file=target.relative_to(R).as_posix(),sha256=hs(target),semantic_sha256=ident(o),origin='Exact earlier own commitments, recovered using original own mixed recipes and byte-identical own source entrypoints from a published source archive'))
source={a['file']:a['sha256']for a in primary+pipeline};source.update({str(p.relative_to(R)):hs(p)for p in[word_source,inverse_source,old_spec,old_manifest,archive]});deps=[S/'initial-manifest.json',S/'construction-input-manifest.json',S/'native-pipeline-own-primary.json',R/'pr1178-native-recovery-source/native-dependencies-manifest.json',R/'pr1672-native-recovery-source/native-input-manifest.json']
out=dict(schema='own1175-final-mixed-selected-native-recovery/1',pr=1175,own_head=head,status='passed_exact_selected_semantic_and_orientation_reconstruction',actual_final_package=base[:-1],actual_final_kappa=spec['expected']['kappa'],older_fixture_not_selected=True,outputs=outputs,steps=steps,checks=checks,checks_passed=len(checks),source_archive_members=members,source_sha256=source,dependency_hashes={str(p.relative_to(R)):hs(p)for p in deps},script_sha256=hs(Path(__file__)),scope='The exact earlier required slot base is byte-recovered by reversing a fully pinned before/after recipe and restoring old report-only fields; its whole raw SHA must equal own final MIXED-PINS. Both original own mixed constructors and source-entrypoint-identical native transport/emitter/scalar/wrapper jobs execute; each complete canonical/program/orientation commitment must match the actual final selected own SPEC. No later algorithm, price, phase proof or original full admission is transferred. Full operator-valued phase, dirty/owner/common-label/all-size/hosting interfaces remain separate.')
(R/'pr1175-final-mixed-selected-native-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'actual final own1175 mixed native recovery checks')
