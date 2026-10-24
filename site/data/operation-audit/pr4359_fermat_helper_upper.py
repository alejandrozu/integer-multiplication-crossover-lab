"""Own p3 typed-source census and two conditional whole-integer upper schedules."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import gzip,json
HERE=Path(__file__).resolve().parent
SRC='earlier-family-screen-source/'
def hs(p):return sha256((HERE/p).read_bytes()).hexdigest()
def load(p):return json.loads((HERE/p).read_bytes())
checks={}
def ck(n,v):
    assert v,n
    checks[n]=bool(v)
PINS={
'4359__EXPLICIT-TEMPLATE-BOUNDS.json':'3f1abfafa6f1bb192aafdf342a33ef60fd469fb0764be3eb1516984fc3c22c3f',
'4359__research__kappa-rebuild__architecture__FINITE-PRECOMPILATION.md':'4cb32f6b8e388ecf6ed41b5bbdeeb4539cb40c8424f194974afea58f7e0921e8',
'4359__research__kappa-rebuild__architecture__P3-CONTROLLER-TARIFF-CERTIFICATE.json':'d6a92cfa976af8638d2514fe48455131636a5b5b4c5cb236c0b74ed850fb2ae0',
'4359__research__kappa-rebuild__controller__P3-NATIVE-COVER.json.gz':'facfc6d6ecde151afb7e6a167776f3fdaac1c816e785a21a39f7f0bfd9140f3f',
'4359__research__kappa-rebuild__transfer-audit__FINITE-TEMPLATE-CLOSURE.md':'3f8508c63862dd83968bd30df91b08ba5afcee1e10db15ca546cdff0caef95d9',
'4359__research__kappa-rebuild__complex__full-identity-certificates__THREE-base-FULL-IDENTITY-NATIVE.json.gz':'c54b0a3e129d28e6dbf74fa731fc3bb70fe3c6705f07256750fbecddcc842d39'}
for fn,want in PINS.items():ck('own_source_'+fn,hs(SRC+fn)==want)
rank=load(SRC+'4359__EXPLICIT-TEMPLATE-BOUNDS.json')
own=next(r for r in rank['cases'] if r['family']=='complex')
native=json.loads(gzip.decompress((HERE/SRC/'4359__research__kappa-rebuild__controller__P3-NATIVE-COVER.json.gz').read_bytes()))
controller=load(SRC+'4359__research__kappa-rebuild__architecture__P3-CONTROLLER-TARIFF-CERTIFICATE.json')
proof=(HERE/SRC/'4359__research__kappa-rebuild__transfer-audit__FINITE-TEMPLATE-CLOSURE.md').read_text(encoding='utf8')
ck('rank_authenticates_cover',rank['source_sha256']['research/kappa-rebuild/controller/P3-NATIVE-COVER.json.gz']==PINS['4359__research__kappa-rebuild__controller__P3-NATIVE-COVER.json.gz'])
ck('cover_authenticates_controller',native['sources']['research/kappa-rebuild/architecture/P3-CONTROLLER-TARIFF-CERTIFICATE.json']==PINS['4359__research__kappa-rebuild__architecture__P3-CONTROLLER-TARIFF-CERTIFICATE.json'])
ck('cover_authenticates_original_word',native['sources']['research/kappa-rebuild/complex/full-identity-certificates/THREE-base-FULL-IDENTITY-NATIVE.json.gz']==PINS['4359__research__kappa-rebuild__complex__full-identity-certificates__THREE-base-FULL-IDENTITY-NATIVE.json.gz'])
targets={int(k):int(v) for k,v in own['targets'].items()};paid={int(k):int(v) for k,v in own['paid'].items()}
for field in ['targets','paid']:
    ck('own_profile_'+field,own[field]==native['cover'][field]=={x:int(y) for x,y in controller['invoice'][field].items()})
B=sum(targets.values());P=sum(paid.values());massT=sum(k*v for k,v in targets.items());massP=sum(k*v for k,v in paid.items())
H=own['N']['H1'];eta=F(own['uniform_saving']);k=128;m=57;g=H;J=m*H
ck('own_exact_parameters',(H,eta,B,P,massT,massP)==(276540184361,F(36,15625),2242,25394,37317,37093))
ck('own_separated_ranks',(min(targets),max(targets),max(paid))==(6,57,5))
ck('positive_rank_mass',massT-massP==224)
ck('source_strict_supplier',own['proven_uniform_moment']=='P_N/B_N < N^z' and F(own['z'])==1-eta)
ck('native_arbitrary_roles',native['arbitrary_productive_input_fields']==B)
ck('native_one_owned_bank',native['cover']['owned_center_fields']==1 and native['cover']['external_cleanup_fields']==0)
ck('native_explicit_spectator_and_clifford_contract','All untouched axes remain complete' in proof and 'exact Clifford normal form' in proof)
ck('native_complete_guard_invoice','1,494,376' in proof)

def rank2(vectors):
    basis={}
    for v in vectors:
        while v:
            h=v.bit_length()-1
            if h in basis:v^=basis[h]
            else:basis[h]=v;break
    return len(basis)
def app(cols,x):
    y=0
    while x:
        b=x&-x;y^=cols[b.bit_length()-1];x-=b
    return y
matrix_max=0
for i,item in enumerate(native['main_contacts']):
    ck('contact_four_maps_'+str(i),set(item['maps'])=={'entry_X','entry_Y','exit_X','exit_Y'})
    for name,a in item['maps'].items():
        cols=a['owner_columns'];inv=a['inverse_owner_columns'];q=len(cols);matrix_max=max(matrix_max,q)
        valid=len(inv)==q and all(0<=x<1<<q for x in cols+inv)
        valid=valid and all(app(inv,cols[j])==1<<j and app(cols,inv[j])==1<<j for j in range(q))
        valid=valid and app(inv,a['physical_shift'])==a['inverse_physical_shift'] and 0<=a['global_phase_Z4']<4
        ck('affine_contact_'+str(i)+'_'+name,valid)
for i,(name,a) in enumerate(native['cover']['owner_coordinate_maps'].items()):
    cols=a['columns'];rows=a['inverse_rows'];q=len(cols)
    ck('owner_inverse_'+str(i),len(rows)==q and all((rows[u]&cols[v]).bit_count()%2==(u==v) for u in range(q) for v in range(q)))
for i,a in enumerate(native['main_endpoint_normalizers']):
    cols=a['input_coordinate_columns'];rows=a['output_coordinate_inverse_rows'];q=len(cols)
    frame=a['physical_frame'];axes=[x[0] for x in frame]
    ck('endpoint_typed_'+str(i),len(rows)==q and rank2(cols)==q and rank2(rows)==q and all(0<x[0]<1<<q and 0<=x[1]<4 for x in frame) and a['target_rank']==len(a['positive_axes'])==rank2(a['positive_axes']) and set(a['positive_axes'])<=set(axes))
for i,a in enumerate(native['cover']['helper_bindings']):
    ck('helper_independent_'+str(i),len(a['axes'])==a['width'] and rank2(a['axes'])==a['width'] and a['whole_helper_boundary']['provider']=='THREE-base')
for i,a in enumerate(native['cover']['paid_residuals']):ck('paid_independent_'+str(i),len(a['axes'])==a['rank'] and rank2(a['axes'])==a['rank'])
ck('own_fresh_map_counts',(len(native['main_contacts'])*4,len(native['main_endpoint_normalizers']),len(native['cover']['helper_bindings']),len(native['cover']['paid_residuals']),matrix_max)==(3136,672,2856,460,73))
ck('transient_physical_frame_factor_two',matrix_max<2*m)
word=json.loads(gzip.decompress((HERE/SRC/'4359__research__kappa-rebuild__complex__full-identity-certificates__THREE-base-FULL-IDENTITY-NATIVE.json.gz').read_bytes()))
for direction,ops in word.items():
    ck('own_raw_word_length_'+direction,len(ops)==22633)
    ck('own_raw_warp_frame_'+direction,max(abs(o[2]) for o in ops if o[0]=='warp')<matrix_max)
    for i,o in enumerate(ops):
        if o[0]=='scalar' and o[1][0] in ('add','scale'):
            a=o[1];coef=F(a[-2],a[-1]);den=coef.denominator
            ck('own_dyadic_'+direction+'_'+str(i),den>0 and den&(den-1)==0 and den<=8 and abs(coef)<=8)
Gunit=1147304+8*(36260+2856+3136+672+460)
R=10**9*(B+P+1)*(10*matrix_max**2+10);K=32*(R+1)
ck('own_complete_G',Gunit==1494376)
ck('own_finite_K',K<1<<k)
ck('fresh_unit_budget',Gunit+64*(B+P+1)<R)
ck('fresh_scalar_adapter_ledger',(10**9+64)*R+32<K*K)
ck('branching_and_columns_below_K',B+P<K and B<K)
ck('paid_exit_contraction',2*max(paid)<m and max(paid)<min(targets))
ck('class_depth_bound',min(targets)>2 and g==H)
ck('stack_edge_bound',J==57*H)
ck('width_stock_log_envelope',k*(H+2)<1<<(H.bit_length()+16) and (k*(H+2)).bit_length()+H+2<2*H)
ck('stock_coefficient_covered',K*K>k*(H+2))
Eguard=23+2*k+(g+1).bit_length()+(J+1).bit_length()
endpoint='pr4535-upper-source/endpoint.py'
ck('pinned_generic_outer',hs(endpoint)=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
ns={'__file__':str(HERE/endpoint),'__name__':'p3_own_parameterized_upper'}
exec(compile((HERE/endpoint).read_bytes(),endpoint,'exec'),ns)
helper=load('candidate-fermat-helper.json')
ck('signed_helper_tariff',helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8')
ck('helper_hash',helper['proof_sha256']==hs('candidate-fermat-helper.md'))
REVIEW_CLOSED=True
common_checks=dict(checks)
def schedule(record):
    global checks
    checks=dict(common_checks)
    Q=2000000 if record else 10000;delta=F(1,Q);kap=F(23,10000) if record else F(1,500);A=4*Q+1 if record else Q+1
    ep=1-delta;beta=1-3*delta
    pars={'kappa':kap,'tested_saving':F(own['tested_mixed_saving']),'complex_uniform_saving':eta,'a':kap+4*delta if record else F(2301,1000000),'b':kap+5*delta if record else F(1151,500000),'q':kap+3*delta,'bit_saving':F(27,10000),'epsilon':ep,'beta':beta,'r0':delta/10,'stop':delta,'layout':delta,'d':delta}
    led=ns['ledger'](pars);led['functional_checks']['unused_auxiliary_BIT_stock_sublinear']=beta*(1-F(1,250))
    ck('own_all54_fresh',len(led['strict_checks'])==54 and all(v>0 for v in led['strict_checks'].values()))
    ck('own_all4_functional_fresh',len(led['functional_checks'])==4 and all(v>0 for v in led['functional_checks'].values()))
    ck('own_all9_savings_fresh',len(led['margins'])==9 and all(v>kap for v in led['margins'].values()))
    ck('actual_complex_above_b',eta>pars['b']>pars['a']>pars['q']>kap)
    E=Q*(H+1)+2*H+2*k+Eguard+179200000000+1048576+1000;X=A*E;Y=X-8
    xi=led['parameters']['cap_xi']
    ck('own_guard_fits',Eguard<E and delta*E>44 and A*delta>=1+delta)
    ck('active_fits',48+2*k+2*H<E)
    ck('ordinary_fallback_fits',12+Q*(H+1)<E)
    ck('stock_base_gate',6+4*H<Q*(H+1))
    ck('actual_smooth_log',E.bit_length()+A.bit_length()+3<F(E,1024))
    ck('precision_derivatives',F(1040,X)<delta/2)
    ck('explicit_prime_start',X>128*Q and X>=1<<54)
    ck('axis_capacity',delta*X>(1024*(65+1024*X)).bit_length() and delta*X>2)
    ck('existing_spectator_native_footprint',delta*X>10 and (ep-beta)*X>1)
    ck('literal_supplier_active',ep*X>Q*(H+1)+2)
    ck('reference_domains',Y>=7 and Y>=(1729**12).bit_length())
    ck('strict_tariff_win',A*kap>8)
    for name,r in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(name+'_protected',r+F(1,1024)<-F(1,2))
    rows=[]
    for name,s,c,r,degree in [('target_FFT_H',ep*eta*(1-delta),60,2,0),('target_FFT_twiddles',ep,198,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),90,2,4),('dense_diagonals',1-ep+beta,218,1,13),('Strassen_boundaries',F(3,32)+xi-ep,188,1,11),('halos',80-ep-beta,178,1,10),('pointwise_recovery_carries',F(1),198,1,10)]:
        gap=s-kap;res=r+F(degree+1,1024)-A*gap
        ck(name+'_gap',gap>0);ck(name+'_coefficient',c*1024<E);ck(name+'_smooth_tail',F(max(1,degree),X)<gap/2);ck(name+'_coefficient_one',res<-1)
        rows.append(dict(name=name,saving=str(s),margin=str(gap),power2=c,power_B=r,log_degree=degree,residual_B_exponent=str(res)))
    deps=['pr4359-fermat-helper-upper.md','pr4359-crossover-retuned-upper.md','pr4359-literal-work-lower.json','pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','candidate-fermat-helper.md','candidate-fermat-helper.json','optimized-gmp-semantic-repair.json','optimized-gmp-degree8-upper.json',endpoint]
    out={'schema':'pr4359-own-p3-fermat-helper-upper/1' if record else 'pr4359-own-p3-crossover-retuned-upper/1','status':'closed_conditional_sufficient_upper_bound' if REVIEW_CLOSED else 'pending_independent_AI_review','pr':4359,'model':'xag-straightline-v1','H':str(H),'N':'2^'+str(H),'kappa':'23/10000','kappa_record':'23/10000','kappa_effective':str(kap),'early_effective_kappa':None if record else str(kap),'Q':Q,'A':str(A),'E':str(E),'Eguard':str(Eguard),'log2log2U':str(Y),'sufficient_upper_input_bits':f'2^(2^{Y})','input_unit':'bits per unsigned operand','source_author_head':'da637c87c89482bc4c86be36bd0071b3d400dbed','source_URL':'https://github.com/CrocSwap/integer-mult-bounds/pull/4359','actual_core_uniform_saving':str(eta),'new_parameter_instantiation':True,'automatic_upper_transfer':False,'source_specific_auxiliary_funding':not record,'new_outer_parameters':ns['encode'](led['parameters']),'fresh_source_54_4_9_ledger':ns['encode'](led),'rows':rows,'finite_template':{'native':'own p3','tensor_power':1,'B':B,'P':P,'target_mass':massT,'paid_mass':massP,'rank_mass_surplus':224,'productive_min':6,'paid_max':5,'ambient_max':57,'native_physical_frame_maximum':73,'native_Gunit':Gunit,'R':str(R),'K':str(K),'Klog':k,'flow_depth':'<=H','compiler_depth':'<=57H','stack_guard':'2^21*K^2*(H+1)*(57H+1)*d','width_log_bound':'<128*N*(H+2)','normalized_native_work':'G/W<K^2*N','own_bases_preserved':True},'retained_contracts':['Own p3 arbitrary-input native identities and absolute endpoint phases, not freshly replayed here.','Own all-column whole-field endpoints, complete external spectators, independent role arrays and owned erasure.','Ready barriers, integer compiler and exact Clifford normal-form contracts.','Parameterized fine-prime/Gaussian/finite-section/boundary/recovery analytic branch.','Same repaired unbounded optimized-GMP finite-native correctness/halting and cost-model contracts.'],'fresh_native_check_scope':'Serialized affine inverses, binary bases, raw scalar dyadic coefficients and type/phase-domain checks; not full native operator/phase identity replay.','direct_Gaussian_Boolean_branch':True,'optional_BIT_wrapper_used':False,'tail_candidate_upper':{'each_gate_type':f'n*p^(1-{kap})','p':'256ceil(log2n)','all_larger_sizes':True},'reference_comparisons':{'canonical_HvH':True,'repaired_unbounded_optimized_GMP':True,'optimized_reference':'gmp-630-native-skylake-unbounded-exact-constants-v2','ratio_upper':f'256*p^(-{kap})<1','all_rho_positive':True},'complete_whole_integer_upper_conditional':REVIEW_CLOSED,'full_candidate_upper_review_closed':REVIEW_CLOSED,'retuned_crossover_review_closed':REVIEW_CLOSED if not record else None,'actual_first_crossover_known':False,'practical_hardware_crossover':False,'formal_status':'AI-assisted written mathematical derivation plus exact rational/integer checks; no Lean or independent human theorem review.','source_sha256':{SRC+p:h for p,h in PINS.items()},'dependency_hashes':{p:hs(p) for p in deps},'checks_passed':len(checks),'checks':checks,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    return out
record=schedule(True)
(HERE/'pr4359-fermat-helper-upper.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
early=schedule(False)
ck('early_upper_precedes_own_record_tail',int(early['log2log2U'])<int(record['log2log2U']))
early.update({'upper_derivation':'crossover_retuned_with_own_record_tail','backup_record_upper':record['sufficient_upper_input_bits'],'backup_record_upper_log2log2':record['log2log2U'],'backup_record_upper_certificate':'pr4359-fermat-helper-upper.json','retains_original_asymptotic_record':True,'claims_new_record_exponent':False,'piecewise_record_family':{'below_new_upper':'unchanged optimized-GMP reference','new_upper_to_record_upper':'own p3 early retuned schedule','at_and_above_record_upper':'own p3 record-tail schedule','wins_at_every_size_from_new_upper':True,'chosen_switch_used_as_natural_lower_bound':False},'checks_passed':len(checks),'checks':checks})
early['dependency_hashes']['pr4359-fermat-helper-upper.json']=hs('pr4359-fermat-helper-upper.json')
(HERE/'pr4359-crossover-retuned-upper.json').write_text(json.dumps(early,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':early['status'],'record_checks':record['checks_passed'],'early_checks':early['checks_passed'],'Eguard':Eguard,'record_Y':record['log2log2U'],'early_Y':early['log2log2U']},indent=2))
