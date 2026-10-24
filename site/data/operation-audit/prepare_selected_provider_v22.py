"""Own582/584 select exact previously executed RAW endpoints, not prior costs."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import ast,copy,gzip,json
R=Path(__file__).resolve().parent
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 b=(R/f).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def blob(b):return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def funcs(s):return {n.name:ast.dump(n,include_attributes=False)for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
IDS={582,584};old=rd('selected-provider-dispatch-v10-inputs.json');mf='early-frame-coalescence-own-source/source-manifest.json';selection=rd(mf)
cf='cold14-source-reconstruction/source-closure-manifest.json';closure=rd(cf);oldspec=rd(closure['SPEC_file']);recf='cold14-typed-chain-native-byte-recovery.json';rec=rd(recf)
assert rec['script_sha256']==hs('recover_cold14_chain_native_bytes.py')and rec['status']=='passed_actual_typed_constructors_scalar_native_wrappers'
for f,h in rec['source_sha256'].items():assert hs(f)==h,f
for f,h in rec['dependency_hashes'].items():assert hs(f)==h,f
oldverf=next(a['file']for a in closure['objects']if a['package']=='package'and a['relative']=='verify.py');oldfun=funcs((R/oldverf).read_text())
cohort=[copy.deepcopy(x)for x in old['cohort_rows']if x['pr']in IDS];assert {r['pr']for r in cohort}==IDS
D=R/'selected-provider-dispatch-v22-source';D.mkdir(exist_ok=True);sources={};bindings={}
for row in cohort:
 pr=row['pr'];z=next(a for a in selection['rows']if a['pr']==pr);files={a['relative']:a for a in z['files']};M=rd(z['MANIFEST_file']);s=rd(z['SPEC_file']);out=D/str(pr);out.mkdir(exist_ok=True)
 assert row['own_head']==z['own_head']and M=={k:a['sha256']for k,a in files.items()if k!='MANIFEST.json'}
 for a in files.values():
  b=(R/a['file']).read_bytes();assert hs(a['file'])==a['sha256']and a['own_head']==z['own_head']and blob(b)==a['git_blob_sha1']==a['own_API_git_blob_sha1']
 api={}
 for f,h in z['primary_changed_file_API_sha256'].items():
  assert hs(f)==h;api.update({a['filename']:a['sha']for a in rd(f)})
 assert all(api[a['path']]==a['git_blob_sha1']for a in files.values())
 v=(R/files['verify.py']['file']).read_text();fn=funcs(v)
 assert "SPECFILE=a.spec.resolve();SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v and"futures={pid:pool.submit(provider,pid)for pid in sorted(BUILD['providers'])}"in v
 assert "'--plan',P/'data/PLAN.json'"in v and"'--owners',P/'data/OWNERS.json.gz'"in v
 assert F(s['expected']['kappa'])==F(next(a['quoted_kappa_fraction']for a in old['claim_metadata']if a['pr']==pr))
 # The complete own-declared source manifests/commits and their selected file
 # maps equal the executed closure; equality is not inferred from names.
 for key,p in s['build']['sources'].items():assert p==oldspec['build']['sources'][key]
 # All own constructor/selection and native-localize function bodies actually
 # used here are exactly those in the executed, larger typed-chain producer.
 # build_word differs only in its available step map, so its literal digest
 # assertions are separately required rather than asserting full AST equality.
 used={'read','sha','content','dump','pinned','ref','omissions','cold_kernel','finalize','multicut','frame_only','promote','joint_prefix'}|({'frame_coalesce'}if pr==584 else set())
 for name in used:assert fn[name]==oldfun[name],(pr,name)
 assert "pinned(d,'word_content_sha256',content(word),pid)"in v
 assert "V/'code/audit_and_transport.py'"in v and"V/'code/emit_local.py'"in v and"V/'code/audit_local.py'"in v and"V/'code/adapters_local.py'"in v
 bindings[str(pr)]={}
 for pid,p in s['providers'].items():
  raw=s['build']['providers'][pid]['word_content_sha256'];aa={a['artifact']:a for a in rec['outputs']if a['raw_content_sha256']==raw}
  assert set(aa)>={'CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz'}
  can,prog=aa['CANONICAL-WORD.json.gz'],aa['LOCAL-PROGRAMS.json.gz'];assert hs(can['file'])==can['sha256']and hs(prog['file'])==prog['sha256']
  assert prog['orientation_sha256']==p['program_hashes']and ident(rd(prog['file']))==prog['semantic_sha256']and ident(rd(can['file']))==can['semantic_sha256']
  for a in (can,prog):sources[a['file']]=dict(file=a['file'],sha256=a['sha256'],origin='actual_executed_typed_RAW_endpoint_and_native_engines_with_exact_own_RAW_digest_and_both_orientation_join',primary=dict(recovery_file=recf,recovery_sha256=hs(recf),payload=a))
  bindings[str(pr)][pid]=dict(own_RAW_content_sha256=raw,program_sha256=prog['semantic_sha256'],orientation_sha256=p['program_hashes'],canonical_sha256=can['semantic_sha256'],canonical_file=can['file'],program_file=prog['file'],canonical_digest_explicit_in_own_SPEC=False,canonical_identity_basis='same exact own-selected RAW endpoint and unchanged full native engine/input closure, plus own complete two-orientation program commitments')
 for kind in ['PLAN','OWNERS']:
  rel='data/PLAN.json'if kind=='PLAN'else'data/OWNERS.json.gz';a=files[rel];assert a['sha256']==s['data'][kind.lower()+'_sha256']
  receipt=dict(pr=pr,own_head=z['own_head'],path=a['path'],file=a['file'],sha256=a['sha256'],bytes=a['bytes'],status='authenticated_own_SPEC_declared_bytes',primary=a)
  (out/(kind+'.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
 f=[a for a in row['verified_components']if a.get('path')==z['selected_package']+'/data/SPEC.json'and a['sha256']==z['SPEC_sha256']];assert len(f)==1;f[0]['file']=z['SPEC_file']
 selector=dict(pr=pr,own_head=z['own_head'],SPEC_file=z['SPEC_file'],SPEC_sha256=z['SPEC_sha256'],MANIFEST_file=z['MANIFEST_file'],MANIFEST_sha256=z['MANIFEST_sha256'],verifier_file=files['verify.py']['file'],verifier_sha256=files['verify.py']['sha256'],verified_primary=z['files'],primary_changed_file_API_sha256=z['primary_changed_file_API_sha256'],actual_own_literal_SPEC_build_native_PLAN_OWNERS_selection=True,own_typed_function_bodies_equal_executed_source=sorted(used),own_complete_external_source_specs_equal_executed_closure=True,exact_own_selected_RAW_native_bindings=bindings[str(pr)],recovery_file=recf,recovery_sha256=hs(recf),original_own_complete_constructor_or_global_verifier_PASS_claimed=False,universal_phase_native_allsize_proved=False)
 (out/'actual-own-selector.json').write_text(json.dumps(selector,indent=2)+'\n',encoding='utf8')
deps=['selected-provider-dispatch-v10-inputs.json','selected_provider_dispatch_v17.py',mf,cf,recf,'recover_cold14_chain_native_bytes.py']
snap=dict(schema='selected-provider-dispatch-frozen-inputs/22',cohort_rows=cohort,claim_metadata=[a for a in old['claim_metadata']if a['pr']in IDS],actual_native_archive_sources=list(sources.values()),recovered_own_native_selection=bindings,original_input_sha256={f:hs(f)for f in deps},scope='Two own selected finite controllers with three providers each. Own literal build endpoints and complete orientation commitments identify actual executed RAW/native objects exactly; same external source/constructor bodies and native inputs are checked. The earlier own SPECs omit a canonical semantic digest, so the recovered catalogue is explicitly bound through the exact RAW and unchanged engine, never represented as a declared source field. Complete own PLAN/OWNERS/full invoice and all runtime parameters require fresh checks. No prior invoice/cutoff or original full-package/phase PASS transfer.')
(R/'selected-provider-dispatch-v22-inputs.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf8')
s=(R/'selected_provider_dispatch_v17.py').read_text().replace('selected-provider-dispatch-v17','selected-provider-dispatch-v22').replace('V17','V22')
needle="p=s['providers'][pid];sem=p.get('artifact_semantic_sha256',{});w=sem.get('CANONICAL-WORD.json.gz');g=sem.get('LOCAL-PROGRAMS.json.gz');pf=actual.get(g)"
replacement="""p=s['providers'][pid];sem=p.get('artifact_semantic_sha256',{});w=sem.get('CANONICAL-WORD.json.gz');g=sem.get('LOCAL-PROGRAMS.json.gz')
            if w is None:
                ownrec=snap['recovered_own_native_selection'][str(row['pr'])][pid]
                require(ownrec['orientation_sha256']==p['program_hashes'] and ownrec['own_RAW_content_sha256']==s['build']['providers'][pid]['word_content_sha256'],'own exact RAW/orientation recovery join')
                w=ownrec['canonical_sha256'];g=ownrec['program_sha256']
            pf=actual.get(g)"""
assert s.count(needle)==1;s=s.replace(needle,replacement)
(R/'selected_provider_dispatch_v22.py').write_text(s,encoding='utf8');print('PASS prepared2 own selected controllers;5 unique actual RAW/native pairs')
