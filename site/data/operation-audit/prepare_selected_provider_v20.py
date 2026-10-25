"""Own646 distinct signed-root K480 selector, no K492 invoice substitution."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import copy,json,shutil
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
old=rd('selected-provider-dispatch-v10-inputs.json');z=rd('late-cold-mixed-source/signed-root-646-source-manifest.json');recfile='late-cold-mixed-native-byte-recovery-646.json';rec=rd(recfile)
assert rec['pr']==646 and rec['own_head']==z['own_head']and rec['checks_passed']==334 and all(rec['checks'].values())and rec['script_sha256']==hs('recover_signed_root_646_native_bytes.py')
for key in('source_sha256','retained_base_sha256','dependency_hashes'):
    for f,h in rec[key].items():assert hs(f)==h,f
cohort=[copy.deepcopy(r)for r in old['cohort_rows']if r['pr']==646];assert len(cohort)==1;row=cohort[0]
assert row['own_head']==z['own_head'];M=rd(z['own_MANIFEST_file']);spec=rd(z['SPEC_file']);verf='late-cold-mixed-source/646/verify.py';v=(R/verf).read_text()
for a in z['source_files']:
    b=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert hs(a['file'])==a['sha256']and blob==a['git_blob_sha1']==a['own_API_git_blob_sha1']and a['own_head']==z['own_head']
    assert a['relative']=='MANIFEST.json'or M[a['relative']]==a['sha256']
assert hs(z['own_MANIFEST_file'])==z['own_MANIFEST_sha256']and hs(z['SPEC_file'])==z['SPEC_sha256']==M['data/SPEC.json']and M['verify.py']==hs(verf)
assert "SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v and "--plan',P/'data/PLAN.json'"in v and "--owners',P/'data/OWNERS.json.gz'"in v and "futures={pid:pool.submit(provider,pid)for pid in sorted(BUILD['providers'])}"in v
assert F(spec['expected']['kappa'])==F(next(a['quoted_kappa_fraction']for a in old['claim_metadata']if a['pr']==646))
sources=[];selected={}
for pid,p in spec['providers'].items():
    raw=spec['build']['providers'][pid]['word_content_sha256'];objects={a['artifact']:a for a in rec['outputs']if a['provider']==pid and a['raw_content_sha256']==raw}
    assert objects['CANONICAL-WORD.json.gz']['semantic_sha256']==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and objects['LOCAL-PROGRAMS.json.gz']['semantic_sha256']==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and objects['LOCAL-PROGRAMS.json.gz']['orientation_sha256']==p['program_hashes']
    for name in('CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz'):
        a=objects[name];assert hs(a['file'])==a['sha256'];sources.append(dict(file=a['file'],sha256=a['sha256'],origin='actual_own_signed_root_K480_constructor_and_native_engines_exact_selected_payload',primary=dict(recovery_file=recfile,recovery_sha256=hs(recfile),payload=a)))
    selected[pid]=dict(raw_content_sha256=raw,canonical_file=objects['CANONICAL-WORD.json.gz']['file'],program_file=objects['LOCAL-PROGRAMS.json.gz']['file'],orientation_sha256=p['program_hashes'])
D=R/'selected-provider-dispatch-v20-source/646';D.mkdir(parents=True,exist_ok=True)
for kind in('PLAN','OWNERS'):
    f=f'selected-provider-dispatch-v10-source/646/{kind}.json';a=rd(f)
    assert a['status']=='authenticated_own_SPEC_declared_bytes'and hs(a['file'])==a['sha256']==spec['data'][kind.lower()+'_sha256']==M['data/PLAN.json'if kind=='PLAN'else'data/OWNERS.json.gz']
    shutil.copyfile(R/f,D/(kind+'.json'))
found=[a for a in row['verified_components']if a.get('path')==z['selected_package']+'/data/SPEC.json'];assert len(found)==1 and found[0]['sha256']==hs(z['SPEC_file']);found[0]['file']=z['SPEC_file']
selector=dict(pr=646,own_head=z['own_head'],SPEC_file=z['SPEC_file'],SPEC_sha256=z['SPEC_sha256'],MANIFEST_file=z['own_MANIFEST_file'],MANIFEST_sha256=z['own_MANIFEST_sha256'],verifier_file=verf,verifier_sha256=hs(verf),actual_literal_spec_driven_native_and_global_data_selection=True,verified_primary=z['source_files'],own_selected_native_recovery_file=recfile,own_selected_native_recovery_sha256=hs(recfile),exact_selected_K480_providers=selected,complete_historical_package_replay_claimed=False,source_selected_partial_operator_and_absolute_phase_proved=False)
(D/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v17.py','late-cold-mixed-source/signed-root-646-source-manifest.json','late-cold-mixed-source/native-source-closure-646.json',recfile,'recover_signed_root_646_native_bytes.py']
snap=dict(schema='selected-provider-dispatch-frozen-inputs/20',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']==646],actual_native_archive_sources=sources,original_input_sha256={f:hs(f)for f in deps},scope='Own646 actual signed-root K480 construction and distinct schedule. Its own complete native/PLAN/OWNERS and literal source selector must match before fresh physical/invoice checks. Exact prior RAW shadows are immutable byte inputs only, not a K492 provider or previous invoice/cutoff. Native/phase/operator/allsize interfaces remain explicit; no original complete global PASS is claimed.')
(R/'selected-provider-dispatch-v20-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v17.py').read_text().replace('selected-provider-dispatch-v17','selected-provider-dispatch-v20').replace('V17','V20')
(R/'selected_provider_dispatch_v20.py').write_text(s,encoding='utf8')
print('PASS prepared own distinct K480 signed-root646 selector and4 exact native payloads')
