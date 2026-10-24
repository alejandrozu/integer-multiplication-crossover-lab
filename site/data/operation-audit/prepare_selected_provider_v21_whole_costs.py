"""Four own joint-entrance finite costs; no prior invoice or cutoff transfer."""
from pathlib import Path
A=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
s=(A/'selected_provider_v17_whole_bounds.py').read_text().replace('Own six K492 mixed','Own four joint-entrance').replace('REVIEW_CLOSED=True',f'REVIEW_CLOSED={COST_REVIEW_CLOSED}')
s=s.replace('ADMITTED={636,638,639,640,642,644}','ADMITTED={1148,1169,1183,1192}').replace('v17','v21').replace('k492-mixed-finite','joint-entrance-finite')
s=s.replace('import ast,hashlib,importlib.util,json,sys','import ast,gzip,hashlib,importlib.util,json,sys')
a=s.index("fast=rd('late-cold-mixed-native-fast-offline-verification.json')");b=s.index("review=rd('selected-provider-review-evidence-screen.json');",a)
s=s[:a]+'''recovery_files=['joint-entrance-selected-native-recovery.json','joint-entrance-extra-selected-native-recovery.json'];recovery_objects={}
for recfile,producer in zip(recovery_files,['recover_joint_entrance_selected_native.py','recover_joint_entrance_extra_native.py']):
    rec=rd(recfile);ck('closed_actual_native_recovery_'+recfile,all(rec['checks'].values())and rec['script_sha256']==hs(producer))
    for key in ['source_sha256','dependency_hashes']:
        for f,h in rec[key].items():ck('actual_native_source_'+f,hs(f)==h)
    for artifact in rec['outputs']:
        ck('actual_native_output_'+artifact['file'],hs(artifact['file'])==artifact['sha256']);recovery_objects[artifact['file']]=artifact
'''+s[b:]
s=s.replace('late-cold-mixed-descriptive-counter-audit','joint-entrance-descriptive-counter-audit').replace('late_cold_mixed_descriptive_counter_audit','joint_entrance_descriptive_counter_audit')
a=s.index("    selector_file=f'selected-provider-dispatch-v21-source/");b=s.index("    for kind,a in cr['own_physical_artifacts'].items():",a)
s=s[:a]+'''    selector_file=f'selected-provider-dispatch-v21-source/{pr}/actual-own-selector.json';selector=rd(selector_file);ownM=selector['MANIFEST_file'];M=rd(ownM);ownV=selector['verifier_file'];v=(R/ownV).read_text();ownfiles={a['relative']:a for a in selector['verified_primary']}
    ck('own_literal_MANIFEST_verifier_claim_selection',selector['own_head']==cr['own_head']and hs(ownM)==selector['MANIFEST_sha256']and hs(ownV)==M['verify.py']==selector['verifier_sha256']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['SPEC.json']and hs(selector['claim_file'])==selector['claim_sha256']and F(rd(selector['claim_file'])['kappa'])==F(cr['kappa_record'])==F(ownspec['expected']['kappa'])and sorted(ownspec['providers'])==selector['selected_provider_names'])
    for a in selector['verified_primary']:
        payload=(R/a['file']).read_bytes();blob=hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\\0'+payload).hexdigest()
        ck('own_primary_'+a['file'],a['own_head']==entry['own_head']and hs(a['file'])==a['sha256']and blob==a['git_blob_sha1']==a['own_API_git_blob_sha1']and(a['relative']=='MANIFEST.json'or M[a['relative']]==a['sha256']));primary[a['file']]=a['sha256']
    primary[selector_file]=hs(selector_file)
    if pr==1148:
        ck('own_verifier_exact_PLAN_gzip_decompression',"(data/'PLAN.json').write_bytes(gzip.decompress((P/'PLAN.json.gz').read_bytes()))"in v and "for name in ('OWNERS.json.gz','SPEC.json')"in v and gzip.decompress((R/ownfiles['PLAN.json.gz']['file']).read_bytes())==(R/cr['own_physical_artifacts']['PLAN']['file']).read_bytes())
    else:
        ck('own_verifier_complete_own_data_overlays',"t.extractall(layout,filter='data')"in v and "'PLAN.json'"in v and "'SPEC.json'"in v and "'OWNERS.json.gz'"in v and M['PLAN.json']==hs(cr['own_physical_artifacts']['PLAN']['file']))
    ck('both_mixed_selected_providers_mandatory',set(ownspec['providers'])==({'gauge44','extra'}if pr in {1183,1192}else{'gauge44'}))
    for recfile,h in selector['native_recovery_files'].items():ck('own_native_recovery_'+recfile,recfile in recovery_files and hs(recfile)==h)
    ck('own_MANIFEST_actual_OWNERS',M['OWNERS.json.gz']==hs(cr['own_physical_artifacts']['OWNERS']['file'])==ownspec['data']['owners_sha256'])
'''+s[b:]
s=s.replace("hs(a['file'])==a['sha256']==a['own_SPEC_expected_sha256']","hs(a['file'])==a['sha256']==ownspec['data'][kind.lower()+'_sha256']")
s=s.replace("        ck(n['provider']+'_actual_canonical_required'", "        ck(n['provider']+'_actual_recovered_native_objects',n['program_file']in recovery_objects and n['canonical_file']in recovery_objects)\n        ck(n['provider']+'_actual_canonical_required'")
s=s.replace("    fallback=32*m*m*sum(P.values());", "    ck('own_complete_invocation_and_payload',role['roles']==(69120 if pr==1148 else 159840)and role['calls']==(144 if pr==1148 else 333)and role['charged_prefix_bits']==(512 if pr==1148 else 1024)and role['row_prefix_extra']==(1024 if pr==1148 else 2048))\n    fallback=32*m*m*sum(P.values());")
a=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'");b=s.index("    dep={p:hs(p)for p in deps};dep.update(cached)",a)
s=s[:a]+'''    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v21.py','prepare_selected_provider_v21_whole_costs.py','selected_provider_v17_whole_bounds.py','selected-provider-v17-whole-upper.md','joint-entrance-own-selection-source/source-manifest.json','joint-entrance-native-source/native-source-closure.json','joint-entrance-selected-native-recovery.json','joint-entrance-extra-selected-native-recovery.json','recover_joint_entrance_selected_native.py','recover_joint_entrance_extra_native.py','joint-entrance-descriptive-counter-audit.md','joint-entrance-descriptive-counter-audit.json','joint_entrance_descriptive_counter_audit.py']
'''+s[b:]
s=s.replace("ck('exact_six_own_selected_K492_packages'","ck('exact_four_own_selected_joint_entrance_packages'")
assert 'late-cold-mixed'not in s and 'fast['not in s
(A/'selected_provider_v21_whole_bounds.py').write_text(s,encoding='utf8')
a=(A/'generated_u8_t37_descriptive_counter_audit.py').read_text().replace('v19','v21').replace('generated-U8-t37','joint-entrance').replace('generated_u8_t37','joint_entrance').replace('These two own SPECs','These four own SPECs')
(A/'joint_entrance_descriptive_counter_audit.py').write_text(a,encoding='utf8')
print('Prepared four own joint-entrance whole instances; closed=',COST_REVIEW_CLOSED)
