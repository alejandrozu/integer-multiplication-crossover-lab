"""Own4713 exact source/critical joins for a new Gaussian-only bit realization."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256,sha1
import json,gzip,subprocess,sys,tempfile
R=Path(__file__).resolve().parent

def rd(p):return json.loads((R/p).read_bytes())
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
checks={}
def ck(n,v):assert v,n;checks[n]=True
M=rd('late-uniform-source-extraction/source-manifest.json')['files'];own=[x for x in M if x['pr']==4713];head=own[0]['head'];prefix='research/native-wordram-tightening/';files={x['source_path'][len(prefix):]:x for x in own if x['source_path'].startswith(prefix)};bound={}
for x in own:
 b=(R/x['local_path']).read_bytes();ck('own_primary_'+x['source_path'],x['head']==head and x['status']=='authenticated_own_head_bytes'and hs(x['local_path'])==x['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1']);bound[x['local_path']]=x['sha256']
get=lambda n:files['transfer/'+n]['local_path'];pins=rd(get('INPUT-PINS.json'))
for name,h in pins.items():ck('own_selected_transfer_pin_'+name,hs(get(name))==h)
ns={'__name__':'own_native_lift_parameters','__file__':str(R/get('native_lift.py'))};exec(compile((R/get('native_lift.py')).read_bytes(),get('native_lift.py'),'exec'),ns)
result=rd(get('RESULT.json'));kap=F(result['word_ram_kappa']);latest=rd(get('LATEST-ARITHMETIC.json'));eta=F(latest['compiler']['uniform_saving']);H=int(latest['compiler']['H']);native=ns['choose'](eta,kap)
ck('own_source_record_and_rank',kap==F(15108879,5000000000)and eta==F(1057621533,350000000000)and H==38569300000000000 and all(F(x)>0 for x in native['guards'].values()))
names=['provider_rebind.py','critical_engine.py','majorant-benchmarks.json','ARITHMETIC.json','LATEST-ARITHMETIC.json','ACTUAL-WORD.json.gz','CONTROLLER.json']
with tempfile.TemporaryDirectory(prefix='own4713-native-critical-')as td:
 d=Path(td)
 for name in names:(d/name).write_bytes((R/get(name)).read_bytes())
 cp=subprocess.run([sys.executable,'-X','utf8',names[0]],cwd=d,capture_output=True,text=True,timeout=180)
ck('original_critical_checker_unmodified',cp.returncode==0)
report=json.loads(cp.stdout);ck('own_critical_exact_original_receipt',report==result['provider']and report['fixed_rank_encoding']==f'2^{H}'and F(report['finite_absorption_log_margin'])==F(6611668,5))
raw=rd(get('ARITHMETIC.json'));T={int(k):v for k,v in raw['targets'].items()};P={int(k):v for k,v in raw['paid'].items()};ck('own_profile_latest_identical',all(raw[k]==latest[k]for k in['targets','paid','local_paid','local_helpers'])and sum(T.values())==10928 and sum(P.values())==64404 and sum(k*v for k,v in T.items())-sum(k*v for k,v in P.items())==752)
comp=rd('pr4610-upper-parameters.json');w0='pr4610-literal-source/research__kappa-round3-warp-20261022__ACTUAL-WORD.json.gz';c0='pr4610-literal-source/research__joint-helper-lattice__CONTROLLER.json';wordbytes=gzip.decompress((R/get('ACTUAL-WORD.json.gz')).read_bytes())
ck('own_selected_exact_native_component',sha256(wordbytes).hexdigest()=='cfcd36b40326d7a5815e1db5313444379b3fb756b27d5201c561574c085cc0dd'and wordbytes==gzip.decompress((R/w0).read_bytes())and(R/get('CONTROLLER.json')).read_bytes()==(R/c0).read_bytes())
ck('actual_own_raw_budget_component',comp['raw_profile']['targets']==raw['targets']and comp['raw_profile']['paid']==raw['paid']and comp['finite_budget']['raw_nonrecursive_upper']==181098496<comp['finite_budget']['raw_allowance_used']==10**9)
for p in['pr4610-upper-parameters.json','pr4610_upper_parameters.py',w0,c0]:bound[p]=hs(p)
B0=sum(T.values());P0=sum(P.values());RU=10**9*(B0+P0+1)*(10*145**2+10);K=32*(RU+1);ck('derived_own_raw_K',181098496+64*(B0+P0+1)<RU and(10**9+64)*RU+32<K*K and K<1<<128)
ctl=rd(get('CONTROLLER.json'));adds=[i for i,e in enumerate(ctl['physical_events'])if e[0]=='ADD'and e[1]!=e[2]and abs(e[3])==1];ck('four_actual_public_boundary_ADDs',len(adds)>=4)
proof=files['transfer/NATIVE-TRANSFER.md']['local_path'];text=(R/proof).read_text(encoding='utf8');ck('own_required_native_semantics_explicit',all(s in text for s in['all-fiber','whole-job','owned','chronological','cfcd36b40326d7a5815e1db5313444379b3fb756b27d5201c561574c085cc0dd','20bb93cd990d2ff683e4d0fc56b87a42cd5d3296']))
row=dict(pr=4713,own_head=head,H=str(H),N=f'2^{H}',kappa_record=str(kap),uniform_saving=str(eta),tested_mixed_saving=str(1-F(report['critical_root']['critical_root_interval'][1])),targets={str(k):v for k,v in T.items()},paid={str(k):v for k,v in P.items()},raw_productive_fields=B0,raw_paid_calls=P0,raw_nonrecursive_allowance=10**9,R_unit=str(RU),Klog=128,critical_report=report,original_critical_checker_replayed=True,original_native_phase_engine_rerun_here=False,selected_provider_proof=proof,controller_file=get('CONTROLLER.json'),literal_boundary_complex_ADD_events=adds[:4],source_sha256=bound,critical_checker_source=get('provider_rebind.py'),new_bit_realization_not_literal_Word_RAM_cost=True)
out=dict(schema='native-provider-source-to-new-xag-bindings/1',status='passed_own_source_and_unmodified_critical_replays',rows=[row],checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name),retained_scope='Own actual all-input/all-fiber required Gaussian endpoint/phase/owned and typed whole-job chronological compiler identities are explicit source premises; no native WordRAM operation tariff or division-free execution theorem is transferred.')
(R/'pr4713-native-xag-source-bindings.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'own4713 source/critical bindings')
