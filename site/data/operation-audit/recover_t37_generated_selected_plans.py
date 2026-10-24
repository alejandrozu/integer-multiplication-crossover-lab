"""Authenticate own1131/1152 complete source-generated PLANs; no runtime theorem."""
from pathlib import Path
from hashlib import sha1,sha256
from fractions import Fraction as F
import gzip,json,subprocess,sys
R=Path(__file__).resolve().parent;checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads(gzip.decompress((R/f).read_bytes())if f.endswith('.gz')else(R/f).read_bytes())
def ck(n,v):assert v,n;checks[n]=True
def blob(b):return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
hintproof='t37-refinement-source-bindings.json';hp=rd(hintproof);hrow=next(a for a in hp['rows']if a['pr']==1009);hint=hrow['selected_historical_PLAN_file'];runtime=hrow['selected_runtime_SPEC_file'];pp=rd('pr1009-selected-t37-gaussian-cost-peer-review.json')
ck('independent_exact_hint_source_binding',hp['status']=='passed_own_source_selection_and_complete_component_identity'and pp['review_status'].startswith('PASS')and pp['reviewed_sha256'][hintproof]==hs(hintproof)and hs(hint)==hrow['selected_historical_PLAN_sha256']and hs(runtime)==hrow['selected_runtime_SPEC_sha256']and rd(runtime)['data']['plan_sha256']==hs(hint))
pins={}
for k in['source_sha256','dependency_hashes']:
 for f,h in hrow.get(k,{}).items():ck('hint_primary_'+f,hs(f)==h);pins[f]=h
