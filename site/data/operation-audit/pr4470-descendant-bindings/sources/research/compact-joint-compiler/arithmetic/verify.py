"""Same-kappa finite compiler improvement on PR4470's frozen native/controller word.
Preserves kappa=0.00302015; no kappa improvement is claimed.
Retains PR4470, PR4447, PR4440, zxv, Cinna Davis and Jacob Alan Sussman attribution.
Apache-2.0; substantial OpenAI Codex assistance.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import intervals as E
import outer_ledger as L
import legacy
HERE=Path(__file__).resolve().parent
KAPPA=Q('.00302015');TESTED=Q('.00302016')
LOW=Q('.0030201659770');HIGH=Q('.0030201659771')
H={4:28,7:7,8:47,9:326};N={1:2237,2:388,3:494,4:147,5:36,8:8}

def need(ok,msg):
 if not ok:raise ValueError(msg)

def encode(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {str(k):encode(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return[encode(v)for v in x]
 return x

def authenticate():
    manifest=json.loads((HERE/'INPUTS.json').read_bytes())
    for row in manifest['files']:
        name=row['path'];need(Path(name).name==name and name not in ('','.','..'),'Simple owned input path')
        need(hashlib.sha256((HERE/name).read_bytes()).hexdigest()==row['sha256'],'Changed arithmetic input: '+name)

def run(local=None):
 authenticate()
 frozen=json.loads((HERE/'profile.json').read_bytes())
 frozenH={int(k):v for k,v in frozen['helpers'].items()};frozenN={int(k):v for k,v in frozen['paid'].items()}
 need(frozenH==H and frozenN==N,'Frozen candidate profile agrees')
 if local is not None:
  need({int(k):v for k,v in local['helpers'].items()}==H and {int(k):v for k,v in local['paid'].items()}==N,'Actual native replay agrees with complete frozen profile')
 word_path=HERE/'controller.json'
 raw=word_path.read_bytes();word=json.loads(raw);T,P=Counter(),Counter();full=thin=idle=0
 for event in word['physical_events']:
  if event[0]=='LOCAL':full+=1;T.update(H);P.update(N)
  elif event[0]=='QUERY_SHEAR':thin+=1;P[1]+=112
  elif event[0]=='IDLE':
   rank=8*len(event[2]);need(rank>0,'No zero idle charge');P[rank]+=224;idle+=224
 for term in word['diagonal']:
  need(term[0]in(-1,1)and all(v in(0,1)for v in term[1:]),'Legal central normalizer')
  T[1+8*sum(term[1:])]+=112
 need((full,thin,idle)==(18,15,3360),'All actual p16 events')
 need(sum(T.values())==10928 and sum(P.values())==64620,'Complete field/call inventory')
 mt=lambda h,c:E.moment(h,1-c)
 def margin(c):
  a,b=mt(T,c),mt(P,c);return a[0]-b[1],a[1]-b[0]
 need(margin(LOW)[0]>0 and margin(HIGH)[1]<0,'Exact new raw root bracket')
 # Prove the margin decreases on C in[0,.05], independently of floating discovery.
 signed={r:T[r]-P[r]for r in T.keys()|P.keys()};derivative=None
 for i in range(16):
  l,r=Q(i,320),Q(i+1,320);low=Q(0)
  for rank,n in signed.items():
   term=E.mul(E.power(rank,1-r if n>0 else 1-l),E.log_bounds(rank));low+=n*term[0 if n>0 else 1]
  derivative=low if derivative is None else min(derivative,low)
 need(derivative>0,'Strict decrease around bracket')
 t,u,v,c,b=1-TESTED,Q(1,8),682,17,21
 target=E.moment(T,t);alpha=E.divide(E.moment(P,t),target)
 gamma=E.divide(E.moment(P,t+u),E.mul(E.power(c,u),target))
 delta=E.divide((Q(sum(T.values())*b),)*2,E.mul(E.power(c,TESTED),target))
 gap0=Q(31,5*10**9);g,d=Q(98102,100000),Q(959,1000)
 need(t+u>=1 and alpha[1]<1-gap0 and gamma[1]<g and delta[1]<d,'Both original/completion paid tails')
 need(g<1 and d<1,'Both exact tail decay ratios')
 bound=1/(1+v*gap0)+2*g**v+2*d**v;need(bound<1 and c**101<b**94,'Strict fully charged tensor moment')
 need(1/(1+681*gap0)+2*g**681+2*d**681>1,'Short product bound rejects')
 theta,power=Q(94,101),143;eta=E.scale(E.power(145,-v*TESTED),t)
 need(2**(101-94)*(17**v)**101<=(145**v)**94 and eta[0]>theta**power,'Shifted exit and complement capacity')
 need(E.power(145,v*TESTED)[1]<2**power,'Initial compiler range')
 need(eta[1]<theta**(power-1),'Previous logarithm power rejects')
 gap=Q(1,100000001);need(0<gap<TESTED-KAPPA and gap.numerator==1,'Larger compiler gap with strict outer slack');step=gap.denominator
 passes=lambda j:(step*j+1)**power<2**j
 lo,hi=1,2
 while not passes(hi):lo,hi=hi,2*hi
 while hi-lo>1:
  mid=(lo+hi)//2
  if passes(mid):hi=mid
  else:lo=mid
 height=step*hi;need(height>8*v and passes(hi)and not passes(hi-1),'Exact sufficient finite rank')
 # Source scalar list/order untouched, inherited upper bound is conservative.
 scalar_bound=158168;route_bound=(sum(N.values())+2*408+688)*1000
 need(scalar_bound+route_bound<10**7,'All local routes and scalar operations charged')
 scalar_upper=18*10**7+15*1792+32*112*(len(word['physical_events'])+sum(len(word['boundaries'][k+'_program'])for k in('left','right')))
 need(scalar_upper<10**9,'Complete raw nonrecursive bill')
 bit=json.loads((HERE/'ordinary-bit.json').read_bytes());atom=Q(bit['atom']);ordinary=(1-atom)*Q(bit['after_cover'])+atom*Q('.0000384599');admitted=Q(bit['admitted'])
 need(atom==Q('.004')and atom>ordinary>admitted>TESTED and atom<1-ordinary,'Ordinary BIT admission and adapters')
 outer_gap=(TESTED-KAPPA-gap)/6;need(outer_gap>0,'Strict outer slack remains')
 params={'kappa':KAPPA,'tested_saving':TESTED,'complex_uniform_saving':TESTED-gap,'b':KAPPA+5*outer_gap,'a':KAPPA+4*outer_gap,'q':KAPPA+3*outer_gap,'bit_saving':admitted,'epsilon':1-outer_gap,'beta':1-3*outer_gap,'r0':outer_gap/10,'stop':outer_gap,'layout':outer_gap,'d':outer_gap}
 outer=L.ledger(params);outer['functional_checks']['actual_new_BIT_stock_sublinear']=params['beta']*(1-atom)
 need(len(outer['strict_checks'])==54 and len(outer['functional_checks'])==4,'Full outer predicate inventory')
 need(all(x>0 for k in('strict_checks','functional_checks')for x in outer[k].values()),'All outer inequalities')
 legacy_result=legacy.check(params,outer,KAPPA)
 controls={}
 for name,patch in [('old_BIT',{'bit_saving':Q('.0027')}),('closed_uniform',{'complex_uniform_saving':params['b']}),('unfunded_endpoint',{'kappa':TESTED}),('closed_epsilon',{'epsilon':Q(1)})]:
  bad=L.ledger(dict(params,**patch));failed=[k for k,x in bad['strict_checks'].items()if x<=0];need(failed,'Reject '+name);controls[name]=failed
 need(margin(TESTED)[0]>0 and margin(HIGH)[1]<0,'Successful and rejected endpoint controls')
 mass=lambda h:sum(r*n for r,n in h.items())
 need(mass(T)-mass(P)==752,'Exact p16 rank surplus retained')
 return encode({'status':'PASS_COMPLETE_CONDITIONAL_ARITHMETIC','kappa':KAPPA,'kappa_decimal':'0.00302015','gain_over_PR4447':KAPPA-Q('.00300123'),'tested':TESTED,'raw_root_bracket':[LOW,HIGH],'derivative_positive_lower':derivative,'local_helpers':H,'local_paid':N,'targets':dict(T),'paid':dict(P),'productive_fields':sum(T.values()),'paid_calls':sum(P.values()),'rank_masses':[mass(T),mass(P)],'rank_surplus':mass(T)-mass(P),'strictification':{'tested':TESTED,'alpha':E.display(alpha),'gamma':E.display(gamma),'delta':E.display(delta),'tensor_power':v,'tail_offset':u,'cutoff':c,'floor':b,'normalized_paid_upper':bound},'compiler':{'theta':theta,'power':power,'eta':E.display(eta),'gap':gap,'H':height,'N':'2^'+str(height),'integer_test_exponent':hi,'word_materialized':False},'raw_nonrecursive':{'local_routes':route_bound,'local_scalar_allowance':scalar_bound,'all_unit_bound':scalar_upper,'budget':10**9},'ordinary_BIT':bit,'outer':outer,'legacy_outer':legacy_result,'negative_controls':controls,'source_hashes':{'p16_controller':hashlib.sha256(raw).hexdigest(),'interval_engine':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),'outer_ledger':hashlib.sha256(Path(L.__file__).read_bytes()).hexdigest()},'remaining':'Requires independent source-pinned native/operator/phase replay of unchanged candidate and source admission. Arithmetic alone is not a new theorem or selected-frontier promotion.'})
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true');args=parser.parse_args()
 result=run()
 if args.write_receipt:(HERE/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 else:need(result==json.loads((HERE/'RESULT.json').read_bytes()),'Exact frozen arithmetic receipt replay')
 print(json.dumps({'status':result['status'],'kappa':result['kappa_decimal'],'uniform_rank':result['compiler']['N'],'outer_predicates':'54 strict + 4 functional + 63 legacy','paid_calls':result['paid_calls']},sort_keys=True))
