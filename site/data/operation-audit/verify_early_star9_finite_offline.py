"""Portable own9 finite witness verification from its frozen21-input closure."""
from pathlib import Path
from hashlib import sha1,sha256
from fractions import Fraction as F
import importlib.util,json,sys
sys.set_int_max_str_digits(0);sys.dont_write_bytecode=True
R=Path(__file__).resolve().parent;D=R/'early-star9-source';checks={}
def ck(k,v):assert v,k;checks[k]=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
mf='early-star9-source/source-fetch-manifest.json';M=rd(mf);head='cfd6a2baded9dba990b987934474a7721d6ca3fb';pins={mf:hs(mf)}
for a in M:
 raw=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();ck('own_primary_'+a['path'],a['own_head']==head and sha256(raw).hexdigest()==a['sha256']and blob==a['git_blob_sha1']and(a['api_changed_blob']is None or a['api_changed_blob']==blob));pins[a['file']]=a['sha256']
sys.path[:0]=[str(D/'research/prime-field-followup'),str(D/'research/prime-field-followup/vendor'),str(D/'scripts')];sp=importlib.util.spec_from_file_location('actual_own9_finite_offline',D/'research/prime-field-followup/verify.py');v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v)
reference=rd('early-star9-source/research/prime-field-followup/vendor/prime-field28.json');saved=rd('early-star9-source/research/prime-field-followup/certificate.json');actual=v.serializable(v.witness(11670540,reference));ck('every_original_witness_field_exact',actual==saved['witness']);ck('all29_original_predicates_positive',len(actual['constraints'])==29 and all(F(x)>0 for x in actual['constraints'].values()));ck('source_selected_reference_complex_exact',actual['retained_complex']==reference['witness']['complex'])
out=dict(schema='portable-own9-finite-witness-verification/1',pr=9,own_head=head,status='PASS_exact_original_witness_arithmetic',network_used=False,mutable_global_queue_or_changed_file_cache_required=False,source_code_modified=False,CPP_native_phase_or_template_engines_rerun=False,checks_passed=len(checks),checks=checks,reviewed_sha256=pins,reproducer_sha256=hs(Path(__file__).name),scope='Portable independent source-byte/Git-blob and original witness arithmetic verification using the frozen21 own inputs. No original producer/native/universal phase replay is asserted; no whole upper is produced.')
(R/'early-star9-source/offline-finite-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own9 portable exact finite checks')
