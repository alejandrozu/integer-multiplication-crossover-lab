"""Own PR4412/4414 tensor-native inventories, exact XAG gates and literal floors."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha1, sha256
import gzip, importlib.util, json

R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):
    b=(R/p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [enc(v)for v in o]
    return o
sp=importlib.util.spec_from_file_location('closed_gaussian_ledger',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
component=rd('gaussian-only-parameter-ledger.json')
assert component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')
allchecks={};outputs=[]
for pr in [4412,4414]:
    checks={}
    def ck(n,v):assert v,f'{pr}: {n}';checks[n]=True
    bindingfile=f'p3-p6-tensor-own-source/{pr}-manifest.json';binding=rd(bindingfile)
    head={4412:'9f0df9bf6f49942faf5f31389e7e387fdfe511b3',4414:'90da4b0ab894350ca12cac9110cc6da2225d18af'}[pr]
    ck('own_source_binding',binding['pr']==pr and binding['own_head']==head and binding['script_sha256']==hs('p3_p6_tensor_source_bindings.py'))
    sourcepins={}
    for a in binding['files']:
        data=(R/a['file']).read_bytes()
        ck('own_'+a['path'],sha256(data).hexdigest()==a['sha256']and sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==a['git_blob_sha1']and a['own_head']==head and a['primary_url']=='https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/'+head+'/'+a['path'])
        sourcepins[a['file']]=a['sha256']
    files={a['path']:a['file']for a in binding['files']};pkg=binding['package']
    replayfile=f'p3-p6-tensor-own-source/{pr}-fresh-replay.json';replay=rd(replayfile)
    ck('own_fresh_replay_binding',replay['source_manifest_sha256']==hs(bindingfile)and replay['script_sha256']==hs('p3_p6_tensor_source_bindings.py')and replay['source_files_sha256']==sourcepins and replay['pr']==pr and replay['own_head']==head)
    ck('own_replayed_scientific_values_exact',not replay['original_source_edited']and replay['all_other_scientific_and_source_fields_exact'])
    ck('original_platform_failure_disclosed',replay['original_default_failure_preserved']and not replay['original_default_verification_passed']and replay['returncode']==1 and replay['temp_only_write_result_returncode']==0 and len(replay['normalized_source_path_dictionary_keys'])==({4412:9,4414:11}[pr])and all(x['normalized_key']==x['original_key'].replace('\\','/')and x['receipt_path'].endswith('source_sha256')for x in replay['normalized_source_path_dictionary_keys']))
    result=rd(files[pkg+'/RESULT.json']);strict=result['strictification'];native=strict['native_inventory'];endpoint=result['endpoint']
    H=int(endpoint['compiler']['H1']);eta=F(endpoint['outer']['parameters']['complex_uniform_saving']);kap=F(endpoint['kappa']);v=strict['exponent'];m=57 if pr==4412 else 105
    own=dict(own_head=head,tested_mixed_saving=strict['tested_saving'],raw_controller_complex_ADDs=4,raw_real_ADD_floor=8)
    T={int(r):n for r,n in native['targets'].items()};Ppaid={int(r):n for r,n in native['paid'].items()};Braw=sum(T.values());Praw=sum(Ppaid.values());Gscalar=native['native_scalar_allowance']
    ck('exact_own_uniform_supplier',H==({4412:8701218254312470001,4414:473129651134046950001}[pr])and 0<kap<eta<F(strict['tested_saving'])<1 and endpoint['compiler']['N_encoding']==f'2^{H}'and strict['strict_moment_verified'])
    ck('source_cutoff_and_separation',v==({4412:15000,4414:150000}[pr])and min(T)==5 and max(T)==m and max(Ppaid)<m and sum(r*n for r,n in T.items())-sum(r*n for r,n in Ppaid.items())==({4412:224,4414:512}[pr])and endpoint['compiler']['tensor_power']==v)
    ck('complete_raw_fields_and_paid',Braw==({4412:3528,4414:6648}[pr])and Praw==({4412:25774,4414:48442}[pr])and Gscalar==({4412:1147304,4414:2166056}[pr]))
    np=next(a['file']for a in binding['files']if a['path'].endswith('THREE-base-FULL-IDENTITY-NATIVE.json.gz'));program=rd(np)
    ck('actual_both_native_orientations',set(program)=={'forward','backward'})
    events=sum(map(len,program.values()));unitadds=[]
    for orient,word in program.items():
        ck(orient+'_all_native_events_typed',all(row[0]in {'scalar','climb','center','phase','adapter','residual_adapter','warp'}for row in word))
        scalar=[row[1]for row in word if row[0]=='scalar']
        ck(orient+'_all_scalar_operations_typed',all(op[0]in {'add','scale','copy','clear'}for op in scalar))
        coefficients=[F(op[-2],op[-1])for op in scalar if op[0]in {'add','scale'}]
        ck(orient+'_all_scalar_coefficients_small_dyadic',all(abs(z.numerator)<=8 and z.denominator<=8 and z.denominator&(z.denominator-1)==0 for z in coefficients))
        ck(orient+'_all_clears_in_owned_namespace',all(op[1][0]=='C'for op in scalar if op[0]=='clear'))
        for i,row in enumerate(word):
            if row[0]!='scalar':continue
            op=row[1]
            if op[0]=='add'and F(op[-2],op[-1])==1 and op[1][0]==op[2][0]=='L'and op[1]!=op[2]:unitadds.append(dict(orientation=orient,event=i,destination=op[1],source=op[2]))
    selected=[];pairs=set()
    for x in unitadds:
        pair=(tuple(x['destination']),tuple(x['source']))
        if pair not in pairs:selected.append(x);pairs.add(pair)
        if len(selected)==4:break
    ck('four_actual_persistent_distinct_unit_ADDs',len(selected)==4 and all(0<=x['source'][1]<632 and 0<=x['destination'][1]<632 for x in selected))
    calls=(m-1)//8
    fresh=64*(calls*events+2*m*(Braw+Praw+1))
    S0=16*(fresh+Braw+Praw+m+1)*(64*(2*m+1)**3+16)
    ck('raw_scalar_grammar_and_complete_route_budget',Gscalar<fresh and S0<2**64 and v<2**20)
    ck('product_and_split_full_cubic_adapter_weights',2048*(fresh+Braw+Praw+m+1)*m**3<S0 and 2048*Praw*m**4<2**64)
    # L_v <= B*L_(v-1)+P^(v-1)*(L_1+whole-job matchers).
    # Both terms, owned banks and <=(P*m)^v split pieces are bounded by
    # S^(2v+5), S=2^64. No tensor/native word is materialized here.
    k=64*(2*v+5)+10;ell=2*v;g=H
    ck('tensor_instruction_and_split_majorant',k==({4412:1920330,4414:19200330}[pr])and k<=65*ell and 16*v<2**64 and max(Ppaid)<=m)
    ck('own_inventory_stock_envelope',2*k+H*(1+F(k,ell))<128*H and (128*(H+2)).bit_length()+H+2<2*H and 2*k>(128*(H+2)).bit_length())
    ck('strict_integer_context_depth',H>k and min(T)**2>2 and endpoint['compiler']['H0']>=({4412:6,4414:7}[pr])*v)
    Eguard=23+2*k+(H+1).bit_length()+H+1
    ck('own_semantic_context_guard',Eguard<H+4*k+128)
    deps=['native-tensor-circuit-costs.md',bindingfile,replayfile,'p3_p6_tensor_source_bindings.py','pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','candidate-fermat-helper.json','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
    common=checks.copy();branchouts={}
    for record in[True,False]:
        checks=common.copy();Q=700000000 if record else 10000;delta=F(1,Q);keff=kap if record else F(1,500);A=4*Q+1 if record else Q+1;epsilon=1-delta;beta=1-3*delta
        if record:a,b,q=keff+4*delta,keff+5*delta,keff+3*delta
        elif pr==4412:a,b,q=F(47,20000),F(3,1250),F(23,10000)
        else:a,b,q=keff+4*delta,keff+5*delta,keff+3*delta
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
        out=dict(schema='own-native-tensor-circuit-upper/1',status='closed_conditional_sufficient_upper_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=own['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',branch='record'if record else'early',kappa_record=str(kap),tensor_power=v,effective_kappa=str(keff),early_effective_kappa=None if record else str(keff),H=str(H),N=f'2^{H}',native_saving=str(eta),Q=Q,delta=str(delta),A=str(A),E=str(E),Eguard=str(Eguard),upper_log2log2_integer=str(Y),log2log2U=str(Y),inputUpper=f'2^(2^{Y})',sufficient_upper_input_bits=f'2^(2^{Y})',new_outer_parameters=enc(led['parameters']),reduced_ledger=enc(led),cost_rows=rows,native_interfaces=dict(raw_ambient=m,transient_frame_bound=2*m,Klog=k,Gunit=f'<2^{64*(2*v+5)}',raw_scalar_allowance=Gscalar,tensor_power=v,compiler_depth='<=N',mixed_depth='<=H',inventory_log2_upper='128*N*(H+2)',normalized_fresh_work='G/W<K²N',active_full_H_coefficient='2^48*K²*N²',semantic_guard_log2=str(Eguard),occupied_stock_cutoff='max(64*(ceil(log2W)+1)^2,(2N)^Q)',ordinary_base_preserved=True),source_binding_file=bindingfile,source_binding_sha256=hs(bindingfile),own_native_unit_source_bound=True,numerical_upper_transferred=False,ordinary_BIT_supplier_consumed=False,actual_first_crossing_known=False,all_PR_implementations=False,original_native_phase_replayed_here=False,own_finite_rank_checker_receipt=replay['status'],retained_contracts=['Own exact all-fresh native and chronological tensor product with arbitrary-input required-boundary/all-column/absolute-phase/Clifford identities and clean-owned/full-spectator semantics; own raw native inventory/main phase replay is bound, full all-column base operator closure remains explicit.','Own new uniform-rank theorem and complete chronological integer compiler with ready barriers, separate role arrays and actual child/complement endpoints.','Concrete normalized Gaussian/finite-LDU/narrow-gap/cyclic-border/fine-prime/exact-recovery interfaces and fixed repaired reference correctness/finite-kernel halting.'],formal_status='Conditional AI-assisted written mathematics and exact source/arithmetic checks, not Lean or independent human review.',source_sha256=sourcepins,dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
        out['early_effective_kappa']=None if record else str(keff);branchouts['record'if record else'early']=out
    recordfile=f'pr{pr}-native-tensor-record-upper.json';(R/recordfile).write_text(json.dumps(branchouts['record'],indent=2)+'\n',encoding='utf8')
    early=branchouts['early'];ck('own_early_precedes_own_record_tail',int(early['log2log2U'])<int(branchouts['record']['log2log2U']))
    early.update(record_tail_quantified=True,record_tail_certificate=recordfile,record_tail_certificate_sha256=hs(recordfile),record_tail_upper_log2log2_integer=branchouts['record']['log2log2U'],piecewise_description='Existence witness uses unchanged GMP below early sufficient gate, own counted early Gaussian circuit, then own counted same-core record circuit. No switch is used as a natural lower.')
    earlyfile=f'pr{pr}-native-tensor-early-upper.json';(R/earlyfile).write_text(json.dumps(early,indent=2)+'\n',encoding='utf8')
    ck('own_literal_unit_add_floor',own['raw_controller_complex_ADDs']==4 and own['raw_real_ADD_floor']==8 and 8*(1<<69)==1<<72)
    lower=dict(schema='own-native-tensor-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=own['own_head'],model=early['model'],baseline_extension_id=early['baseline_extension_id'],H=str(H),N=f'2^{H}',kappa=str(kap),tensor_power=v,selected_native_program_file=np,selected_native_program_sha256=hs(np),selected_unit_complex_ADDs=selected,active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),scope='Own complete unreduced native tensor/controller boundary on full fields/spectators at positive column multiplicity when active, width at least two; identical optimized GMP when inactive.',statistic='Earliest possible strict win in the declared literal enhancement family',all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,source_binding_file=bindingfile,source_binding_sha256=hs(bindingfile),dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),retained_contracts=early['retained_contracts'])
    lowerfile=f'pr{pr}-native-tensor-literal-lower.json';(R/lowerfile).write_text(json.dumps(lower,indent=2)+'\n',encoding='utf8');allchecks.update({str(pr)+'_'+n:v for n,v in checks.items()});outputs.append(dict(pr=pr,H=str(H),Eguard=Eguard,earlyP=early['log2log2U'],recordP=branchouts['record']['log2log2U'],lower=lower['input_bits']))
summary=dict(schema='own-native-tensor-circuit-costs/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=outputs,checks_passed=len(allchecks),checks=allchecks,script_sha256=hs(Path(__file__).name));(R/'native-tensor-circuit-costs.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8');print(json.dumps(summary['rows'],indent=2))