r=subprocess.run([sys.executable,'-X','utf8',str(R/'diagnose_t37_generated_plan_provenance.py')],cwd=R,capture_output=True,text=True,encoding='utf8',timeout=180);ck('fresh_exact_payload_reconstruction',r.returncode==0)
diag=rd('t37-generated-plan-provenance-diagnostic.json');ck('hint_exact_raw_bytes',diag['hint_file']==hint and diag['hint_file_sha256']==hs(hint))
own1131=rd('pr1131-constructor-source/source-manifest.json');shared=rd('ends7-own-selection-source/source-fetch-manifest.json');rows=[]
for pr,root,owner,plan in[(1131,'pr1131-constructor-source','selected-provider-dispatch-source/1131/18ab649f0e8b__OWNERS.json.gz','pr1131-constructor-source/derived/PLAN.json'),(1152,'ends7-own-selection-source/1152','ends7-own-selection-source/1152/data/OWNERS.json.gz','ends7-own-selection-source/1152/derived/PLAN.json')]:
 M=rd(root+'/MANIFEST.json');specf=root+'/data/SPEC.json';spec=rd(specf);order=root+'/data/ORDER.json';claimf=root+'/CLAIM.json';claim=rd(claimf);source={}
 if pr==1131:
  head=own1131['own_head'];listing=rd(root+'/-api.json');a=next(a for a in listing if a['name']=='MANIFEST.json');ck('own1131_immutable_API_manifest_blob',a['sha']==blob((R/(root+'/MANIFEST.json')).read_bytes()))
  for a in own1131['source_manifest']:
   raw=(R/a['file']).read_bytes();ck('own1131_source_'+a['relative'],a['own_head']==head and hs(a['file'])==a['sha256']and blob(raw)==a['api_sha']==a['git_blob_sha1']);source[a['file']]=a['sha256']
  source[root+'/-api.json']=hs(root+'/-api.json')
 else:
  actual=[a for a in shared if a['pr']==pr];head=next(a['own_head']for a in actual if a['path'].endswith('/MANIFEST.json'))
  for a in actual:
   raw=(R/a['file']).read_bytes();ck('own1152_source_'+a['path'],a['own_head']==head and hs(a['file'])==a['sha256']and blob(raw)==a['git_blob_sha1']and a['api_own_blob_verified']);source[a['file']]=a['sha256']
 for rel,f in[('prepare.py',root+'/prepare.py'),('controller.py',root+'/controller.py'),('verify.py',root+'/verify.py'),('common.py',root+'/common.py'),('CLAIM.json',claimf),('data/SPEC.json',specf),('data/ORDER.json',order),('data/OWNERS.json.gz',owner)]:ck(str(pr)+'_own_manifest_'+rel,M[rel]==hs(f));source[f]=hs(f)
 prep=(R/(root+'/prepare.py')).read_text();controller=(R/(root+'/controller.py')).read_text();verify=(R/(root+'/verify.py')).read_text()
 ck(str(pr)+'_actual_source_PLAN_SPEC_and_owner_selection',"spec=read(P/'data/SPEC.json')"in prep and"'plan_sha256':sha(lift/'PLAN.json')"in prep and"read(P/'data/OWNERS.json.gz')"in prep and"--plan',work/'lift/PLAN.json'"in controller and'import prepare,controller,price'in verify)
 p=rd(plan);o=rd(owner);d=next(a for a in diag['rows']if a['pr']==pr);matches=[a for a in d['tests']if a['exact_own_SPEC_matches']]
 ck(str(pr)+'_complete_exact_own_PLAN_byte_commitment',hs(plan)==spec['data']['plan_sha256']==d['own_SPEC_expected_PLAN_sha256']and len(matches)==1 and matches[0]['parent_digest_hint_used']and not matches[0]['schedule_digest_hint_used'])
 ck(str(pr)+'_own_complete_physical_fields',hs(owner)==spec['data']['owners_sha256']and len(o)==159840 and p['order']==rd(order)==spec['call_order']and p['profile']==claim['complex_profile']and sum(int(k)*v for k,v in p['profile'].items())==73*p['live']-11840 and len(p['provider_calls'])==333)
 ck(str(pr)+'_actual_own_target_and_profile_pointer',F(claim['kappa'])==F(spec['expected']['kappa'])and p['profile']==spec['expected']['global_profile'])
 ck(str(pr)+'_only_opaque_parent_digest_restored',p['replica_lift']['parent_template_content_sha256']==rd(hint)['replica_lift']['parent_template_content_sha256'])
 rows.append(dict(pr=pr,own_head=head,own_MANIFEST_file=root+'/MANIFEST.json',own_MANIFEST_sha256=hs(root+'/MANIFEST.json'),own_SPEC_file=specf,own_SPEC_sha256=hs(specf),own_prepare_file=root+'/prepare.py',own_prepare_sha256=hs(root+'/prepare.py'),own_controller_file=root+'/controller.py',own_controller_sha256=hs(root+'/controller.py'),PLAN_file=plan,PLAN_sha256=hs(plan),own_SPEC_expected_PLAN_sha256=spec['data']['plan_sha256'],OWNERS_file=owner,OWNERS_sha256=hs(owner),ORDER_file=order,ORDER_sha256=hs(order),CLAIM_file=claimf,CLAIM_sha256=hs(claimf),kappa_record=claim['kappa'],recovery_method='source_defined_complete_numeric_fields_plus_public_opaque_parent_provenance_literal_then_exact_own_full_payload_commitment',opaque_parent_metadata_hint_file=hint,opaque_parent_metadata_hint_sha256=hs(hint),historical_parent_template_byte_identity_claimed=False,source_equivalent_numeric_parent_still_requires_fresh_cost_and_semantic_census=True,original_full_global_verifier_PASS_claimed=False,whole_integer_upper_claimed=False,source_sha256=source))
deps=['t37-generated-selected-plan-recovery.md','diagnose_t37_generated_plan_provenance.py','t37-generated-plan-provenance-diagnostic.json','recover_pr1131_selected_plan.py','pr1131-constructor-source/source-manifest.json','pr1131-constructor-source/dependencies/manifest.json','ends7-own-selection-source/source-fetch-manifest.json',hintproof,'pr1009-selected-t37-gaussian-cost-peer-review.json'];dep={f:hs(f)for f in deps};dep.update(pins)
out=dict(schema='own-T37-source-generated-selected-PLAN-recovery/1',status='closed_exact_own_SPEC_PLAN_byte_recovery',rows=rows,checks=checks,checks_passed=len(checks),whole_integer_upper_claimed=False,native_operator_or_phase_proved=False,historical_parent_template_byte_identity_claimed=False,original_full_global_verifier_PASS_claimed=False,dependency_hashes=dep,script_sha256=hs(Path(__file__).name))
(R/'t37-generated-selected-plan-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own1131/1152 complete selected PLAN recovery checks')
