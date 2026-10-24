"""Own selected earliest2/3/4/10 finite Gaussian native interfaces."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
import ast,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(n,v):assert v,n;checks[n]=True
def ceil(x):return -(-x.numerator//x.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return{str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return[enc(v)for v in o]
 return o
rf='earliest-23410-source/fresh-selected-complex-arithmetic.json';replay=rd(rf);ck('own_actual_finite_functions_and_complete_sources',replay['status']=='checked_own_selected_finite_functions'and replay['checks_passed']==229 and all(replay['checks'].values())and replay['script_sha256']==hs('replay_earliest_23410_finite.py')and not replay['original_cpp_native_or_universal_phase_replayed'])
for f,h in replay['source_sha256'].items():ck('own_primary_'+f,hs(f)==h)
metadata={r['pr']:r for r in replay['metadata']};sources=dict(replay['source_sha256']);rows=[]
supplement='earliest-23410-source/general-guard-source-supplement.json';sup=rd(supplement);sources[supplement]=hs(supplement)
for a in sup['source_manifest']:ck('own_general_guard_supplement_'+a['path'],a['own_head']==metadata[a['pr']]['own_head_sha']and hs(a['file'])==a['sha256']);sources[a['file']]=a['sha256']
for e in replay['rows']:
 pr=e['pr'];pre=str(pr)+'_';o=rd(e['result_file']);ck(pre+'actual_selected_replay_payload',hs(e['result_file'])==e['result_sha256']and e['own_head']==metadata[pr]['own_head_sha']);sources[e['result_file']]=e['result_sha256']
 module={2:'aligned_paired_network',3:'complex_network',4:'retained_complex',10:'batched_network'}[pr];tree=ast.parse((R/f'earliest-23410-source/{pr}/scripts/{module}.py').read_text());kv=[a.value for a in tree.body if isinstance(a,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='KAPPA'for t in a.targets)]
 ck(pre+'actual_own_selected_target_constant',len(kv)==1 and eval(compile(ast.Expression(kv[0]),'<actual-own-source-target>','eval'),{'Q':F})==F(metadata[pr]['quoted_kappa_fraction']))
 if pr==2:
  n=o['counts'];m=n['m'];W=n['Wc'];mass=n['sc'];eta=F(1,10**11);logbound=F(11737,1000);theta=F(9,10);zeta=F(1,10000);old=o['guard'];E=64*(W+m+1)**3;B=mass+E;C0=ceil(max(F(128*m*B*B),18*m*B*B*(1+1/zeta)));C1=5-4*theta+zeta;steps=12*W
  ck(pre+'original_coarse_and_new_own_general_guard_distinct',old['C1']==2 and int(old['E'])==E and int(old['C0'])==128*m*B*B and C0>int(old['C0'])and C1==F(14001,10000))
  gs=(R/'earliest-23410-source/2/scripts/prepare_layers.py').read_text();gt=(R/'earliest-23410-source/2/notes/compact-control-guard.tex').read_text();ck(pre+'own_general_stopped_guard_source',all(s in gs for s in['def guard(beta, zeta=Q(1, 100), h=50):','C1 = 5-4*beta+zeta','18*m*B*B*(1+1/zeta)'])and 'C_1=5-4' in gt)
 elif pr==3:
  n=o['complex_counts'];m=n['m'];W=n['W'];mass=n['s'];eta=F(o['complex_saving']);logbound=F(o['log_m_upper']);theta=F(4,5);zeta=F(1,10000);E=o['witness']['guard']['E'];B=mass+E;C0=o['witness']['guard']['C0'];C1=5-4*theta+zeta;steps=o['gates']['total_gates']
  ck(pre+'complete_actual_coefficient_and_both_role_frame_checks',o['side_map']['side_map_exact']and o['role_frames']['forward_frames_nested']and o['role_frames']['reverse_complement_frames_nested'])
 elif pr==4:
  n=o['main']['counts'];m=n['m'];W=n['W'];mass=n['s'];eta=F(o['main']['parameters']['sigma']);eta=1-eta;logbound=F(o['main']['log_upper']);theta=F(4,5);zeta=F(1,10000);g=o['main']['guard'];E=g['E'];B=mass+E;C0=g['C0'];C1=5-4*theta+zeta;steps=g['scalar_gates']
  ck(pre+'complete_actual_retained_totals_and_both_frames',o['producer']['full_coefficient_map_exact']and o['producer']['exact_total_multiplicities']and o['frames']['both_physical_frame_directions'])
  actual=(R/'earliest-23410-source/4/docs/research/shared-retained-complex.md').read_text();ck(pre+'actual_selected_shared_retained_variant_not_other_legacy_TeX',all(s in actual for s in['R=90950','Every actual coefficient remains of magnitude at most one, denominator at','2(h-6) scalar gates per invocation','W=761750114048']))
 else:
  n=o['complex']['counts'];m=n['m'];W=n['W'];mass=n['s'];eta=F(o['complex']['complex_saving']);theta=F(1,10**9);zeta=F(1,10000);g=o['assembly']['guard'];E=g['E'];C0=g['C0'];B=mass+E;C1=F(g['rho'])-(F(g['rho'])-1)*theta+zeta;factory=o['actual_selected_complex_factory'];steps=3*n['v']**2*(4*(factory['additions']+factory['side_piece_count'])+4*n['v']+4);logbound=None
  ck(pre+'own_complete_mixed_profile_and_moment',sum(F(x)for x in o['complex']['rank_mass_weights'])==1-F(n['eta'])and F(o['complex']['moment_upper'])<1 and o['actual_selected_complex_factory']['roles']==n['side_roles']and o['actual_selected_complex_factory']['coefficient_alphabet']==['1/2','-1/2'])
  ck(pre+'own_bulk_path_guard',all(F(v)<F(g['theta_upper'])for v in g['path_moment_upper'].values())and g['dependency_constant']*(1-F(g['theta_upper']))>=E and g['at_most_one_selected_edge_per_path'])
 ck(pre+'complete_source_local_instruction_and_small_coefficient_bill',E==64*(W+m+1)**3 and steps<=12*W and 36*W**3+4*mass+4*W+8*m+4<E and 2048*m**4<E)
 ck(pre+'full_own_stopped_path_height',2<=mass<m**5 and mass*(8+E)<=9*B*B and (C0>=128*m*B*B if pr!=10 else C0>=128*m*(1+1/zeta)*g['dependency_constant']))
 ck(pre+'own_complete_nonlinear_width',C0<2**400 and 1<F(C1)<2 and 1-F(51,100)*C1>0)
 if logbound is not None:
  ck(pre+'independent_exact_log_bound',sum(logbound**i/F(factorial(i))for i in range(160))>m)
  alpha=F(mass,W*m)/(1-eta*logbound);ck(pre+'full_dimension_mass_rank_one_overpayment',0<eta*logbound<F(n['eta_c']if pr==2 else n['eta'])and 0<alpha<1)
  profile=dict(single_rank_one_overpayment=mass);moment_kind='source_normalized_tensor_dimension_mass_overpayment'
 else:
  alpha=F(o['complex']['moment_upper']);profile={1:n['singleton_calls']};profile.update({int(z['rank']):z['copies']for z in n['bulk_classes']});moment_kind='own_exact_whole_residual_mixed_profile'
  ck(pre+'complete_mixed_rank_mass',sum(k*v for k,v in profile.items())==mass)
 gap=1-alpha;row=(W-1).bit_length()*(m+1)+2*m+32;L=10**8 if pr==2 else 10**7;work=2**32*m**4*(E+W+mass+1)**2*(1+ceil(1/gap))**2*(1+row)**2
 ck(pre+'complete_row_and_allsize_finite_work',gap>F(1,2**100)and L>F(51*row,25)and 2**128>2*row and 2**128>2*m and work<2**100000 and 1024*E<work and 40*m<work)
 kernel=(R/f'earliest-23410-source/{pr}/upstream/build/sections/05-layers.tex').read_text();ck(pre+'own_normalized_C_kernel_inverse_and_tensor_anchor',all(s in kernel for s in['C=H\\mathsf SH=aI+bX','a=\\frac{1+i}{2}','b=\\frac{1-i}{2}','C^{-1}=bI+aX=-iZCZ','apply $(C^{\\epsilon_h})^{\\otimes f}$']))
 rows.append(dict(pr=pr,own_head=e['own_head'],kappa_record=metadata[pr]['quoted_kappa_fraction'],native_coordinate_rank=m,productive_W=W,total_child_dimension_mass=mass,own_E=E,own_recorded_C0=C0,new_C1=str(C1),new_stop=str(theta),own_uniform_saving=str(eta),own_moment_upper=str(alpha),own_moment_gap=str(gap),own_moment_kind=moment_kind,own_actual_or_overpaid_profile=profile,own_complete_row_coefficient=row,stopped_row_reserve_degree=L,own_allsize_work_coefficient_bound_power2=100000,local_pertype_word_coefficient=1024*E,original_cpp_native_or_simultaneous_phase_rerun=False,actual_selected_complex_arithmetic_replayed=True,source_selected_complete_cpp_native_operator_proved=False,legacy_PR4_other_retained_total_TeX_counts_used=False if pr==4 else None,retained_interfaces=['Own selected full all-role physical input/output Gaussian operator identities, required absolute phases and arbitrary dirty auxiliaries restored. Finite scalar/binary-frame checks alone do not prove the universal operator claim.','Own common-label/all-column/whole-call/all-size compiler and normalized completed Gaussian endpoint identities.','New fixed-wiring complete-row realization, complete native scalar/basis/phase/clear work and once-only row padding; only public-size address routing is free.','Exact dyadic augmented-grid native arithmetic and nonlinear source path guard; completed Gaussian-integer H returns discard only proven-zero fractional guard bits.']))
deps=['earliest-four-native-interfaces.md',rf,'replay_earliest_23410_finite.py','earliest-23410-source/manifest.json','earliest-23410-source/import-closure-manifest.json','earliest-23410-source/native-proof-manifest.json','partial-swap-endpoint-native-interface.md','partial-swap-endpoint-native-interface.json','pr937-historical-two-shear-gaussian-bounds.md','pr937-historical-two-shear-gaussian-peer-review.json','pr937_historical_two_shear_gaussian_bounds.py'];out=dict(schema='earliest-four-own-selected-native-interface/1',status='closed_conditional_component'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks=checks,checks_passed=len(checks),source_sha256=sources,dependency_hashes={f:hs(f)for f in deps},script_sha256=hs(Path(__file__).name),whole_integer_upper_claimed=False,original_cpp_native_or_universal_phase_replayed=False)
(R/'earliest-four-native-interfaces.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own earliest native interfaces; no whole U')
