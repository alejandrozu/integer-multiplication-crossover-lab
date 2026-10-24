"""Own-source PR5413 census and conditional literal-family bounds; offline."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json, math
R=Path(__file__).resolve().parent
S=R/'pr5413-source'
REVIEW_CLOSED=True
checks={}
def ck(n,v):
    assert v,n
    checks[n]=True
def load(p):return json.loads(Path(p).read_text(encoding='utf8'))
def hs(p):return sha256(Path(p).read_bytes()).hexdigest()
meta=load(S/'pull-5413.json')
head='0c1fa2f47fb5ea17b93a4b67063d08e49cc38e51'
ck('own_PR_head',meta['number']==5413 and meta['head']['sha']==head)
binding=load(S/'research__coupled-helper-neutral-completion__SOURCE-BINDINGS.json')
byname={x['path']:x for x in binding['files']}
downloads=load(S/'own-scientific-downloads.json')
sourcepins={}
for x in downloads:
    ck('own_source_'+x['file'],hs(S/x['file'])==x['sha256']==byname[x['path']]['sha256'])
    sourcepins['pr5413-source/'+x['file']]=x['sha256']
for name,path in [('funding','reports/expected/funding.json'),('README','README.md')]:
    local=S/('research__coupled-helper-neutral-completion__'+path.replace('/','__'))
    ck('own_'+name+'_binding',hs(local)==byname[path]['sha256'])
    sourcepins['pr5413-source/'+local.name]=hs(local)
for name in ['research__coupled-helper-neutral-completion__SOURCE-BINDINGS.json','pull-5413.json','certificates__frontier5413__CLAIM.json']:
    sourcepins['pr5413-source/'+name]=hs(S/name)
fund=load(S/'research__coupled-helper-neutral-completion__reports__expected__funding.json')
ck('own_BIT_numeric_values',F(fund['ordinary_BIT']['admitted'])==F(17,5000) and F(fund['ordinary_BIT']['atom'])==F(1,250))
impl=load(S/'files/V16-CALLER-IMPLEMENTATION-v3.json')
packet=load(S/'files/NEUTRAL-CALLER-v16c.json')
precision=load(S/'files/precision.json')
plan=load(S/'files/WHOLECALLER-PLAN-v1.json')
claim=load(S/'certificates__frontier5413__CLAIM.json')
ck('own_global_controller_chronology',packet['controller']['physical_events']==impl['source_physical_events'])
ck('own_bank_width',impl['physical_bank_width']==112)
retained_adds=[e for e in packet['typed_emission'] if e['op']=='RETAINED_MAIN_EVENT' and e['event'][0]=='ADD']
ck('own_literal_ADD_register_join',len(retained_adds)==90 and all(e['ports']==112 and e['event']==impl['source_physical_events'][e['source_event_index']] for e in retained_adds))
ck('own_all_boundary_banks',packet['main_input_fields']==32*112)
ck('own_plan_binding',impl['normalizers']['plan_sha256']==hs(S/'files/WHOLECALLER-PLAN-v1.json'))
ck('own_actual_order',impl['execution_order']==plan['chronology']==precision['execution_order'])
def matrix(program):
    a=[[F(int(i==j)) for j in range(32)] for i in range(32)]
    for op in program:
        if op[0]=='SWAP':a[op[1]],a[op[2]]=a[op[2]],a[op[1]]
        elif op[0]=='ADD':a[op[1]]=[x+F(op[3])*y for x,y in zip(a[op[1]],a[op[2]])]
        elif op[0]=='SCALE':a[op[1]]=[F(op[2])*x for x in a[op[1]]]
        else:raise AssertionError(op)
    return a
for side in ['left','right']:
    ck('own_'+side+'_boundary_matrix',matrix(impl[side+'_program'])==[[F(x) for x in row] for row in packet['controller']['boundaries'][side]])
counts={k:sum(e[0]=='ADD' for e in impl[k]) for k in ['left_program','right_program','source_physical_events']}
ck('fresh_partial_complex_ADD_census',counts=={'left_program':56,'right_program':25,'source_physical_events':90})
for key in counts:
    ck(key+'_unit_coefficients',all(e[1]!=e[2] and abs(F(e[3]))==1 for e in impl[key] if e[0]=='ADD'))
c=2*112*sum(counts.values());j=c.bit_length()-1;q=(j-3)//8
ck('fresh_real_ADD_floor',c==38304 and j==15 and q==1)
H=fund['H'];eta=F(fund['outer']['parameters']['complex_uniform_saving']);kappa=F(fund['kappa'])
ck('own_rank_and_saving',H==38569300000000000 and eta==F(4238203541,1400000000000) and kappa==F(605457647,200000000000))
ck('selected_claim_matches_own_funding',F(claim['kappa'])==kappa and claim['uniform_templates'][0]['rank_encoding']=='2^'+str(H) and F(claim['uniform_templates'][0]['saving'])==eta)
ck('own_funded_height',fund['j']*700000000000==H and (H+1)**1000<2**fund['j'])
ck('own_source_funding_predicates',all(fund['predicates'].values()) and F(fund['eta_lower'])>0 and F(fund['reserve_slack'])>0)
targets={int(k):v for k,v in fund['targets'].items()};paid={int(k):v for k,v in fund['paid'].items()}
Tmass=sum(k*v for k,v in targets.items());Pmass=sum(k*v for k,v in paid.items())
ck('own_raw_profile_counts',(sum(targets.values()),sum(paid.values()),Tmass,Pmass)==(10928,64260,239742,238990))
ck('own_surplus',Tmass-Pmass==packet['rank_mass_surplus']==752)
ck('own_global_profile',packet['productive_profile']==fund['targets'] and packet['paid_profile']==fund['paid'])
ck('own_strictification_tuple',fund['tuple']=={'ambient':145,'cutoff':20,'floor':21,'logarithm_power':1000,'offset':'1/5','tensor_power':1024,'theta':'63/64'})
ck('own_raw_majorant',precision['raw_G_upper']<2**128 and precision['raw_physical_value_upper']<2**128 and precision['raw_total_private_reservation']==418)
ck('own_typed_normalizers',precision['total_new_normalizer_fieldmaps']==30368 and impl['normalizers']['total_field_maps']==30368)
ck('own_native_source_application',precision['mathematical_application']['retained_five_assumptions_only'] and precision['mathematical_application']['proof_sha256']==hs(S/'files/V16-APPLICATION-PROOF-v3.md'))
coeff=precision['raw_global']['scalar_coefficients']
for label,n in coeff.items():
    a=F(label.split(':',1)[1]);ck('small_dyadic_'+label,n>0 and abs(a.numerator)<=8 and a.denominator<=8 and a.denominator&(a.denominator-1)==0)
local_path=S/'files/NEUTRAL-BACKWARD-v16c.json'
local_binding=next(x for x in binding['files'] if x['path'].endswith('/caller/NEUTRAL-BACKWARD-v16c.json'))
ck('own_local_scalar_packet_binding',hs(local_path)==local_binding['sha256'])
sourcepins['pr5413-source/files/NEUTRAL-BACKWARD-v16c.json']=hs(local_path)
def rank2(rows):
    piv={}
    for x in rows:
        while x:
            b=x.bit_length()-1
            if b in piv:x^=piv[b]
            else:piv[b]=x;break
    return len(piv)
local=load(local_path)
for i,op in enumerate(local['operations']):
    if op['op']!='MONOMIAL':continue
    for t,gate in enumerate(op['word']):
        if gate[0]=='P':valid=len(gate[1])==9 and all(type(x)is int and 0<=x<512 for x in gate[1]) and rank2(gate[1])==9
        elif gate[0]=='D':valid=len(gate[1])==len(gate[2])==9 and all(type(x)is int and 0<=x<512 for x in gate[1]) and all(type(x)is int and 0<=x<4 for x in gate[2])
        elif gate[0]=='X':valid=type(gate[1])is int and 0<=gate[1]<512
        elif gate[0]=='phase':valid=type(gate[1])is int and 0<=gate[1]<4
        else:valid=False
        ck('own_literal_Clifford_type_'+str(i)+'_'+str(t),valid)
strictlog=2*(1024*(2+2*128)+10+2*8192)+6+3*8193
klog=1048576
ck('fresh_strictified_budget',strictlog==585757==precision['expanded']['strictified_log_upper'] and strictlog+6+6<klog)
l=4497;m=145**1024;g=H//l;J=m*H
ck('own_completed_minimum',21**1024>2**l)
ck('own_maximum_paid_split_contraction',2*20**1024<m and 20**64<21**63)
ck('own_inventory_512HN',2*klog+F(H)*(1+F(klog,l))<512*H)
ck('own_stock_log_width',H+(512*H).bit_length()+2<2*H)
ck('own_stock_coefficient',2*klog>(512*H).bit_length()+8)
Eguard=22+2*klog+(g+1).bit_length()+(J+1).bit_length()
ck('own_guard_value',Eguard<2**22)
endpoint=R/'pr4535-upper-source/endpoint.py'
ck('source_generic_outer_ledger',hs(endpoint)=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
ns={'__name__':'own5413_exact_outer','__file__':str(endpoint)}
exec(compile(endpoint.read_bytes(),str(endpoint),'exec'),ns)
helper=load(R/'candidate-fermat-helper.json')
ck('same_exact_Fermat_helper',helper['proof_sha256']==hs(R/'candidate-fermat-helper.md') and helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8')
ck('same_GMP_reference',hs(R/'optimized-gmp-degree8-upper.json')=='d81123d030effa06d30ff5e2c087afbafeb8154e705249fec87a2b8f5b03dbe1')
def schedule(target,Q,A,label):
    delta=F(1,Q);ep=1-delta;beta=1-3*delta
    pars={'kappa':target,'tested_saving':F(fund['tested']),'complex_uniform_saving':eta,'b':target+5*delta,'a':target+4*delta,'q':target+3*delta,'bit_saving':F(fund['ordinary_BIT']['admitted']),'epsilon':ep,'beta':beta,'r0':delta/10,'stop':delta,'layout':delta,'d':delta}
    led=ns['ledger'](pars);led['functional_checks']['actual_new_BIT_stock_sublinear']=beta*(1-F(fund['ordinary_BIT']['atom']))
    ck(label+'_all54',len(led['strict_checks'])==54 and all(v>0 for v in led['strict_checks'].values()))
    ck(label+'_all4',len(led['functional_checks'])==4 and all(v>0 for v in led['functional_checks'].values()))
    ck(label+'_all9',len(led['margins'])==9 and all(v>target for v in led['margins'].values()))
    if label=='record':ck('own_record_ledger_source_equality',ns['encode'](led['margins'])==fund['outer']['margins'])
    xi=led['parameters']['cap_xi'];E=Q*(H+1)+2*H+2*klog+Eguard+179200000000+1048576+1000;X=A*E;Y=X-8
    ck(label+'_source_eta_funds',eta>=target+6*delta)
    ck(label+'_guard_and_work',Eguard<E and 48+2*klog+2*H<E and delta*E>44)
    ck(label+'_ordinary_base_and_stock',12+Q*(H+1)<E and 6+4*H<Q*(H+1))
    ck(label+'_actual_smooth_log',E.bit_length()+A.bit_length()+3<F(E,1024) and F(1040,X)<delta/2)
    ck(label+'_prime_window',X>128*Q and X>=2**54)
    ck(label+'_axis_capacity',delta*X>(1024*(65+1024*X)).bit_length() and delta*X>2)
    ck(label+'_core_is_active',ep*X>Q*(H+1)+2)
    ck(label+'_reference_domains',Y>=(1729**12).bit_length() and target*X>8)
    for name,r in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(label+'_'+name+'_precision',r+F(1,1024)<-F(1,2))
    rows=[]
    for name,saving,c0,powb,degree in [('target_FFT_H',ep*eta*(1-delta),60,2,0),('target_FFT_twiddles',ep,198,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),90,2,4),('dense_diagonals',1-ep+beta,218,1,13),('Strassen_boundaries',F(3,32)+xi-ep,188,1,11),('halos',80-ep-beta,178,1,10),('pointwise_recovery_carries',F(1),198,1,10)]:
        gap=saving-target;res=powb+F(degree+1,1024)-A*gap
        ck(label+'_'+name,gap>0 and c0*1024<E and F(max(1,degree),X)<gap/2 and res<-1)
        rows.append(dict(name=name,saving=str(saving),margin=str(gap),power2=c0,power_B=powb,log_degree=degree,residual_B_exponent=str(res)))
    return dict(kappa_effective=str(target),Q=Q,A=str(A),E=str(E),Eguard=str(Eguard),log2log2U=str(Y),sufficient_upper_input_bits=f'2^(2^{Y})',new_outer_parameters=ns['encode'](led['parameters']),fresh54_4_9=ns['encode'](led),rows=rows)
record=schedule(kappa,700000000000,2800000000001,'record')
early=schedule(F(1,500),10000,10001,'early')
ck('early_precedes_own_record_tail',int(early['log2log2U'])<int(record['log2log2U']))
proof=R/'pr5413-fixed-core-feasibility.md'
deps=['pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py','pr5413-fixed-core-feasibility.md']
base=dict(pr=5413,model='xag-straightline-v1',own_head=head,H=str(H),N='2^'+str(H),kappa=str(kappa),eta_uniform=str(eta),source_sha256=sourcepins,dependency_hashes={n:hs(R/n) for n in deps},checks_passed=len(checks),checks=checks,formal_status='Own-source arithmetic/census and AI-assisted written proof under retained native/compiler/analytic/GMP contracts; no Lean or independent human review.',actual_first_crossover_known=False)
native=dict(base,schema='pr5413-own-native-parameters/1',status='PASS_OWN_SOURCE_CENSUS_AND_PARAMETER_BINDING',Klog_upper=klog,Eguard=str(Eguard),inventory_log_upper='512*H*2^H',raw_targets=targets,raw_paid=paid,raw_rank_surplus=752,raw_record_budget='2^128',strictified_record_log_upper=strictlog,tensor_power=1024,completed_productive_floor=21,paid_cutoff=20,partial_bank_ADDs=counts,raw_complex_ADD_floor=c//2,raw_real_ADD_floor=c,core_c=str(c),j=j,q=q,fresh_replay_scope='SHA256s, exact32x32 boundary matrices, typed explicit bankADD count, raw coefficient bounds, rank/funding fields and fresh outer54/4/9 arithmetic; full native/phase engines not rerun.')
(R/'pr5413-native-parameters.json').write_text(json.dumps(native,indent=2)+'\n',encoding='utf8')
lower=dict(base,schema='pr5413-literal-work-lower/1',status='closed_conditional_literal_family_lower_only' if REVIEW_CLOSED else 'pending_independent_AI_review',core_c=str(c),j=j,q=q,lower=f'2^(2^{H-3}-2^69+{q})',upper=None,root_degree=8,baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',reference_upper_per_type='2^(2^72+3)*(n+1)^8',all_implementations_of_PR=False,full_upper_transferred_from_other_PR=False,lower_plot={'Y':math.log2(H-3),'log2_of_integer':str(H-3)},family='Own unreduced normalized PR5413 dense core when active, identical fixed optimizedGMP reference when inactive; width>=2, all-column complete spectators retained.')
(R/'pr5413-literal-work-lower.json').write_text(json.dumps(lower,indent=2)+'\n',encoding='utf8')
common=dict(base,status='closed_conditional_sufficient_upper_bound' if REVIEW_CLOSED else 'pending_independent_AI_review',complete_whole_integer_upper_conditional=REVIEW_CLOSED,automatic_upper_transfer=False,source_parameter_witness_sha256=hs(R/'pr5413-native-parameters.json'),native_source_certificate='pr5413-native-parameters.json',retained_contracts=['Own normalized complete caller/native/all-column/absolute-phase endpoint identities','Source separate role fields, complete spectators, parent-selected axes and owned zero restoration','Constructive finite uniform compiler and source-funded strict leaf efficiency','Completed Clifford endpoint and exact dyadic primitive lowering','Parameterized Gaussian/fine-prime/boundary/precision/exact-recovery analytic lemmas','Fixed optimizedGMP finite-native correctness/halting'],finite_template={'power':1024,'Klog_upper':klog,'paid_cutoff':'20^1024','productive_floor':'21^1024','rawB':10928,'rawP':64260,'raw_target_mass':Tmass,'raw_paid_mass':Pmass,'inventory_log_upper':'512*H*2^H'},reference_comparisons={'optimized_reference':'gmp-630-native-skylake-unbounded-exact-constants-v2','ratio_upper':'256*p^(-kappa_effective)<1','canonical_HvH':True})
tail=dict(common,**record,schema='pr5413-own-record-fermat-helper-upper/1',upper_derivation='own_source_fermat_helper_clifford_stack')
(R/'pr5413-fermat-helper-upper.json').write_text(json.dumps(tail,indent=2)+'\n',encoding='utf8')
retune=dict(common,**early,schema='pr5413-own-fixed-core-retuned-upper/1',upper_derivation='crossover_retuned_with_record_tail',early_effective_kappa='1/500',backup_record_upper=record['sufficient_upper_input_bits'],backup_record_upper_log2log2=record['log2log2U'],backup_record_upper_certificate='pr5413-fermat-helper-upper.json',retains_original_asymptotic_record=True,claims_new_record_exponent=False,piecewise_definition='Own unchangedGMP belowearlyU; ownretunedschedule untilownrecordU; ownoriginalrecordtail thereafter.')
(R/'pr5413-crossover-retuned-upper.json').write_text(json.dumps(retune,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':retune['status'],'checks':len(checks),'c':c,'j':j,'q':q,'Eguard':Eguard,'recordP':record['log2log2U'],'earlyP':early['log2log2U'],'lower':lower['lower']},indent=2))
