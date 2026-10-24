"""Fresh own finite complex arithmetic; no BIT/CPP/universal phase replay claim."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha1,sha256
import argparse,importlib,json,subprocess,sys
R=Path(__file__).resolve().parent;D=R/'earliest-23410-source';sys.set_int_max_str_digits(0)
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def enc(o):
 if isinstance(o,Fraction):return str(o)
 if isinstance(o,dict):return{str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return[enc(v)for v in o]
 return o
ap=argparse.ArgumentParser();ap.add_argument('--worker',type=int);args=ap.parse_args()
if args.worker:
 pr=args.worker;root=D/str(pr);sys.path.insert(0,str(root/'scripts'));import certify
 if pr==2:
  import paired_network
  n=certify.network(50);g=paired_network.guard_certificate();old=json.loads((root/'certificates/aligned-paired-network.json').read_bytes())
  assert {k:str(n[k])for k in old['complex_counts']}==old['complex_counts'] and g==old['stopped_guard'];certify.verify_sources()
  out=dict(counts=n,guard=g,original_selected_complex_arithmetic_executed=True,full_changed_BIT_certificate_executed=False,original_cpp_native_or_universal_phase_replayed=False)
 elif pr==3:
  import complex_network
  out=enc(complex_network.certificate());expected=json.loads((root/'certificates/complex-network.json').read_bytes());assert out==expected, 'own full complex certificate equality'
 elif pr==4:
  import retained_complex
  out=enc(retained_complex.certificate());expected=json.loads((root/'certificates/retained-complex-layer.json').read_bytes());assert out==expected,'own full retained complex certificate equality'
 elif pr==10:
  import batched_network,paired_complex
  c=batched_network.complex_certificate();a=batched_network.assembly(cn=c['counts']);expected=json.loads((root/'certificates/batched-network.json').read_bytes())
  assert enc(c)==expected['complex'] and enc(a)==expected['assembly'];p=paired_complex.PairedComplex(28);assert p.roles==c['counts']['side_roles']
  assert all(coef in(Fraction(1,2),Fraction(-1,2))for _,_,coef in p.pieces)
  out=dict(complex=c,assembly=a,actual_selected_complex_factory=dict(h=p.h,roles=p.roles,additions=p.additions,active=len(p.active),side_piece_count=len(p.pieces),coefficient_alphabet=['1/2','-1/2']),original_full_BIT_certificate_executed=False,original_cpp_native_or_universal_phase_replayed=False)
 print(json.dumps(enc(out),sort_keys=True,separators=(',',':')));raise SystemExit
checks={};pins={};meta=None
def ck(n,v):assert v,n;checks[n]=True
for name in['manifest.json','import-closure-manifest.json','native-proof-manifest.json']:
 f='earliest-23410-source/'+name;m=json.loads((R/f).read_bytes());pins[f]=hs(f)
 if meta is None:meta=m['metadata']
 for a in m['source_manifest']:
  if a.get('status')=='own_head_404':continue
  raw=(R/a['file']).read_bytes();ck('own_source_'+str(a['pr'])+'_'+a['path'],hs(a['file'])==a['sha256']and sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==a['git_blob_sha1']);pins[a['file']]=a['sha256']
rows=[]
for pr in[2,3,4,10]:
 p=subprocess.run([sys.executable,'-B','-X','utf8',str(Path(__file__).resolve()),'--worker',str(pr)],capture_output=True,text=True,encoding='utf8',timeout=300)
 ck(str(pr)+'_unchanged_selected_functions_exit_zero',p.returncode==0 or print(p.stderr));o=json.loads(p.stdout);target=D/str(pr)/'fresh-selected-complex-arithmetic.json';target.write_text(json.dumps(o,indent=2)+'\n',encoding='utf8');rows.append(dict(pr=pr,own_head=next(x['own_head_sha']for x in meta if x['pr']==pr),result_file=target.relative_to(R).as_posix(),result_sha256=hs(target.relative_to(R))))
 print('PASS own selected complex arithmetic',pr,flush=True)
out=dict(schema='earliest-four-own-selected-complex-arithmetic-replay/1',status='checked_own_selected_finite_functions',metadata=meta,rows=rows,checks=checks,checks_passed=len(checks),source_sha256=pins,script_sha256=hs(Path(__file__).name),whole_integer_upper_claimed=False,original_cpp_native_or_universal_phase_replayed=False)
(D/'fresh-selected-complex-arithmetic.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own finite/source checks')
