"""Unchanged own12 finite witness engine; no large C++ producer invocation."""
from pathlib import Path
from hashlib import sha1,sha256
from urllib.request import Request,urlopen
import ast,json,sys,importlib.util
from fractions import Fraction as F
sys.set_int_max_str_digits(0);sys.dont_write_bytecode=True
R=Path(__file__).resolve().parent;D=R/'early-batched12-source';head='35d31e30f28bc5da0ae6a88e7b03d75ebc855534';manifest=json.loads((D/'source-fetch-manifest.json').read_bytes());files={a['path']:a for a in manifest};queue=['controlled_bit_rank_moment','batched_bit_rank_moment','batched_network','bulk_complex_guard','certify','fast_gaussian','compact_control_layer','prepare_layers'];seen=set();extra=[]
if(D/'additional-module-manifest.json').exists():
 extra=json.loads((D/'additional-module-manifest.json').read_bytes())
 for a in extra:files[a['path']]=a
while queue:
 module=queue.pop()
 if module in seen:continue
 seen.add(module);path='scripts/'+module+'.py';p=D/path
 if path not in files:
  url=f'https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/{head}/{path}';raw=urlopen(Request(url,headers={'User-Agent':'Codex-own-source-replay'}),timeout=60).read();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw);a=dict(pr=12,own_head=head,path=path,file=p.relative_to(R).as_posix(),sha256=sha256(raw).hexdigest(),git_blob_sha1=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),primary_url=url);files[path]=a;extra.append(a)
 for n in ast.walk(ast.parse(p.read_bytes())):
  if isinstance(n,ast.ImportFrom)and n.level==0 and n.module and n.module.split('.')[0]not in sys.stdlib_module_names:queue.append(n.module.replace('.','/'))
if extra:(D/'additional-module-manifest.json').write_text(json.dumps(extra,indent=2)+'\n',encoding='utf8')
elif(D/'additional-module-manifest.json').exists():
 for a in json.loads((D/'additional-module-manifest.json').read_bytes()):files[a['path']]=a
for a in files.values():assert a['own_head']==head and sha256((R/a['file']).read_bytes()).hexdigest()==a['sha256']
sys.path.insert(0,str(D/'scripts'));sp=importlib.util.spec_from_file_location('actual_own12_finite_witness',D/'research/batched-followup/witness.py');w=importlib.util.module_from_spec(sp);sp.loader.exec_module(w)
report=json.loads((D/'research/geometric-dimensions/report.json').read_bytes());roles=next(a['roles']for a in report['dimensions']if a['h']==30);actual=w.serializable(w.certificate(roles));saved=json.loads((D/'research/batched-followup/certificate.json').read_bytes());assert set(actual)=={'status','bit','complex','assembly','inherited_pr10_commit','kappa_ratio_to_pr10','scope'}and all(v==saved[k]for k,v in actual.items());retained_fields=sorted(set(saved)-set(actual));assert retained_fields==['matching','producer','source_sha256','template_controls']
for path,h in saved['source_sha256'].items():assert path in files and files[path]['sha256']==h,path
out=dict(schema='own12-exact-finite-arithmetic-replay/1',pr=12,own_head=head,status='passed_exact_original_finite_witness_function_objects',own_selected_roles=roles,own_record_kappa=str(w.KAPPA),all29constraints=len(actual['assembly']['constraints'])==29 and all(F(v)>0 for v in actual['assembly']['constraints'].values()),freshly_replayed_certificate_fields=sorted(actual),additional_recorded_fields_not_freshly_executed=retained_fields,all_recorded_source_hashes_exact=True,source_code_modified=False,own_cpp_fullproducer_or_native_replayed=False,source_sha256={a['file']:a['sha256']for a in files.values()},source_manifest='early-batched12-source/source-fetch-manifest.json',source_manifest_sha256=sha256((D/'source-fetch-manifest.json').read_bytes()).hexdigest(),script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),scope='Original exact finite witness(roles) imported unchanged and evaluated from own committed h30 producer role report; every returned bit/complex histogram/moment/pathguard/29assembly object equals the corresponding own selected certificate object. The committed producer/matching/template controls are additional evidence fields and are NOT freshly executed here; all recorded source hashes are nevertheless checked exact. No fresh huge C++ producer, matching, native/full-phase or simultaneous all-column proof is asserted.')
(D/'fresh-finite-arithmetic.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS own12 original finite arithmetic exact; CPP/native not executed')
