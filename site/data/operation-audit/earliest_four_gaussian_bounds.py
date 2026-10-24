"""New own-source earliest2/3/4/10 direct-Gaussian upper bounds."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return{str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return[enc(v)for v in o]
 return o
cf='earliest-four-native-interfaces.json';c=rd(cf);ck('own_selected_native_interfaces',c['status']in['closed_conditional_component','pending_independent_AI_review']and c['checks_passed']==272 and all(c['checks'].values())and c['script_sha256']==hs('earliest_four_native_interfaces.py')and not c['whole_integer_upper_claimed']and not c['original_cpp_native_or_universal_phase_replayed']and sorted(a['pr']for a in c['rows'])==[2,3,4,10])
if REVIEW_CLOSED:
 ck('native_component_independently_closed',c['status']=='closed_conditional_component')
 for f in['earliest-four-native-interfaces-peer-review.json','earliest-four-native-interfaces-source-peer-review.json']:
  p=rd(f);ck('independent_native_peer_'+f,p['review_status'].startswith('PASS')and all(p['reviewed_sha256'][g]==hs(g)for g in[cf,'earliest-four-native-interfaces.md','earliest_four_native_interfaces.py']))
for key in['source_sha256','dependency_hashes']:
 for f,h in c[key].items():ck('native_'+f,hs(f)==h)
parent='nonlinear_native_gaussian_bounds.py';p9='pr9_nonlinear_native_gaussian_bounds.py'
ck('closed_nonlinear_global_component',hs(parent)=='a3716b41191371e77b44cf5c8a803ced3d26a9ce94d5ecb5631380f4219bf1db'and hs(p9)=='e96d03d4b12f0a251bfc929eafe590df316f820f622188570fe74ac5fa1a00ed')
for p in['pr12-nonlinear-native-gaussian-peer-review.json','pr9-nonlinear-native-gaussian-peer-review.json']:
 x=rd(p);ck('closed_global_math_peer_'+p,x['review_status'].startswith('PASS')and x['reviewed_sha256'][parent if p.startswith('pr12')else p9]==hs(parent if p.startswith('pr12')else p9))
ps=(R/parent).read_text();fn=ast.get_source_segment(ps,next(a for a in ast.parse(ps).body if isinstance(a,ast.FunctionDef)and a.name=='branch'));mods=ast.literal_eval(next(a.value for a in ast.parse((R/p9).read_text()).body if isinstance(a,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='changes'for t in a.targets)))
for i,(before,after)in enumerate(mods):ck('closed_explicit_global_specialization_'+str(i),fn.count(before)==1);fn=fn.replace(before,after)
changes=[('theta==F(19,25)','0<theta<1'),('L==10**7','L in[10**7,10**8]'),("q,aaux,baux=(F(75,10**10),F(8,10**9),F(38,10**9))if record else(F(199,10**11),F(2,10**9),F(2,10**8))","q,aaux,baux=map(F,a['chosen_auxiliary_q_a_b'])")]
for i,(before,after)in enumerate(changes):ck('own_source_explicit_adaptation_'+str(i),fn.count(before)==1);fn=fn.replace(before,after)
sp=importlib.util.spec_from_file_location('closed_reduced_gaussian_for_earliest',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
parameters={2:dict(Q=10**15,E=2**36,early=F(1,10**13),aux=[F(21,10**14),F(3,10**13),F(8,10**12)]),3:dict(Q=10**11,E=2**32,early=F(1,10**9),aux=[F(199,10**11),F(2,10**9),F(13,10**9)]),4:dict(Q=10**11,E=2**32,early=F(1,10**9),aux=[F(199,10**11),F(2,10**9),F(2,10**8)]),10:dict(Q=10**9,E=2**69,early=F(1,10**7),aux=[F(21,10**8),F(3,10**7),F(4,10**7)])}
rows=[]
for a in c['rows']:
 pr=a['pr'];t=parameters[pr];Q=t['Q'];delta=F(1,Q);epsilon=F(51,100);beta=F(1,200);layout=F(9,100);A=4*Q+1;E=t['E'];X=A*E;P=X-8;u=(X+3).bit_length();env=dict(F=F,ceil=ceil,enc=enc,G=G,Q=Q,delta=delta,epsilon=epsilon,beta=beta,layout=layout,A=A,E=E,X=X,P=P,u=u);exec(compile(fn,'own_earliest_nonlinear_branch','exec'),env)
 earlya=dict(a,chosen_auxiliary_q_a_b=t['aux']);early=env['branch'](earlya,t['early'],False);ka=F(a['kappa_record'])
 if pr==10:
  eta=F(a['own_uniform_saving']);theta=F(a['new_stop']);q=(ka/epsilon+eta*(1-theta))/2;aa=(q+eta*(1-theta))/2;bb=(aa+eta)/2;ra=dict(a,chosen_auxiliary_q_a_b=[q,aa,bb])
 else:ra=earlya
 record=env['branch'](ra,ka,True)
 for tag,o in[('early',early),('record',record)]:
  ledger=o['modified_Gaussian_ledger'];gaps=[F(v)for v in ledger['strict_checks'].values()]+[F(v)for v in ledger['functional_checks'].values()]+[F(v)-F(o['kappa'])for v in ledger['margins'].values()];degree=int(o['allsize_work_log_degree'])
  ck(str(pr)+'_'+tag+'_all_strict_functional_margin_full_log_warmup',min(gaps)*X>int(o['allsize_work_coefficient_exponent'])+(degree+1040)*u+100 and F(4*(degree+1040),X)<min(gaps))
  ck(str(pr)+'_'+tag+'_own_stopping_not_outer_slack',F(o['native_stop'])==F(a['new_stop'])and all(o['checks'].values())and F(o['cost_rows'][0]['saving'])==epsilon*F(a['own_uniform_saving'])*(1-F(a['new_stop'])))
 certpath={2:'aligned-paired-network',3:'complex-network',4:'retained-complex-layer',10:'batched-network'}[pr];saved=rd(f'earliest-23410-source/{pr}/certificates/{certpath}.json');selected_target=saved['witness']['parameters']['kappa']if pr in[2,3]else saved['main']['parameters']['kappa']if pr==4 else saved['assembly']['parameters']['kappa']
 ck(str(pr)+'_own_source_exact_target',ka>0 and ka==F(selected_target)and(pr!=4 or ka==F(saved['kappa'])))
 common=dict(pr=pr,own_head=a['own_head'],source_head=a['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=a['kappa_record'],native_coordinate_rank=a['native_coordinate_rank'],not_uniform_2_to_H=True,nonlinear_native_precision=True,original_historical_BIT_algorithm_costed=False,original_cpp_native_or_universal_phase_replayed=False,actual_selected_complex_finite_functions_replayed=True,new_source_core_gaussian_realization=True,new_accepted_record_claimed=False,meaningful_lower=None,actual_first_crossing_known=False,source_sha256=c['source_sha256'],retained_contracts=a['retained_interfaces']+['The separately closed nonlinear whole proof pays exact incoming-grid arithmetic, proven-zero guard-bit discard only at complete Gaussian-integer H returns, disjoint complete coefficient-block direct sums and full C0*d^C1 transient height,33p stored words/66p exact products.','Concrete normalized Gaussian accretivity, bounded scale-aware Schur/finite-LDU, convolution/rounding/boundary/recovery and repaired optimized-reference correctness/halting remain explicit; no false arbitrary-scale theorem or historical BIT expense is used.'],script_sha256=hs(Path(__file__).name),explicit_global_function_adaptations=[dict(before=x,after=y)for x,y in mods+changes],adapted_function_sha256=sha256(fn.encode()).hexdigest())
 deps=['earliest-four-gaussian-bounds.md',cf,'earliest-four-native-interfaces.md','earliest_four_native_interfaces.py',parent,'nonlinear-native-gaussian-bounds.md','nonlinear-native-gaussian-bounds.json',p9,'pr9-nonlinear-native-gaussian-bounds.md','pr9-nonlinear-native-gaussian-peer-review.json','pr12-nonlinear-native-gaussian-peer-review.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger.json','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
 if REVIEW_CLOSED:deps+=['earliest-four-native-interfaces-peer-review.json','earliest-four-native-interfaces-source-peer-review.json']
 dm={f:hs(f)for f in deps};dm.update(c['dependency_hashes']);common['dependency_hashes']=dm
 nf=f'pr{pr}-earliest-selected-gaussian-native.json';ef=f'pr{pr}-earliest-selected-gaussian-early-upper.json';rf=f'pr{pr}-earliest-selected-gaussian-record-upper.json'
 no=dict(common,schema='own-earliest-selected-native-parameters/1',own_native_interface=a)
 ro=dict(common,**record,schema='own-earliest-selected-record-upper/1');(R/rf).write_text(json.dumps(enc(ro),indent=2)+'\n',encoding='utf8')
 eo=dict(common,**early,schema='own-earliest-selected-early-upper/1',early_effective_kappa=str(t['early']),record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Fresh new Gaussian realization at the exact own selected historical record target. Its original BIT network is not priced; a stronger early exponent is not labelled a new accepted record.')
 for f,o in[(nf,no),(ef,eo)]: (R/f).write_text(json.dumps(enc(o),indent=2)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=a['own_head'],kappa_record=a['kappa_record'],native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,early_effective_kappa=str(t['early']),upper_log2log2_integer=str(P),native_stop=a['new_stop'],native_C1=a['new_C1'],Q=Q,record_tail_quantified=True,meaningful_lower=None,checks_passed=early['checks_passed']+record['checks_passed']))
out=dict(schema='earliest-four-own-selected-nonlinear-gaussian-bounds/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks=checks,checks_passed=len(checks)+sum(a['checks_passed']for a in rows),outer_checks_passed=sum(a['checks_passed']for a in rows),script_sha256=hs(Path(__file__).name))
(R/'earliest-four-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',out['checks_passed'],'own earliest4 whole checks',[(r['pr'],r['upper_log2log2_integer'])for r in rows])
