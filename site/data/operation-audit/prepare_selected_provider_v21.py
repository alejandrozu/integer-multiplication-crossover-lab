"""Four own joint-entrance selectors, two actual selected native providers.

This is preparation for fresh physical invoices, not a whole cost certificate.
"""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import copy,gzip,json,tarfile
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 b=(R/f).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def blob(b):return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
IDS={1148,1169,1183,1192};old=rd('selected-provider-dispatch-v10-inputs.json')
selection_file='joint-entrance-own-selection-source/source-manifest.json';selection=rd(selection_file)
recovery_files=['joint-entrance-selected-native-recovery.json','joint-entrance-extra-selected-native-recovery.json']
recs=[rd(f)for f in recovery_files]
assert all(all(r['checks'].values())and r['script_sha256']==hs(s)for r,s in zip(recs,['recover_joint_entrance_selected_native.py','recover_joint_entrance_extra_native.py']))
sources=[]
for recfile,rec in zip(recovery_files,recs):
 for a in rec['outputs']:
  if a['artifact']not in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']:continue
  assert hs(a['file'])==a['sha256']
  sources.append(dict(file=a['file'],sha256=a['sha256'],origin='actual_own_committed_RAW_unchanged_native_engines_exact_selected_objects',primary=dict(recovery_file=recfile,recovery_sha256=hs(recfile),payload=a)))
