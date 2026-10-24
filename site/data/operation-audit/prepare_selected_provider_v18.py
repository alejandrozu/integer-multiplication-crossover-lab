"""Own2077 actual build/selector, source data and selected r480 byte bindings."""
from pathlib import Path
from hashlib import sha256
import copy,json
R=Path(__file__).resolve().parent
def rd(f):return json.loads((R/f).read_bytes())
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
old=rd('selected-provider-dispatch-v10-inputs.json');row=copy.deepcopy(next(r for r in old['cohort_rows']if r['pr']==2077));receipt=rd('pr2077-exact-selected-data-recovery.json');P='pr2077-vacancy-chain-source';M=rd(P+'/MANIFEST.json');source=rd(P+'/source-receipt.json');spec=rd(P+'/data/SPEC.json');candidate=rd(P+'/CANDIDATE.json');v=(R/(P+'/verify.py')).read_text();pins=rd(P+'/INPUTS.json');local=rd(P+'/LOCAL-PINS.json');chrono=rd('pr2077-source-chronology/chronology.json')
assert all(receipt['checks'].values())and receipt['script_sha256']==hs('recover_pr2077_selected_data.py')and source['own_head']==row['own_head']==receipt['own_head']==chrono['own_head']
assert{a['relative']:a['sha256']for a in source['files']}==M and all(hs(a['file'])==a['sha256']and a['own_head']==row['own_head']for a in source['files'])
assert "blobs=mod.derive(main)"in v and"for name in ('OWNERS.json.gz','PLAN.json','SPEC.json')"in v and"source/'verify_t16.py'"in v and"research/community-frontier1094-audit/selected-replay.tar.gz"in v
assert spec['expected']['kappa']==candidate['expected_updates']['kappa']=='418166011373521/250000000000000000'and candidate['baseline_kappa']=='836330098538459/500000000000000000'
authority=next(a for a in row['verified_components']if a.get('path','').endswith('/data/SPEC.json')and a['sha256']==M['data/SPEC.json']);assert hs(authority['file'])==M['data/SPEC.json']==hs(P+'/data/SPEC.json')
recovered=rd('r480-selected-native-recovery.json');sources=[]
for f,h in recovered['source_sha256'].items():
 if f.startswith('r480-selected-recovery-source/')and f.endswith(('__CANONICAL-WORD.json.gz','__LOCAL-PROGRAMS.json.gz')):
  name=f.rsplit('__',1)[-1];assert h==local[name]==hs(f);sources.append(dict(file=f,sha256=h,origin='exact_compressed_own_LOCAL_PINS_selected1094_archive_bytes_no_bound_transfer',primary=dict(file='r480-selected-native-recovery.json',sha256=hs('r480-selected-native-recovery.json'),own_LOCAL_PINS_file=P+'/LOCAL-PINS.json',own_LOCAL_PINS_sha256=hs(P+'/LOCAL-PINS.json'))))
assert len(sources)==2
D=R/'selected-provider-dispatch-v18-source/2077';D.mkdir(parents=True,exist_ok=True)
for kind,name in[('PLAN','PLAN.json'),('OWNERS','OWNERS.json.gz')]:
 f=P+'/data/'+name;h=M['data/'+name];assert hs(f)==h==spec['data']['plan_sha256'if kind=='PLAN'else'owners_sha256'];a=dict(pr=2077,own_head=row['own_head'],file=f,sha256=h,bytes=(R/f).stat().st_size,own_SPEC_expected_sha256=h,status='authenticated_own_SPEC_declared_bytes');(D/(kind+'.json')).write_text(json.dumps(a,indent=2)+'\n',encoding='utf8')
selector=dict(pr=2077,own_head=row['own_head'],SPEC_file=authority['file'],SPEC_sha256=authority['sha256'],MANIFEST_file=P+'/MANIFEST.json',MANIFEST_sha256=hs(P+'/MANIFEST.json'),verifier_file=P+'/verify.py',verifier_sha256=hs(P+'/verify.py'),builder_file=P+'/build.py',builder_sha256=hs(P+'/build.py'),source_recovery_file='pr2077-exact-selected-data-recovery.json',source_recovery_sha256=hs('pr2077-exact-selected-data-recovery.json'),whole_source_inventory=source['files'],actual_own_kappa=spec['expected']['kappa'],frozen_metadata_kappa=candidate['baseline_kappa'],chronology_file='pr2077-source-chronology/chronology.json',chronology_sha256=hs('pr2077-source-chronology/chronology.json'))
(D/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v13.py','pr2077-exact-selected-data-recovery.json','recover_pr2077_selected_data.py',P+'/source-receipt.json','r480-selected-native-recovery.json','pr2077-source-chronology/chronology.json']
snap=dict(schema='selected-provider-dispatch-frozen-inputs/18',cohort_rows=[row],claim_metadata=[a for a in old['claim_metadata']if a['pr']==2077],actual_native_archive_sources=sources,original_input_sha256={f:hs(f)for f in deps},scope='Actual own2077 literal verifier/build selects its exact three reconstructed full source data bytes and own LOCAL-PINS complete native archive bytes. Frozen baseline kappa remains metadata; no equal-kappa heuristic or inherited old cutoff is used.')
(R/'selected-provider-dispatch-v18-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v13.py').read_text().replace('selected-provider-dispatch-v13','selected-provider-dispatch-v18')
s=s.replace("if args.refresh_inputs or not snapshot.exists():","if args.refresh_inputs or not snapshot.exists():\n    raise ValueError('V18 requires its frozen actual own-source selection')")
s=s.replace("snap=rd(snapshot);ledger=","snap=rd(snapshot)\nfor f,h in snap['original_input_sha256'].items():require(hs(R/f)==h,'frozen V18 source SHA '+f)\nledger=")
start=s.index('def selected(row):');end=s.index('\ndef fetch_one',start)
s=s[:start]+"""def selected(row):
    selector=rd(D/str(row['pr'])/'actual-own-selector.json');require(selector['own_head']==row['own_head'],'actual own selector head');a=next(a for a in row['verified_components']if a.get('file')==selector['SPEC_file']and a['sha256']==selector['SPEC_sha256']);require(hs(R/a['file'])==a['sha256'],'actual own SPEC SHA');s=rd(R/a['file']);require(s['expected']['kappa']==selector['actual_own_kappa'],'actual source-selected target');return a,s
"""+s[end:]
# These exact geometry bytes are explicitly pinned by own2077 INPUTS; the new
# resource census may not substitute an equal-profile parent.
s=s.replace("phases=rd(data('/work/complex-nine-native/DATA-PHASES.json'));baseword=rd(data('/split-centres/CANONICAL-WORD.json.gz'))", "phases=rd(data('/work/complex-nine-native/DATA-PHASES.json'));baseword=rd(data('/split-centres/CANONICAL-WORD.json.gz'))\nactual_input_pins=rd(R/'pr2077-vacancy-chain-source/INPUTS.json')\nfor fp in [R/'older-reviewed-source'/next(x['file']for x in old if x['path']=='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz'),data('/work/complex-nine-native/DATA-PHASES.json'),data('/split-centres/CANONICAL-WORD.json.gz')]:require(hs(fp)in actual_input_pins.values(),'own2077 exact parent geometry pin')")
(R/'selected_provider_dispatch_v18.py').write_text(s,encoding='utf8');print('PASS own2077 actual literal source selection and complete selected data preparation')
