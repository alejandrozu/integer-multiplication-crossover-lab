"""Independent narrow review of the PR2077 V16-document digest refresh.

The old frozen and failed-replay bytes were independently compared before the
refresh. Their complete scientific projections, recorded below, are identical.
Only the named document dependency and consequential record SHA may differ.
This does not replace the original whole mathematics/source peer.
"""
from pathlib import Path
from hashlib import sha256
import copy,json,subprocess,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
OLD_DOC='cabb3bb2ac6b276aa685d7caf9f3c04a1c4cc8a70bb28824180b57e92776ae7c'
NEW_DOC='76cf5c7b662126affdffa484a9ff046abeddf1eceeee27f5598bf20ec3c77f98'
SCRIPT='selected_provider_v18_whole_bounds.py'
SCRIPT_SHA='33904e42ab136126a97df017628dfab08350660373b5be54a9eaa512efea9cee'
RECORDS={
 'native':('36d6cf3bdf4d4537e729d036bc5642afb74cbadef26afa0dc12ee8fa794b2f85','b953423d764981d4262b6275147d37761c065ff9f9ed8bff5c3f4335036c9880','e94102e966eb666fb89f3721b59688f93983ab66f2c2b4de05febf9831137401'),
 'early-upper':('63652ad8ba0d36697594d3dad736e115856d5b3952920d074b3f93580e11ac6a','b1032cf07278a9bc5ac7da21d14e394c81971b96dc2375a44f7c9538164f41ef','43a53f65d0f776acf8ef2b5739d25f4394fb2b12e0a283c35f9f864f442f03f6'),
 'record-upper':('c156d927c0be3fa56889654e36fe3b9c04de3b7c925d5b5c2e14666c665dadb2','9ffa4d80de66e93410f9878ef5dc064092d255019d3ae9e7aa3736cd41dc240d','4e755014c69ad43f221aa1d1e5a9629b41e2884e95e1d760214c66d7f7764318')}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def projection(a,kind):
 a=copy.deepcopy(a);del a['dependency_hashes']['selected-provider-v16-whole-upper.md']
 if kind=='early-upper':del a['record_tail_certificate_sha256']
 return sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def differences(a,b,path=''):
 if type(a)!=type(b):return[path]
 if isinstance(a,dict):return sum((differences(a.get(k),b.get(k),path+'/'+k)for k in sorted(a.keys()|b.keys())),[])
 return[path]if a!=b else[]
assert hs(SCRIPT)==SCRIPT_SHA and hs('selected-provider-v16-whole-upper.md')==NEW_DOC
files=[f'pr2077-vacancy-chain-finite-{kind}.json'for kind in RECORDS]
bound={};records=[]
for kind,(old,new,proj)in RECORDS.items():
 f=f'pr2077-vacancy-chain-finite-{kind}.json';a=rd(f)
 previous='pr2077-v16-document-provenance-rebind/previous/'+f;old_a=rd(previous)
 assert hs(previous)==old and old_a['dependency_hashes']['selected-provider-v16-whole-upper.md']==OLD_DOC
 assert projection(old_a,kind)==proj
 assert hs(f)==new and projection(a,kind)==proj
 assert a['pr']==2077 and a['status']=='closed_conditional_upper_only'and a['script_sha256']==SCRIPT_SHA and a['dependency_hashes']['selected-provider-v16-whole-upper.md']==NEW_DOC
 for key in['source_sha256','dependency_hashes']:
  for name,h in a[key].items():assert hs(name)==h,name;bound[name]=h
 paths=['dependency_hashes/selected-provider-v16-whole-upper.md']
 if kind=='early-upper':
  assert a['record_tail_certificate_sha256']==RECORDS['record-upper'][1]
  paths.append('record_tail_certificate_sha256')
 assert differences(old_a,a)==sorted('/'+x for x in paths)
 bound[previous]=old
 records.append(dict(file=f,previous_frozen_sha256=old,current_sha256=new,unchanged_scientific_and_other_metadata_projection_sha256=proj,exact_permitted_changed_paths=paths))
before={f:hs(f)for f in files+['selected-provider-v18-whole-upper.json']};runs=[]
for i in range(2):
 p=subprocess.run([sys.executable,'-B','-X','utf8',str(R/SCRIPT)],cwd=R,capture_output=True,text=True,encoding='utf8',timeout=120)
 assert p.returncode==0,p.stderr
 assert all(hs(f)==h for f,h in before.items())
 runs.append(dict(run=i+1,argv=[SCRIPT],returncode=0,stdout=p.stdout.strip(),all_three_refreshed_certificates_and_bundle_byte_identical=True))
original_peer='pr2077-vacancy-chain-finite-peer-review.json';peer=rd(original_peer)
assert peer['review_status'].startswith('PASS')and all(peer['reviewed_sha256'][f]==hs(f)for f in files+[SCRIPT,'selected-provider-v18-whole-upper.md'])
bound.update({f:hs(f)for f in files+[SCRIPT,'selected-provider-v18-whole-upper.md','selected-provider-v18-whole-upper.json',original_peer,'review_selected_provider_v18_math.py',Path(__file__).name]})
out=dict(schema='independent-narrow-provenance-refresh-peer/1',pr=2077,own_head=rd(files[0])['own_head'],review_status='PASS_narrow_document_dependency_refresh_scientific_fields_identical',reviewed_sha256=bound,material_findings=[],certificate_changes=records,previous_document_sha256=OLD_DOC,current_document_sha256=NEW_DOC,exact_changed_leaf_count=4,unchanged_generator_sha256=SCRIPT_SHA,fresh_reproduction=runs,scientific_changes=False,native_changes=False,invoice_changes=False,parameter_or_endpoint_changes=False,contract_changes=False,packet_or_ledger_modified_by_this_review=False,review_basis=[
 'Independently compared the actual previous frozen three ROOT certificates with ROOT/source-history-replay-failure exact outputs before regeneration. Native/record differ only in the V16 written-document dependency digest; early additionally updates the exact SHA of that record certificate.',
 'Reauthenticates the preserved actual old files in pr2077-v16-document-provenance-rebind/previous on every run. Removes only those explicitly named provenance leaves and compares every remaining parsed field and exact changed-path list. Full projections, old/new certificate byte hashes and both document hashes are recorded; native/program selection, source hashes, full invoice, every parameter/moment/row/check/endpoint and all retained contracts remain identical.',
 'Freshly executes the unchanged V18 evaluator twice; all three refreshed certificates and the whole bundle reproduce byte-identically. The separately refreshed original mathematical peer must bind these same current certificates and unchanged generator/proof.'
 ],limitations=[
 'This is a narrow provenance repair review, not a new mathematical theorem or a rerun of the expensive native/phase source pipeline. The original source/operator/all-size/analytic/reference premises and original peer scope are unchanged.',
 'The initial old-vs-failure comparison was performed before refresh; the reproducer also reads the separately preserved exact old certificates and compares them with the current outputs. No broad scientific projection is silently omitted.'
 ],reproduction_command=[Path(__file__).name])
(R/'pr2077-v16-provenance-refresh-math-peer-review.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8')
print('PASS independent PR2077 narrow provenance refresh: four allowed leaves, all scientific fields identical, two exact fresh reproductions')
