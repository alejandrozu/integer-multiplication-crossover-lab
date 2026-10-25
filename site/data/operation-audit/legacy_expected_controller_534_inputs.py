"""Actual own534 pre-SPEC source/native/owner invoice; no previous allowance."""
from pathlib import Path
from hashlib import sha256
import gzip,importlib.util,json,os,shutil,subprocess,sys,tempfile
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'legacy-expected-controller-source/534';D=R/'legacy-expected-controller-534-derived';D.mkdir(exist_ok=True)
def rd(f):
    b=f.read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def hs(f):return sha256(f.read_bytes()).hexdigest()
checks={}
def ck(k,v):assert v,k;checks[k]=True
M=rd(S/'MANIFEST.json')['sha256'];source=rd(S/'source-manifest.json');ck('own_534_manifest_authority',source['pr']==534 and source['MANIFEST_sha256']==hs(S/'MANIFEST.json'))
for f,h in M.items():ck('own_payload_'+f,hs(S/f)==h)
v=(S/'verify_fast.py').read_text()
ck('actual_literal_own_selected_local_and_data_selector',"local = root/'evidence/local'"in v and "root/'inputs/OWNERS.json.gz'"in v and "root/'inputs/OWNER-PLAN.json'"in v and "expected = read(root/'EXPECTED.json')"in v)
expected=rd(S/'EXPECTED.json');can=rd(S/'evidence/local/CANONICAL-WORD.json.gz');programs=rd(S/'evidence/local/LOCAL-PROGRAMS.json.gz')
spec=importlib.util.spec_from_file_location('own_legacy534_pure_scalar_census',R/'finite_selected_program_census.py');pure=importlib.util.module_from_spec(spec);spec.loader.exec_module(pure)
nc=pure.census(programs,canonical=can);ck('fresh_both_orientation_scalar_only_specialization',all(z['scalar_specialization_columns_checked']and z['native_canonical_frame_catalog_checked']and not z['operator_valued_endpoint_proved_by_this_census']for z in nc.values()))
steps=[];outputs=[]
def normalize_generated_gzip(f):
    payload=gzip.decompress(f.read_bytes());b=bytearray(gzip.compress(payload,compresslevel=9,mtime=0));b[9]=255;f.write_bytes(b)
