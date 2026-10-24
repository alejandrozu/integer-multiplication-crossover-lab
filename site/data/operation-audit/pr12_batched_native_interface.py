"""Own PR12 finite source + nonlinear complex coefficient interface; no whole U."""
from pathlib import Path
from hashlib import sha1,sha256
from fractions import Fraction as F
import json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'early-batched12-source';checks={};REVIEW_CLOSED=True
def ck(k,v):assert v,k;checks[k]=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ceil(x):return -(-x.numerator//x.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
head='35d31e30f28bc5da0ae6a88e7b03d75ebc855534';M=rd('early-batched12-source/source-fetch-manifest.json')+rd('early-batched12-source/additional-module-manifest.json');pins={};source={a['path']:a for a in M}
for a in M:
 raw=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();ck('own_raw_'+a['path'],a['pr']==12 and a['own_head']==head and sha256(raw).hexdigest()==a['sha256']and blob==a['git_blob_sha1']and(a.get('api_changed_blob')is None or a['api_changed_blob']==blob));pins[a['file']]=a['sha256']
f='early-batched12-source/fresh-finite-arithmetic.json';replay=rd(f);ck('unchanged_own_witness_function_only',replay['own_head']==head and replay['own_record_kappa']=='12649/100000000000'and replay['all29constraints']and replay['all_recorded_source_hashes_exact']and not replay['source_code_modified']and not replay['own_cpp_fullproducer_or_native_replayed']and replay['additional_recorded_fields_not_freshly_executed']==['matching','producer','source_sha256','template_controls']);pins[f]=hs(f)
own='early-batched12-source/research/batched-followup/certificate.json';c=rd(own);complex=c['complex'];counts=complex['counts'];g=c['assembly']['guard'];m=counts['m'];W=counts['W'];mass=counts['s'];P={1:counts['singleton_calls']}
for a in counts['bulk_classes']:P[a['rank']]=a['copies']
ck('own_selected_complete_profile',m==21952 and W==2085111546336 and P=={1:2389799139122304,21896:1007397164592,21168:1007397164592}and sum(k*v for k,v in P.items())==mass==45772350635112192 and max(P)<m and W*m>mass)
eta=F(complex['complex_saving']);alpha=F(complex['moment_upper']);gap=1-alpha;logs=[F(x)for x in complex['logarithm_upper_bounds']];weights=[F(x)for x in complex['rank_mass_weights']];ck('own_exact_rational_moment',eta==F(7,10**7)and sum(w/(1-eta*l)for w,l in zip(weights,logs))==alpha<1 and gap>F(1,2**100))
E=64*(W+m+1)**3;ck('own_total_local_scalar_allowance',E==g['E']and 36*W**3+4*mass+4*W+8*m+4<E)
bulk=(D/'notes/bulk-complex-guard.tex').read_text();rows=(D/'notes/batched-complex-rows.tex').read_text();rawc=(D/'notes/complex-circuit-construction.tex').read_text();ck('own_scalar_wrappers_and_circuit_count_passages','36W^3+4s+4W+8m+4<E'in bulk and'12W_'in rawc and'coefficients in'in rawc and'four elementary'in bulk)
ck('own_complete_row_and_arbitrary_stop_source','q_0=\\lceil\\log_2 W\\rceil'in rows and'exactly'in rows and"$1/W$"in rows and'Fix rational $0<\\beta<1$'in rows)
row=(W-1).bit_length()*(m+1)+2*m+32;inv=ceil(1/gap);work=2**32*m**4*(E+W+mass+1)**2*(1+inv)**2*(1+row)**2
ck('own_row_and_geometric_envelopes',10**7>F(51*row,25)and 2**128>2*row and 2**128>2*m and work<2**100000 and 1024*E<work)
rho=F(g['rho']);gamma=F(g['theta_upper']);zeta=F(g['zeta']);dep=F(E+16*m+1)/(1-gamma);C0=ceil(128*m*(1+1/zeta)*dep);theta=F(1,10**9);C1=rho-(rho-1)*theta+zeta;epsilon=F(51,100)
ck('own_recorded_path_constants_exact',gamma==F(999,1000)and max(F(x)for x in g['path_moment_upper'].values())<gamma and dep==g['dependency_constant']and C0==g['C0']and F(g['C1'])==rho-(rho-1)*F(g['beta'])+zeta)
ck('new_nonlinear_stopping_instance',C1>1 and 1-epsilon*C1>0 and C0<2**200)
component=rd('partial-swap-endpoint-native-interface.json');ck('closed_general_coefficient_work_row_depth_lemma',component['status']=='closed_conditional_component'and not component['whole_integer_upper_claimed']and component['script_sha256']==hs('partial_swap_endpoint_native_interface.py')and all(component['checks'].values()))
deps=['pr12-batched-native-interface.md','replay_early_batched12_finite.py','early-batched12-source/source-fetch-manifest.json','early-batched12-source/additional-module-manifest.json','partial-swap-endpoint-native-interface.md','partial-swap-endpoint-native-interface.json','partial_swap_endpoint_native_interface.py','partial-swap-endpoint-native-interface-peer-review.json'];depmap={f:hs(f)for f in deps}
out=dict(schema='own-large-native-nonlinear-precision-interface/1',status='closed_conditional_component'if REVIEW_CLOSED else'pending_independent_AI_review',rows=[dict(pr=12,own_head=head,kappa_record='12649/100000000000',native_coordinate_rank=m,productive_W=W,own_child_profile=P,whole_rank_mass=mass,own_uniform_saving=eta,own_moment_upper=alpha,own_moment_gap=gap,own_E=E,local_pertype_word_coefficient=1024*E,own_complete_row_coefficient=row,compact_address_fields_replaced_by_free_fixed_wiring=True,GL_group_stock_enumerated_or_assumed=False,stopped_row_reserve_degree=10**7,stopped_row_reserve_constant_bits=128,own_allsize_work_coefficient_bound_power2=100000,own_recorded_C0=C0,own_recorded_C1=F(g['C1']),own_recorded_stop=F(g['beta']),new_stop=theta,new_C1=C1,new_epsilon=epsilon,new_semantic_power_gap=1-epsilon*C1,original_cpp_native_or_simultaneous_phase_rerun=False,own_finite_replay_file='early-batched12-source/fresh-finite-arithmetic.json',own_finite_replay_sha256=hs('early-batched12-source/fresh-finite-arithmetic.json'),source_certificate=own,source_certificate_sha256=hs(own),retained_interfaces=component['rows'][0]['retained_interfaces'])],whole_integer_upper_claimed=False,meaningful_lower=None,original_dimension30_BIT_algorithm_costed=False,model='xag-straightline-v1',checks=checks,checks_passed=len(checks),source_sha256=pins,dependency_hashes=depmap,script_sha256=hs(Path(__file__).name))
(R/'pr12-batched-native-interface.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own12 native source/nonlinear interface')
