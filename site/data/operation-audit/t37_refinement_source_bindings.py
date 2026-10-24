"""Own1009/1019 explicit source selection and complete942-component identity."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,tarfile,tempfile,shutil
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D='t37-source-refinement-cases';checks={};prefix=''
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):
 b=(R/p).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def identity(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(k,v):assert v,prefix+k;checks[prefix+k]=True
nativefile='pr942-finite-controller-native.json';native=rd(nativefile);plan=rd(native['numeric_plan_certificate']);inv=rd(native['invoice_certificate']);oldprovider=rd('t21-t37-cost-source/890-0f075414217e__SPEC.json')['providers'];members=rd(D+'/selected-archive-members.json');parent=rd(D+'/exact-parent-inputs.json');ar={a['member']:a for a in members};runtime=rd(ar['runtime/data/SPEC.json']['file']);owned=rd(ar['strict/global/audit/OWNERS-AND-PROFILE.json']['file']);histinvoice=rd(ar['strict/global/audit/PREFIX-AND-INVOICE.json']['file']);literalPLAN=ar['lift/PLAN.json'];actualspec=ar['runtime/data/SPEC.json']
ck('named942_native_theorem_closed',native['status'].startswith('closed_conditional')and native['pr']==942 and native['source_equivalent_numeric_realization']and not native['historical_PLAN_byte_identity_claimed'])
for group in ['source_sha256','dependency_hashes']:
 for path,h in native[group].items():ck('native_theorem_'+path,hs(path)==h)
ck('named_own_native_and_invoice_peers',rd('pr942-finite-controller-peer-review.json')['reviewed_sha256'][nativefile]==hs(nativefile)and rd('pr942-finite-controller-source-peer-review.json')['reviewed_sha256'][nativefile]==hs(nativefile))
for a in members:
 ck('exact_bound_archive_member_'+a['member'],hs(a['file'])==a['sha256']and hs(a['archive_file'])==a['archive_sha256'])
with tarfile.open(R/members[0]['archive_file'])as t:
 for a in members:ck('actual_archive_payload_'+a['member'],sha256(t.extractfile(a['member']).read()).hexdigest()==a['sha256'])
ck('complete_actual_provider_dictionary_identity',runtime['providers']==oldprovider)
ck('actual_historical_PLAN_commitment',hs(literalPLAN['file'])==runtime['data']['plan_sha256'])
helper=ar['runtime/code/generated_identity.py'];env={'__name__':'source_generated_identity'};exec(compile((R/helper['file']).read_bytes(),helper['file'],'exec'),env)
ck('actual_selected_source_identity_implementation',helper['sha256']=='c8af22719c0f3097a991a3f6ccac8f090afd2faba554745733d9ea88f2c25708')
for pid,p in runtime['providers'].items():
 for name,h in p['artifacts'].items():
  f='strict/global/base/providers/'+pid+'/'+name
  if f in ar:ck(pid+'_actual_declared_raw_'+name,hs(ar[f]['file'])==h)
 with tempfile.TemporaryDirectory(prefix='t37-identity-')as td:
  target=Path(td)
  for name in env['FILES']:
   f='strict/global/base/providers/'+pid+'/'+name;ck(pid+'_actual_semantic_payload_present_'+name,f in ar);shutil.copyfile(R/ar[f]['file'],target/name)
  ids=env['artifact_identities'](target)
  ck(pid+'_source_defined_semantic_identities',ids==p['artifact_semantic_sha256'])
 word=rd(ar['strict/global/base/providers/'+pid+'/LOCAL-PROGRAMS.json.gz']['file']);ck(pid+'_both_selected_orientations',{o:identity(v)for o,v in word.items()}==p['program_hashes']and identity(word)==native['selected_program_semantic_sha256'])
ck('actual_profile_live_physical_identity',runtime['expected']['global_profile']==native['invoice']['paid_profile']==owned['paid_profile']and runtime['expected']['live']==native['invoice']['live']==owned['live']and runtime['expected']['physical']==native['invoice']['physical']==owned['physical'])
parentmap={a['path']:a for a in parent};index=rd(next(a['file']for a in rd(D+'/1019-declared-inputs.json')if a['path'].endswith('SELECTED-SOURCE.json')))
ck('identity_helper_in_own_selected_inventory',index['files']['research/complex-sw4-frame8/code/generated_identity.py']==helper['sha256'])
for path,a in parentmap.items():
 ck('own_named_parent_primitive_'+path,a['declared_commit']=='8bddbee377e2f3ce1f1247196c4b290d55767d20'and hs(a['file'])==a['sha256']==index['files'][path]and a['sha256']in native['source_sha256'].values())
roles=rd(parentmap['research/complex-t37-owners/OWNERS.json.gz']['file']);order=rd(parentmap['research/complex-t37-owners/ORDER.json']['file'])
ck('actual_complete_owner_and_order_identity',identity(roles)==native['owners_content_sha256']==plan['owners_content_sha256']and order==plan['order'])
q={a['pr']:a for a in rd('remaining-record-audit/complete-audit-queue.json')['rows']};rows=[]
shareddeps=['t37-refinement-source-bindings.md',D+'/selected-archive-members.json',D+'/exact-parent-inputs.json',nativefile,native['numeric_plan_certificate'],native['invoice_certificate'],'pr942-finite-controller-peer-review.json','pr942-finite-controller-source-peer-review.json','t21-t37-cost-source/890-0f075414217e__SPEC.json']
for pr in [1009,1019]:
 prefix=str(pr)+'_';start=set(checks);mf=f'{D}/{pr}-manifest.json';dm=f'{D}/{pr}-declared-inputs.json';M=rd(mf);L=rd(dm);head=M[0]['own_head'];own={a['path']:a for a in M if a.get('file')};decl={a['path']:a for a in L};source={a['file']:a['sha256']for a in list(own.values())+L+members+parent};pin=rd(next(a['file']for a in own.values()if a['path'].endswith('SOURCES.json')));replayfile=f'{D}/{pr}-fresh-source-arithmetic.json';replay=rd(replayfile)
 ck('own_immutable_head',head==q[pr]['own_head_sha'])
 for a in own.values():ck('own_primary_'+a['path'],a['own_head']==head and hs(a['file'])==a['sha256']and '/'+head+'/'in a['primary_url'])
 for a in L:
  raw=(R/a['file']).read_bytes();trans=raw.replace(b'\r\n',b'\n')if a['declared_normalization']=='CRLF_to_LF'else raw;ck('actual_declared_input_'+a['path'],sha256(raw).hexdigest()==a['sha256']and (a['declared_pin']is None or sha256(trans).hexdigest()==a['declared_pin']))
 ck('actual_same_declared_baseline',pin['base_commit']=='8bddbee377e2f3ce1f1247196c4b290d55767d20')
 baseline=rd(decl['research/community-frontier942-audit/ASSEMBLY.json']['file']);ck('actual_selected_owner_invoice_binding',baseline['input_sha256']['owner_audit']==ar['strict/global/audit/OWNERS-AND-PROFILE.json']['sha256']and baseline['input_sha256']['fresh_invoice']==ar['strict/global/audit/PREFIX-AND-INVOICE.json']['sha256']and baseline['complex_profile']==native['invoice']['paid_profile'])
 ck('fresh_source_arithmetic_receipt',replay['returncode']==0 and replay['pr']==pr and replay['own_head']==head and replay['script_sha256']==hs('replay_t37_source_refinements.py')and all(hs(f)==h for f,h in replay['source_sha256'].items()))
 verifier=next(a['file']for a in own.values()if a['path'].endswith('verify.py'));vr=(R/verifier).read_text(encoding='utf8');certificate=rd(next(a['file']for a in L if a['path'].endswith('/CERTIFICATE.json')))
 if pr==1009:
  kappa=F(certificate['kappa']);ck('own_selected_bootstrap_variant',"RECEIPT = 'research/community-frontier942-audit/ASSEMBLY.json'"in vr and "ADAPTER = 'research/complex-t37-owners/prepare.py'"in vr and "candidate = original_outer_function(engine, c, 6)(b)"in vr and certificate['candidate_levels']==6 and certificate['original_levels']==7 and kappa==F(baseline['kappa'])and replay['unchanged_original_source_executed'])
  ck('own_PREPARE_exact_component',decl['research/complex-t37-owners/prepare.py']['sha256']==parentmap['research/complex-t37-owners/prepare.py']['sha256'])
 else:
  kappa=F(pin['refined_kappa']);committed=rd(next(a['file']for a in L if a['path'].endswith('research/t37-rational-refinement/ASSEMBLY.json')));ck('own_explicit_archive_runtime_selector',"spec_path=work/'runtime/data/SPEC.json'"in vr and "WITNESS_SPEC=str(work/'runtime/data/SPEC.json')"in vr and "ARCHIVE = 'research/community-frontier942-audit/t37-replay.tar.gz'"in vr)
  ck('own_exact_refined_target',kappa==F(committed['kappa'])==F(certificate['kappa'])==F(replay['refined_kappa'])and replay['all47_strict_constraints_pass']and not replay['full_876_source_inventory_replayed'])
  allowed={'kappa','kappa_decimal','gain_over_pr635_percent','conservative_kappa','conservative_kappa_decimal','conservative_outer','native_correction_gain','outer'};ck('own_original_supplier_and_input_bytes_unchanged',set(committed)==set(baseline)and {k for k in baseline if baseline[k]!=committed[k]}==allowed and committed['input_sha256']==baseline['input_sha256']and committed['complex_profile']==baseline['complex_profile'])
 ck('own_record_matches_frozen_metadata',kappa==F(q[pr]['quoted_kappa_fraction']))
 source.update({a['file']:a['sha256']for a in members+parent});source.update(replay['source_sha256']);source.update(native['source_sha256']);dep={f:hs(f)for f in shareddeps+[mf,dm,replayfile,'replay_t37_source_refinements.py']};dep.update(native['dependency_hashes'])
 rows.append(dict(pr=pr,own_head=head,kappa_record=str(kappa),selected_native_profile_sha256=identity(native['invoice']['paid_profile']),selected_program_semantic_sha256=native['selected_program_semantic_sha256'],selected_providers_dictionary_sha256=identity(runtime['providers']),selected_runtime_SPEC_file=actualspec['file'],selected_runtime_SPEC_sha256=actualspec['sha256'],selected_historical_PLAN_file=literalPLAN['file'],selected_historical_PLAN_sha256=literalPLAN['sha256'],own_owner_content_sha256=identity(roles),own_ORDER_sha256=parentmap['research/complex-t37-owners/ORDER.json']['sha256'],same_own_source_native_theorem_file=nativefile,same_own_source_native_theorem_sha256=hs(nativefile),same_source_numeric_plan_file=native['numeric_plan_certificate'],same_source_finite_invoice_file=native['invoice_certificate'],native_coordinate_rank=73,paid_profile=native['invoice']['paid_profile'],productive_live=native['invoice']['live'],physical_families=native['invoice']['physical'],native_same_complete_source_inputs=True,numerical_cutoff_transferred=False,historical_PLAN_metadata_byte_identity_claimed=False,full_original_native_or_phase_replayed_here=False,source_arithmetic_replay_file=replayfile,source_arithmetic_scope=replay['scope'],retained_contracts=native['retained_contracts'],source_sha256=source,dependency_hashes=dep,checks_passed=len(set(checks)-start),checks={k:v for k,v in checks.items()if k not in start}))
prefix='';ck('two_distinct_own_source_variants',len(rows)==2 and {a['pr']for a in rows}=={1009,1019})
out=dict(schema='own-T37-refinement-native-source-bindings/1',status='passed_own_source_selection_and_complete_component_identity',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name),scope='Actual own source selection and exact typed native/owners/order/invoice interface identity only; no new numerical cutoff or full engine theorem is created.')
(R/'t37-refinement-source-bindings.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own1009/1019 source/component identity checks')
