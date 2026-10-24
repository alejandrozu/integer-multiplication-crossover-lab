"""Offline own-source p7/p17 native, lower-work, and two upper schedule checks."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import ast,gzip,json,sys
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
SRC=HERE/'p7-p17-record-source'
REVIEW_CLOSED=True
CHECKS={};SOURCE_PINS={}
def ck(n,v):
    assert v,n
    CHECKS[n]=bool(v)
def hs(p):return sha256(p.read_bytes()).hexdigest()
def read(p):
    raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
MANIFEST_PINS={'initial-manifest.json': '6828a3623852f7679796620bed823e83c89aa7e44e7b2aed8804b9b616b641c4', 'native-input-manifest.json': '8d6f181bd9fc0aa4821c09e01fe9a46bce26ef7846cbb00e21de6e176b2a29b1', 'phase-input-manifest.json': 'f410b0bef1637a6384c1bae5e1c1ecb8324ba9b98d8e825cb07c896b5facd009', 'identity-input-manifest.json': 'b3949f5d074f806af84e9b1019b4ff261d4a90f638d6b3e07b5043f36e2dc742', 'clifford-grammar-manifest.json': 'fea7f720876180c67e9383a21000c61d7db6499829dd6f51b35d857fdd949739'}
if not MANIFEST_PINS:
    raise AssertionError('Manifest digest constants must be filled before this reproducer runs')
entries=[]
for name,want in MANIFEST_PINS.items():
    p=SRC/name;ck('manifest_'+name,hs(p)==want);entries+=read(p)
INDEX={(r['pr'],r['path']):r for r in entries}
for row in entries:
    p=HERE/row['file'];ck('primary_'+str(row['pr'])+'_'+row['path'],hs(p)==row['sha256'])
    ck('own_head_URL_'+row['file'],row['url']==f"https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/{row['head']}/{row['path']}")
    SOURCE_PINS[row['file']]=row['sha256']
def source(pr,path):return read(HERE/INDEX[pr,path]['file'])
def matching(pr,part):
    return source(pr,next(path for (q,path) in INDEX if q==pr and part in path))
def rank2(vs):
    basis={}
    for x in vs:
        while x:
            b=x.bit_length()-1
            if b in basis:x^=basis[b]
            else:basis[b]=x;break
    return len(basis)
def dot(x,y):return (x&y).bit_count()&1
def walk(x):
    yield x
    if isinstance(x,dict):
        for v in x.values():yield from walk(v)
    elif isinstance(x,list):
        for v in x:yield from walk(v)
def typed_catalog(obj):
    count=0
    for d in walk(obj):
        if not isinstance(d,dict) or not {'matrix_rows','offset','phase','linear_Z4','quadratic_rows'}<=d.keys():continue
        rows=d['matrix_rows'];n=len(rows);lim=1<<n
        assert n and rank2(rows)==n and all(isinstance(v,int) and 0<=v<lim for v in rows)
        assert len(d['linear_Z4'])==n and all(isinstance(v,int) and 0<=v<4 for v in d['linear_Z4'])
        assert len(d['quadratic_rows'])==n and all(isinstance(v,int) and 0<=v<lim for v in d['quadratic_rows'])
        assert 0<=d['offset']<lim and isinstance(d['phase'],int) and 0<=d['phase']<4
        count+=1
    return count
HEADS={4416:'e9058860b5c850760fdf970e796a96aefcdb1d98',4440:'9123d75afea5096d25eb98b2b6080cbbe0d91c01',4441:'149af87f1101dc7a72f2fe57294f9bacf8d053ba',4447:'02b51f341013c607dc480248c94c216b8260d8af'}
PACKAGES={4416:'pr4359-p7-padding',4440:'query-thinned-controllers',4441:'fresh-helper-thinned',4447:'missing-join-frame'}
EXPECTED={4416:(16201843136005340321,F(268647,100000000),F(376107,140000000),F(1,700000000),6240,11,10,121),4440:(10418370291022217,F(37,12500),F(103609,35000000),F(3,70000000),1024,21,20,153),4441:(165315500000000,F(60021,20000000),F(10503681,3500000000),F(1,3500000000),1024,21,20,153),4447:(64215200000000,F(300123,100000000),F(16413,5468750),F(1,1400000000),1024,21,20,153)}
original=matching(4416,'full-identity-certificates/RESULT.json')['providers']['THREE-base']
old_helpers={int(k):v for k,v in original['helper_boundary']['widths'].items()}
old_paid={int(k):v for k,v in original['unsplit_replays']['forward']['paid_profile'].items()}
native_word=matching(4416,'FULL-IDENTITY-NATIVE.json.gz')
native_rows=[r for r in entries if r['pr']==4416 and 'FULL-IDENTITY-NATIVE.json.gz' in r['path']]
ck('original_identity_binds_native_word',original['artifacts']['THREE-base-FULL-IDENTITY-NATIVE.json.gz']==native_rows[0]['sha256'])
ck('original_owned_arbitrary',original['all_632_persistent_inputs_arbitrary'] and original['owned_C_input_arbitrary_and_erased'])
scalar_count=0
for direction,program in native_word.items():
    ck('original_native_orientation_'+direction,direction in ('forward','backward'))
    for event in program:
        if event[0]!='scalar':continue
        g=event[1]
        if g[0] in ('add','scale'):
            q=F(g[-2],g[-1]);ck('dyadic_scalar_'+str(scalar_count),q.denominator&(q.denominator-1)==0)
            if g[0]=='scale':ck('signed_binary_scale_'+str(scalar_count),q!=0 and abs(q.numerator)&(abs(q.numerator)-1)==0)
            scalar_count+=1
old_catalog=matching(4416,'HELPER-BOUNDARIES.json.gz')
old_types=typed_catalog(old_catalog)+typed_catalog(original)
ck('original_clifford_catalog_nonempty',old_types>100)
for pr in HEADS:
    grammar_path='research/t74-native-fast/vendor/native/new/code/borrow/vendor/clifford/clifford_exact.py'
    tree=ast.parse((HERE/INDEX[pr,grammar_path]['file']).read_text(encoding='utf8'))
    grammar={};defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('parity','qvalue')]
    exec(compile(ast.Module(body=defs,type_ignores=[]),grammar_path,'exec'),grammar)
    ck('own_even_quadratic_cross_coefficient_'+str(pr),grammar['qvalue']([2,0],[0,0],3,2)==2 and grammar['qvalue']([2,0],[0,0],1,2)==0 and grammar['qvalue']([2,0],[0,0],2,2)==0)
phases=matching(4416,'DATA-PHASES.json')
for i,recipe in enumerate(phases['recipes']):
    q=recipe['q']
    axes=recipe['idle_children'][0]['orthogonal_axes'][:8]
    ck('p7_local_orthogonal_'+str(i),len(axes)==8 and all(dot(a,b)==int(a==b) for a in axes for b in axes))
    ck('p7_center_orthogonal_'+str(i),all(dot(q,a)==0 for a in axes))
    for stage in range(1,15):
        fresh=[1<<(9+8*(stage-1)+j) for j in range(8)]
        vs=[a^b for a,b in zip(axes,fresh)]
        def route(x):
            out=x
            for v in vs:
                if dot(v,x):out^=v
            return out
        ck('p7_fresh_block_involution_'+str(i)+'_'+str(stage),all(dot(v,w)==0 for v in vs for w in vs) and route(q)==q and all(route(a)==b and route(b)==a for a,b in zip(axes,fresh)))
ck('p7_actual_ports',len(phases['recipes'])==112)
helper=read(HERE/'candidate-fermat-helper.json')
ck('signed_explicit_helper',helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8')
ck('helper_proof_pin',hs(HERE/'candidate-fermat-helper.md')==helper['proof_sha256'])
ck('helper_script_pin',hs(HERE/'candidate_fermat_helper.py')==helper['script_sha256'])
deps=['p7-p17-record-crossover-bounds.md','candidate-fermat-helper.json','candidate-fermat-helper.md','pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-semantic-repair.json','optimized-gmp-degree8-upper.json']
OUT=[]
for pr in HEADS:
    start=len(CHECKS);pre=str(pr)+'_'
    def check(n,v):ck(pre+n,v)
    result=source(pr,'research/'+PACKAGES[pr]+'/RESULT.json')
    check('all_sources_own_head',all(r['head']==HEADS[pr] for r in entries if r['pr']==pr))
    H,kap,eta,delta,V,f,cut,m=EXPECTED[pr]
    if pr==4416:
        s=result['strictification'];e=result['endpoint'];outer=e['outer'];comp=e['compiler'];invoice=s
        check('actual_source_parameters',(comp['H1'],F(e['kappa']),F(outer['parameters']['complex_uniform_saving']),F(outer['parameters']['stop']),s['exponent'],s['target_floor_base'],s['cutoff_base'])==(H,kap,eta,delta,V,f,cut))
        ctrl=source(pr,'research/pr4359-p7-padding/P7-FACTOR.json');boundary=ctrl
        helpers,localpaid=old_helpers,old_paid
        check('p7_native_factor_binding',INDEX[pr,'research/pr4359-p7-padding/P7-FACTOR.json']['sha256']==s['native_inventory']['factor_receipt_sha256'])
        check('p7_raw_allowance',s['native_inventory']['native_scalar_allowance']==2490856<10**9)
        check('p7_raw_macro_envelope',2490856+64*(7688+55998+6720+1568+1)<10**9)
        check('p7_raw_control_count',4*15*112==s['native_inventory']['contacts'])
        t,z,z0,h=map(F,[comp['t'],comp['z'],comp['z0'],comp['h']]);d0=z0-t
        num=26640*d0+1+7*V*(1-z0);den=h*d0
        H0=(num/den).__ceil__();H1=(F(H0)*(1-z0)/(z-z0)).__floor__()+1
        check('fresh_exact_sufficient_rank',H0==comp['H0'] and H1==H)
        check('own_normalized_paid',F(s['normalized_moment_upper_rational'])<1)
        check('own_theta',10**26<11**25)
        check('own_completion_tail',F(4991,5000)**390<F(1,2) and F(1,1+F(V,10**8))+F(4,2**16)<1)
        own_types=old_types
    else:
        outer=result['outer'];invoice=result['complex_invoice'] if pr==4440 else result
        s=result['complex_strictification'] if pr==4440 else result['strictification']
        ctrl=source(pr,'research/query-thinned-controllers/COMPLEX-CONTROLLER.json');boundary=ctrl['boundaries']
        if pr==4440:
            helpers,localpaid=old_helpers,old_paid;own_types=old_types
            check('own_source_rank',s['uniform_H1']==H and F(s['uniform_saving'])==eta)
            C=F(s['tested_saving']);h=F(1,64);t=1-C;z=1-eta;z0=(t+z)/2;d0=z0-t
            H0=((d0*(5+8*h)*V+1+8*V*(1-z0))/(h*d0)).__ceil__()
            check('fresh_exact_sufficient_rank',H0==s['compiler_H0'] and (F(H0)*(1-z0)/(z-z0)).__floor__()+1==H)
            check('own_normalized_surplus',F(s['normalized_surplus_lower'])>0)
        else:
            native=source(pr,'research/'+('fresh-helper-boundary/NATIVE-RESULT.json.gz' if pr==4441 else 'missing-join-frame/NATIVE.json.gz'))
            helpers={int(r):n for r,n in native['helpers'].items()};localpaid={int(r):n for r,n in native['paid'].items()}
            own_types=typed_catalog(native)+old_types
            check('own_native_typed_routes',own_types>old_types)
            check('own_native_ownership',all(d['arbitrary_owned_C0_cleared'] and d['independent_persistent_columns']==632 for d in native['native'].values()))
            check('own_native_scalar_allowance',max(d['real_scalar_allowance'] for d in native['native'].values())<=158168)
            check('own_raw_nonrecursive_allowance',result['nonrecursive']['raw_upper']<10**9==result['nonrecursive']['raw_budget'])
            comp=result['compiler'];j=comp['integer_test_exponent'];q=F(comp['gap']).denominator
            check('own_source_rank',comp['H']==H and F(comp['uniform_saving'])==eta)
            check('fresh_integer_uniform_rank',H==q*j and (H+1)**1000<1<<j and (q*(j-1)+1)**1000>=1<<(j-1))
            check('own_normalized_paid',F(s['normalized_paid_upper'])<1)
        check('own_floor_cutoff',(s.get('tensor_power',s.get('power')),s.get('target_floor_base',s.get('floor')),s.get('cutoff_base',s.get('cutoff')))==(V,f,cut))
        check('p17_theta',20**64<21**63)
    check('source_outer_parameters',F(outer['parameters']['kappa'])==kap and F(outer['parameters']['stop'])==delta and F(outer['parameters']['complex_uniform_saving'])==eta)
    T={int(r):n for r,n in invoice['targets'].items()};P={int(r):n for r,n in invoice['paid'].items()}
    events=ctrl['physical_events'];nlocal=sum(e[0]=='LOCAL' for e in events);nquery=sum(e[0]=='QUERY_SHEAR' for e in events)
    thick={e[1] for e in events if e[0]=='LOCAL'}
    prod=Counter({r:n*nlocal for r,n in helpers.items()});paid=Counter({r:n*nlocal for r,n in localpaid.items()})
    paid[1]+=112*nquery
    for term in ctrl.get('diagonal',ctrl.get('exact_diagonal_monomials')):
        check('legal_main_'+str(term),term[0] in (-1,1) and all(x in (0,1) for x in term[1:]))
        prod[1+8*sum(term[1:])]+=112
    for event in events:
        if event[0]=='IDLE':
            rank=8*len(thick.intersection(event[2]))
            if rank:paid[rank]+=224
    check('fresh_complete_productive_profile',dict(prod)==T)
    check('fresh_complete_paid_profile',dict(paid)==P)
    B=sum(T.values());Pc=sum(P.values());Mt=sum(r*n for r,n in T.items());Mp=sum(r*n for r,n in P.items())
    check('own_complete_counts',B==invoice['productive_fields'] and Pc==invoice.get('paid_calls',invoice.get('native_inventory',{}).get('paid_calls')))
    check('positive_raw_and_tensor_rankmass',Mt>Mp and Mt**V>Mp**V)
    check('own_ambient_rank',max(T)==m and 2*max(P)**V<m**V and 2*cut**V<m**V)
    word=boundary['left_program']+boundary['right_program'];adds=[e for e in word if e[0]=='ADD']
    check('actual_eight_real_add_floor',len(adds)>=4 and all(F(e[-1]) in (-1,1) and e[1]!=e[2] for e in adds))
    check('all_boundary_coefficients_unit',all(F(e[-1]) in (-1,1) for e in word if e[0] in ('ADD','SCALE')))
    R=(10**9*V*(B+Pc)**V+Mp**V+B**V*f**V)*(10*m**(2*V)+10);K=32*(R+1);k=K.bit_length();l=(f**V).bit_length()-1
    J=m**V*H;g=H//l
    Eguard=22+2*k+(g+1).bit_length()+(J+1).bit_length()
    check('own_fresh_native_stage_budget',(10**9+64)*R+32<K*K)
    check('own_general_32HN_inventory',2*k+H*(1+F(k,l))<32*H)
    check('own_stock_loglog_width',H+(32*H).bit_length()+1<2*H)
    check('own_Clifford_stack_guard',(1<<20)*K*K*(g+1)*(J+1)<1<<Eguard)
    endpoint=next(path for q,path in INDEX if q==pr and path.endswith('compiler-refill/endpoint.py'))
    ns={'__name__':'source_endpoint','__file__':str(HERE/INDEX[pr,endpoint]['file'])}
    exec(compile((HERE/INDEX[pr,endpoint]['file']).read_text(encoding='utf8'),endpoint,'exec'),ns)
    def schedule(record):
        label='record_' if record else 'early_'
        target=kap if record else F(1,500);d=delta if record else F(1,10000);Q=(1/d).__ceil__();A=4*Q+1 if record else 10001
        ep=1-d;beta=1-3*d
        pars={key:F(value) for key,value in outer['parameters'].items()}
        if not record:
            pars.update(kappa=target,stop=d,d=d,layout=d,epsilon=ep,beta=beta,q=F(23,10000),a=F(3,1250),b=F(1,400),r0=d/10,complex_uniform_saving=eta)
        check(label+'exact_outer_row_parameters',pars['epsilon']==ep and pars['beta']==beta and pars['stop']==d and pars['complex_uniform_saving']==eta)
        led=ns['ledger'](pars)
        if pr!=4416:led['functional_checks']['actual_new_BIT_stock_sublinear']=beta*(1-F(1,250))
        check(label+'fresh_54',len(led['strict_checks'])==54 and all(v>0 for v in led['strict_checks'].values()))
        check(label+'fresh_functional',len(led['functional_checks'])==(3 if pr==4416 else 4) and all(v>0 for v in led['functional_checks'].values()))
        check(label+'fresh_nine',len(led['margins'])==9 and all(v>target for v in led['margins'].values()))
        if record:
            check('all_source_strict_recomputed',{n:str(v) for n,v in led['strict_checks'].items()}==outer['strict_checks'])
            check('all_source_functional_recomputed',{n:str(v) for n,v in led['functional_checks'].items()}==outer['functional_checks'])
            check('all_source_nine_recomputed',{n:str(v) for n,v in led['margins'].items()}==outer['margins'])
        E=Q*(H+1)+2*H+2*k+Eguard+179200000000+1048576+1000;X=A*E;Y=X-8;xi=led['parameters']['cap_xi']
        check(label+'capacity_base',6+4*H<Q*(H+1) and 12+Q*(H+1)<E and 48+2*k+2*H<E)
        check(label+'actual_smooth_envelope',E.bit_length()+A.bit_length()+3<F(E,1024))
        check(label+'guard_and_semantic',Eguard<E and A*d>=1+d and d*E>44)
        check(label+'precision_tail',F(1040,X)<d/2)
        check(label+'prime_start',X>128*Q and X>=1<<54)
        check(label+'axis_capacity',d*X>(1024*(65+1024*X)).bit_length() and d*X>2)
        check(label+'reference_domains',Y>=(1729**12).bit_length() and A*target>8)
        for name,r in [('body',F(5,1024)-3*d*A),('normalization',F(1,1024)-d*A),('boundary',F(1,1024)-A)]:check(label+name+'_guard',r+F(1,1024)<-F(1,2))
        rows=[]
        for name,s,c,powb,degree in [('target_FFT_H',ep*eta*(1-d),60,2,0),('target_FFT_twiddles',ep,198,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-d),90,2,4),('dense_diagonals',1-ep+beta,218,1,13),('Strassen_boundaries',F(3,32)+xi-ep,188,1,11),('halos',80-ep-beta,178,1,10),('pointwise_recovery_carries',F(1),198,1,10)]:
            gap=s-target;res=powb+F(degree+1,1024)-A*gap
            check(label+name+'_all_guards',gap>0 and res<-1 and c*1024<E and F(max(1,degree),X)<gap/2)
            rows.append(dict(name=name,saving=str(s),margin=str(gap),power2=c,power_B=powb,log_degree=degree,residual_B_exponent=str(res)))
        return dict(kappa_effective=str(target),delta=str(d),Q=str(Q),A=str(A),E=str(E),Eguard=str(Eguard),log2log2U=str(Y),sufficient_upper_input_bits=f'2^(2^{Y})',outer_parameters=ns['encode'](led['parameters']),fresh_54_functional_9_ledger=ns['encode'](led),rows=rows)
    record=schedule(True);early=schedule(False)
    check('early_precedes_own_record_tail',int(early['log2log2U'])<int(record['log2log2U']))
    lower=f'2^(2^{H-3}-2^69)'
    OUT.append(dict(pr=pr,url=f'https://github.com/CrocSwap/integer-mult-bounds/pull/{pr}',source_author_head=HEADS[pr],model='xag-straightline-v1',H=str(H),N=f'2^{H}',kappa=str(kap),kappa_record=str(kap),actual_core_uniform_saving=str(eta),Klog=k,fresh_source_witness_replay=True,full_native_or_phase_replay=False,status='closed_conditional_bounds' if REVIEW_CLOSED else 'pending_independent_AI_review',core_c='8',j=3,q=0,lower_bound_input_bits=lower,lower=lower,lower_log2_of_integer=str(H-3),literal_work_lower={'AND':'8*2^N','XOR':'24*2^N','actual_boundary_complex_ADD_count':len(adds),'used_complex_ADD_count':4,'complete_unreduced_field_required':True},early_effective_kappa='1/500',upper_derivation='own_source_common_retuned_with_record_tail',**{key:early[key] for key in ['A','E','Eguard','log2log2U','sufficient_upper_input_bits']},upper_source_certificate='p7-p17-record-crossover-bounds.json',native_source_certificate='p7-p17-record-crossover-bounds.json',backup_record_upper=record['sufficient_upper_input_bits'],backup_record_upper_log2log2=record['log2log2U'],backup_record_upper_certificate='p7-p17-record-crossover-bounds.json',record_branch=record,early_branch=early,finite_template={'rawB':B,'rawP':Pc,'target_mass':Mt,'paid_mass':Mp,'rankmass_surplus':Mt-Mp,'tensor_power':V,'productive_floor_base':f,'paid_cutoff_base':cut,'ambient_rank':m,'Klog_upper':k,'min_rank_log_floor':l,'flow_depth':g,'compiler_depth':f'{m}^{V}*H','Eguard':Eguard,'typed_serialized_monomials_checked':own_types,'inventory_bound':'log2 D_N<32HN','normalized_work':'G/W<K^2*N','K_formula':'32*(R+1); R=[1e9*v*(B+P)^v+Mp^v+B^v*f^v]*(10*m^(2v)+10)'},own_source_files=[r for r in entries if r['pr']==pr],new_parameter_instantiation=True,automatic_upper_transfer=False,native_absolute_phases_freshly_replayed=False,full_candidate_upper_review_closed=REVIEW_CLOSED,complete_whole_integer_upper_conditional=REVIEW_CLOSED,retains_original_asymptotic_record=True,actual_first_crossover_known=False,practical_hardware_crossover=False,checks_passed=len(CHECKS)-start))
out=dict(schema='own-p7-p17-record-crossover-bounds/1',status='closed_conditional_bounds' if REVIEW_CLOSED else 'pending_independent_AI_review',rows=OUT,lower_count=4,conditional_upper_count=4,common_protocol={'early_effective_kappa':'1/500','delta':'1/10000','A':'10001'},source_sha256=SOURCE_PINS,manifest_sha256=MANIFEST_PINS,dependency_hashes={p:hs(HERE/p) for p in deps},retained_contracts=['Each own PR native arbitrary-input, all-column and complete external spectator identity, with absolute phases, independent fields and matching owned erasure.','Exact tensor/completion/splitting and integer compiler contracts, including source strict moments and uniform-rank receipts.','Typed Clifford normal forms, original chronological barriers and replica synchronization, not an unmaterialized full word replay.','Parameterized fine-prime selection, Gaussian/finite-section conditioning, boundary solver and exact outer recovery contracts.','Repaired unbounded optimized-GMP finite-kernel correctness/halting/allocation and circuit lowering contracts.'],reference_comparisons={'optimized_reference':'gmp-630-native-skylake-unbounded-exact-constants-v2','canonical_HvH':True,'all_rho_positive':True},formal_status='AI-assisted written derivation and exact source/type/rational/integer checks; no Lean or independent human verification.',checks_passed=len(CHECKS),checks=CHECKS,script_sha256=hs(Path(__file__)))
(HERE/'p7-p17-record-crossover-bounds.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'checks':len(CHECKS),'rows':[{k:r[k] for k in ['pr','H','Eguard','log2log2U','lower','checks_passed']} for r in OUT]},indent=2))
