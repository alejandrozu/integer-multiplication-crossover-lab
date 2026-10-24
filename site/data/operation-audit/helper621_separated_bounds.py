"""Own-source changed-native separated-product bounds for PR4626."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
from collections import Counter
import ast,gzip,hashlib,json,sys
import uniform_critical_p16_batch as B
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;B.REVIEW_CLOSED=REVIEW_CLOSED
checks={}
def ck(name,value):
 assert value,name
 checks[name]=True
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def read(p):
 raw=(R/p).read_bytes();return json.loads(gzip.decompress(raw)if str(p).endswith('.gz')else raw)
def walk(o):
 yield o
 if isinstance(o,dict):
  for v in o.values():yield from walk(v)
 elif isinstance(o,list):
  for v in o:yield from walk(v)
def rank2(rows):
 basis={}
 for x in rows:
  while x:
   k=x.bit_length()-1
   if k in basis:x^=basis[k]
   else:basis[k]=x;break
 return len(basis)
def native():
 main=read('late-uniform-source-extraction/source-manifest.json')['files'];main=[x for x in main if x['pr']==4626]
 deps=read('changed-native-p16-source/4626/manifest.json');head=deps['head']
 files={x['source_path']:x['local_path']for x in main}
 sha={x['local_path']:x['sha256']for x in main}
 for x in deps['files']:
  ck('own_dependency_status_'+x['path'],x['status']=='authenticated_own_head_bytes'and x['head']==head)
  files[x['path']]=x['file'];sha[x['file']]=x['sha256']
  if x.get('expected_sha256'):ck('declared_payload_'+x['path'],x['expected_sha256']==x['sha256'])
 for i,(path,digest)in enumerate(sha.items()):ck('own_primary_'+str(i),hs(path)==digest)
 def source(path):return read(files[path])
 base='research/helper621-warp-combination/'
 arithmetic=source(base+'ARITHMETIC.json');nr=source(base+'NATIVE-RESULT.json.gz')
 ck('own_native_state',nr['status']=='PASS_HELPER621_NATIVE_AND_ABSOLUTE_PHASE')
 ck('own_selected_native_data_sha',hashlib.sha256(json.dumps(nr,sort_keys=True,separators=(',',':')).encode()).hexdigest()==arithmetic['native_data_sha256'])
 predecessor=source(base+'predecessor/ACTUAL-WORD.json.gz')
 code=ast.parse((R/files[base+'verify_native.py']).read_bytes())
 env=dict(deepcopy=deepcopy,Counter=Counter,P={1:2202,2:414,3:505,4:134,5:36,8:8})
 functions=[n for n in code.body if isinstance(n,ast.FunctionDef)and n.name in ['need','span','synth','regenerate']]
 ck('own_regeneration_functions',len(functions)==4)
 exec(compile(ast.Module(body=functions,type_ignores=[]),'own_helper621_source_regeneration','exec'),env)
 canonical,words=env['regenerate'](predecessor)
 payload=(json.dumps(dict(canonical=canonical,programs=words),sort_keys=True,separators=(',',':'))+'\n').encode()
 ck('actual_regenerated_candidate_payload',hashlib.sha256(payload).hexdigest()==nr['candidate_payload_sha256'])
 ck('public_required_entry_frames_unchanged',canonical['start'][:224]==predecessor['canonical']['start'][:224])
 ck('all_required_output_frames_unchanged',canonical['final']==predecessor['canonical']['final'])
 ck('only_helper621_entrance_changed',[i for i,(a,b)in enumerate(zip(canonical['start'],predecessor['canonical']['start']))if a!=b]==[621])
 for dr in ['forward','backward']:
  z=nr['native'][dr];zz=z['second_literal']
  ck(dr+'_arbitrary_inputs_owned_frames',z['independent_persistent_columns']==zz['independent_borrowed_input_fields']==632 and z['arbitrary_owned_C0_cleared']and z['scalar_frames_checked']and zz['all_scalar_frames_checked']and zz['free_warp_operator_endpoint_matches'])
  ck(dr+'_scalar_height_allowance',z['max_denominator']<=64 and F(z['max_formal_prefix_l1'])<512 and z['real_scalar_allowance']<=158168)
  ck(dr+'_all_scalar_order_and_coefficients',[e[1]for e in words[dr]if e[0]=='scalar']==[e[1]for e in predecessor['programs'][dr]if e[0]=='scalar'])
 typed=0
 for d in walk(nr['phase_checks']):
  if not isinstance(d,dict)or not{'matrix_rows','offset','phase','linear_Z4','quadratic_rows'}<=d.keys():continue
  a=d['matrix_rows'];n=len(a);limit=1<<n
  ck('own_normalizer_recipe_'+str(typed),all(isinstance(x,int)and 0<=x<limit for x in a)and rank2(a)==n and 0<=d['offset']<limit and 0<=d['phase']<4 and len(d['linear_Z4'])==len(d['quadratic_rows'])==n and all(isinstance(x,int)and 0<=x<4 for x in d['linear_Z4'])and all(isinstance(x,int)and 0<=x<limit for x in d['quadratic_rows']))
  typed+=1
 ck('own_normalizers_not_histogram_only',typed>1000)
 h621=next(x for x in nr['phase_checks']['helpers']if x['role']==621)
 ck('helper621_complete_relative_native_rank7',h621['rank']==7 and h621['from']==canonical['start'][621]and h621['to']==canonical['final'][621]and set(h621['recipes'])=={'forward','backward'}and all(h621['recipes'][d]['rank']==7 for d in ['forward','backward']))
 # qvalue explicitly uses 2 times binary quadratic cross terms, not controlled-S.
 grammar=files['research/t74-native-fast/vendor/native/new/code/borrow/vendor/clifford/clifford_exact.py']
 tree=ast.parse((R/grammar).read_bytes());qenv={}
 f=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in ['qvalue','parity']]
 exec(compile(ast.Module(body=f,type_ignores=[]),'own_helper621_clifford_grammar','exec'),qenv)
 ck('Clifford_even_cross_grammar',qenv['qvalue']([2,0],[0,0],3,2)==2 and qenv['qvalue']([2,0],[0,0],1,2)==0)
 rawT={int(k):v for k,v in arithmetic['targets'].items()};rawP={int(k):v for k,v in arithmetic['paid'].items()}
 tm=sum(k*v for k,v in rawT.items());pm=sum(k*v for k,v in rawP.items());m=max(rawT);B0=sum(rawT.values());P0=sum(rawP.values())
 ck('own_changed_controller_invoice',(m,B0,P0,tm-pm)==(145,10928,64422,752))
 ck('own_full_nonrecursive_allowance',arithmetic['nonrecursive']['raw_scalar_upper']==181098496<10**9)
 ck('own_ordinary_BIT',F(arithmetic['ordinary_BIT']['admitted'])==F(17,5000)and F(arithmetic['ordinary_BIT']['atom'])==F(1,250))
 H=int(arithmetic['compiler']['H']);v=arithmetic['strictification']['power'];floor=arithmetic['strictification']['floor'];cut=arithmetic['strictification']['cutoff']
 eta=F(arithmetic['compiler']['uniform_saving']);kappa=F(arithmetic['kappa']);delta=F(arithmetic['outer']['parameters']['d'])
 ck('own_supplier_witness',(H,v,floor,cut)==(337848000000000,1024,21,20))
 ck('own_record_funding',eta==kappa+6*delta and delta==F(1,7000000000))
 ck('own_original_full54_and4',len(arithmetic['outer']['strict_checks'])==54 and all(F(x)>0 for x in arithmetic['outer']['strict_checks'].values())and len(arithmetic['outer']['functional_checks'])==4 and all(F(x)>0 for x in arithmetic['outer']['functional_checks'].values()))
 replay=read('changed-native-p16-source/4626/fresh-replay.json')
 ck('own_unmodified_native_phase_arithmetic_replay',replay['status']=='PASS_OWN_UNMODIFIED_NATIVE_ABSOLUTE_PHASE_AND_ARITHMETIC'and replay['returncode']==0 and replay['own_head']==head and replay['primary_code_changed']is False and replay['source_manifest_sha256']==hs('changed-native-p16-source/4626/manifest.json'))
 ck('both_original_programs_returned_zero',replay['original_program_results']==[{'program':'verify_native.py','returncode':0},{'program':'arithmetic.py','returncode':0}])
 ck('fresh_replay_source_driver_sha',replay['script_sha256']==hs('replay_helper621_own_source.py'))
 Rstar=(10**9*v*(B0+P0)**v+pm**v+(B0*floor)**v)*(10*m**(2*v)+10);K=32*(Rstar+1);k=K.bit_length();ell=(floor**v).bit_length()-1;g=H//ell;J=m**v*H
 ck('source_completed_product_separation',1<cut<floor<m and 2*cut<m)
 ck('own_global_fresh_work_telescope',(10**9+64)*Rstar+32<K*K)
 ck('own_inventory32HN',2*k+F(H)*(1+F(k,ell))<32*H)
 ck('own_loglog_stock_bound',(32*H).bit_length()<H-1)
 Eguard=22+2*k+(g+1).bit_length()+(J+1).bit_length()
 boundary=source('research/query-thinned-controllers/COMPLEX-CONTROLLER.json')['boundaries']
 adds=[x for x in boundary['left_program']+boundary['right_program']if x[0]=='ADD']
 ck('own_literal_boundary_floor',len(adds)>=4 and all(x[1]!=x[2]and F(x[-1])in[-1,1]for x in adds))
 return dict(schema='own-helper621-separated-native/1',pr=4626,model=B.MODEL,own_head=head,H=str(H),N=f'2^{H}',kappa=str(kappa),eta_uniform=str(eta),record_delta=str(delta),tensor_power=v,
  raw_rank=m,raw_productive_fields=B0,raw_paid_jobs=P0,productive_profile=rawT,paid_profile=rawP,rank_surplus=tm-pm,completed_floor_base=floor,paid_cutoff_base=cut,
  Klog=k,minimum_rank_log_floor=ell,G_depth=str(g),compiler_J_bitlength=J.bit_length(),Eguard=str(Eguard),guard_formula='2^20*K^2*(g+1)*(145^1024*H+1)*d',work_per_array_upper='K^2*N',inventory_log_upper='32*H*N',
  actual_regenerated_candidate_sha256=nr['candidate_payload_sha256'],native_phase_recipe_count=typed,original_native_phase_and_arithmetic_engine_replayed=True,word_materialized=False,
  own_boundary_complex_ADDs=len(adds),used_boundary_complex_ADDs=4,source_hashes=sha,
  retained_contracts=['Own changed helper621 complete relative rank7 absolute-phase normalizers at arbitrary physical input; unchanged original public entry and required exit frames, not merely canonical-buffer self-consistency.',
   'Own raw chronological arbitrary-input native identity and full physical scalar/phase/owned-field correctness at all tensor widths; finite original native/phase engine freshly replayed here.',
   'Own separated-product compiler realizes its strict winning supplier with complete paid base cases and source full nonrecursive allowance below1e9.',
   'Separate role fields, exact per-role Clifford endpoints with recorded absolute phase, fixed parent selected subspace, complete spectators and restored owned banks; ordinary parent row reserve outside children.',
   'Declared fine-prime/Gaussian/finite-section/boundary/recovery analytic branch, unchanged fixed XAG and repaired optimized-GMP semantics.'],
  dependency_hashes={p:hs(p)for p in ['late-uniform-source-extraction/source-manifest.json','changed-native-p16-source/4626/manifest.json','changed-native-p16-source/4626/fresh-replay.json','replay_helper621_own_source.py']},checks_passed=len(checks),checks=checks.copy())
def main():
 n=native();nf='pr4626-helper621-native-parameters.json';n['script_sha256']=hs(Path(__file__).name)
 (R/nf).write_text(json.dumps(B.encoded(n),indent=2)+'\n',encoding='utf8')
 endpoint='pr4535-upper-source/endpoint.py';ep={'__file__':str(R/endpoint),'__name__':'own_helper621_outer'}
 ck('used_endpoint_hash',hs(endpoint)=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
 exec(compile((R/endpoint).read_bytes(),endpoint,'exec'),ep)
 helper=read('candidate-fermat-helper.json');ck('signed_helper',helper['proof_sha256']==hs('candidate-fermat-helper.md')and helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8')
 deps=['helper621-separated-bounds.md','middle-p17-separated-bounds.md','p7-p17-record-crossover-bounds.md','uniform_critical_p16_batch.py','candidate-fermat-helper.md','candidate-fermat-helper.json','pr4470-clifford-stack-upper.md','pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','optimized-gmp-degree8-upper.json','optimized-gmp-degree8-upper.md']
 early=B.schedule(n,'early',ep);record=B.schedule(n,'record',ep)
 for kind,out in [('record',record),('early',early)]:
  out.update(schema='own-helper621-separated-whole-upper/1',proof_file='helper621-separated-bounds.md',native_parameter_certificate=nf,native_parameter_certificate_sha256=hs(nf),tensor_power=n['tensor_power'],script_sha256=hs(Path(__file__).name),automatic_unchanged_native_transfer=False,retained_contracts=n['retained_contracts'],dependency_hashes={p:hs(p)for p in deps})
  if kind=='early':out.update(record_tail_quantified=True,record_tail_certificate='pr4626-helper621-record-upper.json',record_tail_upper_log2log2=record['log2log2U'])
  (R/f'pr4626-helper621-{kind}-upper.json').write_text(json.dumps(B.encoded(out),indent=2)+'\n',encoding='utf8')
 H=int(n['H']);low=dict(schema='own-helper621-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_review',pr=4626,own_head=n['own_head'],model=B.MODEL,baseline_extension_id=B.REFERENCE,H=n['H'],N=n['N'],tensor_power=n['tensor_power'],kappa=n['kappa'],
  own_boundary_complex_ADD_count=n['own_boundary_complex_ADDs'],used_boundary_complex_ADD_count=4,active_AND_lower='8*2^N',active_XOR_lower='24*2^N',j=3,q=0,input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),
  scope='Own complete unreduced changed-helper621 boundary/native word when active, width at least two, strict winning own uniform supplier; identical optimized GMP when inactive.',statistic='Earliest input width at which a correct member of this literal enhancement family strictly beats the reference',all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,
  native_parameter_certificate=nf,native_parameter_certificate_sha256=hs(nf),retained_contracts=n['retained_contracts'],dependency_hashes={p:hs(p)for p in ['helper621-separated-bounds.md','optimized-gmp-degree8-upper.md','optimized-gmp-degree8-upper.json','pr4433-literal-boundary-lower.md']},script_sha256=hs(Path(__file__).name))
 ck('literal_prefix_is_positive',H>73 and n['own_boundary_complex_ADDs']>=4)
 (R/'pr4626-helper621-literal-lower.json').write_text(json.dumps(B.encoded(low),indent=2)+'\n',encoding='utf8')
 print(json.dumps(dict(status='PASS_CLOSED_CONDITIONAL'if REVIEW_CLOSED else'PASS_PENDING_REVIEW',checks=len(checks)+early['checks_passed']+record['checks_passed'],H=n['H'],k=n['Klog'],Eguard=n['Eguard'],early_P=early['log2log2U'],record_P=record['log2log2U'],lower=low['input_bits']),indent=2))
if __name__=='__main__':main()
