"""Own18/24 large-rank coefficient work/rows and nonlinear semantic interface."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys,subprocess
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'partial-swap-endpoint-source';checks={};REVIEW_CLOSED=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
rows=[];pins={};theta=F(1,10**9);epsilon=F(51,100)
for pr,stem,name,head in[(18,'partial-swap','partial_swap_network.py','f2ab41aebad47861caf6316282c1793e5513845e'),(24,'endpoint-gauge','endpoint_gauge_network.py','ed90fd940279c336ebc45968631bdebfb087b505')]:
 prefix=str(pr)+'_';M=rd(f'partial-swap-endpoint-source/{pr}-manifest.json')+rd(f'partial-swap-endpoint-source/{pr}-additional-module-manifest.json');source={a['path']:a for a in M}
 for a in M:ck(prefix+'own_raw_'+a['path'],a['own_head']==head and hs(a['file'])==a['sha256']);pins[a['file']]=a['sha256']
 replayf=f'partial-swap-endpoint-source/{pr}-fresh-finite-arithmetic.json';replay=rd(replayf)
 ck(prefix+'unchanged_own_finite_arithmetic',replay['own_head']==head and replay['returncode']==0 and not replay['source_code_modified']and not replay['own_source_cpp_producer_or_full_native_replayed']and replay['all29_original_constraints_pass']and replay['source_path_key_encoding']['all_other_certificate_values_exact']and replay['source_path_key_encoding']['every_source_digest_exact']);pins[replayf]=hs(replayf)
 cf=f'partial-swap-endpoint-source/{pr}/certificates/{stem}-network.json';c=rd(cf);p=c['complex'];g=c['guard'];counts=p['counts'];m=counts['m'];W=counts['W'];mass=counts.get('s',counts.get('total_rank'));P={int(k):v for k,v in p['child_width_multiplicities']if v};eta=F(p['saving']);alpha=F(p['moment_upper']);gap=1-alpha
 ck(prefix+'own_complete_profile',sum(k*v for k,v in P.items())==mass and max(P)<m and W*m>mass and eta>0 and gap>F(1,2**100))
 logbounds={int(k):F(v)for k,v in p['logarithm_upper_bounds'].items()};upper=sum(F(v*k,W*m)/(1-eta*logbounds[k])for k,v in P.items())
 ck(prefix+'own_rational_moment_exact',upper==alpha and all(0<=eta*logbounds[k]<1 for k in P))
 E=(64 if pr==18 else 128)*(W+m+1)**3;op=36*W**3+(4 if pr==18 else 16)*(mass+W)+8*m+4
 ck(prefix+'own_local_operation_allowance',E==g['E']and op<E)
 note=source['notes/'+stem+'-complex.tex'];text=(R/note['file']).read_text();ck(prefix+'own_final_operation_and_rows_passages','36W^3'in text and 'D(e)=0'in text and 'q_0=\\lceil\\log_2W\\rceil D(d)'in text and "exactly $1/W$"in text)
 if pr==18:
  oldsource=source['notes/complex-circuit-construction.tex'];oldtext=(R/oldsource['file']).read_text();ck(prefix+'finite_total_gate_and_small_coefficients_source','12W_'in oldtext and 'coefficients in'in oldtext and 'frac12'in oldtext);pins[oldsource['file']]=oldsource['sha256']
 else:ck(prefix+'new_normal_forms_dyadic_phase_source','All coefficients are Gaussian dyadic.'in text and 'two diagonal phase passes and one scalar phase'in text)
 row=(W-1).bit_length()*(m+1)+2*m+32;reserve_degree=10**7;constbits=128
 ck(prefix+'own_row_reserve_degree',reserve_degree>F(51*row,25))
 ck(prefix+'own_row_reserve_constant',2**constbits>2*row and 2**constbits>2*m)
 inv=ceil(1/gap);work=2**32*m**4*(E+W+mass+1)**2*(1+inv)**2*(1+row)**2
 ck(prefix+'own_allsize_geometric_coefficient',work<2**100000 and 1024*E<work and 40*m<work)
 rho=F(g['rho']);gamma=F(g['gamma']);zeta=F(g.get('zeta','1/10000'));dep=F(E+16*m+1)/(1-gamma);C0=ceil(128*m*(1+1/zeta)*dep)
 ck(prefix+'own_semantic_constants_exact',dep==F(g['dependency_constant'])and C0==g['C0']and F(g['C1'])==rho-(rho-1)/1000+zeta)
 C1=rho-(rho-1)*theta+zeta;ck(prefix+'new_stopping_precision_power',0<theta<1 and C1>1 and 1-epsilon*C1>0 and C0<2**200)
 paths=g['path_moment_upper'];vals=[F(x)for x in paths.values()]if isinstance(paths,dict)else[F(paths),F(g['no_large_path_upper'])];ck(prefix+'own_dependency_path_contraction',max(vals)<gamma<1)
 rows.append(dict(pr=pr,own_head=head,kappa_record=c['kappa'],native_coordinate_rank=m,productive_W=W,own_child_profile=P,whole_rank_mass=mass,own_uniform_saving=eta,own_moment_upper=alpha,own_moment_gap=gap,own_E=E,local_pertype_word_coefficient=1024*E,own_complete_row_coefficient=row,compact_address_fields_replaced_by_free_fixed_wiring=True,GL_group_stock_enumerated_or_assumed=False,stopped_row_reserve_degree=reserve_degree,stopped_row_reserve_constant_bits=constbits,own_allsize_work_coefficient_bound_power2=100000,own_recorded_C0=C0,own_recorded_C1=F(g['C1']),own_recorded_stop=F(1,1000),new_stop=theta,new_C1=C1,new_epsilon=epsilon,new_semantic_power_gap=1-epsilon*C1,original_cpp_native_or_simultaneous_phase_rerun=False,own_finite_replay_file=replayf,own_finite_replay_sha256=hs(replayf),source_certificate=cf,source_certificate_sha256=hs(cf),retained_interfaces=['Own complete all-role native circuit, physical entry/output frames and absolute phases on arbitrary dirty data.','Own nondegenerate binary residual normal forms, normalized completed Gaussian endpoint and all-column/common-label/whole-helper restoration.','Source complete-row volume and spectator identity, with once-only padding; fixed nonuniform routing replaces compact address descriptors only.','Named Gaussian analytic/boundary/recovery interfaces and separate nonlinear C1>1 global precision/count proof; no whole-integer upper admitted by this component.']))
 deps=['partial-swap-endpoint-native-interface.md','replay_partial_swap_endpoint_finite.py',f'partial-swap-endpoint-source/{pr}-manifest.json',f'partial-swap-endpoint-source/{pr}-additional-module-manifest.json'];pins.update({f:hs(f)for f in deps})
out=dict(schema='own-large-native-nonlinear-precision-interface/1',status='closed_conditional_component'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,whole_integer_upper_claimed=False,meaningful_lower=None,model='xag-straightline-v1',checks=checks,checks_passed=len(checks),source_sha256=pins,script_sha256=hs(Path(__file__).name))
(R/'partial-swap-endpoint-native-interface.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own18/24 source/work/rows/C1 interfaces')
