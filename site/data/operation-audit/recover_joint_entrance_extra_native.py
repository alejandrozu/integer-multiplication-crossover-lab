"""Recover the second, own-selected 1183/1192 provider from immutable own bytes.

No constructor, phase engine, complete global CLI or integer cost proof is claimed.
"""
from pathlib import Path
from hashlib import sha256, sha1
import gzip, json, os, subprocess, sys, tarfile, tempfile

R=Path(__file__).resolve().parent
D=R/'joint-entrance-extra-selected-native';D.mkdir(exist_ok=True)
checks={};steps=[]
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(k,v):assert v,k;checks[k]=True
def blob(b):return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

manifest_file='joint-entrance-own-selection-source/source-manifest.json'
manifest=rd(R/manifest_file)
closure_file='joint-entrance-native-source/native-source-closure.json'
closure=rd(R/closure_file)
own={row['pr']:row for row in manifest['rows']}
selected={}
for pr in (1183,1192):
 row=own[pr];files={a['relative']:a for a in row['files']}
 M=rd(R/row['MANIFEST_file'])
 for a in row['files']:
  p=R/a['file'];b=p.read_bytes()
  ck(f'own_{pr}_payload_'+a['relative'],hs(p)==a['sha256']and a['own_head']==row['own_head'])
  ck(f'own_{pr}_Git_blob_'+a['relative'],blob(b)==a['git_blob_sha1']==a['own_API_git_blob_sha1'])
  if a['relative']!='MANIFEST.json':ck(f'own_{pr}_MANIFEST_'+a['relative'],M[a['relative']]==a['sha256'])
 ck(f'own_{pr}_complete_inventory',set(M)==set(files)-{'MANIFEST.json'})
 s=rd(R/files['SPEC.json']['file']);v=(R/files['verify.py']['file']).read_text()
 ck(f'own_{pr}_literal_extra_selection',"('extra',P/'FULL-WORD.json.gz',a.extra_native_from)"in v and "SRC/'research/k8-eight-ends/replay_native.py'"in v)
 selected[pr]=dict(row=row,files=files,spec=s)

# All source bodies and inputs in the previously audited short import closure
# are required to occur byte-for-byte in EACH own, MANIFEST-bound archive.
# The two human/package metadata documents differ and are not executed/read by
# the four native engines. Their exclusion is exact, not an arbitrary wildcard.
metadata_only={'research/k8-joint-entrances/MANIFEST.json','research/k8-joint-entrances/README.md'}
archive_source_rows=[]
for pr,z in selected.items():
 a=z['files']['upstream-layout.tar.gz']
 with tarfile.open(R/a['file'])as t:
  members={x.name:x for x in t.getmembers()}
  for f in closure['objects']:
   if f['path']in metadata_only:continue
   n='joint1148-round45/source/'+f['path']
   ck(f'own_{pr}_archive_member_'+f['path'],n in members and members[n].isfile())
   b=t.extractfile(members[n]).read()
   ck(f'own_{pr}_entire_native_closure_'+f['path'],sha256(b).hexdigest()==f['sha256'])
   archive_source_rows.append(dict(pr=pr,archive=a['file'],member=n,sha256=f['sha256']))
 ck(f'own_{pr}_native_closure_only_metadata_exclusions',len([f for f in closure['objects']if f['path']not in metadata_only])==68)

