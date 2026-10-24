"""Two own immutable U8 controller selectors and exact selected-byte inputs."""
from pathlib import Path
import copy,json,hashlib,shutil
R=Path(__file__).resolve().parent
def rd(f):return json.loads((R/f).read_bytes())
def hs(f):return hashlib.sha256((R/f).read_bytes()).hexdigest()
IDS={869,870};old=rd('selected-provider-dispatch-v10-inputs.json');recovery=rd('u8-exact-earlier-selected-byte-recovery.json');select=rd('u8-own-selection-source/manifest.json');cohort=[copy.deepcopy(r)for r in old['cohort_rows']if r['pr']in IDS]
assert{r['pr']for r in cohort}==IDS and all(recovery['checks'].values())and recovery['script_sha256']==hs('recover_u8_selected_archive_bytes.py')
sources=[dict(file=a['file'],sha256=a['sha256'],origin='actual_source_U8_builder_transport_emitter_scalar_recovery_matching_each_earlier_own_commitment',primary=dict(recovery_receipt='u8-exact-earlier-selected-byte-recovery.json',recovery_receipt_sha256=hs('u8-exact-earlier-selected-byte-recovery.json'),artifact=a))for a in recovery['outputs']if a['file'].endswith(('CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz'))]
assert len(sources)==2
D=R/'selected-provider-dispatch-v16-source';D.mkdir(exist_ok=True)
for row in cohort:
 pr=row['pr'];out=D/str(pr);out.mkdir(exist_ok=True);sel=[a for a in select if a['pr']==pr];ver=next(a for a in sel if a['path'].endswith('.py'));Mfile=ver['own_MANIFEST_file'];M=rd(Mfile);v=(R/ver['file']).read_text();speca=next(a for a in row['verified_components']if a.get('path','').endswith('/data/SPEC.json')and a['sha256']==M['data/SPEC.json']);s=rd(speca['file']);z=next(a for a in recovery['rows']if a['pr']==pr)
 assert z['own_head']==row['own_head']and z['own_SPEC_sha256']==speca['sha256']and hs(Mfile)==ver['own_MANIFEST_sha256']
 for a in sel:assert a['own_head']==row['own_head']and hs(a['file'])==a['sha256']==M[a['path'].rsplit('/',1)[-1]]
 if pr==869:assert"WITNESS_SPEC=str(PACKAGE/'data/SPEC.json')"in v and"--plan', PACKAGE/'data/PLAN.json'"in v and"--owners', PACKAGE/'data/OWNERS.json.gz'"in v
 else:assert"SPEC8, SPEC16 = PKG / 'data/SPEC-T8.json', PKG / 'data/SPEC.json'"in v and"--plan', PKG / 'data/PLAN.json'"in v and"--owners', PKG / 'data/OWNERS.json.gz'"in v
 assert M['data/PLAN.json']==s['data']['plan_sha256']and M['data/OWNERS.json.gz']==s['data']['owners_sha256']
 for kind in['PLAN','OWNERS']:
  art=rd(f'selected-provider-dispatch-v10-source/{pr}/{kind}.json');assert art['status']=='authenticated_own_SPEC_declared_bytes'and hs(art['file'])==art['sha256']==M['data/PLAN.json'if kind=='PLAN'else'data/OWNERS.json.gz'];shutil.copyfile(R/f'selected-provider-dispatch-v10-source/{pr}/{kind}.json',out/(kind+'.json'))
 selector=dict(pr=pr,own_head=row['own_head'],SPEC_file=speca['file'],SPEC_sha256=speca['sha256'],MANIFEST_file=Mfile,MANIFEST_sha256=hs(Mfile),verifier_file=ver['file'],verifier_sha256=hs(ver['file']),verifier_key='verify_global.py'if pr==869 else'verify_t16.py',verified_primary=sel,exact_native_recovery_receipt='u8-exact-earlier-selected-byte-recovery.json',exact_native_recovery_receipt_sha256=hs('u8-exact-earlier-selected-byte-recovery.json'),selection_by_actual_own_entrypoint=True)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','u8-exact-earlier-selected-byte-recovery.json','recover_u8_selected_archive_bytes.py','u8-own-selection-source/manifest.json','fetch_u8_own_selection.py','selected_provider_dispatch_v13.py'];snap=dict(schema='selected-provider-dispatch-frozen-inputs/16',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=sources,original_input_sha256={f:hs(f)for f in deps},scope='Two own actual U8 controller selectors. Each whole native object must match its own committed canonical/program/orientation bytes and complete own PLAN/OWNERS. No later controller, profile, invoice or cutoff is transferred by native equality.')
(R/'selected-provider-dispatch-v16-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v13.py').read_text().replace('selected-provider-dispatch-v13','selected-provider-dispatch-v16')
s=s.replace("if args.refresh_inputs or not snapshot.exists():","if args.refresh_inputs or not snapshot.exists():\n    raise ValueError('V16 requires frozen own-entrypoint source inputs')")
s=s.replace("snap=rd(snapshot);ledger=","snap=rd(snapshot)\nfor f,h in snap['original_input_sha256'].items():require(hs(R/f)==h,'frozen V16 source SHA '+f)\nledger=")
(R/'selected_provider_dispatch_v16.py').write_text(s,encoding='utf8');print('PASS prepared2 own U8 source controllers')
