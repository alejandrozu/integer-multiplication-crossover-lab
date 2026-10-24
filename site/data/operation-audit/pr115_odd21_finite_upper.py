"""Own PR104/130 odd21 finite profiles and full early operation envelopes."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'early-native-producer-source';checks={};REVIEW_CLOSED=True
def read(p):return json.loads((R/p).read_bytes())
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def ck(n,v):assert v,n;checks[n]=True
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x)for x in v]
 return v
def div21(x,w):
 r=q=0
 for i in range(w-1,-1,-1):
  u=2*r+((x>>i)&1);b=int(u>=21);r=u-21*b;q=2*q+b
 return q,r
ck('all16384_fixed21_digit_circuit_examples',all(div21(x,14)==divmod(x,21)for x in range(1<<14)))
ck('fixed21_per_digit_gate_tariff',6*16+6*8+32<1024)
rows=[]
for pr,name in [(115,'partial-gauge')]:
 M_full=read(f'early-native-producer-source/{pr}-manifest.json');M=[x for x in M_full if x['status']=='fetched_own_head_source_bytes'];files={x['path']:'early-native-producer-source/'+x['file']for x in M}
 ck('own_all_manifest_heads',all(x['head']=='cf60442983c153a3a0f5272ea4713f99eba13c86'for x in M_full))
 for x in M:ck(str(pr)+'_own_source_'+x['path'],x['status']=='fetched_own_head_source_bytes' and hs(files[x['path']])==x['sha256'])
 original=read(files[f'certificates/{name}-network.json']);fresh=read(f'early-native-producer-source/{pr}-fresh-arithmetic-certificate.json');replay=read(f'early-native-producer-source/{pr}-fresh-arithmetic-replay.json')
 ck('own_selected_record_value',F(original['kappa'])==F(7237,78125000))
 ck(str(pr)+'_own_untouched_arithmetic_pass',replay['returncode']==0 and replay['primary_code_changed'] is False and replay['native_cpp_producer_rerun'] is False)
 ck(str(pr)+'_same_all_numerical_and_contract_fields',{k:v for k,v in original.items()if k!='source_sha256'}=={k:v for k,v in fresh.items()if k!='source_sha256'})
 c=original['complex'];p=c['counts'];bridge=original['finite_bridge'];b=bridge['complex'];sem=bridge['semantic'];stock=bridge['rows'];m=p['m'];r=p['maxchild'];W=p['W'];s=p['total_rank'];eta=F(c['saving']);mu=1-F(c['moment_upper']);lit=sem['E'];G=b['scalar_group_upper'];C0=sem['C0'];D=b['halving_degree'];degree=stock['degree'];row=stock['coefficient']
 ck(str(pr)+'_native_strict_moment',0<eta<1 and 0<mu<1 and s<m*W)
 ck(str(pr)+'_whole_profile_mass',c['vertices_per_stage']*sum(int(k)*n for k,n in c['child_width_multiplicities'])==s if pr==130 else sum(int(k)*n for k,n in p['child_multiplicities'].items())==s)
 ck(str(pr)+'_halving',2*r**D<m**D)
 ck(str(pr)+'_odd21_not3',sem['fixed_odd_divisor']==21 and 'no child rounding'in sem['exact_grid'])
 ck(str(pr)+'_native_C1',sem['C1']==1)
 inv=-(-(1/mu).numerator//(1/mu).denominator)
 C=2**32*m**4*((1<<20)*lit+W+s+1)**2*(1+inv)**2*(1+row)**2
 ck(str(pr)+'_complete_work_and_macro_tariff',C<2**200000)
 ck(str(pr)+'_common_odd_grid_guard',5*G*(D+1)+C0<2**200000)
 ck(str(pr)+'_row_source_degree',degree>F(51*row,25))
 Q=10**6;delta=F(1,Q);kappa=F(1,100000);A=4*Q+1;E=1<<46;X=A*E;P=X-8;ep=1-delta;beta=1-3*delta;workexp=32*Q+1000000;reserve_degree=degree*Q
 # Own actual ordinary admission, kept as source evidence; direct Boolean
 # kernels do not execute an optional finite-field BIT implementation.
 bit=original['assembly']['parameters'].get('actual_bit_saving')
 if bit is None:bit=original['bit'].get('effective_saving') or original['bit'].get('saving')
 ck(str(pr)+'_own_bit_admission_present',bit is not None and F(bit)>kappa)
 ns={'__name__':f'own{pr}_weak_outer','__file__':str(R/'pr4535-upper-source/endpoint.py')};exec(compile((R/'pr4535-upper-source/endpoint.py').read_bytes(),'own_early_endpoint','exec'),ns)
 pars=dict(kappa=kappa,tested_saving=eta,complex_uniform_saving=eta,a=kappa+4*delta,b=kappa+5*delta,q=kappa+3*delta,bit_saving=F(bit),epsilon=ep,beta=beta,r0=delta/10,stop=delta,layout=delta,d=delta);ledger=ns['ledger'](pars)
 ck(str(pr)+'_fresh53_correctness',len(ledger['strict_checks'])==54 and {k for k,v in ledger['strict_checks'].items()if v<=0}=={'improvement_over_user_baseline'})
 ck(str(pr)+'_fresh3_functional',len(ledger['functional_checks'])==3 and all(v>0 for v in ledger['functional_checks'].values()))
 ck(str(pr)+'_fresh9_savings',len(ledger['margins'])==9 and all(v>kappa for v in ledger['margins'].values()))
 ck(str(pr)+'_full_stopped_stock',delta*X-10>reserve_degree*(X+3).bit_length()+1000)
 ck(str(pr)+'_work_precision_grid_umbrella',delta*E>workexp+200000+1040*(X+3).bit_length()+100)
 ck(str(pr)+'_prime_and_axis_gates',X>=2**54 and X>128*Q and delta*X>(1024*(65+1024*X)).bit_length())
 ck(str(pr)+'_comparator_and_hybrid_domains',P>80 and P>=(1729**12).bit_length() and kappa*X>10)
 for tag,v in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(str(pr)+'_'+tag+'_protected',v+F(1,1024)<-F(1,2))
 costs=[];xi=ledger['parameters']['cap_xi']
 for label,saving,power2,power,extra in [('target_FFT_H',ep*eta*(1-delta),252,2,8),('target_FFT_twiddles',ep,262,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),282,2,12),('dense_diagonals',1-ep+beta,282,1,13),('Strassen_boundaries',F(3,32)+xi-ep,252,1,11),('halos',80-ep-beta,242,1,10),('pointwise_recovery',F(1),262,1,10)]:
  gap=saving-kappa;d=reserve_degree+extra;bound=E*power+power2+d*(X+3).bit_length()-X*gap;ck(str(pr)+'_'+label+'_gap',gap>0);ck(str(pr)+'_'+label+'_whole_tail',F(4*d,X)<gap);ck(str(pr)+'_'+label+'_one_eighth',bound<=-3);costs.append(dict(name=label,saving=str(saving),margin=str(gap),power2=power2,power_B=power,log_degree=d,base_log2_ratio_upper=str(bound)))
 deps=['pr115-odd21-finite-upper.md','early-odd21-finite-uppers.md','early_odd21_finite_uppers.py','pr147-stopped-stock-correction.md','pr147-stopped-stock-correction-peer-review.json','pr147-finite-controller-upper.md','candidate-fermat-helper.json','fixed-small-rational-xag.json','fixed-exact-division-via-multiply.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py',f'early-native-producer-source/{pr}-manifest.json',f'early-native-producer-source/{pr}-fresh-arithmetic-replay.json',f'early-native-producer-source/{pr}-fresh-arithmetic-certificate.json']
 out=dict(schema='own-early-odd21-finite-controller-upper/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=M[0]['head'],source_head=M[0]['head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',native_coordinate_rank=m,N_is_not_coordinate_rank=True,kappa_record=str(original['kappa']),early_effective_kappa=str(kappa),delta=str(delta),Q=Q,A=str(A),E=str(E),upper_log2log2_integer=str(P),log2log2U=str(P),inputUpper=f'2^(2^{P})',upper=f'2^(2^{P})',meaningful_lower=None,meaningful_lower_bound=None,actual_first_crossing_known=False,record_tail_quantified=False,original_record_hybrid_compatibility=dict(extra_retained_same_XAG_record_realization_contract_required=True,public_size_choice='min totalAND+XOR across own originalrecord and explicit own earlycircuits',each_gate_type_upper='2*n*p^(1-1/100000)',weighted_ratio_upper='512*p^(-1/100000)<1',preserves_record_asymptotic_only_under_extra_contract=True,numeric_original_tail_bound=None),native_saving=str(eta),native_moment_gap=str(mu),odd_grid_divisor=21,fixed_rational_macro_pertype_upper='2^20*(w+1)',allsize_work_coefficient_exponent=str(workexp),allsize_work_log_degree=str(reserve_degree),unresolved_naive_import_candidates=[dict(path=x['path'],error=x.get('error'))for x in M_full if x['status']=='error'],native_cpp_producer_rerun=False,native_cpp_correctness_retained_as_hypothesis=True,arithmetic_numeric_receipt_reproduced=True,source_digest_inventory_byte_identity_claimed=False,new_outer_parameters=enc(ledger['parameters']),fresh_ledger=enc(ledger),cost_rows=costs,retained_contracts=['Own original C++ scalar/frame/matching producer, absolute phase, normalized-wrapper, whole-job and owned/spectator correctness; not freshly replayed here.','Own exact common21-odd grid, completed Gaussian-dyadic endpoint/new-child odd divisibility, C1=1 and all-size/common-label realization.','Gaussian/fine-prime/finite-section/boundary/recovery analytic branch and fixed comparator correctness/halting interfaces.'],formal_status='Conditional AI-assisted written derivation and exact source/arithmetic checks; not Lean or independent human verification.',source_sha256={files[x['path']]:x['sha256']for x in M},dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name))
 rows.append(out)
for out in rows:
 out.update(checks_passed=len(checks),checks=checks);(R/f'pr{out["pr"]}-odd21-partial-gauge-finite-early-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps({'checks':len(checks),'status':rows[0]['status'],'P':rows[0]['upper_log2log2_integer'],'prs':[r['pr']for r in rows]}))