z=selected[1183];raw=R/z['files']['FULL-WORD.json.gz']['file']
other=R/selected[1192]['files']['FULL-WORD.json.gz']['file']
ck('two_own_selected_extra_RAW_payloads_exact',gzip.decompress(raw.read_bytes())==gzip.decompress(other.read_bytes()))
ck('two_own_extra_full_commitment_objects_equal',z['spec']['providers']['extra']==selected[1192]['spec']['providers']['extra'])
with tempfile.TemporaryDirectory(prefix='joint-extra-')as temp:
 T=Path(temp)
 # Read the code from the actual 1183 archive, after exact source-body checks.
 with tarfile.open(R/z['files']['upstream-layout.tar.gz']['file'])as t:
  members={x.name:x for x in t.getmembers()}
  for f in closure['objects']:
   if f['path']in metadata_only:continue
   p=T/f['path'];ck('safe_materialization_'+f['path'],p.resolve().is_relative_to(T.resolve()));p.parent.mkdir(parents=True,exist_ok=True)
   p.write_bytes(t.extractfile(members['joint1148-round45/source/'+f['path']]).read())
 rawp=T/'selected-extra-RAW.json.gz';rawp.write_bytes(raw.read_bytes())
 src=T/'research/complex-k492-owner-repair/vendor/multicold'
 up=T/'research/complex-sw4-frame8/vendor/pr635/research/complex-571-cold14-st2/code'
 par=src/'vendor/pr558/vendor/pr552';local=T/'native'
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTHONINTMAXSTRDIGITS='0',MULTICOLD_SOURCE=str(src),GAIN_PR564_SOURCE=str(src));env.pop('PYTHONOPTIMIZE',None)
 stages=[('audit_and_transport.py',['--raw',rawp,'--routing',par/'complex-local/inputs/phase-baseline/CANONICAL-WORD.json.gz','--out',local]),('emit_local.py',[local]),('audit_local.py',[local]),('adapters_local.py',[local/'CANONICAL-WORD.json.gz',local/'RESIDUAL-ADAPTERS.json',local/'WRAPPER-CHECKS.json'])]
 for name,args in stages:
  p=subprocess.run([sys.executable,'-B',str(src/'code/run_portable.py'),str(up/('hpe_'+name)),*map(str,args)],cwd=T,env=env,capture_output=True,text=True,encoding='utf8')
  if p.returncode:raise RuntimeError(p.stdout[-6000:]+p.stderr[-6000:])
  ck('actual_unchanged_native_stage_'+name,p.returncode==0);steps.append(dict(name=name,exit_code=p.returncode));print('PASS own extra',name,flush=True)
 outputs=[]
 for name in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz','LOCAL-CHECKS.json','RESIDUAL-ADAPTERS.json','WRAPPER-CHECKS.json']:
  p=local/name;b=p.read_bytes();obj=rd(p);out=D/name
  out.write_bytes(gzip.compress(gzip.decompress(b),mtime=0)if b[:2]==b'\x1f\x8b'else b)
  outputs.append(dict(artifact=name,file=out.relative_to(R).as_posix(),sha256=hs(out),semantic_sha256=ident(obj),orientation_sha256={o:ident(v)for o,v in obj.items()}if name=='LOCAL-PROGRAMS.json.gz'else None))
 for pr,z in selected.items():
  can=next(a for a in outputs if a['artifact']=='CANONICAL-WORD.json.gz');prog=next(a for a in outputs if a['artifact']=='LOCAL-PROGRAMS.json.gz');provider=z['spec']['providers']['extra']
  ck(f'own_{pr}_entire_selected_canonical',can['semantic_sha256']==provider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz'])
  ck(f'own_{pr}_entire_selected_program',prog['semantic_sha256']==provider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz'])
  ck(f'own_{pr}_both_orientation_programs',prog['orientation_sha256']==provider['program_hashes'])

out=dict(schema='own-joint-entrance-second-provider-native-recovery/1',status='passed_actual_own_selected_RAW_four_native_engines',prs=[1183,1192],own_heads={str(p):z['row']['own_head']for p,z in selected.items()},checks_passed=len(checks),checks=checks,steps=steps,outputs=outputs,archive_native_source_bindings=archive_source_rows,excluded_nonexecuted_metadata_only=sorted(metadata_only),source_sha256={a['file']:a['sha256']for z in selected.values()for a in z['row']['files']},dependency_hashes={f:hs(R/f)for f in [manifest_file,closure_file,'joint-entrance-selected-native-recovery.json','recover_joint_entrance_selected_native.py']},script_sha256=hs(Path(__file__)),source_constructor_replayed=False,full_phase_engine_replayed=False,original_complete_package_or_global_PASS_claimed=False,whole_integer_cost_proved=False,scope='Actual primary extra RAW payloads selected by both own verifiers coincide exactly. All 68 executable/input-closure objects are byte-identical in each own MANIFEST-bound archive; only two nonexecuted package metadata documents are excluded. The actual 1183 archived four native engines execute in an isolated short tree and complete canonical/program/both-orientation commitments match BOTH own SPECs. This is native byte/scalar/frame/wrapper evidence, not an operator/phase/allsize or crossover theorem. Deterministic derived gzip containers are not historical Git containers.')
(R/'joint-entrance-extra-selected-native-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('PASS',len(checks),'own extra source/native checks')
