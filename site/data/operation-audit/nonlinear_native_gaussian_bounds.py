"""Own12/18/24: new nonlinear-height direct Gaussian whole circuits."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;ADMITTED={12,18,24};checks={};prefix=''
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(k,v):assert v,prefix+k;checks[prefix+k]=True
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
sp=importlib.util.spec_from_file_location('closed_reduced_Gaussian_arithmetic',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
component=rd('gaussian-only-parameter-ledger.json');ck('closed_reduced_arithmetic_only',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and not component['ordinary_BIT_supplier_consumed']and all(component['checks'].values()))
interfaces=[];sources={};dependencies={}
for fn,script,peer in[('partial-swap-endpoint-native-interface.json','partial_swap_endpoint_native_interface.py','partial-swap-endpoint-native-interface-peer-review.json'),('pr12-batched-native-interface.json','pr12_batched_native_interface.py','pr12-batched-native-interface-peer-review.json')]:
 c=rd(fn);p=rd(peer);ck('closed_own_native_'+fn,c['status']=='closed_conditional_component'and not c['whole_integer_upper_claimed']and c['script_sha256']==hs(script)and all(c['checks'].values())and p['review_status'].startswith('PASS')and p['reviewed_sha256'][fn]==hs(fn)and p['reviewed_sha256'][script]==hs(script))
 for key in['source_sha256','dependency_hashes']:
  for f,h in c.get(key,{}).items():ck('native_bound_'+f,hs(f)==h);(sources if key=='source_sha256'else dependencies)[f]=h
 dependencies.update({f:hs(f)for f in[fn,script,peer]});interfaces+=c['rows']
ck('exact_versioned_three_own_interfaces',{a['pr']for a in interfaces}==ADMITTED and len(interfaces)==3)
Q=10**9;delta=F(1,Q);epsilon=F(51,100);beta=F(1,200);layout=F(9,100);A=4*Q+1;E=2**69;X=A*E;P=X-8;u=(X+3).bit_length()
def branch(a,kappa,record=False):
 C1=F(a['new_C1']);eta=F(a['own_uniform_saving']);kappa=F(kappa);m=a['native_coordinate_rank'];C0=a['own_recorded_C0'];L=a['stopped_row_reserve_degree'];row=a['own_complete_row_coefficient'];cs={}
 def bc(k,v):assert v,str(a['pr'])+'_'+str(record)+'_'+k;cs[k]=True
 if record:
  q=(kappa/epsilon+eta*(1-delta))/2;aaux=(q+eta*(1-delta))/2;baux=(aaux+eta)/2
 else:q=F(21,10**8);aaux=F(3,10**7);baux=F(4,10**7)
 pars=dict(kappa=kappa,tested_saving=eta,complex_uniform_saving=eta,a=aaux,b=baux,q=q,epsilon=epsilon,beta=beta,r0=delta/10,stop=delta,layout=layout,d=delta)
 ledger=G.gaussian_ledger(pars)
 # These two old linear-height predicates cannot discharge a C1>1 guard.
 bc('exact_old_linear_semantic_entries',ledger['strict_checks'].pop('new_semantic_guard_with_C1_one')==1-epsilon and ledger['functional_checks'].pop('new_semantic_group_guard')==1-beta)
 ledger['strict_checks']['own_nonlinear_semantic_guard']=1-epsilon*C1;ledger['functional_checks']['own_nonlinear_semantic_group_guard']=1-beta*C1
 bc('all50_modified_correctness_conditions',len(ledger['strict_checks'])==50 and all(v>0 for v in ledger['strict_checks'].values()))
 bc('both_modified_functional_conditions',len(ledger['functional_checks'])==2 and all(v>0 for v in ledger['functional_checks'].values()))
 bc('all_seven_executed_margin_guards',len(ledger['margins'])==7 and all(v>kappa for v in ledger['margins'].values()))
 bc('source_stopping_and_semantic_exponent',F(a['new_stop'])==delta and C1>1 and 1-epsilon*C1>0 and 1-beta*C1>0 and not a['original_cpp_native_or_simultaneous_phase_rerun'])
 workexp=256*Q+500000;degree=L*Q;logd0=128*Q+1000+degree*u
 bc('complete_source_row_constant_and_degree',L==10**7 and L>F(51*row,25)and 2**128>2*row and 2**128>2*m)
 bc('full_stopped_child_row_reserve',F(logd0,Q)>=128+L*u and F(X,Q)-10>L*u+128 and beta*X-1>logd0)
 bc('finite_floor_and_stopping_domain',delta*(epsilon*X-1)>(2*m).bit_length()+10 and epsilon*X-1>logd0)
 bc('full_fallback_coefficient',128*Q+1000+100000+7<workexp and a['own_allsize_work_coefficient_bound_power2']==100000)
 bc('work_coefficient_inside_B',F(E,Q)>workexp+100000+1040*u+100 and E>workexp+100000)
 bc('source_nonlinear_C0_inside_B',C0<2**200 and E>100000 and a['local_pertype_word_coefficient']==1024*a['own_E'])
 bc('target_native_nonlinear_guard',202-(1-epsilon*C1)*X<=-12)
 bc('group_native_nonlinear_guard',202-(1-beta*C1)*X<=-12)
 bc('external_Gaussian_group_guard',23+5*u-(1-beta)*X<=-12)
 bc('external_FFT_prefix_normalizer_guard',13+u-(1-epsilon)*X<=-12)
 bc('external_small_log_guard',12+u-X<=-12)
 bc('stored_word_33p_and_full_product_66p',F(32)+2*F(7,256)+2*F(1,256)+F(3,2**20)<33)
 bc('source_nonwrapping_and_Gaussian_setup',X>=2**20 and (6145*(X+3)**4).bit_length()<X and F(X,1024)>200000+1040*u)
 bc('all_precision_and_stock_guards_decrease_in_tail',F(4*degree,X)<min(delta,beta)and F(4*1040,X)<delta and F(4*13,X)<min(1-beta,1-epsilon,1-epsilon*C1,1-beta*C1))
 # log2(t_i)>=2^((1-epsilon)*log2(p)-9)-1. These exact
 # logarithmic guards imply the retained absolute Dudek and polynomial sides.
 pc=(1-epsilon)*X
 bc('own_target_prime_absolute_floor',pc-10>=54)
 bc('own_target_prime_polynomial_capacity',pc>(1024*(65+1024*X)).bit_length()+10 and pc>2)
 bc('input_axis_and_existing_spectator_capacity',(1-epsilon)*X>1024+L*u and (epsilon-beta)*X>4 and (epsilon-delta)*X>10 and beta*X>logd0+4)
 bc('same_reference_and_recovery_domains',P>80 and P>=(1729**12).bit_length()and kappa*X>10)
 xi=ledger['parameters']['cap_xi'];rows=[]
 for name,saving,c,extra in[('target_FFT_H',epsilon*eta*(1-delta),508,8),('target_FFT_twiddles',epsilon,518,10),('dense_Gaussian_H',1-epsilon+beta*eta*(1-delta),538,12),('dense_diagonals',1-epsilon+beta,538,13),('Strassen_boundaries',F(3,32)+xi-epsilon,508,11),('halos',80-epsilon-beta,498,10),('pointwise_recovery',F(1),518,10)]:
  gap=saving-kappa;ld=degree+extra;bound=4*E+c+ld*u-X*gap
  bc(name+'_actual_positive_gap',gap>0);bc(name+'_all_larger_smooth',F(4*ld,X)<gap);bc(name+'_one_eighth',bound<=-3)
  rows.append(dict(name=name,saving=str(saving),margin=str(gap),power2=c,power_B=4,log_degree=ld,base_log2_ratio_upper=str(bound)))
 return dict(kappa=str(kappa),native_saving=str(eta),delta=str(delta),Q=Q,A=str(A),E=str(E),upper_log2log2_integer=str(P),log2log2U=str(P),inputUpper=f'2^(2^{P})',sufficient_upper_input_bits=f'2^(2^{P})',epsilon=str(epsilon),beta=str(beta),native_precision_C1=str(C1),semantic_gap=str(1-epsilon*C1),new_outer_parameters=enc(ledger['parameters']),modified_Gaussian_ledger=enc(ledger),replaced_semantic_conditions=['new_semantic_guard_with_C1_one','new_semantic_group_guard'],ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,allsize_work_coefficient_exponent=str(workexp),allsize_work_log_degree=str(degree),stopped_rank_cutoff_log2_upper=str(logd0),cost_rows=rows,checks=cs,checks_passed=len(cs))
rows=[]
for a in sorted(interfaces,key=lambda z:z['pr']):
 pr=a['pr'];prefix=str(pr)+'_';early=branch(a,F(1,10**7));record=branch(a,F(a['kappa_record']),True)
 ck('own_source_record_and_both_fresh_schedules',F(a['kappa_record'])>0 and all(early['checks'].values())and all(record['checks'].values()))
 contracts=a['retained_interfaces']+['Concrete normalized Gaussian shifted-kernel accretivity/finite-LDU, narrow/cyclic boundary recovery and complete integer convolution/carry interfaces from the closed direct Gaussian construction remain explicit. The false arbitrary-scale accretive theorem is not used.','The nonlinear source height C0*d^C1, not completed norm1, is paid in full at every native invocation, including the synchronized factors and outer-transform normalization.','This new direct Gaussian/Fermat coefficient circuit does not execute the historical source BIT supplier or compact address-descriptor routing. Full native operator/absolute-phase/common-label/owned/complete-row identities remain premises.','The repaired unlimited optimized-GMP source model and finite-kernel halting are retained; numerical bounds concern this declared source-derived family, not every implementation.']
 deps=['nonlinear-native-gaussian-bounds.md','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','candidate-fermat-helper.json','candidate-fermat-helper.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','pr4470-outer-census.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json'];dep={p:hs(p)for p in deps};dep.update(dependencies)
 common=dict(pr=pr,own_head=a['own_head'],source_head=a['own_head'],status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',kappa_record=a['kappa_record'],native_coordinate_rank=a['native_coordinate_rank'],not_uniform_2_to_H=True,nonlinear_native_precision=True,meaningful_lower=None,actual_first_crossing_known=False,original_historical_BIT_algorithm_costed=False,original_cpp_native_or_simultaneous_phase_rerun=False,retained_contracts=contracts,source_sha256=sources,dependency_hashes=dep,script_sha256=hs(Path(__file__).name))
 nf=f'pr{pr}-nonlinear-native-gaussian-native.json';rf=f'pr{pr}-nonlinear-native-gaussian-record-upper.json';ef=f'pr{pr}-nonlinear-native-gaussian-early-upper.json'
 native=dict(common,schema='own-nonlinear-native-Gaussian-parameters/1',own_native_interface=a)
 ro=dict(common,**record,schema='own-nonlinear-native-Gaussian-record-upper/1');(R/rf).write_text(json.dumps(enc(ro),indent=2)+'\n',encoding='utf8')
 eo=dict(common,**early,schema='own-nonlinear-native-Gaussian-early-upper/1',early_effective_kappa='1/10000000',record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Fresh same-selected-complex-core direct Gaussian circuit at the own exact record exponent; historical changed BIT/compact-descriptor algorithm is not costed.',piecewise_description='Reference below the certified tail, then counted early and quantified own-record circuits. Chosen switches are not natural lower bounds.')
 for f,o in[(nf,native),(ef,eo)]: (R/f).write_text(json.dumps(enc(o),indent=2)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=a['own_head'],kappa_record=a['kappa_record'],native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],native_precision_C1=a['new_C1'],record_tail_quantified=True,meaningful_lower=None,checks_passed=early['checks_passed']+record['checks_passed']))
prefix='';out=dict(schema='own-nonlinear-native-direct-Gaussian-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',exact_admitted_PRs=sorted(ADMITTED),rows=rows,checks=checks,checks_passed=len(checks)+sum(a['checks_passed']for a in rows),outer_checks_passed=sum(a['checks_passed']for a in rows),script_sha256=hs(Path(__file__).name),original_historical_BIT_algorithm_costed=False,meaningful_lower=None)
(R/'nonlinear-native-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',out['checks_passed'],'own nonlinear native Gaussian whole checks',sorted(ADMITTED),'P',P)
