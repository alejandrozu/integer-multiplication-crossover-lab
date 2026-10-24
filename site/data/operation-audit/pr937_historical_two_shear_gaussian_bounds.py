"""Own937 historical two-shear core: fresh arbitrary-rank nonlinear Gaussian costs."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha1,sha256
from math import factorial
import ast,base64,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
head='b303fed6dfe2066dcd78c0d8ed74d2a3b153ba72';mf='pr937-finite-source/source-manifest.json';manifest=rd(mf);pins={};paths={}
for a in manifest['source_manifest']:
 raw=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();ck('own_source_'+a['path'],a['pr']==937 and a['own_head']==head and hs(a['file'])==a['sha256']and blob==a['git_blob_sha1']and(a['expected_api_blob_sha1']is None or a['expected_api_blob_sha1']==blob)and(a['own_declared_sha256']is None or a['own_declared_sha256']==hs(a['file'])));pins[a['file']]=a['sha256'];paths[a['path']]=a['file']
rf='pr937-finite-source/fresh-finite-verification.json';replay=rd(rf);ck('untouched_complete_own_finite_replay',replay['pr']==937 and replay['own_head']==head and replay['source_manifest_sha256']==hs(mf)and replay['script_sha256']==hs('replay_pr937_finite_source.py')and replay['original_own_finite_verifier_executed']and replay['returncode']==0 and all(replay['checks'].values())and not replay['full_integer_algorithm_or_universal_phase_proved'])
for f,h in replay['source_sha256'].items():ck('replayed_'+f,hs(f)==h)
chronf='pr937-finite-source/chronology.json';chron=rd(chronf);ck('actual_merge_includes_exact_own_head',chron['pr']==937 and chron['own_head']==head and chron['source_included_at_actual_merge']and chron['direct_source_parent_number']>=1)
for f,h in chron['source_primary_sha256'].items():ck('chronology_'+f,hs(f)==h);pins[f]=h
kf='pr937-kernel-definition-source/manifest.json';kernel=rd(kf);km={a['path']:a['file']for a in kernel}
for a in kernel:
 raw=(R/a['file']).read_bytes();api=rd(a['primary_receipt']);blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
 ck('own_kernel_definition_'+a['path'],a['pr']==937 and a['own_head']==head and hs(a['file'])==a['sha256']and hs(a['primary_receipt'])==a['primary_receipt_sha256']and api['path']==a['path']and api['sha']==blob==a['git_blob_sha1']and base64.b64decode(api['content'])==raw)
 pins[a['file']]=a['sha256'];pins[a['primary_receipt']]=a['primary_receipt_sha256']
layertext=(R/km['upstream/build/sections/05-layers.tex']).read_text();rowtext=(R/km['notes/batched-complex-rows.tex']).read_text()
ck('actual_source_normalized_two_point_kernel_and_inverse_phase',all(s in layertext for s in['C=H\\mathsf SH=aI+bX','a=\\frac{1+i}{2}','b=\\frac{1-i}{2}','C^{-1}=bI+aX=-iZCZ','apply $(C^{\\epsilon_h})^{\\otimes f}$']))
ck('actual_source_residual_tensor_block_product',all(s in rowtext for s in['\\prod_{v=1}^{a}(C^{\\varepsilon_v})^{\\otimes f}','=(-i)^{f|B|}Z_B C^{\\otimes af}Z_B','the basis maps before and after the operation are unchanged']))
zero=(F(0),F(0));one=(F(1),F(0));ii=(F(0),F(1));aa=(F(1,2),F(1,2));bb=(F(1,2),F(-1,2))
def ga(x,y):return(x[0]+y[0],x[1]+y[1])
def gm(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def mm(x,y):return[[sumg(gm(u,v)for u,v in zip(row,col))for col in zip(*y)]for row in x]
def sumg(xs):
 z=zero
 for x in xs:z=ga(z,x)
 return z
def kron(x,y):return[[gm(a,b)for a in rowx for b in rowy]for rowx in x for rowy in y]
I2=[[one,zero],[zero,one]];Z=[[one,zero],[zero,(-F(1),F(0))]];C=[[aa,bb],[bb,aa]];Ci=[[bb,aa],[aa,bb]]
ck('exact_gaussian_inverse_and_absolute_quarter_phase',mm(C,Ci)==I2 and [[gm((F(0),-F(1)),v)for v in row]for row in mm(mm(Z,C),Z)]==Ci)
C2=kron(C,C);I4=kron(I2,I2)
ck('exact_normalized_block_tensor_associativity',mm(kron(C2,I4),kron(I4,C2))==kron(C2,C2))
own=rd(paths['research/dyadic-center-two-shear/EXPECTED.json']);n=own['counts_unchanged'];invoice=own['scalar_invoice'];g=invoice['guard'];quote=rd(paths['research/dyadic-center-two-shear/BASE-SELECTED.json'])['kappa'];kappa=F(1,2**31)
targetsource=paths['scripts/audit_complex_centers.py'];tree=ast.parse((R/targetsource).read_text());target=[q.value for q in ast.walk(tree)if isinstance(q,ast.keyword)and q.arg=='retained_kappa'];ck('own_historical_core_target_not_contemporary_quote',len(target)==1 and eval(compile(ast.Expression(target[0]),'<own-retained-kappa>','eval'),{'Q':F})==kappa and F(quote)==F(own['selected_kappa'])and F(quote)>kappa and 'The integrated conditional kappa remains\n2^-31'in(R/paths['docs/research/dyadic-central-factor.md']).read_text())
m=n['m'];W=n['W'];mass=n['s'];Esource=64*(W+m+1)**3;steps=invoice['after'];eta=F(35,10**9);theta=F(4,5);zeta=F(1,1000)
ck('actual_complete_native_profile_and_improved_scalar_invoice',m==26**3 and W==1247192960000 and mass==21920655731520000 and W*m-mass==n['deficit']>0 and n['side_roles']==89622 and steps==15846305280000<invoice['before']==15959102640000 and own['candidate']==dict(G=10100,H=32500,G_plus_H=42600))
ck('complete_local_word_phase_remainder_allowance',Esource==invoice['E']and Esource-(4*steps+8*mass+8*W+8*m)==invoice['slack']>0)
ck('bounded_actual_scalar_grammar',own['candidate_coefficient_check']['all_scalar_weights_dyadic']and own['candidate_coefficient_check']['integer_product_verified']and all(a['total']==781376 for k,a in own['emitted_instruction_census'].items()if k.startswith('candidate'))and own['three_stage_reused_bank'])
ck('explicit_unit_gather_half_scatter_source_grammar',"x in (-1,0,1,2)"in(R/paths['scripts/experiments/complex_centers.py']).read_text()and 'Q(weight,2)'in(R/paths['scripts/experiments/complex_centers.py']).read_text()and "abs(x) <= 2"in(R/paths['research/dyadic-center-two-shear/circuit.py']).read_text())
ck('independent_log_integer_upper',sum(F(10**j,factorial(j))for j in range(41))>m)
alpha=F(mass,W*m)/(1-10*eta);gap=1-alpha
ck('coarse_complete_integer_rank_moment',0<eta*10<F(n['eta'])and 0<alpha<1 and gap>F(1,2**100))
B=mass+Esource;C0=ceil(max(F(128*m*B*B),18*m*B*B*(1+1/zeta)));C1=5-4*theta+zeta
ck('own_full_nonlinear_layer_constant',2<=mass<m**5 and mass*(8+Esource)<=9*B*B and C0==g['C0']and C0>=9*m*B*B*(1+1/zeta)+18 and F(g['C1'])==5-4*F(g['beta'])+zeta and F(g['alpha'])==5 and C0<2**400)
ck('new_fixed_stopping_power_and_full_semantic_gap',C1==F(1801,1000)and 1-F(51,100)*C1==F(8149,100000)>0)
row=(W-1).bit_length()*(m+1)+2*m+32;L=10**7;work=2**32*m**4*(Esource+W+mass+1)**2*(1+ceil(1/gap))**2*(1+row)**2
ck('own_complete_row_stock_and_allsize_coefficient',L>F(51*row,25)and 2**128>2*row and 2**128>2*m and work<2**100000 and 1024*Esource<work and 40*m<work)
parent='nonlinear_native_gaussian_bounds.py';p9='pr9_nonlinear_native_gaussian_bounds.py';pp='pr9-nonlinear-native-gaussian-peer-review.json';peer=rd(pp)
ck('frozen_nonlinear_whole_and_reviewed_specialization',hs(parent)=='a3716b41191371e77b44cf5c8a803ced3d26a9ce94d5ecb5631380f4219bf1db'and hs(p9)=='e96d03d4b12f0a251bfc929eafe590df316f820f622188570fe74ac5fa1a00ed'and peer['review_status'].startswith('PASS')and peer['reviewed_sha256'][p9]==hs(p9))
ps=(R/parent).read_text();fn=ast.get_source_segment(ps,next(a for a in ast.parse(ps).body if isinstance(a,ast.FunctionDef)and a.name=='branch'));changes=ast.literal_eval(next(a.value for a in ast.parse((R/p9).read_text()).body if isinstance(a,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='changes'for t in a.targets)))
for i,(before,after)in enumerate(changes):ck('explicit_nonlinear_specialization_'+str(i),fn.count(before)==1);fn=fn.replace(before,after)
before='theta==F(19,25)';ck('own937_theta_specialization',fn.count(before)==1);fn=fn.replace(before,'theta==F(4,5)')
sp=importlib.util.spec_from_file_location('closed_reduced_Gaussian_own937',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
Q=10**11;delta=F(1,Q);epsilon=F(51,100);beta=F(1,200);layout=F(9,100);A=4*Q+1;E=2**32;X=A*E;P=X-8;u=(X+3).bit_length()
env=dict(F=F,ceil=ceil,enc=enc,G=G,Q=Q,delta=delta,epsilon=epsilon,beta=beta,layout=layout,A=A,E=E,X=X,P=P,u=u);exec(compile(fn,'own937_nonlinear_source_specialization','exec'),env)
a=dict(pr=937,new_C1=C1,new_stop=theta,native_coordinate_rank=m,own_recorded_C0=C0,stopped_row_reserve_degree=L,own_complete_row_coefficient=row,own_uniform_saving=eta,original_cpp_native_or_simultaneous_phase_rerun=False,own_allsize_work_coefficient_bound_power2=100000,local_pertype_word_coefficient=1024*Esource,own_E=Esource)
# Both fresh targets deliberately use the independently funded EARLY auxiliary
# values; the contemporary799 target is not evaluated as a source937 record.
early=env['branch'](a,F(1,10**9),False);record=env['branch'](a,kappa,False)
for tag,o in[('early',early),('historical_record',record)]:
 led=o['modified_Gaussian_ledger'];gaps=[F(v)for v in led['strict_checks'].values()]+[F(v)for v in led['functional_checks'].values()]+[F(v)-F(o['kappa'])for v in led['margins'].values()];degree=int(o['allsize_work_log_degree'])
 ck(tag+'_all_strict_functional_margin_log_warmup',min(gaps)*X>int(o['allsize_work_coefficient_exponent'])+(degree+1040)*u+100 and F(4*(degree+1040),X)<min(gaps))
 ck(tag+'_own_stop_and_exact_runtime_rows',o['native_stop']=='4/5'and F(o['native_stop'])!=delta and all(o['checks'].values())and F(o['cost_rows'][0]['saving'])==F(357,10**11))
deps=['pr937-historical-two-shear-gaussian-bounds.md',mf,rf,chronf,kf,'replay_pr937_finite_source.py',parent,'nonlinear-native-gaussian-bounds.md','nonlinear-native-gaussian-bounds.json','pr12-nonlinear-native-gaussian-peer-review.json',p9,'pr9-nonlinear-native-gaussian-bounds.md',pp,'pr9-nonlinear-native-gaussian-source-peer-review.json','partial-swap-endpoint-native-interface.md','partial-swap-endpoint-native-interface.json','partial_swap_endpoint_native_interface.py','partial-swap-endpoint-native-interface-peer-review.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger.json','gaussian-only-parameter-ledger-peer-review.json','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json'];dm={f:hs(f)for f in deps}
contracts=['Own historical937 full all-role native circuit, required physical entry/output maps and absolute phases; arbitrary dirty auxiliaries are restored. Finite scalar/frame checks are not a universal operator theorem.','Own common-label/all-column/whole-call/all-size phase-transfer and normalized Gaussian endpoint contracts, with source nonlinear stopped-depth recurrence at arbitrary fixedtheta.','New fixed-wiring arbitrary-rank complete-row realization and once-only padding; no free data arithmetic or unbounded descriptors are assumed.','Exact dyadic augmented-grid native arithmetic, completed Gaussian-integer H return and disjoint complete coefficient blocks with nonlinear convexity are those of the closed global proof, with ownC0/C1 paid in full.','Concrete normalized accretivity/finite-LDU/FFT/narrow/cyclic convolution/boundary/recovery and repaired optimized-reference correctness/halting remain explicit; the false scale-free general theorem is not imported.']
common=dict(pr=937,own_head=head,source_head=head,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(kappa),frozen_metadata_kappa=quote,source_selected_kappa_correction=True,source_selected_kappa_correction_basis='Own actual historical h26 complex construction retains2^-31 in own scripts/audit_complex_centers.py and explicit own historical research note. The preserved contemporary BASE-SELECTED PR799 quote is unrelated context and is not implemented or improved by937.',unrelated_contemporary_BASE_SELECTED_kappa=quote,new_accepted_exponent_record_claimed=False,costed_variant='new_direct_Gaussian_realization_of_own_historical_two_shear_core',source_chronology=chron,native_coordinate_rank=m,not_uniform_2_to_H=True,nonlinear_native_precision=True,original_historical_BIT_algorithm_costed=False,source_cpp_or_fullnative_rerun=False,original_own_finite_verifier_replayed=True,new_fixedwiring_row_realization=True,meaningful_lower=None,actual_first_crossing_known=False,source_sha256=pins,dependency_hashes=dm,retained_contracts=contracts,script_sha256=hs(Path(__file__).name),explicit_function_adaptations=[dict(before=x,after=y)for x,y in changes]+[dict(before=before,after='theta==F(4,5)')],adapted_function_sha256=sha256(fn.encode()).hexdigest())
nf='pr937-historical-two-shear-gaussian-native.json';ef='pr937-historical-two-shear-gaussian-early-upper.json';of='pr937-historical-two-shear-gaussian-record-upper.json'
native=dict(common,schema='own937-historical-two-shear-native-costs/1',own_complete_counts=n,own_scalar_invoice=invoice,own_local_pertype_coefficient=1024*Esource,own_row_coefficient=row,own_moment_saving=str(eta),own_moment_upper=str(alpha),own_moment_gap=str(gap),new_native_stop=str(theta),new_native_precision_C1=str(C1),own_recorded_C0=str(C0),own_allsize_work_coefficient_bound_power2=100000,whole_instance_checks=checks.copy())
ro=dict(common,**record,schema='own937-historical-two-shear-record-upper/1');(R/of).write_text(json.dumps(enc(ro),indent=2)+'\n',encoding='utf8')
eo=dict(common,**early,schema='own937-historical-two-shear-early-upper/1',early_effective_kappa='1/1000000000',record_tail_quantified=True,record_tail_certificate=of,record_tail_certificate_sha256=hs(of),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Fresh own historical-core2^-31 target only. The contemporary PR799 quote is preserved unrelated context, not a funded tail of this core.')
for f,o in[(nf,native),(ef,eo)]: (R/f).write_text(json.dumps(enc(o),indent=2)+'\n',encoding='utf8')
out=dict(schema='own937-historical-two-shear-nonlinear-whole-costs/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',pr=937,own_head=head,kappa_record=str(kappa),frozen_metadata_kappa=quote,source_selected_kappa_correction=True,native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=of,upper_log2log2_integer=str(P),checks=checks,checks_passed=len(checks)+early['checks_passed']+record['checks_passed'],outer_checks_passed=early['checks_passed']+record['checks_passed'],script_sha256=hs(Path(__file__).name))
(R/'pr937-historical-two-shear-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',out['checks_passed'],'own937 historical-core nonlinear checks; P',P)
