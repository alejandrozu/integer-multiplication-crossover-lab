"""Own591/608/615 exact typed native identities and complete physical inputs."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import copy,gzip,json
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 b=(R/f).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
IDS={591,608,615};old=rd('selected-provider-dispatch-v10-inputs.json')
mf='early-hyperplane-cold-own-source/source-manifest.json';selection=rd(mf)
recf='early-hyperplane-cold-selected-native-recovery.json';rec=rd(recf)
assert rec['status']=='passed_actual_own_typed_constructor_and_native_scalar_frame_wrapper_engines'and rec['script_sha256']==hs('recover_early_hyperplane_cold_native.py')and set(rec['prs'])==IDS and all(rec['checks'].values())
for key in ['source_sha256','executed_external_source_sha256','retained_base_sha256','dependency_hashes']:
 for f,h in rec[key].items():assert hs(f)==h,f
cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS];assert {r['pr']for r in cohort}==IDS
D=R/'selected-provider-dispatch-v23-source';D.mkdir(exist_ok=True);sources={};bindings={}
for row in cohort:
 pr=row['pr'];z=next(a for a in selection['rows']if a['pr']==pr);files={a['relative']:a for a in z['files']};M=rd(z['MANIFEST_file']);s=rd(z['SPEC_file']);out=D/str(pr);out.mkdir(exist_ok=True)
 assert row['own_head']==z['own_head']and M=={k:a['sha256']for k,a in files.items()if k!='MANIFEST.json'}
 api={}
 for f,h in z['primary_changed_file_API_sha256'].items():assert hs(f)==h;api.update({a['filename']:a['sha']for a in rd(f)})
 for a in files.values():
  b=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  assert hs(a['file'])==a['sha256']and a['own_head']==z['own_head']and blob==a['git_blob_sha1']==a['own_API_git_blob_sha1']==api[a['path']]
 v=(R/files['verify.py']['file']).read_text()
 assert "SPECFILE=a.spec.resolve();SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v and "futures={pid:pool.submit(provider,pid)for pid in sorted(BUILD['providers'])}"in v
 assert "'--plan',P/'data/PLAN.json'"in v and "'--owners',P/'data/OWNERS.json.gz'"in v
 assert F(s['expected']['kappa'])==F(next(a['quoted_kappa_fraction']for a in old['claim_metadata']if a['pr']==pr))
 bindings[str(pr)]={}
 for pid,p in s['providers'].items():
  raw=s['build']['providers'][pid]['word_content_sha256'];ownpair=next(a for a in rec['selected_own_providers']if a['pr']==pr and a['provider']==pid)
  assert ownpair['own_head']==z['own_head']and ownpair['own_SPEC_file']==z['SPEC_file']and ownpair['own_SPEC_sha256']==z['SPEC_sha256']and ownpair['RAW_content_sha256']==raw and hs(ownpair['RAW_file'])==ownpair['RAW_sha256']
  aa={a['artifact']:a for a in rec['outputs']if a['pr']==pr and a['provider']==pid};can,prog=aa['CANONICAL-WORD.json.gz'],aa['LOCAL-PROGRAMS.json.gz']
  assert prog['orientation_sha256']==p['program_hashes']and ident(rd(prog['file']))==prog['semantic_sha256']==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and ident(rd(can['file']))==can['semantic_sha256']==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']
  for a in (can,prog):
   assert hs(a['file'])==a['sha256'];sources[a['file']]=dict(file=a['file'],sha256=a['sha256'],origin='actual_own_typed_constructor_and_native_engines_with_exact_own_RAW_canonical_program_both_orientation_joins',primary=dict(recovery_file=recf,recovery_sha256=hs(recf),payload=a))
  bindings[str(pr)][pid]=dict(own_RAW_content_sha256=raw,canonical_sha256=can['semantic_sha256'],program_sha256=prog['semantic_sha256'],orientation_sha256=p['program_hashes'],canonical_file=can['file'],program_file=prog['file'],canonical_digest_explicit_in_own_SPEC=True)
 for kind in ['PLAN','OWNERS']:
  rel='data/PLAN.json'if kind=='PLAN'else'data/OWNERS.json.gz';a=files[rel];assert a['sha256']==s['data'][kind.lower()+'_sha256']
  receipt=dict(pr=pr,own_head=z['own_head'],path=a['path'],file=a['file'],sha256=a['sha256'],bytes=a['bytes'],status='authenticated_own_SPEC_declared_bytes',primary=a)
  (out/(kind+'.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
 found=[a for a in row['verified_components']if a.get('path')==z['selected_package']+'/data/SPEC.json'and a['sha256']==z['SPEC_sha256']];assert len(found)==1;found[0]['file']=z['SPEC_file']
 selector=dict(pr=pr,own_head=z['own_head'],SPEC_file=z['SPEC_file'],SPEC_sha256=z['SPEC_sha256'],MANIFEST_file=z['MANIFEST_file'],MANIFEST_sha256=z['MANIFEST_sha256'],verifier_file=files['verify.py']['file'],verifier_sha256=files['verify.py']['sha256'],verified_primary=z['files'],primary_changed_file_API_sha256=z['primary_changed_file_API_sha256'],actual_own_literal_SPEC_build_native_PLAN_OWNERS_selection=True,actual_literal_spec_driven_native_and_global_data_selection=True,exact_own_selected_RAW_native_bindings=bindings[str(pr)],recovery_file=recf,recovery_sha256=hs(recf),own_selected_native_recovery_file=recf,own_selected_native_recovery_sha256=hs(recf),complete_historical_package_replay_claimed=False,own_constructor_functions_executed_without_text_changes=True,portable_import_adapter=rec['portable_import_adapter'],original_own_complete_constructor_or_global_verifier_PASS_claimed=False,universal_phase_native_allsize_proved=False)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v17.py',mf,recf,'recover_early_hyperplane_cold_native.py']
snap=dict(schema='selected-provider-dispatch-frozen-inputs/23',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=list(sources.values()),recovered_own_native_selection=bindings,original_input_sha256={f:hs(f)for f in deps},scope='Three own selected hyperplane/cold-end finite controllers. Complete own MANIFEST/API blobs, exact own typed RAW/canonical/program/both-orientation commitments and actual source/native execution are bound separately. External GK import-path fallback only; all source text and guards unchanged. Fresh own complete PLAN/OWNERS/physical invoices and all cost schedules still required; no prior bill/cutoff or original full global/phase PASS transfer.')
(R/'selected-provider-dispatch-v23-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v17.py').read_text().replace('selected-provider-dispatch-v17','selected-provider-dispatch-v23').replace('V17','V23')
(R/'selected_provider_dispatch_v23.py').write_text(s,encoding='utf8')
print('PASS prepared own591/608/615 selected inputs; native objects',len(sources))
