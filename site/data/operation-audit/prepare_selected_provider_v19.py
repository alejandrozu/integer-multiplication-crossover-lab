"""Own962/991 exact source-generated semantic data, not another T37 invoice."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import copy,gzip,json
A=Path(__file__).resolve().parent
def hs(f):return sha256((A/f).read_bytes()).hexdigest()
def rd(f):return json.loads(gzip.decompress((A/f).read_bytes())if f.endswith('.gz')else(A/f).read_bytes())
IDS={962,991};old=rd('selected-provider-dispatch-v10-inputs.json');recovery=rd('u8-t37-generated-data-recovery.json');inventory=rd('u8-t37-generated-source/manifest.json')
assert recovery['status']=='checked_exact_own_source_generated_PLAN_OWNER_semantics'and all(recovery['checks'].values())and recovery['script_sha256']==hs('recover_u8_t37_generated_data.py')
for k in['source_sha256','dependency_hashes']:
 for f,h in recovery[k].items():assert hs(f)==h,f
cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS];assert {x['pr']for x in cohort}==IDS
D=A/'selected-provider-dispatch-v19-source';D.mkdir(exist_ok=True)
native=rd('u8-exact-earlier-selected-byte-recovery.json');sources=[]
for x in native['outputs']:
 if x['file'].rsplit('/',1)[-1]in['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']:
  assert hs(x['file'])==x['sha256'];sources.append(dict(file=x['file'],sha256=x['sha256'],origin='actual_byteobject_matches_each_own_full_semantic_and_orientation_commitments',primary=dict(recovery_receipt='u8-exact-earlier-selected-byte-recovery.json',recovery_receipt_sha256=hs('u8-exact-earlier-selected-byte-recovery.json'),payload=x)))
assert len(sources)==2
for row in cohort:
 pr=row['pr'];z=next(r for r in recovery['rows']if r['pr']==pr);original=rd(z['own_SPEC_file']);runtime=rd(z['runtime_SPEC_file']);M=rd(z['own_MANIFEST_file']);inv=next(r for r in inventory['rows']if r['pr']==pr);out=D/str(pr);out.mkdir(exist_ok=True)
 assert row['own_head']==z['own_head']==inv['own_head']and hs(z['own_SPEC_file'])==M['data/SPEC.json']==z['own_SPEC_sha256']and hs(z['runtime_SPEC_file'])==z['runtime_SPEC_sha256']
 expected=copy.deepcopy(original);expected['data']['plan_sha256']=z['PLAN_sha256'];expected['data']['owners_sha256']=z['OWNERS_sha256'];assert runtime==expected and F(runtime['expected']['kappa'])==F(original['expected']['kappa'])
 component=[x for x in row['verified_components']if x.get('path','').endswith('/data/SPEC.json')and x['sha256']==z['own_SPEC_sha256']];assert len(component)==1
 component[0].update(file=z['runtime_SPEC_file'],sha256=z['runtime_SPEC_sha256'],origin='own_actual_runtime_spec_authorized_raw_container_rebinding',original_primary_SPEC_file=z['own_SPEC_file'],original_primary_SPEC_sha256=z['own_SPEC_sha256'])
 for kind,f,want in [('PLAN',z['selected_PLAN_file'],runtime['data']['plan_sha256']),('OWNERS',z['OWNERS_file'],runtime['data']['owners_sha256'])]:
  assert hs(f)==want
  art=dict(pr=pr,own_head=z['own_head'],file=f,sha256=want,bytes=(A/f).stat().st_size,own_SPEC_expected_sha256=want,status='authenticated_own_SPEC_source_generated_selected_bytes',source_selection_receipt='u8-t37-generated-data-recovery.json',source_selection_receipt_sha256=hs('u8-t37-generated-data-recovery.json'),own_original_raw_digest=original['data']['plan_sha256'if kind=='PLAN'else'owners_sha256'],full_own_mathematical_semantic_commitment_exact=True,only_own_runtime_spec_authorized_container_digest_rebound=True,original_full_global_verifier_PASS_claimed=False)
  (out/(kind+'.json')).write_text(json.dumps(art,indent=2)+'\n')
 selector=dict(pr=pr,own_head=z['own_head'],MANIFEST_file=z['own_MANIFEST_file'],MANIFEST_sha256=z['own_MANIFEST_sha256'],original_SPEC_file=z['own_SPEC_file'],original_SPEC_sha256=z['own_SPEC_sha256'],runtime_SPEC_file=z['runtime_SPEC_file'],runtime_SPEC_sha256=z['runtime_SPEC_sha256'],verifier_file=z['own_verifier_file'],owner_constructor_file=z['own_owner_constructor_file'],parent_constructor_file=z['own_parent_constructor_file'],PLAN_file=z['selected_PLAN_file'],PLAN_sha256=z['PLAN_sha256'],OWNERS_file=z['OWNERS_file'],OWNERS_sha256=z['OWNERS_sha256'],verified_primary=inv['files'],source_recovery_receipt='u8-t37-generated-data-recovery.json',source_recovery_receipt_sha256=hs('u8-t37-generated-data-recovery.json'),full_own_PLAN_OWNER_semantic_commitments_exact=True,actual_own_runtime_spec_portability_authorized=True,complete_original_global_verifier_PASS_claimed=False)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v14.py','prepare_selected_provider_v19.py','u8-t37-generated-data-recovery.json','recover_u8_t37_generated_data.py','u8-t37-generated-data-recovery.md','u8-t37-generated-source/manifest.json','u8-exact-earlier-selected-byte-recovery.json']
snapshot=dict(schema='selected-provider-dispatch-frozen-inputs/19',cohort_rows=cohort,claim_metadata=[x for x in old['claim_metadata']if x['pr']in IDS],actual_native_archive_sources=sources,own_source_generated_plan_recovery=dict(file='u8-t37-generated-data-recovery.json',sha256=hs('u8-t37-generated-data-recovery.json')),original_input_sha256={f:hs(f)for f in deps},scope='Own962/991 source-selected generated data. Full own mathematical PLAN and OWNER commitments are exact under each actual own verifier semantic portability route; only raw container digests are rebound. Original source bodies and complete parent7db payload are recovered, without an opaque hint or source invoice transfer. Fresh own complete role/program/invoice checks remain mandatory; no global verifier/operator/phase PASS is claimed.')
(A/'selected-provider-dispatch-v19-inputs.json').write_text(json.dumps(snapshot,indent=2)+'\n')
s=(A/'selected_provider_dispatch_v14.py').read_text().replace('selected-provider-dispatch-v14','selected-provider-dispatch-v19')
s=s.replace("recovery['checks_passed']==203 and all(recovery['checks'].values())","recovery['status']=='checked_exact_own_source_generated_PLAN_OWNER_semantics'and all(recovery['checks'].values())")
(A/'selected_provider_dispatch_v19.py').write_text(s,encoding='utf8');print('PASS own962/991 actual source semantic portability preparation')
