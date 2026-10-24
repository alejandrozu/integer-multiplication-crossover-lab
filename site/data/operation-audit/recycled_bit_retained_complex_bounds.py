"""Own150/151 retained complex core, corrected finite lemma and Gaussian cost rows."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from collections import Counter
from math import prod
import ast,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={};prefix=''
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(k,v):assert v,prefix+k;checks[prefix+k]=True
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x)for x in v]
 return v
heads={150:'40d4038760ebb6d6d3d702ce88fa3645de29f0c1',151:'5a46ac37ae2e2f8f75637cb2cf6b9d0b36afc436'}
claims={150:F(471809569,10**12),151:F(472154791,10**12)}
original=rd('early-native-producer-source/149-manifest.json');reference=rd('pr147-source-native-profile.json')
component=rd('gaussian-only-parameter-ledger.json');ck('closed_exact_reduced_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values()))
sp=importlib.util.spec_from_file_location('own_recycled_gaussian_ledger',R/'gaussian_only_parameter_ledger.py');reduced=importlib.util.module_from_spec(sp);sp.loader.exec_module(reduced)
deps=['recycled-bit-retained-complex-bounds.md','replay_recycled_bit_selected_complex.py','early-native-producer-source/149-manifest.json','pr149-finite-controller-upper.md','pr149-finite-controller-early-upper.json','pr149-finite-controller-peer-review.json','pr147-source-native-profile.json','pr147-stopped-stock-correction.md','pr147-stopped-stock-corrected-upper.json','pr147-stopped-stock-correction-peer-review.json','pr147-finite-gate-refined-upper.json','finite-controller-gate-refinement.md','finite-controller-gate-refinement-peer-review.json','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','candidate-fermat-helper.json','fixed-small-rational-xag.json','fixed-exact-division-via-multiply.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
for p,h in component['dependency_hashes'].items():ck('reduced_component_'+p,hs(p)==h)
rows=[]
for pr,head in heads.items():
 prefix=str(pr)+'_';mf=f'recycled-bit-complex-source/{pr}-manifest.json';M=rd(mf);files={a['path']:a['file']for a in M};own_checks_start=len(checks)
 for a in M:ck('own_primary_'+a['path'],a['head']==head and a['pr']==pr and a['status']=='authenticated_own_head_primary_bytes'and hs(a['file'])==a['sha256']and '/'+head+'/'in a['primary_url'])
 for a in original:ck('entire_selected_complex_producer_closure_'+a['path'],hs(files[a['path']])==a['sha256'])
 nrfile=f'recycled-bit-complex-source/{pr}-fresh-selected-complex-replay.json';nr=rd(nrfile);pfile=f'recycled-bit-complex-source/{pr}-fresh-price-replay.json';price=rd(pfile)
 for label,o in [('complex',nr),('price',price)]:
  ck(label+'_actual_own_source_replay',o['pr']==pr and o['own_head']==head and o['returncode']==0 and o['primary_code_changed']is False and o['source_manifest_sha256']==hs(mf)and o['script_sha256']==hs('replay_recycled_bit_selected_complex.py'))
  for p,h in o['source_sha256'].items():ck(label+'_source_'+p,hs(p)==h)
 selected=rd(files['certificates/paired-cube-complex-input.json']);ck('fresh_selected_complete_complex_object',json.loads(nr['stdout'])['selected']==selected and nr['selected_matches_own_committed_object']and not nr['changed_bit_geometry_or_wholeword_replayed'])
 ck('original_own_claim_price_exact',F(price['price']['kappa'])==claims[pr]and not price['original_bit_scalar_frame_or_geometric_replay_performed'])
 selector=(R/files['research/bit-reuse-147/price147.py']).read_text(encoding='utf8')
 ck('actual_explicit_complex_selection',"ROOT / 'certificates' / 'paired-cube-complex-input.json'"in selector and 'pcn.complex_certificate(crow)'in selector and 'pcn.finite_bridge(phase, None, crow)'in selector and 'pcn.assembly(assembly_bit, pcn.AC, bridge'in selector)
 if pr==150:ck('own_selected_original_record',F(rd(files['research/bit-reuse-147/expected.json'])['kappa'])==claims[pr])
 else:ck('own_selected_original_record','Q(472154791, 10**12)'in(R/files['research/gauge-recycling/verify.py']).read_text(encoding='utf8')and F(price['price']['atom'])==F(473,10**6))
 env=dict(Q=F,Counter=Counter,prod=prod,require=lambda condition,message:ck(message,condition),GRID=1<<120,COARSE=F(4617656,10**10),ATOM=F(1,1000),OLD=F(384599,10**10),AC=F(4856569,10**10));env['AB']=(1-env['ATOM'])*env['COARSE']+env['ATOM']*env['OLD']
 tree=ast.parse((R/files['scripts/paired_cube_network.py']).read_bytes());literal={'Q':F};assign=[n for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id in {'AC','COARSE','ATOM','OLD','AB'}for t in n.targets)];exec(compile(ast.Module(body=assign,type_ignores=[]),'own_complex_literals','exec'),literal)
 for key in ['AC','COARSE','ATOM','OLD','AB']:ck('own_network_literal_'+key,literal[key]==env[key])
 for p,names in [('scripts/three_stage_cover_network.py',{'up','log_upper','exp_upper'}),('scripts/structured_bulk_assembly.py',{'halving'}),('scripts/paired_cube_network.py',{'clean','shared_profile','exact_moment','complex_certificate','finite_bridge'})]:
  tree=ast.parse((R/files[p]).read_bytes());fn=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in names];ck(p+'_exact_functions',len(fn)==len(names));exec(compile(ast.Module(body=fn,type_ignores=[]),p,'exec'),env)
 c=env['complex_certificate'](selected);b=env['finite_bridge'](c,None,selected);m=72;eta=env['AC'];mu=1-c['moment_upper'];inverse=-(-(1/mu).numerator//(1/mu).denominator)
 for key,value in [('full_role_count_W',c['W']),('paid_rank_mass_s',c['total_rank']),('G',b['complex']['finite_group_router_upper']),('E',b['semantic']['E']),('C0',b['semantic']['C0'])]:ck('own_complete_native_constant_'+key,int(reference[key])==value)
 ck('own_rank72_fourth_power_halving',c['counts']['m']==72 and c['counts']['maxchild']==60 and 2*60**4<72**4)
 ck('own_complete_semantic_row_and_gap',b['semantic']['C1']==1 and b['rows']['coefficient']==20445 and b['rows']['degree']==70000 and mu>F(2,10**10)and inverse<2**33)
 ck('own_allsize_coefficient',2**32*m**4*(b['semantic']['E']+c['W']+c['total_rank']+1)**2*(1+inverse)**2*(1+20445)**2<2**100000)
 ck('own_odd_grid_guard',2*m*b['complex']['finite_group_router_upper']+b['semantic']['C0']<2**100000)
 params=[]
 for kind,kappa,Q,A,E in [('early-upper',F(1,5000),10000,10001,((1<<54)+10000)//10001),('record-upper',claims[pr],10**9,4000000001,2**66)]:
  delta=F(1,Q);ep=1-delta;beta=1-3*delta;X=A*E;P=X-8;u=(X+3).bit_length();a,bb,q=(F(301,10**6),F(302,10**6),F(3,10000))if kind=='early-upper'else(kappa+4*delta,kappa+5*delta,kappa+3*delta)
  pars=dict(kappa=kappa,tested_saving=eta,complex_uniform_saving=eta,a=a,b=bb,q=q,epsilon=ep,beta=beta,r0=delta/10,stop=delta,layout=delta,d=delta);ledger=reduced.gaussian_ledger(pars)
  ck(kind+'_fresh50_correctness',len(ledger['strict_checks'])==50 and all(v>0 for v in ledger['strict_checks'].values()))
  ck(kind+'_fresh2_functional',len(ledger['functional_checks'])==2 and all(v>0 for v in ledger['functional_checks'].values()))
  ck(kind+'_fresh7_savings',len(ledger['margins'])==7 and all(v>kappa for v in ledger['margins'].values()))
  ck(kind+'_no_BIT_parameter','bit_saving'not in pars)
  workexp=32*Q+500000;degree=70000*Q
  ck(kind+'_full_stopped_reserve',delta*X-10>degree*u+1000)
  ck(kind+'_complete_work_precision',delta*E>workexp+220000+1040*u+100)
  ck(kind+'_prime_target_capacity',X>=2**54 and X>128*Q and delta*X>(1024*(65+1024*X)).bit_length())
  ck(kind+'_same_reference_recovery',P>80 and P>=(1729**12).bit_length()and kappa*X>10)
  for tag,v in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(kind+'_'+tag+'_protected',v+F(1,1024)<-F(1,2))
  xi=ledger['parameters']['cap_xi'];costs=[]
  for name,saving,power2,power,extra in [('target_FFT_H',ep*eta*(1-delta),252,2,8),('target_FFT_twiddles',ep,262,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),282,2,12),('dense_diagonals',1-ep+beta,282,1,13),('Strassen_boundaries',F(3,32)+xi-ep,252,1,11),('halos',80-ep-beta,242,1,10),('pointwise_recovery',F(1),262,1,10)]:
   gap=saving-kappa;d=degree+extra;bound=E*power+power2+d*u-X*gap;ck(kind+'_'+name+'_positive_gap',gap>0);ck(kind+'_'+name+'_smooth_tail',F(4*d,X)<gap);ck(kind+'_'+name+'_one_eighth',bound<=-3);costs.append(dict(name=name,saving=str(saving),margin=str(gap),power2=power2,power_B=power,log_degree=d,base_log2_ratio_upper=str(bound)))
  params.append(dict(kind=kind,kappa=str(kappa),early_effective_kappa='1/5000'if kind=='early-upper'else None,delta=str(delta),Q=Q,A=str(A),E=str(E),upper_log2log2_integer=str(P),log2log2U=str(P),inputUpper=f'2^(2^{P})',upper=f'2^(2^{P})',new_outer_parameters=enc(ledger['parameters']),reduced_ledger=enc(ledger),cost_rows=costs,allsize_work_coefficient_exponent=str(workexp),allsize_work_log_degree=str(degree)))
 dep={p:hs(p)for p in deps+[mf,nrfile,pfile]};source={a['file']:a['sha256']for a in M};base=dict(pr=pr,own_head=head,source_head=head,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(claims[pr]),native_coordinate_rank=72,N_is_not_coordinate_rank=True,native_saving=str(eta),native_moment_gap=str(mu),full_selected_complex_producer_rerun=True,original_BIT_producer_rerun=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,meaningful_lower_bound=None,actual_first_crossing_known=False,source_equivalent_numeric_realization=True,source_correspondence_scope='All38 own selected complex producer/input/bridge closure bytes match the named independently counted native; actual own-head complex producer freshly replayed. Original changed bit words are distinct and not replayed or executed by this new direct Gaussian realization.',retained_contracts=rd('pr147-finite-gate-refined-upper.json')['retained_contracts'],source_sha256=source,dependency_hashes=dep,checks_passed=len(checks)-own_checks_start,checks={k:v for k,v in checks.items()if k.startswith(prefix)},script_sha256=hs(Path(__file__).name))
 record=params[1];tailfile=f'pr{pr}-retained-complex-record-upper.json';tail=dict(base,**record,schema='own-retained-complex-record-upper/1');(R/tailfile).write_text(json.dumps(enc(tail),indent=2)+'\n',encoding='utf8')
 early=dict(base,**params[0],schema='own-retained-complex-early-upper/1',record_tail_quantified=True,record_tail_certificate=tailfile,record_tail_certificate_sha256=hs(tailfile),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Own original claim exponent is quantified by the new counted direct Gaussian realization of its own selected complex core, not by replay of the historical changed bit implementation.',piecewise_description='Repaired GMP below early gate, own counted early direct Gaussian branch, then own counted same-core record branch. No switch is a natural lower bound.')
 earlyfile=f'pr{pr}-retained-complex-early-upper.json';(R/earlyfile).write_text(json.dumps(enc(early),indent=2)+'\n',encoding='utf8')
 native=dict(base,schema='own-retained-complex-native-parameters/1',source_complex_certificate=enc(c),source_finite_bridge=enc(b),own_original_bit_row_price=price['price'],record_tail_quantified=True)
 nativefile=f'pr{pr}-retained-complex-native-parameters.json';(R/nativefile).write_text(json.dumps(enc(native),indent=2)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=head,kappa_record=str(claims[pr]),native_certificate=nativefile,early_upper_certificate=earlyfile,record_upper_certificate=tailfile,upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None))
prefix='';ck('exact_two_own_selected_complex_cases',set(x['pr']for x in rows)=={150,151})
out=dict(schema='own-retained-complex-source-cost-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,script_sha256=hs(Path(__file__).name));(R/'recycled-bit-retained-complex-bounds.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own150/151 selected-complex and fresh cost checks',flush=True)
