"""Own authenticated4411/4405 rank choices plus exact retained p3 native chain."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import gzip,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;O=R/'p3-compiler-refinement-source';checks={};rows=[]
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 b=(R/f).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ck(n,v):assert v,n;checks[n]=True
old=rd('pr4359-crossover-retuned-upper.json');peer=rd('pr4359-crossover-retuned-peer-review.json')
for f,h in peer['reviewed_sha256'].items():ck('frozen_p3_census_'+f,hs(f)==h)
base='earlier-family-screen-source/'
controller_file=base+'4359__research__kappa-rebuild__architecture__P3-CONTROLLER-TARIFF-CERTIFICATE.json'
raw_file=base+'4359__research__kappa-rebuild__complex__full-identity-certificates__THREE-base-FULL-IDENTITY-NATIVE.json.gz'
closure_file=base+'4359__research__kappa-rebuild__transfer-audit__FINITE-TEMPLATE-CLOSURE.md'
PRS=[int(sys.argv[1])]if len(sys.argv)>1 else[4411,4405]
for pr in PRS:
 m=rd(f'p3-compiler-refinement-source/{pr}-manifest.json');by={x['path']:x for x in m};head=m[0]['own_head'];tag=str(pr)+'_';ck(tag+'exact_own_author_head',head=={4411:'ec2c9505d863c7f5f2a5f08628e8ee6fb740c0a7',4405:'873d1b3c96a83b701a5c0bba8e37a861e6672fef'}[pr])
 for x in m:
  b=(R/x['file']).read_bytes();ck(tag+'own_byte_'+x['path'],x['own_head']==head and sha256(b).hexdigest()==x['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['expected_api_blob'])
 pre='research/log-potential-template-ranks/'if pr==4411 else'search'
 if pr==4405:pre='research/pr4359-compiler-refill/'
 get=lambda p:by[pre+p]['file']
 result=rd(get('RESULT.json'));replay_file=f'p3-compiler-refinement-source/{pr}-fresh-replay.json'if pr==4411 else'p3-compiler-refinement-source/4405-receipt-difference.json';replay=rd(replay_file)
 if pr==4411:ck(tag+'fresh_unchanged_checker',replay['status']=='passed_unchanged_own_finite_checker')
 else:ck(tag+'own_math_checker_platform_receipt_difference_explicit',replay['all_original_numeric_guards_executed']and replay['source_verifier_modified']is False and replay['original_saved_receipt_reproduced']is False and replay['path_key_only_platform_difference']and replay['all_numeric_and_source_values_identical_after_explicit_path_key_normalization'])
 ck(tag+'own_replay_source_binding',replay['own_head']==head and replay['source_manifest_sha256']==hs(f'p3-compiler-refinement-source/{pr}-manifest.json'))
 manifest=rd(get('VENDOR.json'if pr==4411 else'EXPORTED-SOURCES.json'))
 ck(tag+'explicit_native_origin',manifest.get('source_commit',manifest.get('head'))=='da637c87c89482bc4c86be36bd0071b3d400dbed')
 for x in manifest['files']:
  rel=x['path'];p=rel if pr==4411 else pre+rel;b=(R/by[p]['file']).read_bytes();ck(tag+'export_'+rel,sha256(b).hexdigest()==x['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob'])
 cover_file=get('vendor/P3-NATIVE-COVER.json.gz'if pr==4411 else'source/research/kappa-rebuild/controller/P3-NATIVE-COVER.json.gz')
 cover=rd(cover_file);controller=rd(controller_file)
 ck(tag+'own_cover_authenticates_controller',cover['sources']['research/kappa-rebuild/architecture/P3-CONTROLLER-TARIFF-CERTIFICATE.json']==hs(controller_file))
 ck(tag+'own_cover_authenticates_full_native_word',cover['sources']['research/kappa-rebuild/complex/full-identity-certificates/THREE-base-FULL-IDENTITY-NATIVE.json.gz']==hs(raw_file))
 ck(tag+'same_raw_typed_native_census',hs(cover_file)==hs(base+'4359__research__kappa-rebuild__controller__P3-NATIVE-COVER.json.gz')and hs(closure_file)=='3f8508c63862dd83968bd30df91b08ba5afcee1e10db15ca546cdff0caef95d9')
 adds=[x for x in controller['controller']['left_program']+controller['controller']['right_program']if x[0]=='ADD'and F(x[3])]
 ck(tag+'actual_four_literal_unit_ADDs',len(adds)==4 and all(abs(F(x[3]))==1 and x[1]!=x[2]for x in adds))
 if pr==4411:
  case=next(x for x in result['cases']if x['family']=='complex/kappa-0023');H=case['N']['H'];eta=F(case['uniform_saving']);kap=F(23,10000);test=F(case['tested_mixed_saving']);z=1-eta;q=9
  final=case['final_integer_test'];ck(tag+'own_strict_majorant',final['left_base']**final['left_exponent']<final['right_base']**final['right_exponent']and H==465000 and eta==F(4601,2000000))
  ck(tag+'actual_selected_retuned_outer',F(result['kappa_0023_retuned_outer']['parameters']['kappa'])==kap and all(F(x)>0 for x in result['kappa_0023_retuned_outer']['functional_gaps'].values()))
 else:
  case=result['new_endpoint_sharper_rank'];H=case['H1'];p=result['endpoint_refill'];eta=F(p['outer']['parameters']['complex_uniform_saving']);kap=F(p['kappa']);test=F(p['mixed_test_saving']);z=1-eta
  ck(tag+'own_exact_higher_endpoint',H==2099384703303215709 and kap==F(230509,100000000)and eta==F(806781557,350000000000)and F(case['z'])==z)
 targets={int(k):int(v)for k,v in cover['cover']['targets'].items()};paid={int(k):int(v)for k,v in cover['cover']['paid'].items()}
 ck(tag+'own_full_profile',targets=={int(k):int(v)for k,v in controller['invoice']['targets'].items()}and paid=={int(k):int(v)for k,v in controller['invoice']['paid'].items()})
 ck(tag+'strict_supplier_and_positive_surplus',0<eta<test<1 and min(targets)==6 and max(targets)==57 and max(paid)==5 and sum(k*v for k,v in targets.items())-sum(k*v for k,v in paid.items())==224)
 rows.append(dict(pr=pr,own_head=head,kappa_record=str(kap),H=str(H),N='2^'+str(H),actual_uniform_saving=str(eta),tested_mixed_saving=str(test),strict_uniform_supplier='P_N/B_N<N^(1-eta)',own_rank_case=case,native_coordinate_rank=57,transient_frame_max73=True,targets=targets,paid=paid,raw_controller_complex_ADDs=4,raw_real_ADD_floor=8,native_complete_G=1494376,Klog=128,original_unit_rank_surplus=224,own_cover_file=cover_file,own_cover_sha256=hs(cover_file),own_result_file=get('RESULT.json'),own_result_sha256=hs(get('RESULT.json')),own_readme_file=get('README.md'),own_source_manifest=f'p3-compiler-refinement-source/{pr}-manifest.json',own_fresh_replay=replay_file,own_fresh_replay_sha256=hs(replay_file),own_source_manifest_sha256=hs(f'p3-compiler-refinement-source/{pr}-manifest.json'),retained_native_controller_file=controller_file,retained_raw_native_file=raw_file,retained_source_closure_file=closure_file,exact_native_census_lemma='pr4359-fermat-helper-upper.md',native_census_lemma_certificate='pr4359-crossover-retuned-upper.json',native_census_peer='pr4359-crossover-retuned-peer-review.json',native_program_scope='Exact own exported cover binds the original4359 controller/fullnative word; all raw typed operation bounds and completed Clifford/owned/spectator contracts retained. No upper or activation threshold transferred. New H/eta requires fresh compiler inventory/guard/stock/outer costs.',operator_phase_freshly_replayed=False))
out=dict(schema='own-p3-compiler-refinement-source-bindings/1',status='passed_own_source_and_finite_checker_bindings',rows=rows,checks_passed=len(checks),checks=checks,source_sha256={x['file']:x['sha256']for pr in PRS for x in rd(f'p3-compiler-refinement-source/{pr}-manifest.json')},retained_native_source_sha256={f:hs(f)for f in [controller_file,raw_file,closure_file]},dependency_sha256={f:hs(f)for f in ['pr4359-crossover-retuned-upper.json','pr4359-crossover-retuned-peer-review.json','pr4359-fermat-helper-upper.md']},script_sha256=hs(Path(__file__).name),scope='Own rank/compiler variants authenticated; no standalone cost upper certificate or phase theorem is asserted by this source-binding output.')
(R/(f'pr{PRS[0]}-p3-compiler-source-bindings.json'if len(PRS)==1 else'p3-compiler-refinement-native-bindings.json')).write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'own source/rank/native chain bindings')
