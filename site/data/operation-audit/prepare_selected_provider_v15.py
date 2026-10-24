"""Bind two own committed ends7 owner-exchange selections, without V13 changes."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import copy,json,shutil
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
IDS={1150,1172};old=rd('selected-provider-dispatch-v10-inputs.json');selection=rd('ends7-exchange-own-selection-source/source-fetch-manifest.json');recovery=rd('pr1104-exact-selected-ends7-native-recovery.json')
assert recovery['script_sha256']==hs('recover_pr1104_ends7_selected_native.py')and all(recovery['checks'].values())and recovery['original_own_raw_constructor_replayed']and not recovery['full_operator_or_absolute_phase_replayed']
sources=[]
for a in recovery['outputs']:
 if a['file'].rsplit('/',1)[-1]in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']:
  assert hs(a['file'])==a['sha256'];sources.append(dict(file=a['file'],sha256=a['sha256'],origin='actual_own_literal_recipe_native_engines_exact_selected_bytes',primary=a))
assert len(sources)==2
cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS];assert {x['pr']for x in cohort}==IDS
D=R/'selected-provider-dispatch-v15-source';D.mkdir(exist_ok=True)
for row in cohort:
 pr=row['pr'];out=D/str(pr);out.mkdir(exist_ok=True);files=[a for a in selection if a['pr']==pr];M=next(a for a in files if a['path'].endswith('/MANIFEST.json'));root=M['path'].removesuffix('/MANIFEST.json');mf=rd(M['file']);assert M['api_own_blob_verified']
 assert all(a['own_head']==row['own_head']and hs(a['file'])==a['sha256']for a in files)
 for a in files:
  rel=a['path'].removeprefix(root+'/')
  if rel!='MANIFEST.json':assert mf[rel]==a['sha256']
 selected=next(a for a in files if a['path'].endswith('/data/SPEC.json'));spec=rd(selected['file'])
 assert F(spec['expected']['kappa'])==F(next(a['quoted_kappa_fraction']for a in old['claim_metadata']if a['pr']==pr))
 if pr==1150:
  source=rd('ends7-exchange-own-selection-source/1150/SOURCE.json');parentM='ends7-own-selection-source/1104/MANIFEST.json';parentV='ends7-own-selection-source/1104/verify_t16.py';v=(R/'ends7-exchange-own-selection-source/1150/verify.py').read_text()
  assert source['pr']==1104 and source['head']=='d8982686afd7ef6ce52ddeaa17011ccda558d666'and source['manifest_sha256']==hs(parentM)and source['files']==rd(parentM)
  assert source['files']['verify_t16.py']==hs(parentV)and"for name in ('OWNERS.json.gz','PLAN.json','SPEC.json'):"in v and"shutil.copyfile(P/'data'/name,source/'data'/name)"in v and"source/'verify_t16.py'"in v
  authority=dict(kind='own_verified_SOURCE_exact_manifest_to_unchanged1104_strict_selector_then_own_three_data_overlays',source_file='ends7-exchange-own-selection-source/1150/SOURCE.json',source_sha256=hs('ends7-exchange-own-selection-source/1150/SOURCE.json'),parent_manifest_file=parentM,parent_manifest_sha256=hs(parentM),parent_verifier_file=parentV,parent_verifier_sha256=hs(parentV),upstream_archive_bytes_or_original_whole_replay_claimed=False)
 else:
  V=next(a for a in files if a['path'].endswith('/verify_t16.py'));v=(R/V['file']).read_text();assert mf['verify_t16.py']==V['sha256']and"SPEC8, SPEC16 = PKG / 'data/SPEC-T8.json', PKG / 'data/SPEC.json'"in v and"--plan', PKG / 'data/PLAN.json'"in v and"--owners', PKG / 'data/OWNERS.json.gz'"in v
  authority=dict(kind='own_manifest_and_literal_strict_selector',verifier=V)
 assert spec['data']==dict(plan_sha256=mf['data/PLAN.json'],owners_sha256=mf['data/OWNERS.json.gz'])
 assert spec['providers']['gauge44']['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']==recovery['selected_program_semantic_sha256']and spec['providers']['gauge44']['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']==recovery['selected_canonical_semantic_sha256']and spec['providers']['gauge44']['program_hashes']==recovery['orientation_hashes']
 for kind in ['PLAN','OWNERS']:
  f=f'selected-provider-dispatch-v10-source/{pr}/{kind}.json';a=rd(f);assert a['status']=='authenticated_own_SPEC_declared_bytes'and hs(a['file'])==a['sha256']==spec['data'][kind.lower()+'_sha256'];shutil.copyfile(R/f,out/(kind+'.json'))
 matches=[a for a in row['verified_components']if a.get('path','').endswith('/data/SPEC.json')and a['sha256']==selected['sha256']];assert len(matches)==1;matches[0]['file']=selected['file']
 (out/'actual-own-selector.json').write_text(json.dumps(dict(pr=pr,own_head=row['own_head'],SPEC_file=selected['file'],SPEC_sha256=selected['sha256'],MANIFEST=M,own_source_authority=authority,verified_primary=files,own_selected_committed_PLAN=True,own_selected_full_native_commitments_checked=True,original_full_global_verifier_PASS_claimed=False),indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v13.py','pr1104-exact-selected-ends7-native-recovery.json','ends7-exchange-own-selection-source/source-fetch-manifest.json','ends7-own-selection-source/1104/MANIFEST.json','ends7-own-selection-source/1104/verify_t16.py']
snapshot=dict(schema='selected-provider-dispatch-frozen-inputs/15',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=sources,original_input_sha256={f:hs(f)for f in deps},scope='Two own source-selected committed-PLAN ends7 owner exchanges. PR1150 explicitly names the exact1104 manifest and unchanged strict selector then replaces only own SPEC/PLAN/OWNERS. PR1172 own manifest and literal selector name its own data. Each own full native commitment and every complete physical/owner/invoice field is freshly checked. No earlier invoice, numerical bound or original whole-verifier PASS is transferred.')
(R/'selected-provider-dispatch-v15-inputs.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v13.py').read_text().replace('selected-provider-dispatch-v13','selected-provider-dispatch-v15')
s=s.replace('if args.refresh_inputs or not snapshot.exists():',"if args.refresh_inputs or not snapshot.exists():\n    raise ValueError('V15 requires frozen own-source preparation; no mutable discovery refresh')")
s=s.replace('snap=rd(snapshot);ledger=',"snap=rd(snapshot)\nfor f,h in snap['original_input_sha256'].items():require(hs(R/f)==h,'frozen V15 source/dependency SHA '+f)\nledger=")
s=s.replace('source_equivalent_numeric_parent=True,historical_parent_byte_identity_claimed=False',"source_equivalent_numeric_parent=True,own_source_selector_file=(D/str(pr)/'actual-own-selector.json').relative_to(R).as_posix(),own_source_selector_sha256=hs(D/str(pr)/'actual-own-selector.json'),original_full_global_verifier_PASS_claimed=False,historical_parent_byte_identity_claimed=False")
(R/'selected_provider_dispatch_v15.py').write_text(s,encoding='utf8');print('PASS prepared 2 distinct own-source owner exchanges')
