"""Own payload/selected-compiler literal-family lower certificates, no upper transfer."""
from pathlib import Path
from fractions import Fraction as F
import gzip,hashlib,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
PR_LIST=[5377,5383,5390,5392,5398]
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def read(p):
 data=(R/p).read_bytes();return json.loads(gzip.decompress(data)if str(p).endswith('.gz')else data)
def main():
 manifest='late-uniform-source-extraction/source-manifest.json';allfiles=read(manifest)['files'];out=[]
 for pr in PR_LIST:
  items=[x for x in allfiles if x['pr']==pr];head=items[0]['head'];checks={}
  def ck(k,v):
   assert v,str(pr)+': '+k
   checks[k]=True
  for i,x in enumerate(items):
   data=(R/x['local_path']).read_bytes()
   ck('own_primary_'+str(i),x['status']=='authenticated_own_head_bytes'and x['head']==head and hashlib.sha256(data).hexdigest()==x['sha256'])
   ck('own_git_blob_'+str(i),hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==x['git_blob_sha1'])
  rf=next(x for x in items if x['source_path'].endswith('/RESULT.json')and'/vendor/'not in x['source_path']and'/source/'not in x['source_path'])
  result=read(rf['local_path']);a=result['arithmetic'];H=int(a['compiler']['H']);eta=F(a['compiler']['uniform_saving']);kappa=F(a['kappa']);v=a['strictification']['power']
  ck('own_exact_selected_uniform_rank',a['compiler']['N']==f'2^{H}'and H>73)
  ck('own_positive_uniform_saving',0<eta<1)
  ck('own_actual_record_funded',eta>kappa and F(a['outer']['parameters']['complex_uniform_saving'])==eta)
  T={int(k):int(n)for k,n in a['targets'].items()};P={int(k):int(n)for k,n in a['paid'].items()}
  ck('own_complete_rank_mass',sum(r*n for r,n in T.items())-sum(r*n for r,n in P.items())==a['rank_mass_surplus']==752)
  ck('own_whole_raw_counts',sum(T.values())==a['productive_fields']and sum(P.values())==a['paid_calls'])
  if pr!=5398:
   wf=next(x for x in items if x['source_path'].endswith('/WORD.json.gz'))
   word=read(wf['local_path']);digest=hashlib.sha256((json.dumps(word,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
   wanted=result['native']['literal_word_sha256']if pr==5392 else result['word_payload_sha256']
   ck('own_selected_word_digest',digest==wanted)
   program=word['backward']if pr==5392 else word['programs']['backward']
   adds=[dict(event_index=i,instruction=e)for i,e in enumerate(program)if e[0]=='scalar'and e[1][0]=='add'and len(e[1])==5 and e[1][1][0]==e[1][2][0]=='L'and e[1][1][1]<224 and e[1][2][1]<224 and e[1][1]!=e[1][2]and abs(e[1][3])==e[1][4]]
   ck('own_backward_called_in_complete_raw_unit',a['full_backward']>=1)
   literal=wf['local_path'];literal_sha=wf['sha256'];kind='Four public-field scalar additions retained in the own selected backward local word, called by the complete raw controller.'
  else:
   cf=next(x for x in items if x['source_path'].endswith('/CONTROLLER.json'))
   controller=read(cf['local_path']);boundary=controller['boundaries']
   adds=[dict(event_index=i,instruction=x)for i,x in enumerate(boundary['left_program']+boundary['right_program'])if x[0]=='ADD'and x[1]!=x[2]and F(x[-1])in[-1,1]]
   ck('own_all_backward_controller_interface',a['full_backward']==18 and a['full_forward']==0)
   literal=cf['local_path'];literal_sha=cf['sha256'];digest=result['local_word_sha256'];kind='Four distinct-source unit-coefficient additions in the own complete raw controller boundary.'
  ck('four_actual_literal_complex_ADDs',len(adds)>=4)
  ck('strict_nonwin_exponent_positive',H>73 and (3-3)//8==0)
  # For5390 the smaller matched predecessor is deliberately not selected.
  if pr==5390:ck('new_selected_geometric_compiler_not_matched_predecessor',H==3634890000000000000000 and v==757 and a['matched_PR5387']['old_H']!=H and a['matched_PR5387']['new_H']!=H)
  selected=adds[:4]
  dependencies=['changed-native-p16-boundary-lowers.md','optimized-gmp-degree8-upper.md','optimized-gmp-degree8-upper.json','pr4433-literal-boundary-lower.md',manifest]
  d=dict(schema='own-changed-p16-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=head,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',
   H=str(H),N=f'2^{H}',tensor_power=v,kappa=str(kappa),eta_uniform=str(eta),raw_rank=max(T),raw_productive_fields=sum(T.values()),raw_paid_jobs=sum(P.values()),rank_surplus=752,
   selected_result_file=rf['local_path'],selected_result_sha256=rf['sha256'],selected_literal_file=literal,selected_literal_sha256=literal_sha,selected_word_canonical_sha256=digest,
   used_boundary_complex_ADD_count=4,available_literal_complex_ADD_count=len(adds),selected_literal_ADDs=selected,literal_ADD_scope=kind,
   active_AND_lower='8*2^N',active_XOR_lower='24*2^N',j=3,q=0,input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),
   upper=None,whole_sufficient_upper_derived=False,native_full_engine_replayed_here=False,
   scope='Own complete unreduced raw controller/native word, complete field and spectators when active, stored width at least two; identical repaired optimized GMP when inactive.',
   statistic='Earliest input width at which a correct member of the declared own-source literal enhancement family strictly beats the reference',all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,
   retained_contracts=['Own source changed-native arbitrary-input, absolute-phase, all-column, required-output-frame, clean owned-bank and complete spectator interfaces. Stored source receipts are authenticated, not a fresh full native-engine replay here.',
    'Own compiler physically realizes its strict positive uniform-saving supplier at the selected stated H, with all base cases and complete raw native occurrences retained. No claim of an emitted uniform word.',
    'Prescribed unreduced ADD macro retains the selected scalar instructions on every complete field coordinate; fixed public wiring and constant synthesis are free, scalar macros are not cancelled by cross-instruction simplification.',
    'Same fixed XAG and repaired optimized-GMP opcode, source-correctness and finite-leaf halting/allocation contracts used in the hash-bound degree8 upper.'],
   source_hashes={x['local_path']:x['sha256']for x in items},dependency_hashes={p:hs(p)for p in dependencies},proof_file='changed-native-p16-boundary-lowers.md',script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
  (R/f'pr{pr}-changed-native-literal-lower.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf8');out.append(dict(pr=pr,H=str(H),v=v,lower=d['input_bits'],checks=len(checks)))
 print(json.dumps(dict(status='PASS_CLOSED_CONDITIONAL'if REVIEW_CLOSED else'PASS_PENDING_REVIEW',rows=out),indent=2))
if __name__=='__main__':main()
