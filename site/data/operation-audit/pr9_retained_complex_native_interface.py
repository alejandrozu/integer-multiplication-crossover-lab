"""Own9 explicit original-core binding and nonlinear interface; no whole U."""
from pathlib import Path
from hashlib import sha1,sha256
from fractions import Fraction as F
import importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'early-star9-source';checks={};REVIEW_CLOSED=True
def rd(f):return json.loads((R/f).read_bytes())
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
mf='early-star9-source/source-fetch-manifest.json';M=rd(mf);files={a['path']:a for a in M};pins={};head='cfd6a2baded9dba990b987934474a7721d6ca3fb'
for a in M:
 raw=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();ck('own_raw_'+a['path'],a['pr']==9 and a['own_head']==head and sha256(raw).hexdigest()==a['sha256']and blob==a['git_blob_sha1']and(a['api_changed_blob']is None or blob==a['api_changed_blob']));pins[a['file']]=a['sha256']
own='early-star9-source/research/prime-field-followup/certificate.json';c=rd(own);w=c['witness'];p=w['retained_complex'];provenance=rd('early-star9-source/research/prime-field-followup/provenance.json');reference=rd('early-star9-source/research/prime-field-followup/vendor/prime-field28.json');vf='early-star9-source/research/prime-field-followup/verify.py';text=(R/vf).read_text()
ck('actual_own_selected_original_supplier',provenance['commit']==c['provenance']['commit']=='6725c6a17b17871a35353fd29157f4ed851bc114'and"reference['witness']['complex']"in text and'unchanged, conditional PR #7 dependency'in text and p==reference['witness']['complex'])
for name,a in provenance['files'].items():ck('own_vendor_source_'+name,files['research/prime-field-followup/vendor/'+name]['sha256']==a['sha256'])
rf='early-star9-source/fresh-finite-arithmetic.json';replay=rd(rf);ck('actual_unchanged_witness_fresh',replay['own_head']==head and replay['own_record_kappa']=='19/5000000000'and replay['all29constraints']and not replay['source_code_modified']and not replay['large_CPP_native_matching_and_template_engines_rerun']);pins[rf]=hs(rf)
m,W,s=p['m'],p['W'],p['s'];eta=F(w['complex_saving']);E=64*(W+m+1)**3;B=s+E;g=w['guard'];theta=F(g['beta']);zeta=F(g['zeta']);C0=ceil(max(F(128*m*B*B),18*m*B*B*(1+1/zeta)));C1=5-4*theta+zeta;epsilon=F(51,100)
ck('own_local_gate_count_and_cubic_allowance',p['scalar_gates']<12*W and E==g['E']and B==g['B']and 36*W**3+4*s+4*W+4<E)
ck('new_integer_remainder_fits_same_own_E',36*W**3+4*s+4*W+8*m+4<E)
ck('own_nonlinear_guard_exact',m>=3 and 2<=s<m**5 and s*(8+E)<=9*B*B and C0==g['C0']and F(g['C1'])==C1==F(19601,10000)and theta==F(19,25)and 1-epsilon*C1==F(349,10**6))
sys.path.insert(0,str(D/'scripts'));sp=importlib.util.spec_from_file_location('own9_logbounds',D/'scripts/search_network.py');lb=importlib.util.module_from_spec(sp);sp.loader.exec_module(lb);logupper=lb.log_integer_bounds(m)[1];alpha=F(s,W*m)/(1-eta*logupper);gap=1-alpha
ck('own_positive_complete_rank1_moment',eta==F(39,10**9)and 0<eta*logupper<F(p['eta'])and 0<alpha<1 and gap>F(1,2**100))
row=(W-1).bit_length()*(m+1)+2*m+32;work=2**32*m**4*(E+W+s+1)**2*(1+ceil(1/gap))**2*(1+row)**2
ck('new_own_complete_row_cost_envelope',10**7>F(51*row,25)and 2**128>2*row and work<2**100000)
sp=importlib.util.spec_from_file_location('reduced_Gaussian_arithmetic_own9',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G);screens=[]
for label,kappa,a,b,q in[('early',F(1,10**9),F(2,10**9),F(2,10**8),F(199,10**11)),('record',F(19,5*10**9),F(8,10**9),F(38,10**9),F(75,10**10))]:
 pars=dict(kappa=kappa,tested_saving=eta,complex_uniform_saving=eta,a=a,b=b,q=q,epsilon=epsilon,beta=F(1,200),layout=F(9,100),stop=theta,r0=F(1,10**12),d=F(1,10**11));ledger=G.gaussian_ledger(pars);ck(label+'_fresh50strict_2functional_7margins',all(x>0 for x in ledger['strict_checks'].values())and all(x>0 for x in ledger['functional_checks'].values())and min(ledger['margins'].values())>kappa);screens.append(dict(label=label,parameters=ledger['parameters'],minimum_margin=min(ledger['margins'].values()),native_height_power_gap=1-epsilon*C1,whole_runtime_rows_or_global_precision_proved=False))
deps=['pr9-retained-complex-native-interface.md','replay_early_star9_finite.py',mf,'partial-swap-endpoint-native-interface.md','partial-swap-endpoint-native-interface.json','partial_swap_endpoint_native_interface.py','partial-swap-endpoint-native-interface-peer-review.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger.json'];depmap={f:hs(f)for f in deps}
out=dict(schema='own9-original-complex-nonlinear-interface/1',status='closed_conditional_component'if REVIEW_CLOSED else'pending_independent_AI_review',pr=9,own_head=head,kappa_record='19/5000000000',native_coordinate_rank=m,productive_W=W,own_child_profile={1:s},whole_rank_mass=s,own_uniform_saving=eta,own_moment_upper=alpha,own_moment_gap=gap,own_E=E,local_pertype_word_coefficient=1024*E,own_complete_row_coefficient=row,stopped_row_reserve_degree=10**7,stopped_row_reserve_constant_bits=128,own_allsize_work_coefficient_bound_power2=100000,own_C0=C0,own_C1=C1,own_stop=theta,new_epsilon=epsilon,new_semantic_power_gap=1-epsilon*C1,new_fixedwiring_row_realization_not_original_PR9_schedule=True,original_ternary_BIT_algorithm_costed=False,source_cpp_or_fullnative_rerun=False,whole_integer_upper_claimed=False,meaningful_lower=None,feasible_parameter_screens=screens,model='xag-straightline-v1',retained_interfaces=['Own explicit original PR7 complete complex native map and physical input/output/absolute-phase/all-column/arbitrary-dirty/common-label contracts.','New application of the named arbitrary-rank complete-row coefficient lemma to the exact own finite core, not execution of an original PR9 mixed-row schedule.','Distinct nonlinear C1=5−4theta+zeta semantic-depth induction and all unproved source analytic/all-size interfaces; parameter screens alone are not whole runtime bounds.'],source_sha256=pins,dependency_hashes=depmap,checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__).name))
(R/'pr9-retained-complex-native-interface.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own9 explicit-source nonlinear interface; no integer upper')
