"""Fresh XAG bit circuits for own4630/4635 algebraic providers, not WordRAM cost translation."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,importlib.util
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True

def rd(p):return json.loads((R/p).read_bytes())
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return[enc(v)for v in x]
 return x
sp=importlib.util.spec_from_file_location('closed_gaussian',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
bind=rd('native-provider-xag-source-bindings.json');assert bind['status']=='passed_own_source_and_unmodified_critical_replays'and bind['script_sha256']==hs('native_provider_xag_source_bindings.py')
allchecks={};summary=[]
for own in bind['rows']:
 pr=own['pr'];checks={}
 def ck(n,v):assert v,f'{pr}_{n}';checks[n]=True
 for p,h in own['source_sha256'].items():ck('own_source_'+p,hs(p)==h)
 ck('own_exact_source_critical_H',pr in[4630,4635]and own['original_critical_checker_replayed']and own['H']=='1000000000000'and not own['original_native_phase_engine_rerun_here'])
 H=int(own['H']);eta=F(own['uniform_saving']);kap=F(own['kappa_record']);tested=F(own['tested_mixed_saving']);T={int(k):v for k,v in own['targets'].items()};P={int(k):v for k,v in own['paid'].items()};Braw=sum(T.values());Praw=sum(P.values());k=128
 Runit=10**9*(Braw+Praw+1)*(10*145**2+10);K=32*(Runit+1)
 ck('actual_native_budget_and_K',Runit==int(own['R_unit'])and own['raw_nonrecursive_allowance']==10**9 and K<1<<k and(10**9+64)*Runit+32<K*K)
 ck('positive_raw_surplus',sum(r*v for r,v in T.items())-sum(r*v for r,v in P.items())==752 and max(T)==145 and min(T)==4)
 ck('integer_descent_and_normalized_inventory',H>73 and(512*(H+3)).bit_length()+H+2<2*H and K*K>512*(H+3))
 Eguard=23+2*k+(H+1).bit_length()+H+1
 ck('own_suspended_context_guard',Eguard>H+2*k and tested>eta>kap>0)
 deps=['native-provider-derived-xag-costs.md','native-provider-xag-source-bindings.json','native_provider_xag_source_bindings.py','gaussian-only-parameter-ledger.md','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger.json','gaussian-only-parameter-ledger-peer-review.json','candidate-fermat-helper.json','pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4470-higher-kappa-bindings/bindings.json','pr4610-upper-parameters.json']
 common=checks.copy();outbranches={}
 for record in[True,False]:
  checks=common.copy();Q=10**12 if record else 10000;delta=F(1,Q);keff=kap if record else F(1,500);A=4*Q+1 if record else Q+1;ep=1-delta;beta=1-3*delta
  a,b,q=(keff+4*delta,keff+5*delta,keff+3*delta)
  pars=dict(kappa=keff,tested_saving=tested,complex_uniform_saving=eta,a=a,b=b,q=q,epsilon=ep,beta=beta,r0=delta/10,stop=delta,layout=delta,d=delta);led=G.gaussian_ledger(pars)
  ck('all50_actual_native_guards',all(v>0 for v in led['strict_checks'].values()));ck('both_actual_functional',all(v>0 for v in led['functional_checks'].values()));ck('all7_actual_margins',all(v>keff for v in led['margins'].values()))
  ck('own_native_stopped_funding',eta>b>a>q>keff and(1-delta)*b>a)
  E=Q*(H+1)+2*H+2*k+Eguard+179200000000+1048576+1000;X=A*E;Y=X-8
  ck('own_complete_semantic_and_precision_gate',delta*E>44 and A*delta>=1+delta and E>Eguard)
  ck('actual_full_work_and_global_base',48+2*k+2*H<E and 12+Q*(H+1)<E and 6+4*H<Q*(H+1))
  ck('smooth_precision_log',E.bit_length()+A.bit_length()+3<F(E,1024)and F(1040,X)<delta/2)
  ck('actual_absolute_prime_and_capacity',X>128*Q and delta*X-10>=54 and delta*X>(1024*(65+1024*X)).bit_length()and delta*X>2)
  ck('complete_native_existing_array',delta*X>10 and(ep-beta)*X>1 and ep*X>Q*(H+1)+2)
  ck('reference_tariff_domains',Y>80 and Y>=(1729**12).bit_length()and A*keff>8)
  for name,r in[('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(name+'_protected',r+F(1,1024)<-F(1,2))
  xi=led['parameters']['cap_xi'];rows=[]
  for name,s,c,powB,degree in[('target_FFT_H',ep*eta*(1-delta),60,2,0),('target_FFT_twiddles',ep,198,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),90,2,4),('dense_diagonals',1-ep+beta,218,1,13),('Strassen_boundaries',F(3,32)+xi-ep,188,1,11),('halos',80-ep-beta,178,1,10),('pointwise_recovery',F(1),198,1,10)]:
   gap=s-keff;bound=powB*E+c+degree*(X+3).bit_length()-X*gap
   ck(name+'_positive_gap',gap>0);ck(name+'_eighth_budget',bound<=-3);ck(name+'_smooth_decreasing',F(4*max(1,degree),X)<gap);rows.append(dict(name=name,saving=str(s),margin=str(gap),power2=c,power_B=powB,log_degree=degree,base_log2_ratio_upper=str(bound)))
  o=dict(schema='native-provider-new-xag-bit-upper/1',status='closed_conditional_sufficient_upper_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=own['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',branch='record'if record else'early',kappa_record=str(kap),effective_kappa=str(keff),early_effective_kappa=None if record else str(keff),H=str(H),N=f'2^{H}',native_saving=str(eta),Q=Q,delta=str(delta),A=str(A),E=str(E),Eguard=str(Eguard),upper_log2log2_integer=str(Y),inputUpper=f'2^(2^{Y})',sufficient_upper_input_bits=f'2^(2^{Y})',new_outer_parameters=enc(led['parameters']),cost_rows=rows,compiler_interfaces=dict(Klog=128,derived_R_unit=str(Runit),rank_descent='strict positive integer; simultaneous depth<=N',mixed_depth='<=H',inventory_log2_upper='512*N*(H+3)',normalized_fresh_work='G/W<K²N',semantic_context_guard_log2=str(Eguard),active_full_H_coefficient='2^48*K²*N²',global_stock_cutoff='max(64*(ceil(log2W)+1)^2,(2N)^Q)'),new_source_core_bit_realization=True,literal_Word_RAM_cost_transferred=False,ordinary_BIT_supplier_consumed=False,actual_first_crossing_known=False,all_PR_implementations=False,original_critical_checker_replayed=True,original_native_phase_engine_rerun_here=False,source_sha256=own['source_sha256'],dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks.copy(),retained_contracts=['Own actual selected arbitrary-input required Gaussian endpoint/absolute-phase/all-fiber/owned/spectator and bounded finite-Clifford monomial identities; same raw component recovered by exact source hashes, not a fresh universal native proof.','Own chronological source/complement/exit complete integer compiler, ready barriers and nested widths with strict rank descent, and own freshly replayed critical majorant.','Concrete normalized Gaussian/finite-LDU/narrow-gap/cyclic-border/fine-prime/exact-recovery and fixed repaired optimizedGMP correctness/finite-kernel halting.'],formal_status='Conditional AI-assisted written mathematics and exact source/arithmetic checks, not Lean or independent human review.')
  outbranches['record'if record else'early']=o
 rfile=f'pr{pr}-derived-xag-record-upper.json';(R/rfile).write_text(json.dumps(outbranches['record'],indent=2)+'\n');early=outbranches['early'];early.update(record_tail_quantified=True,record_tail_certificate=rfile,record_tail_certificate_sha256=hs(rfile),record_tail_upper_log2log2_integer=outbranches['record']['upper_log2log2_integer'],record_tail_scope='New explicit Gaussian/Fermat bit realization of same own algebraic native core; no literal WordRAM lowering claim.')
 (R/f'pr{pr}-derived-xag-early-upper.json').write_text(json.dumps(early,indent=2)+'\n')
 ck('own_literal_boundary_floor',len(own['literal_boundary_complex_ADD_events'])==4 and 8*(1<<69)==1<<72)
 lower=dict(schema='native-provider-derived-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=own['own_head'],model=early['model'],baseline_extension_id=early['baseline_extension_id'],H=str(H),N=f'2^{H}',kappa=str(kap),active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),scope='Derived bit-circuit enhancement family retaining own complete unreduced raw controller/native boundary on full fields/spectators, width at least two when active; identical optimizedGMP when inactive. Not all WordRAM or bit implementations.',statistic='Earliest possible strict win in this own-source literal bit enhancement family',all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,source_sha256=own['source_sha256'],dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),retained_contracts=early['retained_contracts'])
 (R/f'pr{pr}-derived-xag-literal-lower.json').write_text(json.dumps(lower,indent=2)+'\n');summary.append(dict(pr=pr,H=str(H),earlyP=early['upper_log2log2_integer'],recordP=outbranches['record']['upper_log2log2_integer'],lower=lower['input_bits']));allchecks.update({str(pr)+'_'+n:v for n,v in checks.items()})
out=dict(schema='native-provider-new-xag-bit-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=summary,checks_passed=len(allchecks),checks=allchecks,script_sha256=hs(Path(__file__).name));(R/'native-provider-derived-xag-costs.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary,indent=2));print('PASS',len(allchecks))

