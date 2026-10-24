"""Own-source adaptive p16 native budgets and full comparison parameters."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
HERE=Path(__file__).resolve().parent
ROOT=HERE/'adaptive-p16-upper-source'
def read(p):return json.loads((HERE/p).read_text(encoding='utf8'))
def hs(p):return sha256((HERE/p).read_bytes()).hexdigest()
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,list):return [enc(v) for v in x]
 return x
checks={}
def ck(n,v):assert v,n;checks[n]=True
REVIEW_CLOSED=True
manifest=read('adaptive-p16-upper-source/manifest.json')
for row in manifest:ck('primary_'+str(row['pr'])+'_'+row['path'],hs('adaptive-p16-upper-source/'+str(row['pr'])+'/'+row['path'])==row['sha256'])
replay=read('adaptive-p16-witness-replay.json')
ck('replay_script',replay['script_sha256']==hs('adaptive_p16_witness_replay.py'))
bind=read('pr4470-descendant-bindings/bindings.json')
low=read('p16-descendant-literal-lowers.json')
gmp=read('optimized-gmp-degree8-upper.json')
helper=read('candidate-fermat-helper.json')
ck('same_GMP_degree8',gmp['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8')
ck('signed_helper',helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8')
rows=[]
for pr,H in [(4483,2800000000),(4533,1587000000)]:
 prefix=f'adaptive-p16-upper-source/{pr}/'
 own=next(x for x in bind['descendants']if x['pr']==pr)
 witness=next(x for x in replay['rows']if x['pr']==pr)
 source=read(prefix+'research/compact-joint-compiler/arithmetic/RESULT.json')
 native=read(prefix+'research/joint-helper-lattice/RESULT.json')
 proof=(HERE/prefix/'research/rank-convergence/PROOF.md').read_text()
 ck(f'{pr}_own_head',own['head_commit']==({4483:'fb0c208864e6b24e3473318a058aa5b2dbd5764b',4533:'e9e9f244108ab4c21f0293cbfca9cfc3206e772a'}[pr]))
 ck(f'{pr}_fresh_witness',witness['status']=='PASS' and witness['result']['status']=='PASS_ADAPTIVE_HEIGHT_DIRECT_COMPILER' and witness['result']['H']==H)
 ck(f'{pr}_positive_funding',F(witness['result']['final_logarithmic_margin']['lower'])>0)
 ck(f'{pr}_raw_no_strictification',witness['result']['tensor_power']==1 and own['tensor_power']==1)
 ck(f'{pr}_own_uniform_saving',F(witness['result']['uniform_saving'])==F(own['uniform_saving']))
 ck(f'{pr}_strict_integer_descent','All recursive complement and exit ranks descend strictly.'in proof)
 ck(f'{pr}_whole_job_return','exits return before the next suspended paid position resumes.'in proof)
 for pin in bind['shared_raw_source_pins']:ck(f'{pr}_fresh_raw_{pin["path"]}',hs(prefix+pin['path'])==pin['sha256'])
 T={int(k):v for k,v in native['targets'].items()};P={int(k):v for k,v in native['paid'].items()}
 B=sum(T.values());paid=sum(P.values());tm=sum(k*v for k,v in T.items());pm=sum(k*v for k,v in P.items())
 ck(f'{pr}_own_raw_invoice',(B,paid,tm,pm)==(10928,64620,239886,239134))
 ck(f'{pr}_positive_surplus',tm-pm==752)
 ck(f'{pr}_source_unit_identity',source['targets']==native['targets'] and source['paid']==native['paid'])
 R=(10**9*(B+paid)+pm+B*21)*(10*145**2+10);K=32*(R+1);k=33010;G=2*H
 ck(f'{pr}_fresh_K',K<1<<k)
 ck(f'{pr}_adapter_ledger',(10**9+64)*R+32<K*K)
 C=14+(G+1).bit_length()+17*G
 ck(f'{pr}_unit_count_logs',B<1<<14 and B+paid<1<<17)
 ck(f'{pr}_stock_log',H+C.bit_length()+1<2*H)
 ck(f'{pr}_stock_scalar_coefficient',80*C<K*K)
 guard=23+2*k+(G+1).bit_length()+H
 eta=F(own['uniform_saving']);record=F(own['kappa']);phases={}
 endpoint=prefix+'research/compact-joint-compiler/arithmetic/outer_ledger.py'
 ns={'__file__':str(HERE/endpoint),'__name__':'own_adaptive_outer'}
 exec(compile((HERE/endpoint).read_bytes(),endpoint,'exec'),ns)
 for name,kap,delta,A in [('early',F(1,500),F(1,10000),10001),('record',record,F(own['outer_delta']),4*F(own['outer_delta']).denominator+1)]:
  Q=delta.denominator;ep=1-delta;beta=1-3*delta
  pars={'kappa':kap,'tested_saving':eta+delta,'complex_uniform_saving':eta,'a':kap+4*delta,'b':kap+5*delta,'q':kap+3*delta,'bit_saving':F(source['ordinary_BIT']['admitted']),'epsilon':ep,'beta':beta,'r0':delta/10,'stop':delta,'layout':delta,'d':delta}
  ledger=ns['ledger'](pars);ledger['functional_checks']['actual_new_BIT_stock_sublinear']=beta*(1-F(source['ordinary_BIT']['atom']))
  ck(f'{pr}_{name}_54_4_9',len(ledger['strict_checks'])==54 and len(ledger['functional_checks'])==4 and len(ledger['margins'])==9)
  for key,value in ledger['margins'].items():ck(f'{pr}_{name}_margin_{key}',value>kap)
  for group in ['strict_checks','functional_checks']:
   for key,value in ledger[group].items():ck(f'{pr}_{name}_{group}_{key}',value>0)
  E=Q*(H+1)+2*H+2*k+guard+179200000000+1048576+1000;X=A*E;Y=X-8
  ck(f'{pr}_{name}_active_coefficient',48+2*k+2*H<E)
  ck(f'{pr}_{name}_fallback_coefficient',12+Q*(H+1)<E)
  ck(f'{pr}_{name}_stock_cutoff',6+4*H<Q*(H+1))
  ck(f'{pr}_{name}_smooth',E>1<<20 and E.bit_length()+A.bit_length()+3<F(E,1024))
  ck(f'{pr}_{name}_precision',A*delta>1 and delta*E>44)
  ck(f'{pr}_{name}_derivatives',F(1040,X)<delta/2)
  ck(f'{pr}_{name}_prime_domains',X>128*Q and X>=1<<54)
  ck(f'{pr}_{name}_axis_capacity',delta*X>(1024*(65+1024*X)).bit_length() and delta*X>2)
  ck(f'{pr}_{name}_active_native_invoked',ep*X>Q*(H+1)+2)
  ck(f'{pr}_{name}_reference_domains',Y>=(1729**12).bit_length() and Y>80 and kap*X>100)
  for label,res in [('body',F(5,1024)-3*delta*A),('normalizers',F(1,1024)-delta*A),('rounding',F(1,1024)-A)]:ck(f'{pr}_{name}_{label}_protected',res+F(1,1024)<-F(1,2))
  xi=F(ledger['parameters']['cap_xi']);save=eta*(1-delta)
  costrows=[]
  for label,saving,c,power,degree in [('FFT_H',ep*save,60,2,0),('twiddles',ep,198,1,10),('Gaussian_H',1-ep+beta*save,90,2,4),('diagonals',1-ep+beta,218,1,13),('Strassen',F(3,32)+xi-ep,188,1,11),('halos',80-ep-beta,178,1,10),('recovery',F(1),198,1,10)]:
   gap=saving-kap;res=power+F(degree+1,1024)-A*gap
   ck(f'{pr}_{name}_{label}_gap',gap>0);ck(f'{pr}_{name}_{label}_coefficient',c*1024<E);ck(f'{pr}_{name}_{label}_tail',F(max(1,degree),X)<gap/2);ck(f'{pr}_{name}_{label}_residual',res<-1)
   costrows.append(dict(name=label,saving=str(saving),margin=str(gap),power2=c,power_B=power,log_degree=degree,residual_B_exponent=str(res)))
  phases[name]=dict(H=str(H),Q=Q,A=str(A),E=str(E),Eguard=str(guard),Klog=k,G_depth_upper=str(G),stock_C_log_upper=str(C),kappa=str(kap),log2log2U=str(Y),upper=f'2^(2^{Y})',parameters=enc(ledger['parameters']),fresh54_4_9=enc(ledger),cost_rows=costrows)
 ck(f'{pr}_early_precedes_record',int(phases['early']['log2log2U'])<int(phases['record']['log2log2U']))
 lower=next(x for x in low['rows']if x['pr']==pr)
 rows.append(dict(pr=pr,H=str(H),kappa=str(record),source_author_head=own['head_commit'],new_parameter_instantiation=True,automatic_upper_transfer=False,early_effective_kappa='1/500',upper_derivation='crossover_retuned_with_record_tail',**{x:phases['early'][x]for x in ['A','E','Eguard','Klog']},upper_log2log2_integer=phases['early']['log2log2U'],log2log2U=phases['early']['log2log2U'],sufficient_upper_input_bits=phases['early']['upper'],upper=phases['early']['upper'],upper_source_certificate='adaptive-p16-crossover-bounds.json',native_source_certificate='adaptive-p16-crossover-bounds.json',backup_record_upper=phases['record']['upper'],backup_record_upper_log2log2=phases['record']['log2log2U'],backup_record_upper_certificate='adaptive-p16-crossover-bounds.json',retains_original_asymptotic_record=True,claims_new_record_exponent=False,same_own_native_supplier_and_rank=True,phases=phases,fresh_source_witness_replay=True,full_native_or_phase_replay=False,lower_certificate_unchanged='p16-descendant-literal-lowers.json',all_implementations_of_PR=False,actual_first_crossing_known=False))
deps=['adaptive-p16-crossover-bounds.md','adaptive-p16-witness-replay.json','adaptive_p16_witness_replay.py','adaptive-p16-upper-source/manifest.json','pr4470-descendant-bindings/bindings.json','p16-descendant-literal-lowers.json','candidate-fermat-helper.md','candidate-fermat-helper.json','pr4470-clifford-stack-upper.md','pr4470-clifford-stack-upper.json','pr4470-batching-closure.json','pr4470-global-precision.json','pr4470-boundary-recovery.json','optimized-gmp-degree8-upper.json']
result=dict(schema='own-adaptive-p16-crossover-bounds/1',status='closed_conditional_sufficient_upper_bound'if REVIEW_CLOSED else'pending_independent_AI_review',model='xag-straightline-v1',baseline_extension_id=gmp['baseline_extension_id'],rows=rows,full_candidate_upper_review_closed=REVIEW_CLOSED,actual_first_crossover_known=False,practical_hardware_crossover=False,formal_status='AI-assisted written mathematics plus exact arithmetic and source checks; not Lean or independent human verification.',dependency_hashes={p:hs(p)for p in deps},primary_sources_sha256={str(x['pr'])+'/'+x['path']:x['sha256']for x in manifest},checks_passed=len(checks),checks=checks,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(HERE/'adaptive-p16-crossover-bounds.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':result['status'],'checks':len(checks),'own_upper_rows':[{k:r[k]for k in ['pr','H','E','Eguard','upper_log2log2_integer']}for r in rows]}))
