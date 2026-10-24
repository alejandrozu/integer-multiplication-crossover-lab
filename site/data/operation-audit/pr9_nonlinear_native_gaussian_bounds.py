"""Own9 nonlinear native circuit; native stop .76 is distinct from outer slack."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
cf='pr9-retained-complex-native-interface.json';c=rd(cf);peerf='pr9-retained-complex-native-interface-peer-review.json';p=rd(peerf)
ck('own_closed_native_component_and_root_peer',c['status']=='closed_conditional_component'and c['pr']==9 and c['own_head']=='cfd6a2baded9dba990b987934474a7721d6ca3fb'and not c['whole_integer_upper_claimed']and c['checks_passed']==35 and all(c['checks'].values())and c['script_sha256']==hs('pr9_retained_complex_native_interface.py')and p['review_status'].startswith('PASS')and p['reviewed_sha256'][cf]==hs(cf))
for key in['source_sha256','dependency_hashes']:
 for f,h in c[key].items():ck('own_native_'+f,hs(f)==h)
gf='pr9-native-grammar-supplement.json'
grammar=rd(gf)
ck('own_bounded_scalar_grammar_supplement',grammar['pr']==9 and grammar['own_head']==c['own_head']and grammar['status']=='closed_conditional_component'and grammar['frozen_interface_sha256']==hs(cf)and grammar['script_sha256']==hs('pr9_native_grammar_supplement.py')and all(grammar['checks'].values())and grammar['normalized_scalar_gate_alphabet']==['0','1','-1','1/2','-1/2']and grammar['local_pertype_word_coefficient']==c['local_pertype_word_coefficient']and grammar['whole_scalar_gate_count']<12*c['productive_W']and grammar['original_selected_factory_rebuilt']and not grammar['full_native_CPP_or_universal_phase_replayed']and not grammar['whole_integer_upper_claimed'])
for key in['source_sha256','dependency_hashes']:
 for f,h in grammar[key].items():ck('actual_selected_grammar_'+f,hs(f)==h)
gpeer='pr9-native-grammar-supplement-peer-review.json';gp=rd(gpeer)
ck('independent_actual_grammar_peer',gp['pr']==9 and gp['own_head']==c['own_head']and gp['review_status'].startswith('PASS')and all(gp['reviewed_sha256'][f]==hs(f)for f in[gf,'pr9-native-grammar-supplement.md','pr9_native_grammar_supplement.py']))
sp=importlib.util.spec_from_file_location('closed_reduced_Gaussian_component_own9',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
parent='nonlinear_native_gaussian_bounds.py';ck('frozen_nonlinear_whole_component',hs(parent)=='a3716b41191371e77b44cf5c8a803ced3d26a9ce94d5ecb5631380f4219bf1db'and rd('nonlinear-native-gaussian-bounds.json')['status']=='closed_conditional_batch')
parentpeer='pr12-nonlinear-native-gaussian-peer-review.json';pp=rd(parentpeer);ck('independent_nonlinear_whole_proof_peer',pp['review_status'].startswith('PASS')and pp['reviewed_sha256'][parent]==hs(parent)and pp['reviewed_sha256']['nonlinear-native-gaussian-bounds.md']==hs('nonlinear-native-gaussian-bounds.md'))
text=(R/parent).read_text();node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)and n.name=='branch');fn=ast.get_source_segment(text,node)
changes=[
 (';cs={}',";theta=F(a['new_stop']);cs={}"),
 (' if record:\n  q=(kappa/epsilon+eta*(1-delta))/2;aaux=(q+eta*(1-delta))/2;baux=(aaux+eta)/2\n else:q=F(21,10**8);aaux=F(3,10**7);baux=F(4,10**7)'," q,aaux,baux=(F(75,10**10),F(8,10**9),F(38,10**9))if record else(F(199,10**11),F(2,10**9),F(2,10**8))"),
 ('stop=delta,layout=layout','stop=theta,layout=layout'),
 ("F(a['new_stop'])==delta","theta==F(19,25)"),
 ('workexp=256*Q+500000;degree=L*Q;logd0=128*Q+1000+degree*u','cutoffconstant=ceil(F(1128)/theta);degree=ceil(F(L)/theta);workexp=100000+cutoffconstant+32;logd0=cutoffconstant+degree*u'),
 ('F(logd0,Q)>=128+L*u and F(X,Q)-10>L*u+128','theta*logd0>=1128+L*u and theta*(beta*X-1)>L*u+1128'),
 ('delta*(epsilon*X-1)','theta*(beta*X-1)'),
 ('128*Q+1000+100000+7<workexp','cutoffconstant+100000+7<workexp'),
 ('F(E,Q)>workexp+100000+1040*u+100','delta*X/10>workexp+1040*u+100'),
 ('C0<2**200','C0<2**400'),
 ('202-(1-epsilon*C1)*X','402-(1-epsilon*C1)*X'),
 ('202-(1-beta*C1)*X','402-(1-beta*C1)*X'),
 ('F(4*degree,X)<min(delta,beta)','F(4*degree,X)<min(theta*beta,beta)'),
 ('F(4*1040,X)<delta','F(4*1040,X)<delta/10'),
 ('epsilon*eta*(1-delta)','epsilon*eta*(1-theta)'),
 ('1-epsilon+beta*eta*(1-delta)','1-epsilon+beta*eta*(1-theta)'),
 ('delta=str(delta),Q=Q','delta=str(delta),native_stop=str(theta),Q=Q'),
]
for ix,(before,after)in enumerate(changes):ck('explicit_component_adaptation_'+str(ix),fn.count(before)==1);fn=fn.replace(before,after)
Q=10**11;delta=F(1,Q);epsilon=F(51,100);beta=F(1,200);layout=F(9,100);A=4*Q+1;E=2**32;X=A*E;P=X-8;u=(X+3).bit_length()
env=dict(F=F,ceil=ceil,enc=enc,G=G,Q=Q,delta=delta,epsilon=epsilon,beta=beta,layout=layout,A=A,E=E,X=X,P=P,u=u);exec(compile(fn,'own9_explicit_nonlinear_specialization','exec'),env)
own=dict(c,new_C1=c['own_C1'],new_stop=c['own_stop'],own_recorded_C0=c['own_C0'],original_cpp_native_or_simultaneous_phase_rerun=c['source_cpp_or_fullnative_rerun'])
early=env['branch'](own,F(1,10**9));record=env['branch'](own,F(c['kappa_record']),True)
for tag,o in[('early',early),('record',record)]:
 led=o['modified_Gaussian_ledger'];gaps=[F(v)for v in led['strict_checks'].values()]+[F(v)for v in led['functional_checks'].values()]+[F(v)-F(o['kappa'])for v in led['margins'].values()]
 degree=int(o['allsize_work_log_degree'])
 ck(tag+'_every_strict_power_and_full_log_warmup',min(gaps)*X>int(o['allsize_work_coefficient_exponent'])+(degree+1040)*u+100 and F(4*(degree+1040),X)<min(gaps))
 ck(tag+'_own_native_stop_not_outer_slack',o['native_stop']=='19/25'and F(o['native_stop'])!=delta and all(o['checks'].values()))
 screen=next(a for a in c['feasible_parameter_screens']if a['label']==tag);ck(tag+'_own_explicit_auxiliary_parameters',all(F(o['new_outer_parameters'][k])==F(screen['parameters'][k])for k in['kappa','a','b','q','epsilon','beta','layout','stop','r0','d']))
deps=['pr9-nonlinear-native-gaussian-bounds.md',cf,'pr9-retained-complex-native-interface.md','pr9_retained_complex_native_interface.py',peerf,gf,'pr9-native-grammar-supplement.md','pr9_native_grammar_supplement.py',gpeer,'nonlinear-native-gaussian-bounds.md','nonlinear-native-gaussian-bounds.json',parent,parentpeer,'gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json'];dm={f:hs(f)for f in deps};dm.update(c['dependency_hashes']);dm.update(grammar['dependency_hashes']);sourcepins=dict(c['source_sha256']);sourcepins.update(grammar['source_sha256'])
contracts=c['retained_interfaces']+['Own bounded dyadic coefficient grammar and full1024Ew scalar/phase/clear tariff must satisfy the separate own-source grammar supplement.','Exact augmented-grid native arithmetic and completed Gaussian-integer H return, nonlinear C0*d^C1, coefficient-block direct sums and full outer amplitude/rounding/33p/66p guards are those of the separately closed nonlinear whole proof, specialized with native theta.76.','Concrete normalized Gaussian accretivity/finite-LDU/narrow/cyclic-boundary/prime/recovery and repaired-reference correctness/halting remain explicit; no false arbitrary-scale analytic assertion or original historical ternary BIT cost is used.']
common=dict(pr=9,own_head=c['own_head'],source_head=c['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=c['kappa_record'],native_coordinate_rank=c['native_coordinate_rank'],not_uniform_2_to_H=True,nonlinear_native_precision=True,original_historical_BIT_algorithm_costed=False,source_cpp_or_fullnative_rerun=False,new_fixedwiring_row_realization_not_original_PR9_schedule=True,meaningful_lower=None,actual_first_crossing_known=False,source_sha256=sourcepins,dependency_hashes=dm,retained_contracts=contracts,script_sha256=hs(Path(__file__).name),explicit_function_adaptations=[dict(before=b,after=a)for b,a in changes],adapted_function_sha256=sha256(fn.encode()).hexdigest())
nf='pr9-nonlinear-native-gaussian-native.json';ef='pr9-nonlinear-native-gaussian-early-upper.json';rf='pr9-nonlinear-native-gaussian-record-upper.json'
n=dict(common,schema='own9-nonlinear-native-Gaussian-parameters/1',own_native_interface=c)
r=dict(common,**record,schema='own9-nonlinear-native-Gaussian-record-upper/1');(R/rf).write_text(json.dumps(enc(r),indent=2)+'\n',encoding='utf8')
e=dict(common,**early,schema='own9-nonlinear-native-Gaussian-early-upper/1',early_effective_kappa='1/1000000000',record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Fresh Gaussian circuit at own selected complex core and exact own record target; changed historical ternary BIT routine is not costed.')
for f,o in[(nf,n),(ef,e)]: (R/f).write_text(json.dumps(enc(o),indent=2)+'\n',encoding='utf8')
out=dict(schema='own9-nonlinear-native-Gaussian-whole-costs/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',pr=9,own_head=c['own_head'],native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,upper_log2log2_integer=str(P),record_tail_quantified=True,checks=checks,checks_passed=len(checks)+early['checks_passed']+record['checks_passed'],outer_checks_passed=early['checks_passed']+record['checks_passed'],script_sha256=hs(Path(__file__).name))
(R/'pr9-nonlinear-native-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8');print('PASS',out['checks_passed'],'own9 nonlinear whole checks; P',P)
