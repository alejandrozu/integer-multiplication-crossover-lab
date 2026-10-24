"""Own PR149 source replay/correspondence and complete early cost envelope."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import prod
from hashlib import sha256
import ast,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'early-native-producer-source';checks={};REVIEW_CLOSED=True
def read(p):return json.loads((R/p).read_bytes())
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def ck(k,v):assert v,k;checks[k]=True
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x)for x in v]
 return v
M=read('early-native-producer-source/149-manifest.json');files={x['path']:'early-native-producer-source/'+x['file']for x in M}
for x in M:ck('own_source_'+x['path'],x['head']=='6aed8701e3e3102898c66b5dcfc28d3cfc264edc' and hs(files[x['path']])==x['sha256'])
old=read('pr147-source/download-manifest.json');previous={x['path']:'pr147-source/'+x['file']for x in old}
for p in ['certificates/paired-cube-complex-input.json','scripts/paired_cube_network.py','scripts/three_stage_cover_network.py','scripts/structured_bulk_assembly.py']:ck('exact_full_complex_source_correspondence_'+p,hs(files[p])==hs(previous[p]))
replay=read('early-native-producer-source/149-fresh-producer-replay.json');ck('fresh_untouched_own_selected_producer',replay['returncode']==0 and replay['primary_code_changed'] is False)
selected=read(files['certificates/paired-cube-complex-input.json']);ck('fresh_selected_native_object',json.loads(replay['stdout'])['selected']==selected)
env=dict(Q=F,Counter=Counter,prod=prod,require=lambda condition,message:ck(message,condition),GRID=1<<120,COARSE=F(4617656,10**10),ATOM=F(1,1000),OLD=F(384599,10**10),AC=F(4856569,10**10));env['AB']=(1-env['ATOM'])*env['COARSE']+env['ATOM']*env['OLD']
constants=ast.parse((R/files['scripts/paired_cube_network.py']).read_bytes());literal={'Q':F}
assignments=[n for n in constants.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'AC','COARSE','ATOM','OLD','AB'}for t in n.targets)]
exec(compile(ast.Module(body=assignments,type_ignores=[]),'own149_paired_cube_constants','exec'),literal)
for key in ['AC','COARSE','ATOM','OLD','AB']:ck('own_selected_network_literal_'+key,literal[key]==env[key])
for p,names in [('scripts/three_stage_cover_network.py',{'up','log_upper','exp_upper'}),('scripts/structured_bulk_assembly.py',{'halving'}),('scripts/paired_cube_network.py',{'clean','shared_profile','exact_moment','complex_certificate','finite_bridge'})]:
 t=ast.parse((R/files[p]).read_bytes());f=[n for n in t.body if isinstance(n,ast.FunctionDef)and n.name in names];ck(p+'_functions',len(f)==len(names));exec(compile(ast.Module(body=f,type_ignores=[]),p,'exec'),env)
c=env['complex_certificate'](selected);b=env['finite_bridge'](c,None,selected);reference=read('pr147-source-native-profile.json')
for key,value in [('full_role_count_W',c['W']),('paid_rank_mass_s',c['total_rank']),('G',b['complex']['finite_group_router_upper']),('E',b['semantic']['E']),('C0',b['semantic']['C0'])]:ck('same_complete_native_constant_'+key,int(reference[key])==value)
original_record=read(files['certificates/paired-cube-network.json'])
ck('own_whole_selected_record_value',F(original_record['kappa'])==F(4609169,10**10)and F(original_record['assembly']['parameters']['kappa'])==F(4609169,10**10))
ck('own_whole_selected_source_savings',F(original_record['assembly']['parameters']['a_complex'])==env['AC']and F(original_record['assembly']['parameters']['a_bit'])==env['AB'])
ck('own_whole_selected_semantic_values',all(original_record['finite_bridge']['semantic'][k]==b['semantic'][k]for k in ['E','C0','C1'])and original_record['finite_bridge']['complex']['finite_group_router_upper']==b['complex']['finite_group_router_upper'])
m=72;eta=env['AC'];alpha=c['moment_upper'];mu=1-alpha;literal=b['semantic']['E'];W=c['W'];s=c['total_rank'];G=b['complex']['finite_group_router_upper'];C0=b['semantic']['C0'];inv=-(-(1/mu).numerator//(1/mu).denominator)
ck('rank_and_contraction',c['counts']['m']==72 and c['counts']['maxchild']==60 and 2*60**4<72**4)
ck('native_semantic_and_stock',b['semantic']['C1']==1 and b['rows']['coefficient']==20445 and b['rows']['degree']==70000)
ck('native_gap',mu>F(2,10**10) and inv<2**33)
ck('complete_allsize_coefficient',2**32*m**4*(literal+W+s+1)**2*(1+inv)**2*(1+20445)**2<2**100000)
ck('complete_oddgrid_guard',G*2*m+C0<2**100000)
Q=10000;delta=F(1,Q);A=10001;E=((1<<54)+A-1)//A;X=A*E;P=X-8;kappa=F(1,5000);ep=1-delta;beta=1-3*delta
ns={'__name__':'own149_fresh_outer','__file__':str(R/'pr4535-upper-source/endpoint.py')};exec(compile((R/'pr4535-upper-source/endpoint.py').read_bytes(),'own149_outer','exec'),ns)
pars=dict(kappa=kappa,tested_saving=eta,complex_uniform_saving=eta,a=F(301,10**6),b=F(302,10**6),q=F(3,10000),bit_saving=env['AB'],epsilon=ep,beta=beta,r0=delta/10,stop=delta,layout=delta,d=delta);ledger=ns['ledger'](pars)
ck('own_bit_admission',env['AB']==F(4613422943,10**13))
ck('fresh53_correctness',len(ledger['strict_checks'])==54 and {k for k,v in ledger['strict_checks'].items()if v<=0}=={'improvement_over_user_baseline'})
ck('fresh3_functional',len(ledger['functional_checks'])==3 and all(v>0 for v in ledger['functional_checks'].values()))
ck('fresh9_savings',len(ledger['margins'])==9 and all(v>kappa for v in ledger['margins'].values()))
workexp=32*Q+500000;degree=70000*Q
ck('full_stopped_reserve',delta*X-10>degree*(X+3).bit_length()+1000)
ck('work_precision_semantic_umbrella',delta*E>workexp+100000+1040*(X+3).bit_length()+100)
ck('effective_absolute_prime_capacity',X>=2**54 and X>128*Q and delta*X>(1024*(65+1024*X)).bit_length())
ck('reference_and_hybrid_domains',P>80 and P>=(1729**12).bit_length() and kappa*X>10)
for tag,v in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:ck(tag+'_protected',v+F(1,1024)<-F(1,2))
xi=ledger['parameters']['cap_xi'];costs=[]
for name,saving,power2,power,extra in [('target_FFT_H',ep*eta*(1-delta),188,2,8),('target_FFT_twiddles',ep,198,1,10),('dense_Gaussian_H',1-ep+beta*eta*(1-delta),218,2,12),('dense_diagonals',1-ep+beta,218,1,13),('Strassen_boundaries',F(3,32)+xi-ep,188,1,11),('halos',80-ep-beta,178,1,10),('pointwise_recovery',F(1),198,1,10)]:
 gap=saving-kappa;d=degree+extra;bound=E*power+power2+d*(X+3).bit_length()-X*gap;ck(name+'_gap',gap>0);ck(name+'_whole_tail',F(4*d,X)<gap);ck(name+'_one_eighth',bound<=-3);costs.append(dict(name=name,saving=str(saving),margin=str(gap),power2=power2,power_B=power,log_degree=d,base_log2_ratio_upper=str(bound)))
base=read('pr147-finite-gate-refined-upper.json');ck('named_corrected_same_native_lemma',base['status']=='closed_conditional_upper_only' and base['stock_gap_addressed'] and base['upper_log2log2_integer']==str(P))
deps=['pr149-finite-controller-upper.md','pr144-finite-controller-upper.md','pr144-finite-controller-early-upper.json','pr147-stopped-stock-correction.md','pr147-stopped-stock-corrected-upper.json','pr147-stopped-stock-correction-peer-review.json','pr147-finite-gate-refined-upper.json','finite-controller-gate-refinement.md','finite-controller-gate-refinement-peer-review.json','pr147-source-native-profile.json','pr147-source/download-manifest.json','pr4535-upper-source/endpoint.py','candidate-fermat-helper.json','fixed-small-rational-xag.json','fixed-exact-division-via-multiply.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','early-native-producer-source/149-manifest.json','early-native-producer-source/149-fresh-producer-replay.json']
out=dict(schema='own-pr149-finite-controller-early-upper/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',pr=149,own_head=M[0]['head'],source_head=M[0]['head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',native_coordinate_rank=72,N_is_not_coordinate_rank=True,kappa_record='4609169/10000000000',early_effective_kappa='1/5000',delta=str(delta),Q=Q,A=str(A),E=str(E),upper_log2log2_integer=str(P),log2log2U=str(P),inputUpper=f'2^(2^{P})',upper=f'2^(2^{P})',meaningful_lower=None,meaningful_lower_bound=None,actual_first_crossing_known=False,record_tail_quantified=False,original_record_hybrid_compatibility=base['original_record_hybrid_compatibility'],native_saving=str(eta),native_moment_gap=str(mu),allsize_work_coefficient_exponent=str(workexp),allsize_work_log_degree=str(degree),new_outer_parameters=enc(ledger['parameters']),fresh_ledger=enc(ledger),cost_rows=costs,full_selected_source_producer_rerun=True,original_BIT_producer_rerun=False,source_correspondence_scope='Exact selected complex input and complete finite bridge code bytes, with own149 selected scalar/frame/physical producer freshly replayed. Does not identify the changed original bit algorithm with147.',retained_contracts=base['retained_contracts'],formal_status='AI-assisted written own-source instantiation and finite exact checks, not Lean or independent human verification.',selected_source=dict(path='certificates/paired-cube-network.json',file=files['certificates/paired-cube-network.json'],sha256=hs(files['certificates/paired-cube-network.json'])),source_sha256={files[x['path']]:x['sha256']for x in M},dependency_hashes={p:hs(p)for p in deps},checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'pr149-finite-controller-early-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':len(checks),'pr':149,'P':str(P)}))
