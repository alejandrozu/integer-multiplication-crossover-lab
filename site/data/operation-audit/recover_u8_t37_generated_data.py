"""Own962/991 source-generated data recovery; no whole-cost theorem."""
from pathlib import Path
from hashlib import sha256
import copy,gzip,importlib.util,json,shutil,subprocess,sys,tempfile
sys.set_int_max_str_digits(0)
A=Path(__file__).resolve().parent;checks={};used={}
def hs(f):return sha256((A/f).read_bytes()).hexdigest()
def rd(f):
 b=(A/f).read_bytes();return json.loads(gzip.decompress(b)if str(f).endswith('.gz')else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(n,v):assert v,n;checks[n]=True
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
manifest=rd('u8-t37-generated-source/manifest.json');rows=[]
source={}
for pr in [535,799,890,942]:
 for x in rd(f'older-reviewed-source/{pr}-manifest.json'):
  if'error'not in x:source.setdefault(x['path'],'older-reviewed-source/'+x['file'])
for x in rd('t21-t37-cost-source/manifest.json'):
 if'error'not in x:source[x['path']]='t21-t37-cost-source/'+x['file']
baseplan=source['research/gauge44-frames-x/data/PLAN.json'];baseowners=source['research/gauge44-frames-x/data/OWNERS.json.gz'];proto=source['research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz']
for f in[baseplan,baseowners,proto]:used[f]=hs(f)
with tempfile.TemporaryDirectory(prefix='own962991_')as td:
 root=Path(td)
 for entry in manifest['rows']:
  M=rd(entry['MANIFEST_file']);ck(str(entry['pr'])+'_own_manifest',hs(entry['MANIFEST_file'])==entry['MANIFEST_sha256']);used[entry['MANIFEST_file']]=entry['MANIFEST_sha256']
  for x in entry['files']:
   ck(str(entry['pr'])+'_own_file_'+x['relative'],hs(x['file'])==x['sha256']==M[x['relative']]);used[x['file']]=x['sha256'];dst=root/x['path'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((A/x['file']).read_bytes())
 # Own962 explicitly pins the original T21 constructor. Own991 vendors those
 # exact files, so they are copied only after their complete byte pins match.
 origin=A/'u8-t37-generated-source/991/vendor/pr890';target=root/'research/complex-t21-owners'
 for f in origin.rglob('*'):
  if f.is_file()and'__pycache__'not in f.parts:
   rel=f.relative_to(origin);dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(f.read_bytes())
 vroot=A/'u8-t37-generated-source/991/vendor/pr870'
 for f in vroot.rglob('*'):
  if f.is_file()and'__pycache__'not in f.parts:
   rel=f.relative_to(vroot);dst=target/'vendor/pr870'/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(f.read_bytes())
 pins=rd('u8-t37-generated-source/962/DEPENDENCY-PINS.json')
 for rel in['research/complex-t21-owners/build_owners.py','research/complex-t21-owners/common.py','research/complex-t21-owners/VENDOR-PINS.json','research/complex-t21-owners/data/T5-OWNERS.json.gz','research/complex-t21-owners/data/EDITS.json']:
  ck('actual_own962_T21_dependency_'+rel,sha256((root/rel).read_bytes()).hexdigest()==pins[rel])
 vendor=json.loads((target/'VENDOR-PINS.json').read_bytes());ck('actual_own962_nested_T16_constructor_pin',sha256((target/'vendor/pr870/t16/build_owners.py').read_bytes()).hexdigest()==vendor['pr870']['files']['t16/build_owners.py'])
 for rel,f in [('research/gauge44-frames-x/data/PLAN.json',baseplan),('research/gauge44-frames-x/data/OWNERS.json.gz',baseowners)]:
  ck('source_T8_dependency_'+rel,hs(f)==pins[rel]);dst=root/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((A/f).read_bytes())
 # The exact source baseline parent is restored by its own unchanged supplied
 # producer, not replaced by the merely window-equivalent geometry fixture.
 prefix='research/community-k492-audit/pr622/replay/baseline558/complex-global/'
 inherited={x['path']:x['file']for x in rd('u8-t37-generated-parent-inputs/manifest.json')['rows']}
 inherited[prefix+'base/split-centres/CANONICAL-WORD.json.gz']=source[prefix+'base/split-centres/CANONICAL-WORD.json.gz']
 inherited[prefix+'base/work/complex-nine-native/DATA-PHASES.json']=source[prefix+'base/work/complex-nine-native/DATA-PHASES.json']
 baseline=root/'exact-baseline';restore_source=root/'restore-source'
 for rel,f in inherited.items():
  ck('actual_pinned_parent_input_'+rel,hs(f)==pins[rel]);used[f]=hs(f);dst=baseline/'complex-global'/rel.removeprefix(prefix);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((A/f).read_bytes())
 parentpath=restore_source/'vendor/pr558/vendor/pr552/complex-global/vendor535/inputs/ROUND20-PARENT-TEMPLATE.json.gz';parentpath.parent.mkdir(parents=True);parentpath.write_bytes((A/proto).read_bytes())
 restore_script=A/'u8-t37-generated-source/991/vendor/pr870/code/restore_parent.py';process=subprocess.run([sys.executable,'-X','utf8',str(restore_script),'--source',str(restore_source),'--baseline',str(baseline),'--out',str(root/'restored-parent')],capture_output=True,text=True,encoding='utf8')
 ck('actual_unchanged_reviewed_parent_restoration',process.returncode==0)
 actualparent=root/'restored-parent/complex-global/base/split-centres/GLOBAL-TEMPLATE.json.gz';restored=json.loads(gzip.decompress(actualparent.read_bytes()));ck('exact_reviewed_parent_complete_payload',ident(restored)=='7db047a427a7979d69e163c78a1e32bd445628fb86723e131a3138361355a9c3')
 durable=A/'u8-t37-generated-parent-inputs/RESTORED-GLOBAL-TEMPLATE.json.gz';durable.write_bytes(actualparent.read_bytes())
 for entry in manifest['rows']:
  pr=entry['pr'];p=root/entry['root'];common=load(p/'common.py',f'own{pr}_common');old=sys.modules.get('common');sys.modules['common']=common
  try:
   om=load(p/'build_owners.py',f'own{pr}_owner_constructor');result=om.construct(root/'research/gauge44-frames-x/data/PLAN.json',root/'research/gauge44-frames-x/data/OWNERS.json.gz');owners,order=result[:2];spec=rd(f'u8-t37-generated-source/{pr}/data/SPEC.json')
   ck(str(pr)+'_complete_own_owner_semantic_identity',ident(owners)==spec['data']['owners_content_sha256']and len(owners)==167832 and len(order)==333)
   out=A/f'u8-t37-generated-data/{pr}';out.mkdir(parents=True,exist_ok=True);common.write_gzip(out/'OWNERS.json.gz',owners);common.dump(out/'ORDER.json',order)
   base=root/f'base-{pr}';(base/'split-centres').mkdir(parents=True);(base/'split-centres/GLOBAL-TEMPLATE.json.gz').write_bytes(actualparent.read_bytes())
   bm=load(p/'build_parent.py',f'own{pr}_parent_constructor');savedargv=sys.argv;sys.argv=[str(p/'build_parent.py'),'--base',str(base),'--owners',str(out/'OWNERS.json.gz'),'--order',str(out/'ORDER.json'),'--out',str(root/f'lift-{pr}')]
   try:bm.main()
   finally:sys.argv=savedargv
   generated=root/f'lift-{pr}/PLAN.json';plan=json.loads(generated.read_bytes());semantic=copy.deepcopy(plan);semantic['assignment_sha256']=semantic['replica_lift']['owners_file_sha256']=ident(owners)
   ck(str(pr)+'_complete_own_PLAN_semantic_identity',ident(semantic)==spec['data']['plan_semantic_sha256'])
   common.dump(out/'PLAN.json',plan)
   verifier=load(p/'verify.py',f'own{pr}_runtime_SPEC_authority');runtime,ids=verifier.runtime_spec(out/'PLAN.json',out/'OWNERS.json.gz');runtime['pivot_swap']['recipe']=spec['pivot_swap']['recipe'];expected=copy.deepcopy(spec);expected['data']['owners_sha256']=hs(f'u8-t37-generated-data/{pr}/OWNERS.json.gz');expected['data']['plan_sha256']=hs(f'u8-t37-generated-data/{pr}/PLAN.json')
   ck(str(pr)+'_actual_own_runtime_SPEC_authorizes_only_raw_portability_rebinding',runtime==expected and ids==dict(owners_content_sha256=ident(owners),plan_semantic_sha256=ident(semantic)))
   common.dump(out/'RUNTIME-SPEC.json',runtime)
   print('OWN EXACT DATA',pr,'ownersraw',hs(f'u8-t37-generated-data/{pr}/OWNERS.json.gz')==spec['data']['owners_sha256'],'wholePLANsemantic',True,'ownruntime_SPEC',True,flush=True)
   common.write_gzip(out/'GLOBAL-TEMPLATE.json.gz',common.read(root/f'lift-{pr}/GLOBAL-TEMPLATE.json.gz'))
   rows.append(dict(pr=pr,own_head=entry['own_head'],own_source_root=entry['root'],own_MANIFEST_file=entry['MANIFEST_file'],own_MANIFEST_sha256=entry['MANIFEST_sha256'],own_SPEC_file=f'u8-t37-generated-source/{pr}/data/SPEC.json',own_SPEC_sha256=hs(f'u8-t37-generated-source/{pr}/data/SPEC.json'),own_verifier_file=f'u8-t37-generated-source/{pr}/verify.py',own_owner_constructor_file=f'u8-t37-generated-source/{pr}/build_owners.py',own_parent_constructor_file=f'u8-t37-generated-source/{pr}/build_parent.py',OWNERS_file=f'u8-t37-generated-data/{pr}/OWNERS.json.gz',OWNERS_sha256=hs(f'u8-t37-generated-data/{pr}/OWNERS.json.gz'),owners_content_sha256=ident(owners),own_expected_owner_content_sha256=spec['data']['owners_content_sha256'],selected_PLAN_file=f'u8-t37-generated-data/{pr}/PLAN.json',PLAN_sha256=hs(f'u8-t37-generated-data/{pr}/PLAN.json'),PLAN_semantic_sha256=ident(semantic),own_expected_PLAN_semantic_sha256=spec['data']['plan_semantic_sha256'],runtime_SPEC_file=f'u8-t37-generated-data/{pr}/RUNTIME-SPEC.json',runtime_SPEC_sha256=hs(f'u8-t37-generated-data/{pr}/RUNTIME-SPEC.json'),raw_owner_container_matches_frozen=hs(f'u8-t37-generated-data/{pr}/OWNERS.json.gz')==spec['data']['owners_sha256'],raw_PLAN_container_matches_frozen=hs(f'u8-t37-generated-data/{pr}/PLAN.json')==spec['data']['plan_sha256'],only_own_authorized_raw_portability_fields_rebound=True,whole_cost_claimed=False))
  finally:
   if old is None:sys.modules.pop('common',None)
   else:sys.modules['common']=old
out=dict(schema='own962991-source-generated-data-recovery/1',status='checked_exact_own_source_generated_PLAN_OWNER_semantics',rows=rows,checks=checks,checks_passed=len(checks),source_sha256=used,dependency_hashes={f:hs(f)for f in['u8-t37-generated-source/manifest.json','u8-t37-generated-parent-inputs/manifest.json','u8-t37-generated-data-recovery.md','fetch_u8_t37_generated_parent_inputs.py']},script_sha256=hs(Path(__file__).name),whole_cost_claimed=False,original_global_verifier_PASS_claimed=False,native_operator_or_phase_proved=False,source_bodies_changed=False,opaque_parent_hint_used=False)
(A/'u8-t37-generated-data-recovery.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS own owner/data investigation',len(checks))
