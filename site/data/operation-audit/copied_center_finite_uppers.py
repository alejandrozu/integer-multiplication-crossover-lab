"""Source-specific copied-center finite controllers: own profiles and explicit weak early upper."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from collections import Counter
from math import comb
import ast,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/"copied-center-finite-source";checks={};REVIEW_CLOSED=True
PRS=[46,48,49,50,51,52,54,55,56,57,58,60,61,62]
def read(p):return json.loads((R/p).read_bytes())
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def ck(n,v):assert v,n;checks[n]=True
def require(v,msg):assert v,msg
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x)for x in v]
 return v
def halving(m,r):
 d=1
 while 2*r**d>=m**d:d+=1
 return d
def funcs(path,names,env):
 tree=ast.parse((R/path).read_bytes());nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in names];assert {n.name for n in nodes}==set(names);exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),"exec"),env)
def ln_upper(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(t):
  y=(t-1)/(t+1);terms=64;s=sum(y**(2*j+1)/F(2*j+1)for j in range(terms));tail=y**(2*terms+1)/((2*terms+1)*(1-y*y));return 2*s,2*(s+tail)
 lo2,up2=series(F(2));lo,up=series(x)
 return up+k*(up2 if k>=0 else lo2)
def moment_upper(p,eta):
 ans=F(0)
 for r,n in p['child_multiplicities'].items():
  t=eta*ln_upper(F(p['m'],int(r)));assert 0<=t<1
  ans+=F(n*int(r),p['m'])*(1+t+t*t/(2*(1-t/3)))
 return ans/p['W']
D=read('finite-controller-cost-dispatch.json');by={x['pr']:x for x in D['rows']};rows=[]
scalar=read('copied-center-finite-source/h28-d19-scalar-replay.json')
ck('unchanged_factory_scalar_linear_binary_frame_replay',scalar['status']=='PASS'and scalar['primary_factory_code_changed'] is False and scalar['native_cpp_matching_rerun'] is False and all(scalar['construction']['scalar_validation'].values()))
reference=read('copied-center-finite-source/46-manifest.json');ref={x['path']:x['sha256']for x in reference}
for pr in PRS:
 src=by[pr];prefix=str(pr)+'_';manifest=read(f'copied-center-finite-source/{pr}-manifest.json')+read(f'copied-center-finite-source/{pr}-invoice-extra-manifest.json');files={x['path']:'copied-center-finite-source/'+x['file']for x in manifest}
 for x in manifest:ck(prefix+'own_byte_'+x['path'],x['head']==src['own_head']and hs(files[x['path']])==x['sha256']and src['own_head']in x['url'])
 for path,digest in ref.items():ck(prefix+'exact_common_native_factory_'+path,next(x for x in manifest if x['path']==path)['sha256']==digest)
 # Exact quoted alignment identifies which explicit own candidate is priced;
 # it is not proof of historical first-claim priority or a record.
 selected=[x for x in src['finite_candidates']if x['exact_quoted_kappa_alignment']];ck(prefix+'one_explicit_candidate_for_quoted_source_value',len(selected)==1);selected=selected[0];original=read(selected['source_file']);ck(prefix+'own_selected_artifact',hs(selected['source_file'])==selected['sha256']and selected['own_head']==src['own_head']and F(original['kappa'])==F(src['quoted_kappa_fraction']))
 inp=read(files['certificates/copied-centers-complex-input.json']);h=inp['h'];d=inp['central_disjoint'];ck(prefix+'actual_dyadic_factory_scale',h==28 and d==19 and abs(2*(3-d))==32)
 factory=(R/files['scripts/structured_bulk/complex.py']).read_text();ck(prefix+'factory_scalar_grammar_anchors',all(x in factory for x in ['Ordinary additions must be cancellation-free','Center coefficients must be exactly doubled','2*(3-d)','Fraction(len((target_set-Dset).intersection(source)),2)','binary_frames_nondegenerate=True']))
 ck(prefix+'native_input_raw_replay_counts',all(inp[x]==scalar['construction'][y]for x,y in [('h','h'),('v','v'),('c','c'),('q','q'),('baseline_R','R'),('loss','loss')]))
 ck(prefix+'selected_matching_accounting',inp['baseline_R']==inp['c']+inp['q']and inp['R']==inp['baseline_R']-inp['matched']and sum(i*n for i,n in enumerate(inp['histogram']))==h*inp['R']+2*inp['loss'])
 env=dict(require=require,Counter=Counter,comb=comb,Q=F,halving=halving)
 funcs(files['scripts/copied_centers/physical.py'],['copied_histogram'],env);env['physical_histogram']=env.pop('copied_histogram')
 funcs(files['scripts/copied_centers_network.py'],['copied_histogram','profile','finite_bridge'],env)
 profile=env['profile']([inp,inp]);bridge=original['finite_bridge'];freshbridge=env['finite_bridge'](bridge['bit'],profile,[inp,inp]);ck(prefix+'complete_own_complex_bridge_regenerated',enc(freshbridge)==bridge or all(enc(freshbridge[k])==bridge[k]for k in ['bit','complex','semantic'])and all(enc(freshbridge['rows'][k])==bridge['rows'][k]for k in ['coefficient','degree','degree_gap','suffix_slope']))
 stored=original.get('complex',{}).get('counts',original.get('phase'))
 if stored:ck(prefix+'own_full_rank_histogram_matches',all(enc(profile[k])==stored[k]for k in ['m','W','total_rank','maxchild','child_multiplicities']))
 m=profile['m'];W=profile['W'];s=profile['total_rank'];eta=F(original['assembly']['parameters']['a_complex']);mu=1-moment_upper(profile,eta);sem=bridge['semantic'];lit=sem['E'];G=bridge['complex']['scalar_group_upper'];C0=sem['C0'];degree=bridge['rows']['degree'];row=bridge['rows']['coefficient'];D_c=bridge['complex']['halving_degree']
 ck(prefix+'actual_source_uniform_saving',eta==F(717,10**7)and 0<mu<1 and s<m*W)
 ck(prefix+'native_C1_and_halving',sem['C1']==1 and 2*profile['maxchild']**D_c<m**D_c)
 # All source scalar ADDs have coefficient 1, doubled center sums have 2,
 # scatter coefficients are half-integers of absolute value <=1, and total
 # recovery is (sum B-2sum D)/(-32). Coefficient macro bound is conservative.
 ck(prefix+'fixed_dyadic_coefficient_range',h-1<32 and max(abs(F(k-1,2))for k in range(4))<=1 and abs(F(1,2*(3-d)))==F(1,32))
 inv=-(-(1/mu).numerator//(1/mu).denominator);C=2**32*m**4*((1<<20)*lit+W+s+1)**2*(1+inv)**2*(1+row)**2
 ck(prefix+'complete_work_and_dyadic_macro_tariff',C<2**200000 and C0<2**200000)
 ck(prefix+'full_row_source_degree',degree>F(51*row,25))
 Q=10**6;delta=F(1,Q);kappa=F(1,100000);A=4*Q+1;E=1<<46;X=A*E;P=X-8;ep=1-delta;beta=1-3*delta;workexp=32*Q+1000000;reserve_degree=degree*Q
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
 deps=['copied-center-finite-uppers.md','pr147-stopped-stock-correction.md','pr147-stopped-stock-correction-peer-review.json','pr147-finite-controller-upper.md','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py','copied-center-finite-source/h28-d19-scalar-replay.json',f'copied-center-finite-source/{pr}-manifest.json',f'copied-center-finite-source/{pr}-invoice-extra-manifest.json']
 out=dict(schema='own-copied-center-finite-controller-upper/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=src['own_head'],source_head=src['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',native_coordinate_rank=m,N_is_not_coordinate_rank=True,kappa_record=str(original['kappa']),early_effective_kappa=str(kappa),delta=str(delta),Q=Q,A=str(A),E=str(E),upper_log2log2_integer=str(P),log2log2U=str(P),inputUpper=f'2^(2^{P})',upper=f'2^(2^{P})',meaningful_lower=None,meaningful_lower_bound=None,actual_first_crossing_known=False,record_tail_quantified=False,original_record_hybrid_compatibility=dict(extra_retained_same_XAG_record_realization_contract_required=True,public_size_choice='min total AND+XOR across own original record and explicit own early circuits',each_gate_type_upper='2*n*p^(1-1/100000)',weighted_ratio_upper='512*p^(-1/100000)<1',preserves_record_asymptotic_only_under_extra_contract=True,numeric_original_tail_bound=None),native_saving=str(eta),native_moment_gap=str(mu),odd_grid_divisor=1,actual_recovery_scale='-1/32',fixed_rational_macro_pertype_upper='2^20*(w+1)',allsize_work_coefficient_exponent=str(workexp),allsize_work_log_degree=str(reserve_degree),native_scalar_factory_replay=True,native_cpp_matching_rerun=False,native_cpp_correctness_retained_as_hypothesis=True,selection_basis='Explicit own artifact exactly states the quoted source kappa, and its own complete finite bridge is regenerated from its own native input/factory/profile. No record-priority inference.',selected_source=dict(path=selected['source_path'],file=selected['source_file'],sha256=selected['sha256']),new_outer_parameters=enc(ledger['parameters']),fresh_ledger=enc(ledger),cost_rows=costs,retained_contracts=['Own matched physical scalar/frame/absolute-phase and copied-stream scheduling correctness, simultaneous bases and owned/spectator interface; C++ matching not freshly replayed.','Own all-size exact common-label dyadic supplier realization with C1=1 and full sequential row-stock/guard semantics.','Gaussian/fine-prime/finite-section/boundary/exact-recovery analytic branch and fixed comparator correctness/halting interfaces.'],formal_status='Conditional AI-assisted written derivation and exact source/arithmetic checks; not Lean or independent human verification.',source_sha256={files[x['path']]:x['sha256']for x in manifest}|{selected['source_file']:selected['sha256']},dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name))
 rows.append(out)
for out in rows:
 out.update(checks_passed=len(checks),checks=checks);(R/f'pr{out["pr"]}-copied-center-finite-early-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps({'checks':len(checks),'status':rows[0]['status'],'P':rows[0]['upper_log2log2_integer'],'prs':PRS}))
