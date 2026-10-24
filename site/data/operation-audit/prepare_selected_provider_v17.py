"""Six independently selected own K492 mixed controllers; fresh costs still open."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import copy,json,shutil
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
IDS={636,638,639,640,642,644};old=rd('selected-provider-dispatch-v10-inputs.json');base=rd('late-cold-mixed-source/native-source-closure-638.json');variant=rd('late-cold-mixed-source/variant-own-source-manifest.json');rec=rd('late-cold-mixed-native-variant-recovery.json')
assert rec['status']=='passed_actual_source_variant_constructors_and_native_scalar_frame_wrappers'and all(rec['checks'].values())and rec['script_sha256']==hs('recover_late_cold_variants_native_bytes.py')
for f,h in rec['dependency_hashes'].items():assert hs(f)==h,f
cohort=[copy.deepcopy(a)for a in old['cohort_rows']if a['pr']in IDS];assert {a['pr']for a in cohort}==IDS
D=R/'selected-provider-dispatch-v17-source';D.mkdir(exist_ok=True);sources=[];seen=set()
for a in rec['outputs']:
 if a['artifact']not in ['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']or a['file']in seen:continue
 assert hs(a['file'])==a['sha256'];seen.add(a['file']);sources.append(dict(file=a['file'],sha256=a['sha256'],origin='actual_own_source_typed_constructor_and_native_engines_exact_selected_objects',primary=dict(recovery_file='late-cold-mixed-native-variant-recovery.json',recovery_sha256=hs('late-cold-mixed-native-variant-recovery.json'),payload=a)))
assert len(sources)==12
for row in cohort:
 pr=row['pr'];out=D/str(pr);out.mkdir(exist_ok=True)
 if pr==638:
  files=[a for a in base['objects']if a['package']=='package'];head=base['own_head'];specf=base['SPEC_file'];Mf='late-cold-mixed-source/638/MANIFEST.json';root='research/pr637-improvement-20261013/witness637'
 else:
  z=next(a for a in variant['rows']if a['pr']==pr);files=z['source_files'];head=z['own_head'];specf=z['SPEC_file'];Mf=z['own_MANIFEST_file'];root=z['selected_package']
 assert row['own_head']==head;spec=rd(specf);M=rd(Mf);verf=f'late-cold-mixed-source/{pr}/verify.py';v=(R/verf).read_text()
 for a in files:
  assert hs(a['file'])==a['sha256']
  if a['relative']!='MANIFEST.json':assert M[a['relative']]==a['sha256']
 assert M['verify.py']==hs(verf)and M['data/SPEC.json']==hs(specf)
 assert "SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v 
 assert "--plan',P/'data/PLAN.json'"in v and"--owners',P/'data/OWNERS.json.gz'"in v 
 assert "futures={pid:pool.submit(provider,pid)for pid in sorted(BUILD['providers'])}"in v
 assert F(spec['expected']['kappa'])==F(next(a['quoted_kappa_fraction']for a in old['claim_metadata']if a['pr']==pr))
 reference=rd(base['SPEC_file']);assert spec['build']['sources']==reference['build']['sources']
 for pid,p in spec['providers'].items():
  matches=[a for a in rec['exact_own_selected_provider_matches']if a['pr']==pr and a['provider']==pid];assert len(matches)==1 and matches[0]['own_head']==head and matches[0]['SPEC_sha256']==hs(specf)
 for kind in ['PLAN','OWNERS']:
  f=f'selected-provider-dispatch-v10-source/{pr}/{kind}.json';a=rd(f);assert a['status']=='authenticated_own_SPEC_declared_bytes'and hs(a['file'])==a['sha256']==spec['data'][kind.lower()+'_sha256']==M['data/PLAN.json'if kind=='PLAN'else'data/OWNERS.json.gz'];shutil.copyfile(R/f,out/(kind+'.json'))
 found=[a for a in row['verified_components']if a.get('path')==root+'/data/SPEC.json'];assert len(found)==1 and found[0]['sha256']==hs(specf);found[0]['file']=specf
 selector=dict(pr=pr,own_head=head,SPEC_file=specf,SPEC_sha256=hs(specf),MANIFEST_file=Mf,MANIFEST_sha256=hs(Mf),verifier_file=verf,verifier_sha256=hs(verf),actual_literal_spec_driven_native_and_global_data_selection=True,verified_primary=files,own_selected_native_recovery_file='late-cold-mixed-native-variant-recovery.json',own_selected_native_recovery_sha256=hs('late-cold-mixed-native-variant-recovery.json'),complete_historical_package_replay_claimed=False,source_selected_partial_operator_and_absolute_phase_proved=False)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v13.py','late-cold-mixed-source/native-source-closure-638.json','late-cold-mixed-source/variant-own-source-manifest.json','late-cold-mixed-native-byte-recovery-638.json','late-cold-mixed-native-variant-recovery.json','recover_late_cold_mixed_native_bytes.py','recover_late_cold_variants_native_bytes.py']
snap=dict(schema='selected-provider-dispatch-frozen-inputs/17',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=sources,original_input_sha256={f:hs(f)for f in deps},scope='Six actual own immutable source-selected K492 mixed controllers. Native input/body/recipe sharing is exact-byte data recovery only; each own full canonical/program/orientation identity and selected complete PLAN/OWNERS must match, followed by fresh physical/invoice checks. Raw-schema source local counts are checked directly; an absent historical complete_contract field is not invented. A newly charged complete adapter realization is explicit, with universal native/operator/allsize conditions retained. No old invoice or cutoff transfers.')
(R/'selected-provider-dispatch-v17-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v13.py').read_text().replace('selected-provider-dispatch-v13','selected-provider-dispatch-v17')
s=s.replace('if args.refresh_inputs or not snapshot.exists():',"if args.refresh_inputs or not snapshot.exists():\n    raise ValueError('V17 requires frozen actual own-selector preparation, not mutable discovery')")
s=s.replace('snap=rd(snapshot);ledger=',"snap=rd(snapshot)\nfor f,h in snap['original_input_sha256'].items():require(hs(R/f)==h,'frozen V17 source SHA '+f)\nledger=")
a=s.index("            contract=p['complete_contract'];");b=s.index('            # JSON caches',a)
s=s[:a]+'''            if 'complete_contract'in p:contract=p['complete_contract']
            else:
                require(ident(f['widths'])==p['width_digest']and dict(Counter(f['widths']))=={int(k):v for k,v in p['inventory'].items()},'own raw-schema whole-width digest and inventory')
                local=p.get('expected_local')or{o:p['expected_local.'+o]for o in ['backward','forward']}
                contract=dict(widths=f['widths'],local=local,new_adapter_realization_not_historical_complete_contract=True)
            require(f['widths']==contract['widths']and {int(k):v for k,v in f['paid_profile'].items()}=={int(k):v for k,v in p['expected_profile'].items()},'own width/profile contract mismatch')
''' +s[b:]
s=s.replace("            require(adapter==contract['local_adapters'],'own actual adapter invoice mismatch')", "            if 'local_adapters'in contract:require(adapter==contract['local_adapters'],'own actual adapter invoice mismatch')")
s=s.replace("e=contract['local'][o];require(v['real_component_primitives']==e['real_component_primitives']and F(v['prefix_l1'])==F(e['prefix_l1']),'own scalar/prefix contract mismatch')", "e=contract['local'][o];require(v['real_component_primitives']==e['real_component_primitives']and F(v['prefix_l1'])==F(e['prefix_l1']),'own scalar/prefix contract mismatch')\n                if 'macros'in e:require(v['scalar_macros']==e['macros']and v['events']==e['events']and v['coefficient_work_primitives']==e['coefficient_work_primitive_count'],'own complete local source primitive/macro/event bill')")
s=s.replace('source_equivalent_numeric_parent=True,historical_parent_byte_identity_claimed=False',"source_equivalent_numeric_parent=True,own_source_selector_file=(D/str(pr)/'actual-own-selector.json').relative_to(R).as_posix(),own_source_selector_sha256=hs(D/str(pr)/'actual-own-selector.json'),historical_complete_native_contract_field_invented=False,new_full_adapter_realization_charged=True,original_full_global_verifier_PASS_claimed=False,historical_parent_byte_identity_claimed=False")
(R/'selected_provider_dispatch_v17.py').write_text(s,encoding='utf8');print('PASS prepared6 own source-selected K492 mixed controllers;12 exact selected native payloads')
