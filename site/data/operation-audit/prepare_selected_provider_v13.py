"""Four own committed-PLAN ends7 controllers after exact raw/native recovery.

PR1152 shares actual selected bytes but has a distinct generated-PLAN interface
and is deliberately not admitted by this preparation.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import copy,json,shutil
R=Path(__file__).resolve().parent
def rd(f):return json.loads((R/f).read_bytes())
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
IDS={1104,1107,1117,1121};old=rd('selected-provider-dispatch-v10-inputs.json');recovery=rd('pr1104-exact-selected-ends7-native-recovery.json');selection=rd('ends7-own-selection-source/source-fetch-manifest.json');cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS]
assert {x['pr']for x in cohort}==IDS
assert recovery['script_sha256']==hs('recover_pr1104_ends7_selected_native.py')and all(recovery['checks'].values())and len(recovery['steps'])==5 and all(x['exit_code']==0 for x in recovery['steps'])and recovery['original_own_raw_constructor_replayed']and not recovery['full_operator_or_absolute_phase_replayed']
sources=[]
for a in recovery['outputs']:
 if a['file'].rsplit('/',1)[-1]in['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']:
  assert hs(a['file'])==a['sha256'];sources.append(dict(file=a['file'],sha256=a['sha256'],origin='actual_own1104_literal_recipe_and_native_engines_exact_selected_bytes',primary=a))
assert len(sources)==2
D=R/'selected-provider-dispatch-v13-source';D.mkdir(exist_ok=True)
for row in cohort:
 pr=row['pr'];out=D/str(pr);out.mkdir(exist_ok=True)
 for kind in['PLAN','OWNERS']:
  f=f'selected-provider-dispatch-v10-source/{pr}/{kind}.json';a=rd(f);assert a['status']=='authenticated_own_SPEC_declared_bytes'and hs(a['file'])==a['sha256'];shutil.copyfile(R/f,out/(kind+'.json'))
 files=[a for a in selection if a['pr']==pr];M=next(a for a in files if a['path'].endswith('/MANIFEST.json'));V=next(a for a in files if a['path'].endswith('/verify_t16.py'));mf=rd(M['file']);v=(R/V['file']).read_text()
 assert all(a['own_head']==row['own_head']and hs(a['file'])==a['sha256']and a['api_own_blob_verified']for a in files)
 assert mf['verify_t16.py']==V['sha256']and "SPEC8, SPEC16 = PKG / 'data/SPEC-T8.json', PKG / 'data/SPEC.json'"in v and"--plan', PKG / 'data/PLAN.json'"in v and"--owners', PKG / 'data/OWNERS.json.gz'"in v
 selected=[a for a in row['verified_components']if a.get('path','').endswith('/data/SPEC.json')and a['sha256']==mf['data/SPEC.json']];assert len(selected)==1;spec=rd(selected[0]['file'])
 assert spec['data']==dict(plan_sha256=mf['data/PLAN.json'],owners_sha256=mf['data/OWNERS.json.gz'])
 assert spec['providers']['gauge44']['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']==recovery['selected_program_semantic_sha256']and spec['providers']['gauge44']['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']==recovery['selected_canonical_semantic_sha256']and spec['providers']['gauge44']['program_hashes']==recovery['orientation_hashes']
 (out/'actual-own-selector.json').write_text(json.dumps(dict(pr=pr,own_head=row['own_head'],SPEC_file=selected[0]['file'],SPEC_sha256=selected[0]['sha256'],MANIFEST=M,verifier=V,verified_primary=files,own_selected_committed_PLAN=True,own_selected_full_native_commitments_checked=True),indent=2)+'\n',encoding='utf8')
snapshot=dict(schema='selected-provider-dispatch-frozen-inputs/13',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=sources,original_input_sha256={p:hs(p)for p in['selected-provider-dispatch-v10-inputs.json','pr1104-exact-selected-ends7-native-recovery.json','ends7-own-selection-source/source-fetch-manifest.json']},scope='Four own explicitly selected committed-PLAN ends7 source controllers. Native objects are exact own commitments recovered by the actual literal recipe and scalar-native engines; no phase theorem, complete invoice or runtime bound is transferred. PR1152 is not included because its own generated-PLAN source interface requires a separate binding.')
(R/'selected-provider-dispatch-v13-inputs.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v12.py').read_text();s=s.replace('selected-provider-dispatch-v12','selected-provider-dispatch-v13')
s=s.replace("source_declared_meter_style='actual_initial_nonzero_frames'if declared==actual", "source_declared_meter_style='not_declared_in_own_expected'if declared is None else'actual_initial_nonzero_frames'if declared==actual")
s=s.replace('source_declared_counter_matches_actual=declared==actual','source_declared_counter_matches_actual=None if declared is None else declared==actual')
(R/'selected_provider_dispatch_v13.py').write_text(s,encoding='utf8')
print('PASS prepared',len(cohort),'own committed-PLAN ends7 sources; two exact selected native objects')
