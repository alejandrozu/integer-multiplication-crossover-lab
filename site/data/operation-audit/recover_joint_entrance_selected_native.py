"""Replay own1148's selected committed RAW through four unchanged native stages."""
from pathlib import Path
from hashlib import sha256
import gzip,json,os,subprocess,sys,tempfile
R=Path(__file__).resolve().parent;D=R/'joint-entrance-selected-native';D.mkdir(exist_ok=True);checks={};steps=[]
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):
    b=p.read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(k,v):assert v,k;checks[k]=True
m=rd(R/'joint-entrance-native-source/native-source-closure.json');original=rd(R/'joint-entrance-native-source/source-discovery.json');root=original['selected_package'];M=original['own_package_manifest'];objects={a['path']:a for a in m['objects']}
ck('own_source_discovery_receipt',m['source_discovery_sha256']==hs(R/m['source_discovery_file']))
for a in m['objects']:
    ck('primary_'+a['path'],hs(R/a['file'])==a['sha256']and a['own_head']==m['own_head'])
    if a['path'].startswith(root+'/')and a['path']!=root+'/MANIFEST.json':ck('own_MANIFEST_'+a['path'],M[Path(a['path']).relative_to(root).as_posix()]==a['sha256'])
for a in m['implicit_native_inputs']:ck('literal_import_Git_contents_'+a['path'],hs(R/a['Git_contents_file'])==a['Git_contents_sha256']and rd(R/a['Git_contents_file'])['sha']==a['git_blob_sha1'])
spec=rd(R/objects[root+'/SPEC.json']['file']);recipe=rd(R/objects[root+'/RECIPE.json']['file']);raw=R/objects[root+'/FULL-WORD.json.gz']['file']
ck('own_literal_primary_RAW_selection',sha256(gzip.decompress(raw.read_bytes())).hexdigest()==recipe['output_content_sha256'])
v=(R/objects[root+'/verify.py']['file']).read_text()
ck('own_verifier_selects_committed_RAW_and_recipe',"payload(raw)==payload(P/'FULL-WORD.json.gz')==rd(P/'RECIPE.json')['output_content_sha256']"in v and "WORDPRE/'replay_native.py'"in v)
with tempfile.TemporaryDirectory(prefix='joint1148-')as temp:
    T=Path(temp)
    for a in m['objects']:
        p=T/a['path'];ck('safe_materialization_'+a['path'],p.resolve().is_relative_to(T.resolve()));p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/a['file']).read_bytes())
    src=T/'research/complex-k492-owner-repair/vendor/multicold';up=T/'research/complex-sw4-frame8/vendor/pr635/research/complex-571-cold14-st2/code';par=src/'vendor/pr558/vendor/pr552';local=T/'native'
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(src),GAIN_PR564_SOURCE=str(src));env.pop('PYTHONOPTIMIZE',None)
    for name,args in [('audit_and_transport.py',['--raw',T/root/'FULL-WORD.json.gz','--routing',par/'complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz','--out',local]),('emit_local.py',[local]),('audit_local.py',[local]),('adapters_local.py',[local/'CANONICAL-WORD.json.gz',local/'RESIDUAL-ADAPTERS.json',local/'WRAPPER-CHECKS.json'])]:
        a=subprocess.run([sys.executable,'-B',str(src/'code/run_portable.py'),str(up/('hpe_'+name)),*map(str,args)],cwd=T,env=env,capture_output=True,text=True,encoding='utf8');ck('actual_unchanged_native_stage_'+name,a.returncode==0);steps.append(dict(name=name,exit_code=a.returncode))
        if a.returncode:raise RuntimeError(a.stdout[-6000:]+a.stderr[-6000:])
        print('PASS own1148',name,flush=True)
    outputs=[]
    for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','LOCAL-CHECKS.json','RESIDUAL-ADAPTERS.json','WRAPPER-CHECKS.json']:
        p=local/name;b=p.read_bytes();obj=rd(p);out=D/name;out.write_bytes(gzip.compress(gzip.decompress(b),mtime=0)if b[:2]==b'\x1f\x8b'else b);outputs.append(dict(artifact=name,file=out.relative_to(R).as_posix(),sha256=hs(out),semantic_sha256=ident(obj),orientation_sha256={o:ident(v)for o,v in obj.items()}if name=='LOCAL-PROGRAMS.json.gz'else None))
    own=spec['providers']['gauge44'];can=next(a for a in outputs if a['artifact']=='CANONICAL-WORD.json.gz');prog=next(a for a in outputs if a['artifact']=='LOCAL-PROGRAMS.json.gz')
    ck('entire_own_selected_canonical',can['semantic_sha256']==own['artifact_semantic_sha256']['CANONICAL-WORD.json.gz'])
    ck('entire_own_selected_program',prog['semantic_sha256']==own['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz'])
    ck('both_own_orientation_programs',prog['orientation_sha256']==own['program_hashes'])
out=dict(schema='own1148-committed-RAW-native-byte-recovery/1',pr=1148,own_head=m['own_head'],status='passed_actual_own_committed_RAW_native_scalar_frame_wrapper_engines',checks_passed=len(checks),checks=checks,steps=steps,outputs=outputs,primary_RAW_file=objects[root+'/FULL-WORD.json.gz']['file'],primary_RAW_sha256=hs(raw),primary_RAW_content_sha256=sha256(gzip.decompress(raw.read_bytes())).hexdigest(),source_sha256={a['file']:a['sha256']for a in m['objects']},dependency_hashes={f:hs(R/f)for f in ['joint-entrance-native-source/native-source-closure.json','joint-entrance-native-source/source-discovery.json','complete_joint_entrance_native_closure.py','fetch_joint_entrance_native_sources.py']},source_constructor_replayed=False,full_phase_engine_replayed=False,original_complete_package_or_global_PASS_claimed=False,whole_integer_cost_proved=False,script_sha256=hs(Path(__file__)),scope='Own immutable-head primary committed RAW is literally selected by the own verifier/recipe and passed through the unchanged four own source-pinned native stages. Complete selected canonical/program and both orientation commitments are exact; deterministic derived gzip containers are not original Git containers. The two implicit routing/import paths omitted by SOURCE-PINS are bound by own immutable-head Git Contents blobs, not invented source pins. No constructor/full phase/global/allsize or crossover proof is claimed.')
(R/'joint-entrance-selected-native-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own1148 native/source checks')
