"""Own PR32 structured three-axis finite controller and conditional weak early upper."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from collections import Counter
from math import comb,prod
import ast,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={};prefix='32_';pr=32
# Load only pure mathematical/source-extraction utilities, not another PR loop.
utility=ast.parse((R/'copied_center_finite_uppers.py').read_bytes());names={'read','hs','ck','require','enc','halving','funcs','ln_upper','moment_upper'};nodes=[n for n in utility.body if isinstance(n,ast.FunctionDef)and n.name in names];assert {n.name for n in nodes}==names
exec(compile(ast.Module(body=nodes,type_ignores=[]),'copied_finite_pure_utilities','exec'),globals())
M=read('finite-bridge-source-expansion/32-manifest.json');Xtra=read('pr32-structured-finite-source/manifest.json');files={x['path']:'finite-bridge-source-expansion/'+x['file']for x in M};files.update({x['path']:x['file']for x in Xtra});source={}
for x in M+Xtra:
 f=files[x['path']];ck('own_source_'+x['path'],x['head']=='0ef3aeb61f55cc0b321ce6a0ef00acee25cefe52'and hs(f)==x['sha256']);source[f]=x['sha256']
original=read(files['certificates/structured-bulk-network.json']);data=read(files['certificates/structured-bulk-complex-input.json']);replay=read('pr32-structured-finite-source/scalar-replay.json')
ck('own_quoted_selected_value',F(original['kappa'])==F(2504683,200000000000))
ck('own_scalar_factory_replay',replay['status']=='PASS'and replay['script_sha256']==hs('replay_pr32_structured_scalar.py')and all(not r['primary_factory_code_changed']and not r['native_cpp_matching_rerun']and all(r['construction']['scalar_validation'].values())for r in replay['rows']))
for f,h in replay['source_sha256'].items():ck('replayed_source_'+f,hs(f)==h)
ck('actual_three_axes',data['dimensions']==[30,30,40]and data['central_disjoint']==[19,19,35])
for row in data['scalar_circuits']:
 rr=next(r for r in replay['rows']if(r['h'],r['d'])==(row['h'],row['central_disjoint']));c=rr['construction'];ck('own_raw_scalar_'+str(row['h']),all(row[k]==c[v]for k,v in [('h','h'),('v','v'),('c','c'),('q','q'),('baseline_R','R'),('loss','loss')]))
 ck('own_selected_matching_'+str(row['h']),row['R']==row['baseline_R']-row['matched']and row['rank_sum']==sum(i*n for i,n in enumerate(row['histogram'])))
env=dict(require=require,Counter=Counter,comb=comb,prod=prod,Q=F)
funcs(files['scripts/structured_bulk_network.py'],['complex_profile'],env);computed,z=env['complex_profile'](data);profile=dict(computed,child_multiplicities=dict(z),maxchild=max(z))
ck('own_full_complex_profile',all(enc(computed[k])==original['complex']['counts'][k]for k in computed)and dict(original['complex']['child_width_multiplicities'])==dict(z))
bridge=original['finite_bridge'];be=bridge['bit'];env['halving']=halving;funcs(files['scripts/structured_bulk_assembly.py'],['finite_bridge'],env);fresh=env['finite_bridge'](be['m'],be['W'],be['maxchild'],data);ck('whole_own_finite_invoice',enc(fresh)==bridge)
m=profile['m'];W=profile['W'];s=profile['total_rank'];eta=F(original['assembly']['parameters']['a_complex']);mu=1-moment_upper(profile,eta);sem=bridge['semantic'];lit=sem['E'];G=bridge['complex']['scalar_group_upper'];C0=sem['C0'];degree=bridge['rows']['degree'];row=bridge['rows']['coefficient'];D_c=bridge['complex']['halving_degree']
ck('own_strict_native_moment',m==36000 and W==8465185828400 and s==304746555127840000 and eta==F(131,5000000)and 0<mu<1 and s<m*W)
ck('actual_dyadic_scales',[(2*(3-r['central_disjoint']))for r in data['scalar_circuits']]==[-32,-32,-64])
ck('coefficient_range_and_C1',max(r['h']for r in data['scalar_circuits'])<64 and sem['C1']==1 and max(abs(F(k-1,2))for k in range(4))<=1)
inv=-(-(1/mu).numerator//(1/mu).denominator);C=2**32*m**4*((1<<20)*lit+W+s+1)**2*(1+inv)**2*(1+row)**2
ck('complete_own_native_work_guard',C<2**200000 and C0<2**200000)
ck('own_full_stock_degree',degree==108000 and degree>F(51*row,25)and D_c==832)
Q=10**7;delta=F(1,Q);kappa=F(1,1000000);A=4*Q+1;E=1<<56;X=A*E;P=X-8;ep=1-delta;beta=1-3*delta;workexp=32*Q+1000000;reserve_degree=degree*Q
bit=F(original['assembly']['parameters']['a_bit']);ck(prefix+'own_ordinary_bit_admission',bit>kappa)
ns={'__name__':f'own{pr}_weak_outer','__file__':str(R/'pr4535-upper-source/endpoint.py')};exec(compile((R/'pr4535-upper-source/endpoint.py').read_bytes(),'own_copied_endpoint','exec'),ns)
pars=dict(kappa=kappa,tested_saving=eta,complex_uniform_saving=eta,a=kappa+4*delta,b=kappa+5*delta,q=kappa+3*delta,bit_saving=bit,epsilon=ep,beta=beta,r0=delta/10,stop=delta,layout=delta,d=delta);ledger=ns['ledger'](pars)
ck(prefix+'fresh53_correctness',len(ledger['strict_checks'])==54 and {k for k,v in ledger['strict_checks'].items()if v<=0}=={'improvement_over_user_baseline'})
ck(prefix+'fresh3_functional',len(ledger['functional_checks'])==3 and all(v>0 for v in ledger['functional_checks'].values()))
ck(prefix+'fresh9_savings',len(ledger['margins'])==9 and all(v>kappa for v in ledger['margins'].values()))
ck(prefix+'full_stopped_stock',delta*X-10>reserve_degree*(X+3).bit_length()+1000)
ck(prefix+'work_precision_grid_umbrella',delta*E>workexp+200000+1040*(X+3).bit_length()+100)
ck(prefix+'prime_axis_gates',X>=2**54 and X>128*Q and delta*X>(1024*(65+1024*X)).bit_length())
ck(prefix+'comparator_hybrid_domains',P>80 and P>=(1729**12).bit_length()and kappa*X>10)
for tag,v in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(prefix+tag+'_protected',v+F(1,1024)<-F(1,2))
costs=[];xi=ledger['parameters']['cap_xi']
for label,saving,power2,power,extra in [('target_FFT_H',ep*eta*(1-delta),252,2,8),('target_FFT_twiddles',ep,262,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),282,2,12),('dense_diagonals',1-ep+beta,282,1,13),('Strassen_boundaries',F(3,32)+xi-ep,252,1,11),('halos',80-ep-beta,242,1,10),('pointwise_recovery',F(1),262,1,10)]:
 gap=saving-kappa;dg=reserve_degree+extra;bound=E*power+power2+dg*(X+3).bit_length()-X*gap;ck(prefix+label+'_gap',gap>0);ck(prefix+label+'_whole_tail',F(4*dg,X)<gap);ck(prefix+label+'_one_eighth',bound<=-3);costs.append(dict(name=label,saving=str(saving),margin=str(gap),power2=power2,power_B=power,log_degree=dg,base_log2_ratio_upper=str(bound)))
deps=['pr32-structured-finite-upper.md','copied-center-finite-uppers.md','copied_center_finite_uppers.py','pr147-stopped-stock-correction.md','pr147-stopped-stock-correction-peer-review.json','pr147-finite-controller-upper.md','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py','finite-bridge-source-expansion/32-manifest.json','pr32-structured-finite-source/manifest.json','pr32-structured-finite-source/scalar-replay.json','replay_pr32_structured_scalar.py']
out=dict(schema='own-pr32-structured-finite-controller-upper/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',pr=32,own_head='0ef3aeb61f55cc0b321ce6a0ef00acee25cefe52',source_head='0ef3aeb61f55cc0b321ce6a0ef00acee25cefe52',model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',native_coordinate_rank=m,N_is_not_coordinate_rank=True,kappa_record=str(original['kappa']),early_effective_kappa=str(kappa),delta=str(delta),Q=Q,A=str(A),E=str(E),upper_log2log2_integer=str(P),log2log2U=str(P),inputUpper=f'2^(2^{P})',upper=f'2^(2^{P})',meaningful_lower=None,meaningful_lower_bound=None,actual_first_crossing_known=False,record_tail_quantified=False,original_record_hybrid_compatibility=dict(extra_retained_same_XAG_record_realization_contract_required=True,public_size_choice='min total AND+XOR of own originalrecord and own quantified weak early realization',pertype_target='2*n*p^(1-1/1000000)',weighted_ratio_upper='512*p^(-1/1000000)<1',numeric_original_tail_bound=None),native_saving=str(eta),native_moment_gap=str(mu),odd_grid_divisor=1,actual_recovery_scales=['-1/32','-1/32','-1/64'],fixed_rational_macro_pertype_upper='2^20*(w+1)',allsize_work_coefficient_exponent=str(workexp),allsize_work_log_degree=str(reserve_degree),native_scalar_factory_replay=True,native_cpp_matching_and_BIT_CRT_engine_replayed=False,new_outer_parameters=enc(ledger['parameters']),fresh_ledger=enc(ledger),cost_rows=costs,retained_contracts=['Own h30/h40 matched native absolute-phase, simultaneous physical bases, scalar/normalized-wrapper and full public input/output/owned/spectator contracts; original C++ matching and fixed-basis BIT CRT profiler not rerun.','Own all-size complete common-label Gaussian-dyadic supplier, full three-axis physical profile, C1=1 and sequential full row stock.','Same Gaussian/fine-prime/finite-section/boundary/recovery analytic and fixed repaired optimized-GMP correctness/halting contracts.','Preserving original record asymptotic additionally requires own original-record same-XAG realization; no quantified original-tail threshold.'],formal_status='Conditional AI-assisted written derivation and exact source/scalar/rational checks, not Lean or independent human verification.',selected_source=dict(path='certificates/structured-bulk-network.json',file=files['certificates/structured-bulk-network.json'],sha256=hs(files['certificates/structured-bulk-network.json'])),source_sha256=source,dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
(R/'pr32-structured-finite-early-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n');print(json.dumps(dict(checks=len(checks),status=out['status'],P=str(P))))
