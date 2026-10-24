"""Own source bindings and exact critical replays for new native-core bit circuits.
This does not translate Word RAM lookup instructions into Boolean gates.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256,sha1
import gzip,json,subprocess,sys,tempfile
R=Path(__file__).resolve().parent
M=json.loads((R/'late-uniform-source-extraction/source-manifest.json').read_text())['files']
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
checks={}
def ck(n,v):assert v,n;checks[n]=True
allrows=[]
for pr in[4630,4635]:
 prefix='research/native-kappa-30201655/'if pr==4630 else'research/native-provider-lift/'
 files={x['source_path'][len(prefix):]:x for x in M if x['pr']==pr and x['source_path'].startswith(prefix)}
 ownhead=next(iter(files.values()))['head'];bound={}
 for name,x in files.items():
  b=(R/x['local_path']).read_bytes();ck(str(pr)+'_own_'+name,x['head']==ownhead and x['status']=='authenticated_own_head_bytes'and sha256(b).hexdigest()==x['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1']);bound[x['local_path']]=x['sha256']
 get=lambda name:files[name]['local_path']
 names=['critical_check.py','critical_engine.py','majorant-benchmarks.json','raw-profile.json']if pr==4630 else['critical_provider_check.py','critical_engine.py','majorant-benchmarks.json','ARITHMETIC.json','ACTUAL-WORD.json.gz','CONTROLLER.json']
 with tempfile.TemporaryDirectory(prefix='source-native-critical-')as td:
  d=Path(td)
  for name in names:(d/name).write_bytes((R/get(name)).read_bytes())
  cp=subprocess.run([sys.executable,'-X','utf8',names[0]],cwd=d,capture_output=True,text=True,timeout=180)
 ck(str(pr)+'_unmodified_critical_replay',cp.returncode==0)
 report=json.loads(cp.stdout);eta=F(report['native_provider_saving']if pr==4630 else report['uniform_saving'])
 H=10**12;ck(str(pr)+'_own_critical_rank',report['fixed_rank_encoding']==f'2^{H}'and F(report['finite_absorption_log_margin'])>0)
 raw=rd(get('raw-profile.json'if pr==4630 else'ARITHMETIC.json'));T={int(k):v for k,v in raw['targets'].items()};P={int(k):v for k,v in raw['paid'].items()}
 ck(str(pr)+'_actual_full_profile',sum(T.values())==10928 and sum(P.values())==(64620 if pr==4630 else 64404)and sum(k*v for k,v in T.items())-sum(k*v for k,v in P.items())==752 and max(T)==145)
 if pr==4630:
  ledger_source=get('native_ledger.py');ns={'__name__':'own_native_ledger_checked_without_main','__file__':str(R/ledger_source)};exec(compile((R/ledger_source).read_bytes(),ledger_source,'exec'),ns);native_ledger=ns['check']();kap=F(native_ledger['kappa'])
  ck('4630_own_selected_assembly_target',kap==F('0.0030201655')and F(native_ledger['source_provider_saving'])==eta and all(F(v)>0 for v in native_ledger['strict_guards'].values()))
  quoted=rd(get('sources/4535-RESULT.json'));ck('4630_quoted_critical_result',hs(get('sources/4535-RESULT.json'))=='e830f4cab30e70ab02d2ecca283969bd97f3a6925948b61d0eb15df3be831b14'and F(quoted['uniform_saving'])==eta)
  nativepins=rd('pr4470-higher-kappa-bindings/bindings.json')['raw_source_sha256'];ctlfile='native-provider-original-4470-source/CONTROLLER.json'
  original_manifest='native-provider-original-4470-source/manifest.json';original={x['path'].rsplit('/',1)[1]:x for x in rd(original_manifest)};bound[original_manifest]=hs(original_manifest)
  named_original='b9a13c1673e0e9697de410de16e8bbf3207a7363';named_bridge='a6d7237f697185e857090e174c23c1cb22c6563c'
  selector=(R/get('NATIVE-PROVIDER-4535.md')).read_text(encoding='utf8');bridge_proof=get('sources/4535-PROOF.md');bridge_text=(R/bridge_proof).read_text(encoding='utf8')
  bridge_manifest='pr4470-higher-kappa-bindings/download-manifest.json';bridge_rows=rd(bridge_manifest);bound[bridge_manifest]=hs(bridge_manifest)
  proof_rows=[z for z in bridge_rows if z.get('pr')==4535 and z.get('commit')==named_bridge and z.get('path')=='research/critical-root-multiplication/PROOF.md']
  ck('4630_exact_transitive_source_selector',named_original in selector and named_bridge in selector and named_original in bridge_text and len(proof_rows)==1 and proof_rows[0]['sha256']==hs(bridge_proof)=='870cc213c847175f3717db057539686de638594e8c509b2a2daf8d8e72497102')
  ck('4630_five_original_inputs_present',set(original)==set(nativepins))
  for name,h in nativepins.items():
   p='pr4470-higher-kappa-bindings/4535/research/joint-helper-lattice/'+name;z=original[name];raw_original=(R/z['file']).read_bytes()
   ck('4630_original_selected_commit_'+name,z['commit']==named_original and z['path']=='research/joint-helper-lattice/'+name and z['url']=='https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/'+named_original+'/'+z['path']and sha1(b'blob '+str(len(raw_original)).encode()+b'\0'+raw_original).hexdigest()==z['git_blob_sha1'])
   ck('4630_raw_exact_'+name,hs(p)==hs(z['file'])==z['sha256']==h and raw_original==(R/p).read_bytes());bound[p]=h;bound[z['file']]=h
  ck('4630_explicit_RESULT_and_constructor_pins',quoted['source_sha256']['research/joint-helper-lattice/RESULT.json']==nativepins['RESULT.json']and quoted['source_sha256']['research/joint-helper-lattice/native_joint.py']==nativepins['native_joint.py'])
  ck('4630_source_raw_allowance',raw['nonrecursive']['raw_upper']==181098496<raw['nonrecursive']['raw_budget']==10**9)
  proof=get('NATIVE-PROVIDER-4535.md');flow=get('sources/PR4483-DIRECT-MIXED-FLOW.md');unit=rd('pr4470-higher-kappa-bindings/4535/research/joint-helper-lattice/RESULT.json');ck('4630_raw_profile_component',unit['targets']==raw['targets']and unit['paid']==raw['paid'])
 else:
  pars=rd(get('PARAMETERS.json'));kap=F(pars['target']);ck('4635_own_selected_target',kap==F('0.0030217754')and F(pars['provider'])==eta)
  ctlfile=get('CONTROLLER.json');wordfile=get('ACTUAL-WORD.json.gz');wordbytes=gzip.decompress((R/wordfile).read_bytes());word=json.loads(wordbytes)
  comp=rd('pr4610-upper-parameters.json');p0='pr4610-literal-source/research__kappa-round3-warp-20261022__ACTUAL-WORD.json.gz';c0='pr4610-literal-source/research__joint-helper-lattice__CONTROLLER.json'
  ck('4635_exact_selected_native_component',sha256(wordbytes).hexdigest()=='cfcd36b40326d7a5815e1db5313444379b3fb756b27d5201c561574c085cc0dd'and wordbytes==gzip.decompress((R/p0).read_bytes())and(R/ctlfile).read_bytes()==(R/c0).read_bytes())
  ck('4635_own_raw_budget_component',comp['raw_profile']['targets']==raw['targets']and comp['raw_profile']['paid']==raw['paid']and comp['finite_budget']['raw_nonrecursive_upper']==raw['nonrecursive']['raw_scalar_upper']==181098496<comp['finite_budget']['raw_allowance_used']==10**9)
  for p in[p0,c0,'pr4610-upper-parameters.json','pr4610_upper_parameters.py']:bound[p]=hs(p)
  ck('4635_own_component_schema',all(len(es)==21449 for es in word['programs'].values())and len(word['canonical']['start'])==632 and word['canonical']['h']==9)
  proof=get('NATIVE-PROVIDER-4610.md');flow=get('sources/PR4483-DIRECT-MIXED-FLOW.md')
 ctl=rd(ctlfile);adds=[(i,e)for i,e in enumerate(ctl['physical_events'])if e[0]=='ADD'and e[1]!=e[2]and abs(e[3])==1]
 ck(str(pr)+'_actual_distinct_unit_boundary_ADDs',len(adds)>=4 and len({i for i,e in adds[:4]})==4)
 B=sum(T.values());Pcount=sum(P.values());Runit=10**9*(B+Pcount+1)*(10*145**2+10);K=32*(Runit+1)
 ck(str(pr)+'_derived_full_raw_K',181098496+64*(B+Pcount+1)<Runit and(10**9+64)*Runit+32<K*K and K<1<<128)
 text=(R/proof).read_text(encoding='utf8');fl=(R/flow).read_text(encoding='utf8')
 ck(str(pr)+'_explicit_actual_all_column_interface',('all-column'in text.lower()or'all-fiber'in text.lower())and'whole-job'in text.lower()and'phase'in text.lower()and'owned'in text.lower())
 ck(str(pr)+'_strict_rank_chronology_interface','nested widths'in text and'strict rank descent'in text and('caller'in fl or'parent'in fl))
 row=dict(pr=pr,own_head=ownhead,H=str(H),N=f'2^{H}',kappa_record=str(kap),uniform_saving=str(eta),tested_mixed_saving=str(1-F(report['critical_root']['critical_root_interval'][1])),targets={str(k):v for k,v in T.items()},paid={str(k):v for k,v in P.items()},raw_productive_fields=B,raw_paid_calls=Pcount,raw_nonrecursive_allowance=10**9,R_unit=str(Runit),Klog=128,critical_report=report,original_critical_checker_replayed=True,original_native_phase_engine_rerun_here=False,selected_provider_proof=proof,direct_flow_proof=flow,controller_file=ctlfile,literal_boundary_complex_ADD_events=[i for i,e in adds[:4]],source_sha256=bound,critical_checker_source=get(names[0]),new_bit_realization_not_literal_Word_RAM_cost=True)
 allrows.append(row)
out=dict(schema='native-provider-source-to-new-xag-bindings/1',status='passed_own_source_and_unmodified_critical_replays',rows=allrows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name),retained_scope='All-input all-fiber native Gaussian endpoint/absolute phase/owned and typed whole-job compiler identities remain explicit source premises; this job checks exact selected bytes/profile/finite arithmetic, not those universal identities.')
(R/'native-provider-xag-source-bindings.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'own provider source/critical/budget checks')

