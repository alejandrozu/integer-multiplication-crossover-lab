"""Prepare two own source-generated T37 PLANs for fresh physical censuses.

This is a new snapshot. It does not edit the frozen V13 committed-PLAN batch.
The full recovered PLAN bytes must equal each own SPEC's exact SHA; the opaque
historical parent digest is not treated as a claim about the newly built parent.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import copy,gzip,json
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads(gzip.decompress((R/f).read_bytes())if f.endswith('.gz')else(R/f).read_bytes())
IDS={1131,1152};old=rd('selected-provider-dispatch-v10-inputs.json')
recovery=rd('t37-generated-selected-plan-recovery.json')
assert recovery['status']=='closed_exact_own_SPEC_PLAN_byte_recovery' and recovery['checks_passed']==203 and all(recovery['checks'].values())
assert recovery['script_sha256']==hs('recover_t37_generated_selected_plans.py')
for f,h in recovery['dependency_hashes'].items():assert hs(f)==h,f
cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS];assert {x['pr']for x in cohort}==IDS
D=R/'selected-provider-dispatch-v14-source';D.mkdir(exist_ok=True)
sources=[]
for folder,receipt in [('r480-selected-recovery-source','r480-selected-native-recovery.json'),('pr1104-recovered-ends7-native','pr1104-exact-selected-ends7-native-recovery.json')]:
 rec=rd(receipt)
 if folder.startswith('r480'):
  payloads=[dict(file=f,sha256=h)for f,h in rec['source_sha256'].items()if f.startswith(folder+'/')and f.endswith(('__CANONICAL-WORD.json.gz','__LOCAL-PROGRAMS.json.gz'))]
 else:payloads=[x for x in rec['outputs']if x['file'].rsplit('/',1)[-1]in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']]
 assert len(payloads)==2
 for a in payloads:
  assert hs(a['file'])==a['sha256'];sources.append(dict(file=a['file'],sha256=a['sha256'],origin='actual_selected_bytes_rechecked_against_each_own_SPEC',primary=dict(recovery_receipt=receipt,recovery_receipt_sha256=hs(receipt),payload=a)))
for row in cohort:
 pr=row['pr'];z=next(a for a in recovery['rows']if a['pr']==pr);out=D/str(pr);out.mkdir(exist_ok=True)
 assert row['own_head']==z['own_head'];spec=rd(z['own_SPEC_file']);M=rd(z['own_MANIFEST_file'])
 assert F(z['kappa_record'])==F(spec['expected']['kappa'])
 for f,h in z['source_sha256'].items():assert hs(f)==h,f
 assert hs(z['own_SPEC_file'])==M['data/SPEC.json']==z['own_SPEC_sha256']
 match=[a for a in row['verified_components']if a.get('path','').endswith('/data/SPEC.json')and a['sha256']==z['own_SPEC_sha256']];assert len(match)==1
 match[0]['file']=z['own_SPEC_file']
 for kind,key in [('PLAN','plan_sha256'),('OWNERS','owners_sha256')]:
  f=z[kind+'_file'];want=spec['data'][key];assert hs(f)==want==z[kind+'_sha256']
  art=dict(pr=pr,own_head=z['own_head'],file=f,sha256=want,bytes=(R/f).stat().st_size,own_SPEC_expected_sha256=want,status='authenticated_own_SPEC_source_generated_selected_bytes'if kind=='PLAN'else'authenticated_own_SPEC_declared_bytes',source_selection_receipt='t37-generated-selected-plan-recovery.json',source_selection_receipt_sha256=hs('t37-generated-selected-plan-recovery.json'),historical_parent_template_byte_identity_claimed=False,original_full_global_verifier_PASS_claimed=False)
  (out/(kind+'.json')).write_text(json.dumps(art,indent=2)+'\n',encoding='utf8')
 selector=dict(pr=pr,own_head=z['own_head'],SPEC_file=z['own_SPEC_file'],SPEC_sha256=z['own_SPEC_sha256'],MANIFEST_file=z['own_MANIFEST_file'],MANIFEST_sha256=z['own_MANIFEST_sha256'],prepare_file=z['own_prepare_file'],prepare_sha256=z['own_prepare_sha256'],controller_file=z['own_controller_file'],controller_sha256=z['own_controller_sha256'],PLAN_file=z['PLAN_file'],PLAN_sha256=z['PLAN_sha256'],OWNERS_file=z['OWNERS_file'],OWNERS_sha256=z['OWNERS_sha256'],full_source_binding=z['source_sha256'],source_recovery_receipt='t37-generated-selected-plan-recovery.json',source_recovery_receipt_sha256=hs('t37-generated-selected-plan-recovery.json'),own_selected_source_generated_PLAN=True,complete_own_PLAN_byte_commitment_checked=True,original_full_global_verifier_PASS_claimed=False,historical_parent_template_byte_identity_claimed=False)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v13.py','t37-generated-selected-plan-recovery.json','recover_t37_generated_selected_plans.py','t37-generated-selected-plan-recovery.md','r480-selected-native-recovery.json','pr1104-exact-selected-ends7-native-recovery.json']
snapshot=dict(schema='selected-provider-dispatch-frozen-inputs/14',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=sources,own_source_generated_plan_recovery=dict(file='t37-generated-selected-plan-recovery.json',sha256=hs('t37-generated-selected-plan-recovery.json')),original_input_sha256={f:hs(f)for f in deps},scope='Two own selected source-generated T37 controllers. Each complete PLAN matches the exact own SPEC commitment after recovery of one publicly authenticated opaque provenance string. That string does not assert the newly built parent has historical byte identity. Fresh actual native/physical/owner/window/complete invoice checks are mandatory; no native operator theorem, original global PASS, prior invoice or numerical bound is transferred.')
(R/'selected-provider-dispatch-v14-inputs.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v13.py').read_text();s=s.replace('selected-provider-dispatch-v13','selected-provider-dispatch-v14')
s=s.replace("if args.refresh_inputs or not snapshot.exists():","if args.refresh_inputs or not snapshot.exists():\n    raise ValueError('V14 requires its frozen own-source preparation; mutable discovery refresh is forbidden')")
s=s.replace("snap=rd(snapshot);ledger=", "snap=rd(snapshot)\nfor f,h in snap['original_input_sha256'].items():require(hs(R/f)==h,'frozen V14 source/dependency SHA '+f)\nrecovery=rd(R/snap['own_source_generated_plan_recovery']['file']);require(recovery['checks_passed']==203 and all(recovery['checks'].values()),'own complete PLAN source recovery')\nledger=")
s=s.replace("r.get('status')=='authenticated_own_SPEC_declared_bytes'and", "r.get('status')in ['authenticated_own_SPEC_declared_bytes','authenticated_own_SPEC_source_generated_selected_bytes']and")
s=s.replace("source_equivalent_numeric_parent=True,historical_parent_byte_identity_claimed=False", "source_equivalent_numeric_parent=True,own_source_generated_PLAN_recovery=snap['own_source_generated_plan_recovery'],own_source_selector_file=(D/str(pr)/'actual-own-selector.json').relative_to(R).as_posix(),own_source_selector_sha256=hs(D/str(pr)/'actual-own-selector.json'),original_full_global_verifier_PASS_claimed=False,historical_parent_byte_identity_claimed=False")
(R/'selected_provider_dispatch_v14.py').write_text(s,encoding='utf8')
print('PASS prepared 2 own source-generated exact PLANs and 4 actual native byte objects')