assert len(sources)==4
cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS];assert {x['pr']for x in cohort}==IDS
D=R/'selected-provider-dispatch-v21-source';D.mkdir(exist_ok=True)
for row in cohort:
 pr=row['pr'];z=next(x for x in selection['rows']if x['pr']==pr);files={a['relative']:a for a in z['files']};M=rd(z['MANIFEST_file']);spec=rd(z['SPEC_file']);out=D/str(pr);out.mkdir(exist_ok=True)
 assert z['own_head']==row['own_head']and M=={k:a['sha256']for k,a in files.items()if k!='MANIFEST.json'}
 for a in files.values():
  b=(R/a['file']).read_bytes();assert hs(a['file'])==a['sha256']and a['own_head']==z['own_head']and blob(b)==a['git_blob_sha1']==a['own_API_git_blob_sha1']
 claim_rel='CANDIDATE.json'if pr==1169 else'CLAIM.json';claim=rd(files[claim_rel]['file'])
 assert F(spec['expected']['kappa'])==F(claim['kappa'])==F(next(a['quoted_kappa_fraction']for a in old['claim_metadata']if a['pr']==pr))
 verf=files['verify.py']['file'];v=(R/verf).read_text();assert M['verify.py']==hs(verf)
 if pr==1148:
  assert "(data/'PLAN.json').write_bytes(gzip.decompress((P/'PLAN.json.gz').read_bytes()))"in v and"for name in ('OWNERS.json.gz','SPEC.json')"in v and"WORDPRE/'replay_native.py'"in v
  authority='own MANIFEST and literal verifier selects own gzip-decompressed PLAN plus own OWNERS/SPEC and own RAW/recipe'
 else:
  assert "t.extractall(layout,filter='data')"in v
  if pr==1169:
   assert "for name in ['PLAN.json','OWNERS.json.gz','SPEC.json','PROFILE.json','GLOBAL-TEMPLATE.json.gz']"in v and"SRC/'research/k8-joint-entrances/FULL-WORD.json.gz'"in v
  else:
   assert "for name in ('PLAN.json','SPEC.json','PROFILE.json','OWNERS.json.gz','DISPATCH.json','CONSTRUCTION.json','GLOBAL-TEMPLATE.json.gz')"in v
   assert "('base',P/'baseline/FULL-WORD.json.gz',a.base_native_from),('extra',P/'FULL-WORD.json.gz',a.extra_native_from)"in v
  authority='own MANIFEST and literal archive-based verifier selects own complete SPEC/PLAN/OWNERS and exact own native provider set'
  # Both own source archives bind the same complete base native closure. This
  # validates byte recovery reuse; it does not import a previous physical bill.
  a=files['upstream-layout.tar.gz'];closure=rd('joint-entrance-native-source/native-source-closure.json')
  with tarfile.open(R/a['file'])as t:
   ns={x.name:x for x in t.getmembers()}
   for f in closure['objects']:
    if f['path']in {'research/k8-joint-entrances/MANIFEST.json','research/k8-joint-entrances/README.md'}:continue
    n='joint1148-round45/source/'+f['path'];assert n in ns and ns[n].isfile()and sha256(t.extractfile(ns[n]).read()).hexdigest()==f['sha256']
 for pid,p in spec['providers'].items():
  r=recs[1]if pid=='extra'else recs[0]
  ca=next(a for a in r['outputs']if a['artifact']=='CANONICAL-WORD.json.gz');pa=next(a for a in r['outputs']if a['artifact']=='LOCAL-PROGRAMS.json.gz')
  assert ca['semantic_sha256']==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and pa['semantic_sha256']==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and pa['orientation_sha256']==p['program_hashes']
 assert set(spec['providers'])==({'gauge44','extra'}if pr in {1183,1192}else{'gauge44'})
 for kind in ['PLAN','OWNERS']:
  rel='PLAN.json.gz'if kind=='PLAN'and pr==1148 else'PLAN.json'if kind=='PLAN'else'OWNERS.json.gz';a=files[rel];f=a['file']
  if kind=='PLAN'and pr==1148:
   dst=out/'own-verifier-decompressed-PLAN.json';dst.write_bytes(gzip.decompress((R/f).read_bytes()));f=dst.relative_to(R).as_posix()
  assert hs(f)==spec['data'][kind.lower()+'_sha256']
  receipt=dict(pr=pr,own_head=z['own_head'],path=z['selected_package']+'/'+rel,file=f,sha256=hs(f),bytes=(R/f).stat().st_size,status='authenticated_own_SPEC_declared_bytes',primary_container=a,own_verifier_exact_gzip_decompression_only=kind=='PLAN'and pr==1148)
  (out/(kind+'.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
 found=[a for a in row['verified_components']if a.get('path')==z['selected_package']+'/SPEC.json'and a['sha256']==z['SPEC_sha256']];assert len(found)==1;found[0]['file']=z['SPEC_file']
 selector=dict(pr=pr,own_head=z['own_head'],SPEC_file=z['SPEC_file'],SPEC_sha256=z['SPEC_sha256'],MANIFEST_file=z['MANIFEST_file'],MANIFEST_sha256=z['MANIFEST_sha256'],verifier_file=verf,verifier_sha256=hs(verf),claim_file=files[claim_rel]['file'],claim_sha256=files[claim_rel]['sha256'],actual_literal_source_selection=authority,verified_primary=z['files'],selected_provider_names=sorted(spec['providers']),native_recovery_files={f:hs(f)for f in recovery_files},source_constructor_or_complete_original_global_PASS_claimed=False,physical_entry_output_absolute_phase_proved=False)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v17.py',selection_file,'joint-entrance-native-source/native-source-closure.json',*recovery_files,'recover_joint_entrance_selected_native.py','recover_joint_entrance_extra_native.py']
snap=dict(schema='selected-provider-dispatch-frozen-inputs/21',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=sources,original_input_sha256={f:hs(f)for f in deps},scope='Four distinct own joint-entrance constructions selected by each actual own MANIFEST, verifier and claim. Exact native byte reuse is checked against each own canonical/program/both-orientation commitments. Mixed1183/1192 require BOTH actual provider objects. PR1148 PLAN is exactly the own verifier gzip decompression of its committed primary container. Fresh full physical/owner/invoice checks are mandatory, with no previous bill/cutoff or full original verifier/phase PASS transferred.')
(R/'selected-provider-dispatch-v21-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v17.py').read_text().replace('selected-provider-dispatch-v17','selected-provider-dispatch-v21').replace('V17','V21')
(R/'selected_provider_dispatch_v21.py').write_text(s,encoding='utf8')
print('PASS prepared4 distinct own joint-entrance selectors and4 exact native byte objects')
