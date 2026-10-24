"""Own PR4413 rebalance: fresh H-specific p3 guard, costs and literal lower."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import importlib.util,json
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [enc(v)for v in o]
    return o
sp=importlib.util.spec_from_file_location('closed_gaussian_ledger',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
component=rd('gaussian-only-parameter-ledger.json');assert component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')
allchecks={};outputs=[]
for pr in[4413]:
    checks={}
    def ck(n,v):assert v,f'{pr}: {n}';checks[n]=True
    bindingfile=f'pr{pr}-p3-rebalance-source-bindings.json';binding=rd(bindingfile);own=binding['rows'][0]
    ck('own_source_binding',binding['status']=='passed_own_source_and_finite_checker_bindings'and own['pr']==pr and binding['script_sha256']==hs('pr4413_p3_rebalance_source_bindings.py'))
    ck('own_binding_all31_checks',binding['checks_passed']==31 and all(binding['checks'].values()))
    for group in['source_sha256','dependency_sha256']:
        for p,h in binding[group].items():ck('own_bound_'+p,hs(p)==h)
    replayfile='pr4413-source-fresh-replay.json';replay=rd(replayfile)
    ck('own_fresh_replay_binding',hs(replayfile)==binding['dependency_sha256'][replayfile])
    ck('own_source_manifest_binding',hs(own['own_source_manifest'])==binding['dependency_sha256'][own['own_source_manifest']])
    ck('own_untouched_finite_replay',replay['status']=='passed_unchanged_own_finite_checker'and not replay['source_modified']and replay['report']['ranks']['complex']['H1']==int(own['H']))
    H=int(own['H']);eta=F(own['actual_uniform_saving']);kap=F(own['kappa_record']);k=128;m=57;g=H;J=m*H
    T={int(k):v for k,v in own['targets'].items()};Ppaid={int(k):v for k,v in own['paid'].items()};Braw=sum(T.values());Praw=sum(Ppaid.values())
    ck('own_raw_profile_and_surplus',(Braw,Praw,sum(k*v for k,v in T.items()),sum(k*v for k,v in Ppaid.items()))==(2242,25394,37317,37093)and min(T)==6 and max(T)==57 and max(Ppaid)==5)
    ck('strict_own_supplier',0<kap<eta<1 and own['N']==f'2^{H}'and H>73)
    Runit=10**9*(Braw+Praw+1)*(10*73**2+10);K=32*(Runit+1)
    ck('actual_own_complete_native_budget',own['native_complete_G']==1494376 and own['Klog']==128 and K<1<<k and 1494376+64*(Braw+Praw+1)<Runit and (10**9+64)*Runit+32<K*K)
    ck('own_logical_and_transient_frames',own['native_coordinate_rank']==57 and own['transient_frame_max73']and 73<2*m)
    ck('own_paid_exit_and_source_depth',2*max(Ppaid)<m and max(Ppaid)<min(T)and min(T)>2 and g==H and J==57*H)
    ck('own_inventory_stock_envelope',(128*(H+2)).bit_length()+H+2<2*H and K*K>128*(H+2))
    Eguard=23+2*k+(g+1).bit_length()+(J+1).bit_length()
    ck('own_semantic_context_guard',Eguard==23+256+(H+1).bit_length()+(57*H+1).bit_length())
    deps=['pr4413-p3-rebalance-costs.md',bindingfile,'pr4413_p3_rebalance_source_bindings.py',own['own_source_manifest'],replayfile,'p3-compiler-refinement-costs.md','p3_compiler_refinement_costs.py','pr4411-p3-refined-cost-peer-review.json','pr4359-fermat-helper-upper.md','pr4359-crossover-retuned-upper.json','pr4359-crossover-retuned-peer-review.json','pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','candidate-fermat-helper.json','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
    common=checks.copy();branchouts={}
    for record in[True,False]:
        checks=common.copy();Q=10**8 if record else 10000;delta=F(1,Q);keff=kap if record else F(1,500);A=4*Q+1 if record else Q+1;epsilon=1-delta;beta=1-3*delta
        if record:a,b,q=keff+4*delta,keff+5*delta,keff+3*delta
        elif pr==4411:a,b,q=F(46001,20000000),F(5751,2500000),F(229,100000)
        else:a,b,q=F(2301,10**6),F(1151,500000),F(23,10000)
        pars=dict(kappa=keff,tested_saving=F(own['tested_mixed_saving']),complex_uniform_saving=eta,a=a,b=b,q=q,epsilon=epsilon,beta=beta,r0=delta/10,stop=delta,layout=delta,d=delta)
        led=G.gaussian_ledger(pars)
        ck('all50_native_only_correctness',all(v>0 for v in led['strict_checks'].values()))
        ck('both_nonBIT_functional',all(v>0 for v in led['functional_checks'].values()))
        ck('all7_nonBIT_margin_guards',all(v>keff for v in led['margins'].values()))
        ck('own_stopped_and_uniform_auxiliary_funding',eta>b>a>q>keff and(1-delta)*b>a)
        E=Q*(H+1)+2*H+2*k+Eguard+179200000000+1048576+1000;X=A*E;Y=X-8
        ck('own_semantic_precision_gate',Eguard<E and delta*E>44 and A*delta>=1+delta)
        ck('complete_active_and_direct_base_work_fit',48+2*k+2*H<E and 12+Q*(H+1)<E)
        ck('global_occupied_stock_base',6+4*H<Q*(H+1))
        ck('smooth_precision_log',E.bit_length()+A.bit_length()+3<F(E,1024)and F(1040,X)<delta/2)
        ck('absolute_prime_target_scale',X>128*Q and delta*X-10>=54)
        ck('fine_prime_capacity',delta*X>(1024*(65+1024*X)).bit_length()and delta*X>2)
        ck('transient_native_existing_spectators',delta*X>10 and(epsilon-beta)*X>1)
        ck('literal_supplier_active',epsilon*X>Q*(H+1)+2)
        ck('reference_and_tariff_domains',Y>80 and Y>=(1729**12).bit_length()and A*keff>8)
        for name,r in[('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(name+'_protected',r+F(1,1024)<-F(1,2))
        xi=led['parameters']['cap_xi'];rows=[]
        for name,s,c,powB,degree in[('target_FFT_H',epsilon*eta*(1-delta),60,2,0),('target_FFT_twiddles',epsilon,198,1,10),('dense_Gaussian_H',1-epsilon+beta*eta*(1-delta),90,2,4),('dense_diagonals',1-epsilon+beta,218,1,13),('Strassen_boundaries',F(3,32)+xi-epsilon,188,1,11),('halos',80-epsilon-beta,178,1,10),('pointwise_recovery',F(1),198,1,10)]:
            gap=s-keff;bound=powB*E+c+degree*(X+3).bit_length()-X*gap
            ck(name+'_positive_gap',gap>0);ck(name+'_one_eighth',bound<=-3);ck(name+'_decreasing_tail',F(4*max(1,degree),X)<gap)
            rows.append(dict(name=name,saving=str(s),margin=str(gap),power2=c,power_B=powB,log_degree=degree,base_log2_ratio_upper=str(bound)))
        out=dict(schema='own-p3-compiler-refinement-upper/1',status='closed_conditional_sufficient_upper_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=own['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',branch='record'if record else'early',kappa_record=str(kap),effective_kappa=str(keff),early_effective_kappa=None if record else str(keff),H=str(H),N=f'2^{H}',native_saving=str(eta),Q=Q,delta=str(delta),A=str(A),E=str(E),Eguard=str(Eguard),upper_log2log2_integer=str(Y),log2log2U=str(Y),inputUpper=f'2^(2^{Y})',sufficient_upper_input_bits=f'2^(2^{Y})',new_outer_parameters=enc(led['parameters']),reduced_ledger=enc(led),cost_rows=rows,native_interfaces=dict(raw_ambient=57,transient_frame_bound=73,Klog=128,Gunit=1494376,compiler_depth='<=57H',mixed_depth='<=H',inventory_log2_upper='128*N*(H+2)',normalized_fresh_work='G/W<K²N',active_full_H_coefficient='2^48*K²*N²',semantic_guard_log2=str(Eguard),occupied_stock_cutoff='max(64*(ceil(log2W)+1)^2,(2N)^Q)',ordinary_base_preserved=True),source_binding_file=bindingfile,source_binding_sha256=hs(bindingfile),source_same_raw_component_only=True,numerical_upper_transferred=False,ordinary_BIT_supplier_consumed=False,actual_first_crossing_known=False,all_PR_implementations=False,original_native_phase_replayed_here=False,own_finite_rank_checker_receipt=replay['status'],retained_contracts=['Own explicitly selected original p3 raw native arbitrary-input required-boundary/all-column/absolute-phase/Clifford identities and clean-owned/full-spectator semantics; type/census component bound, not a fresh native operator proof.','Own new uniform-rank theorem and complete chronological integer compiler with ready barriers, separate role arrays and actual child/complement endpoints.','Concrete normalized Gaussian/finite-LDU/narrow-gap/cyclic-border/fine-prime/exact-recovery interfaces and fixed repaired reference correctness/finite-kernel halting.'],formal_status='Conditional AI-assisted written mathematics and exact source/arithmetic checks, not Lean or independent human review.',source_sha256=binding['source_sha256'],dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
        out['early_effective_kappa']=None if record else str(keff);branchouts['record'if record else'early']=out
    recordfile=f'pr{pr}-p3-rebalance-record-upper.json';(R/recordfile).write_text(json.dumps(branchouts['record'],indent=2)+'\n',encoding='utf8')
    early=branchouts['early'];ck('own_early_precedes_own_record_tail',int(early['log2log2U'])<int(branchouts['record']['log2log2U']))
    early.update(record_tail_quantified=True,record_tail_certificate=recordfile,record_tail_certificate_sha256=hs(recordfile),record_tail_upper_log2log2_integer=branchouts['record']['log2log2U'],piecewise_description='Existence witness uses unchanged GMP below early sufficient gate, own counted early Gaussian circuit, then own counted same-core record circuit. No switch is used as a natural lower.')
    earlyfile=f'pr{pr}-p3-rebalance-early-upper.json';(R/earlyfile).write_text(json.dumps(early,indent=2)+'\n',encoding='utf8')
    ck('own_literal_unit_add_floor',own['raw_controller_complex_ADDs']==4 and own['raw_real_ADD_floor']==8 and 8*(1<<69)==1<<72)
    lower=dict(schema='own-p3-refined-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=own['own_head'],model=early['model'],baseline_extension_id=early['baseline_extension_id'],H=str(H),N=f'2^{H}',kappa=str(kap),active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),scope='Own complete unreduced p3 native/controller boundary on full fields/spectators at positive column multiplicity when active, width at least two; identical optimized GMP when inactive.',statistic='Earliest possible strict win in the declared literal enhancement family',all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,source_binding_file=bindingfile,source_binding_sha256=hs(bindingfile),dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),retained_contracts=early['retained_contracts'])
    lowerfile=f'pr{pr}-p3-rebalance-literal-lower.json';(R/lowerfile).write_text(json.dumps(lower,indent=2)+'\n',encoding='utf8');allchecks.update({str(pr)+'_'+n:v for n,v in checks.items()});outputs.append(dict(pr=pr,H=str(H),Eguard=Eguard,earlyP=early['log2log2U'],recordP=branchouts['record']['log2log2U'],lower=lower['input_bits']))
summary=dict(schema='own-p3-rebalance-circuit-costs/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=outputs,checks_passed=len(allchecks),checks=allchecks,script_sha256=hs(Path(__file__).name));(R/'pr4413-p3-rebalance-costs.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8');print(json.dumps(summary['rows'],indent=2))
