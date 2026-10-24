"""A new own582/584 instance of the frozen finite Gaussian cost arithmetic."""
from pathlib import Path
R=Path(__file__).resolve().parent
COST_REVIEW_CLOSED=True
s=(R/'selected_provider_v17_whole_bounds.py').read_text()
s=s.replace('Own six K492 mixed','Own two early frame-coalescence').replace('ADMITTED={636,638,639,640,642,644}','ADMITTED={582,584}').replace('REVIEW_CLOSED=True',f'REVIEW_CLOSED={COST_REVIEW_CLOSED}')
s=s.replace('import ast,hashlib,importlib.util,json,sys','import ast,gzip,hashlib,importlib.util,json,sys').replace('v17','v22').replace('k492-mixed-finite','early-frame-finite')
a=s.index("fast=rd('late-cold-mixed-native-fast-offline-verification.json')");b=s.index("review=rd('selected-provider-review-evidence-screen.json');",a)
s=s[:a]+"""recovery=rd('cold14-typed-chain-native-byte-recovery.json')
ck('actual_typed_RAW_native_recovery',recovery['status']=='passed_actual_typed_constructors_scalar_native_wrappers'and recovery['script_sha256']==hs('recover_cold14_chain_native_bytes.py'))
for f,h in recovery['source_sha256'].items():ck('executed_native_source_'+f,hs(f)==h)
for f,h in recovery['dependency_hashes'].items():ck('executed_native_dependency_'+f,hs(f)==h)
for f,h in recovery['retained_base_sha256'].items():ck('actual_retained_base_payload_'+f,hs(f)==h)
"""+s[b:]
a=s.index("meter_audit=rd('late-cold-mixed-descriptive-counter-audit.json')");b=s.index('rows=[]',a);s=s[:a]+s[b:]
a=s.index("    ck('actual_entry_meter_source_value_and_cost_noninterference'");b=s.index("    for kind,a in cr['own_physical_artifacts'].items():",a)
s=s[:a]+'''    meter=cr['descriptive_entering_counter']
    ck('actual_source_entry_meter_matches',meter['source_declared_entering_helper_roles']==meter['actual_nonzero_start_frame_roles']==meter['width_below_9_roles']and meter['source_declared_counter_matches_actual']is True and not meter['used_by_new_cost_stock_or_precision'])
    selector_file=f'selected-provider-dispatch-v22-source/{pr}/actual-own-selector.json';selector=rd(selector_file);M=rd(selector['MANIFEST_file']);v=(R/selector['verifier_file']).read_text()
    ck('own_actual_MANIFEST_and_literal_selector',selector['own_head']==cr['own_head']and selector['SPEC_sha256']==cr['own_SPEC_sha256']==M['data/SPEC.json']and hs(selector['MANIFEST_file'])==selector['MANIFEST_sha256']and M['verify.py']==hs(selector['verifier_file'])==selector['verifier_sha256']and selector['actual_own_literal_SPEC_build_native_PLAN_OWNERS_selection']and selector['own_complete_external_source_specs_equal_executed_closure']and not selector['original_own_complete_constructor_or_global_verifier_PASS_claimed'])
    ck('own_literal_SPEC_and_complete_dispatch_authority',"SPECFILE=a.spec.resolve();SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v and "futures={pid:pool.submit(provider,pid)for pid in sorted(BUILD['providers'])}"in v and "'--plan',P/'data/PLAN.json'"in v and "'--owners',P/'data/OWNERS.json.gz'"in v and F(ownspec['expected']['kappa'])==F(cr['kappa_record']))
    primary[selector_file]=hs(selector_file)
    actual_API={}
    for f,h in selector['primary_changed_file_API_sha256'].items():
        ck('actual_own_changed_file_API_'+f,hs(f)==h);primary[f]=h
        actual_API.update({a['filename']:a['sha']for a in json.loads(gzip.decompress((R/f).read_bytes()))})
    for a in selector['verified_primary']:
        payload=(R/a['file']).read_bytes();blob=hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\\0'+payload).hexdigest()
        ck('own_primary_'+a['file'],a['own_head']==entry['own_head']and hs(a['file'])==a['sha256']and blob==a['git_blob_sha1']==a['own_API_git_blob_sha1']==actual_API[a['path']]and entry['own_head']in a['primary_url']and(a['relative']=='MANIFEST.json'or M[a['relative']]==a['sha256']));primary[a['file']]=a['sha256']
    ck('own_MANIFEST_actual_PLAN_OWNERS',M['data/PLAN.json']==hs(cr['own_physical_artifacts']['PLAN']['file'])==ownspec['data']['plan_sha256']and M['data/OWNERS.json.gz']==hs(cr['own_physical_artifacts']['OWNERS']['file'])==ownspec['data']['owners_sha256'])
    ck('own_exact_RAW_recovery_receipt',hs(selector['recovery_file'])==selector['recovery_sha256']and set(selector['exact_own_selected_RAW_native_bindings'])==set(ownspec['providers']))
    primary[selector['recovery_file']]=selector['recovery_sha256']
    for pid,bind in selector['exact_own_selected_RAW_native_bindings'].items():
        p=ownspec['providers'][pid];raw=ownspec['build']['providers'][pid]['word_content_sha256'];pairs={a['artifact']:a for a in recovery['outputs']if a['raw_content_sha256']==raw}
        ck(pid+'_own_exact_RAW_full_program_and_orientation_commitments',raw==bind['own_RAW_content_sha256']and pairs['LOCAL-PROGRAMS.json.gz']['semantic_sha256']==bind['program_sha256']and pairs['LOCAL-PROGRAMS.json.gz']['orientation_sha256']==bind['orientation_sha256']==p['program_hashes'])
        ck(pid+'_canonical_is_explicit_derived_fact_not_invented_source_field',not bind['canonical_digest_explicit_in_own_SPEC']and 'artifact_semantic_sha256'not in p and pairs['CANONICAL-WORD.json.gz']['semantic_sha256']==bind['canonical_sha256']and bind['canonical_file']==pairs['CANONICAL-WORD.json.gz']['file'])
'''+s[b:]
s=s.replace("hs(a['file'])==a['sha256']==a['own_SPEC_expected_sha256']","hs(a['file'])==a['sha256']==ownspec['data'][kind.lower()+'_sha256']")
needle="    for n in cr['selected_native_censuses']:\n";s=s.replace(needle,needle+"        ownlocal=ownspec['providers'][n['provider']];nc=rd(n['census_file']);widths=nc['forward']['widths']\n")
s=s.replace("[b-a for a,b in zip(n['initial_helper_ranks'],n['final_helper_ranks'])]==ownspec['providers'][n['provider']]['complete_contract']['widths']","[b-a for a,b in zip(n['initial_helper_ranks'],n['final_helper_ranks'])]==widths")
needle="        ck(n['provider']+'_actual_initial_final_helper_dimensions'";a=s.index(needle);b=s.index('\n    rev=rm[pr]',a)
s=s[:b]+'''
        ck(n['provider']+'_own_complete_width_digest_inventory_and_local_bill',hashlib.sha256(json.dumps(widths,sort_keys=True,separators=(',',':')).encode()).hexdigest()==ownlocal['width_digest']and {str(k):widths.count(k)for k in set(widths)}==ownlocal['inventory']and all(nc[o]['real_component_primitives']==ownlocal['expected_local'][o]['real_component_primitives']and F(nc[o]['prefix_l1'])==F(ownlocal['expected_local'][o]['prefix_l1'])and nc[o]['scalar_macros']==ownlocal['expected_local'][o]['macros']and nc[o]['events']==ownlocal['expected_local'][o]['events']and nc[o]['coefficient_work_primitives']==ownlocal['expected_local'][o]['coefficient_work_primitive_count']for o in ['forward','backward']))
'''+s[b:]
a=s.index("    deps+=['gaussian-only-parameter-ledger-peer-review.json'");b=s.index('\n    dep={p:hs(p)for p in deps}',a)
s=s[:a]+"""    deps+=['gaussian-only-parameter-ledger-peer-review.json','prepare_selected_provider_v22.py','prepare_selected_provider_v22_whole_costs.py','selected_provider_v17_whole_bounds.py','selected-provider-v17-whole-upper.md','early-frame-coalescence-own-source/source-manifest.json','cold14-typed-chain-native-byte-recovery.json','recover_cold14_chain_native_bytes.py','cold14-source-reconstruction/source-closure-manifest.json','cold14-retained-baseline-seeds/manifest.json']
""".rstrip()+s[b:]
s=s.replace("ck('exact_six_own_selected_K492_packages'","ck('exact_two_own_selected_frame_coalescence_packages'")
assert 'late-cold-mixed'not in s and "fast['"not in s and 'meter_by'not in s
(R/'selected_provider_v22_whole_bounds.py').write_text(s,encoding='utf8')
print('Prepared own V22 two source-specific whole-cost instances; closed=',COST_REVIEW_CLOSED)
