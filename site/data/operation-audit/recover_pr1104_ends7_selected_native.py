"""Literal own ends7 constructor on the exact selected c2b raw byteobject.

Every actual output and both orientations must match the own SPEC exactly.
No exploratory canonical-coordinate reconstruction is used.
"""
from pathlib import Path
from hashlib import sha256,sha1
import gzip,json,os,subprocess,sys,tarfile,tempfile
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'pr1104-ends7-selected-source';D=R/'pr1104-recovered-ends7-native';D.mkdir(exist_ok=True);checks={}
def ck(n,v):assert v,n;checks[n]=True
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_bytes())
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
M=rd(S/'source-fetch-manifest.json');sourcepins={str((S/'source-fetch-manifest.json').relative_to(R)).replace('\\','/'):hs(S/'source-fetch-manifest.json')}
authority=rd(S/'MANIFEST.json')
for x in M['files']:
 p=R/x['file'];raw=p.read_bytes();ck('own_source_'+x['relative_path'],x['head']==M['own_head']=='d8982686afd7ef6ce52ddeaa17011ccda558d666'and hs(p)==x['sha256']and sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['git_blob_sha1']);sourcepins[x['file']]=x['sha256']
 if x['relative_path']in authority:ck('own_manifest_'+x['relative_path'],authority[x['relative_path']]==x['sha256'])