with tempfile.TemporaryDirectory(prefix='own534-source-inputs-')as td:
    T=Path(td);base=T/'base';host=T/'hosted';audit=T/'audit';audit.mkdir()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONINTMAXSTRDIGITS='0');env.pop('PYTHONPATH',None);env.pop('PYTHONOPTIMIZE',None)
    def run(name,script,*args):
        p=subprocess.run([sys.executable,'-B','-X','utf8',str(S/'code'/script),*map(str,args)],cwd=T,env=env,capture_output=True,text=True,encoding='utf8',timeout=600)
        assert p.returncode==0,(name,p.stdout[-3000:],p.stderr[-3000:]);steps.append(dict(name=name,exit_code=0));print('PASS actualown534',name,flush=True)
    run('bind_actual_selected_local_to_own_data_controller','prepare_supplier_base.py','--data-base',S/'inputs/data-base','--local',S/'evidence/local','--out',base)
    normalize_generated_gzip(base/'split-centres/GLOBAL-TEMPLATE.json.gz')
    run('emit_complete_own_OWNER_PLAN_and_OWNERS','emit_supplier_hosted.py','--base',base,'--owners',S/'inputs/OWNERS.json.gz','--plan',S/'inputs/OWNER-PLAN.json','--out',host)
    for f in host.glob('*.gz'):normalize_generated_gzip(f)
    run('independent_actual_whole_owner_and_seven_controls','audit_supplier_hosted.py',base,host,audit/'ASYNC-AUDIT.json','--mutation-controls')
    for f in host.glob('*.gz'):normalize_generated_gzip(f)
    run('actual_complete_fresh_invoice_WITHOUT_retained_invoice','invoice_final.py','--base',base,'--hosted',host,'--audit',audit,'--out',audit)
    own=rd(audit/'OWNERS-AND-PROFILE.json');inv=rd(audit/'PREFIX-AND-INVOICE.json');control=rd(audit/'ASYNC-AUDIT.json');template=rd(host/'GLOBAL-TEMPLATE.json.gz')
    ck('own_frozen_complete_hosted_template_mathematical_identity',template==rd(S/'evidence/hosted/GLOBAL-TEMPLATE.json.gz')and own['template_sha256']==expected['global_template_content_sha256'])
    ck('own_complete_owner_profile_and_row_counts',own['paid_profile']==expected['global_profile']and own['live']==expected['live']and own['physical']==expected['physical']and own['rank_mass']==expected['rank_mass']and own['hosted_residuals']==expected['whole_helper_roles']==36288 and control['complete_invocations']==72 and len(control['mutations_rejected'])==7)
    ck('actual_fresh_source_invoice_no_previous_allowance',inv['retained_prior_overcharge']is None and inv['global_prefix_bits']==expected['global_prefix_bits']==225 and inv['charged_prefix_bits']==512 and all(inv['strict_checks'].values()))
    for rel in['base/split-centres/GLOBAL-TEMPLATE.json.gz','base/split-centres/INTEGRATION.json','hosted/GLOBAL-TEMPLATE.json.gz','hosted/HOSTED.json','hosted/ACTUAL-SIGMAS.json.gz','hosted/IDLE-REMAINDER-FRAMES.json.gz','audit/ASYNC-AUDIT.json','audit/OWNERS-AND-PROFILE.json','audit/IDLE-REMAINDER-FRAMES.json','audit/PREFIX-AND-INVOICE.json','audit/GLOBAL-PREFIX.json']:
        f=T/rel;out=D/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f,out);outputs.append(dict(file=out.relative_to(R).as_posix(),sha256=hs(out)))
    cn=D/'fresh-scalar-only-census.json';cn.write_text(json.dumps(nc,indent=2)+'\n',encoding='utf8');outputs.append(dict(file=cn.relative_to(R).as_posix(),sha256=hs(cn)))
sourcepins={(S/f).relative_to(R).as_posix():h for f,h in M.items()}
dep={f:hs(R/f)for f in['legacy-expected-controller-source/534/source-manifest.json','legacy-expected-controller-source/534/MANIFEST.json','finite_selected_program_census.py','legacy-expected-controller-534-inputs.md']}
out=dict(schema='own-pre-SPEC-finite-controller-source-inputs/1',status='checked_actual_own_selected_program_and_complete_owner_invoice_no_bound',pr=534,own_head=source['own_head'],source_selection_by_literal_verifier=True,complete_historical_global_verifier_PASS_claimed=False,original_phase_engines_freshly_replayed=False,scalar_only_specialization_not_full_native_operator_proof=True,actual_own_source_stages=steps,outputs=outputs,own_invoice=inv,own_owner_receipt=own,own_controller_receipt=control,selected_canonical_file='legacy-expected-controller-source/534/evidence/local/CANONICAL-WORD.json.gz',selected_program_file='legacy-expected-controller-source/534/evidence/local/LOCAL-PROGRAMS.json.gz',own_expected_file='legacy-expected-controller-source/534/EXPECTED.json',retained_previous_invoice=None,derived_gzip_container_normalization='Only generated gzip containers use deterministic mtime0 and OS255; complete decompressed mathematical objects unchanged. All committed primary/native byteobjects remain exact own MANIFEST bytes.',source_sha256=sourcepins,dependency_hashes=dep,checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__)),scope='Own immutable pre-SPEC finite core, literal own verifier and exact committed canonical/program/owner inputs. Actual original prepare/emitter/independent owner+seven controls/invoice run, with NO retained invoice. The complete generated hosted mathematical template equals its own committed template. Fresh scalar-only specialization does not prove operator/phase identities. Original completed phase/data and full required normalized/native/all-size/analytic contracts remain explicit; no numerical cutoff is admitted here.')
(R/'legacy-expected-controller-534-inputs.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('PASS',len(checks),'own534 native/physical source checks;fresh complete invoice;no numerical upper yet')