provider=rd(S/'data/SPEC.json')['providers']['gauge44'];pins=rd(S/'construction/ends7/ENDS7-PINS-k8.json');recipe=rd(S/'construction/ends7/RECIPE-ENDS7-k8.json')
rawfile=R/'pr1175-final-mixed-native/exact-slot-base.json.gz';base=rd(rawfile)
ck('exact_own_selected_raw_base',sha256(gzip.decompress(rawfile.read_bytes())).hexdigest()==ident(base)==pins['base_sha256']==recipe['input_sha256']=='c2b294300760e1fd6eeab8c22c4d13e4633dca40e52cac8da0d68163a76e3ca8')
prior=rd(R/'pr1175-final-mixed-selected-native-recovery.json');ck('exact_base_recovery_receipt',all(prior['checks'].values())and prior['script_sha256']==hs(R/'recover_pr1175_final_mixed_native.py'))
archivef='pr1672-native-recovery-source/a0cc229bb0fc__upstream-layout.tar.gz';archive=R/archivef;prior_sources={k.replace('\\','/'):v for k,v in prior['source_sha256'].items()};ck('authenticated_native_source_archive',hs(archive)==prior_sources[archivef])
steps=[];outputs=[]
with tempfile.TemporaryDirectory(prefix='ends7-own-')as temporary:
 T=Path(temporary)
 with tarfile.open(archive)as tar:
  for a in tar:
   rel=Path(a.name);ck('archive_path_'+a.name,a.isfile()and not rel.is_absolute()and'..'not in rel.parts)
   data=tar.extractfile(a).read();ck('archive_member_'+a.name,sha256(data).hexdigest()==prior['source_archive_members'][a.name]);p=T/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 root=T/'joint1148-round45/source';src=root/'research/complex-k492-owner-repair/vendor/multicold';up=root/'research/complex-sw4-frame8/vendor/pr635/research/complex-571-cold14-st2/code';portable=src/'code/run_portable.py';routing=src/'vendor/pr558/vendor/pr552/complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz';local=T/'local';built=T/'ENDS7-FULL-WORD.json.gz'
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(src),GAIN_PR564_SOURCE=str(src));env.pop('PYTHONOPTIMIZE',None)
 def run(label,args):
  p=subprocess.run([sys.executable,'-B',*map(str,args)],cwd=root,env=env,capture_output=True,text=True,encoding='utf8');ck('executed_'+label,p.returncode==0);steps.append(dict(name=label,exit_code=p.returncode))
  if p.returncode:raise RuntimeError(p.stdout[-3000:]+p.stderr[-3000:])
 run('own_literal_build_ends7',[S/'construction/ends7/build_ends7.py',rawfile,S/'construction/ends7/RECIPE-ENDS7-k8.json',built])
 ck('exact_own_raw_output_commitment',sha256(gzip.decompress(built.read_bytes())).hexdigest()==recipe['expected']['output_sha256']==pins['word_sha256']=='f64e0942edc5eb2d45b0a3b068ba942436f35ba9a077ff53d7e4424d1617b2cd')
 jobs=[('native_transport',[portable,up/'hpe_audit_and_transport.py','--raw',built,'--routing',routing,'--out',local]),('native_emitter',[portable,up/'hpe_emit_local.py',local]),('native_scalar_replay',[portable,up/'hpe_audit_local.py',local]),('normalized_wrapper_check',[portable,up/'hpe_adapters_local.py',local/'CANONICAL-WORD.json.gz',local/'RESIDUAL-ADAPTERS.json',local/'WRAPPER-CHECKS.json'])]
 for name,args in jobs:run(name,args)
 canonical,programs=rd(local/'CANONICAL-WORD.json.gz'),rd(local/'LOCAL-PROGRAMS.json.gz')
 ck('exact_own_canonical_commitment',ident(canonical)==pins['canonical_sha256']==provider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']=='a8a009fa1a48780a7e9cdbc0a782a26d7059a4dbcb9a8d8389ecd5d17a084a5a')
 ck('exact_own_complete_selected_program',ident(programs)==provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']=='d361480e71f39003ba7cbb696172354df6761f49a12aa988b4ba340cd638af44')
 ck('both_own_selected_program_orientations',{o:ident(p)for o,p in programs.items()}==pins['program_sha256']==provider['program_hashes'])
 ck('exact_own_local_profile',canonical['local_profile']==provider['expected_profile']==recipe['expected']['local_profile'])
 for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','RESIDUAL-ADAPTERS.json','LOCAL-CHECKS.json','WRAPPER-CHECKS.json']:
  out=D/name;out.write_bytes((local/name).read_bytes());o=rd(out);outputs.append(dict(file=out.relative_to(R).as_posix(),sha256=hs(out),semantic_sha256=ident(o),origin='Own literal ends7 constructor plus source-native transport/emitter/scalar/wrapper engines; exact earlier own selected commitments required'))
 (D/'FULL-WORD.json.gz').write_bytes(built.read_bytes());outputs.append(dict(file=(D/'FULL-WORD.json.gz').relative_to(R).as_posix(),sha256=hs(D/'FULL-WORD.json.gz'),semantic_sha256=ident(rd(built)),origin='Actual own unchanged build_ends7.py output'))
deps=['recover_pr1104_ends7_selected_native.py','fetch_pr1104_ends7_selected_source.py','pr1175-final-mixed-selected-native-recovery.json','recover_pr1175_final_mixed_native.py','pr1175-final-mixed-native/exact-slot-base.json.gz',archivef]
out=dict(schema='own1104-literal-selected-ends7-native-recovery/1',pr=1104,own_head=M['own_head'],status='actual_source_selected_native_recovered_no_whole_cost',selected_package=M['selected_package'],source_raw_content_sha256=pins['base_sha256'],own_raw_output_content_sha256=pins['word_sha256'],selected_canonical_semantic_sha256=ident(canonical),selected_program_semantic_sha256=ident(programs),orientation_hashes={o:ident(p)for o,p in programs.items()},steps=steps,outputs=outputs,
 scope='Actual unchanged own build_ends7.py runs on the exact raw c2b byteobject selected by its own recipe. Raw output, canonical, complete program and both orientations must equal own commitments. Published source-native transport, scalar emission/replay and normalized wrappers are freshly executed; full operator/absolute-phase engines and original global controller are not. Later archives provide exact source/byteobjects only, not a later construction or runtime estimate. No whole cost or native phase theorem is inherited.',
 original_own_raw_constructor_replayed=True,native_scalar_and_normalized_wrapper_stages_replayed=True,full_operator_or_absolute_phase_replayed=False,whole_controller_or_integer_cost_claimed=False,
 source_sha256=sourcepins,dependency_hashes={p:hs(R/p)for p in deps},checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__)))
(R/'pr1104-exact-selected-ends7-native-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'literal own ends7 source+native checks; exact selectedd361480 bytes')
