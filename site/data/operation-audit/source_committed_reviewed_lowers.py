"""Own5395/5399 selected-word byte commitments and literal lower endpoints."""
from pathlib import Path
from fractions import Fraction as F
import gzip,json,hashlib
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True

def rd(p):
 b=(R/p).read_bytes();return json.loads(gzip.decompress(b)if str(p).endswith('.gz')else b)
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
M=rd('late-uniform-source-extraction/source-manifest.json')['files'];ref=rd('optimized-gmp-degree8-upper.json');summ=[]
for pr in[5395,5399]:
 checks={}
 def ck(n,v):assert v,f'{pr}_{n}';checks[n]=True
 rows=[x for x in M if x['pr']==pr];head=rows[0]['head'];source={}
 for x in rows:
  b=(R/x['local_path']).read_bytes();ck('own_primary_'+x['source_path'],x['head']==head and x['status']=='authenticated_own_head_bytes'and hs(x['local_path'])==x['sha256']and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1']);source[x['local_path']]=x['sha256']
 root=f'late-uniform-source-extraction/files/{pr}/'
 if pr==5395:
  rf=root+'6761870e770edb54__RESULT.json';ff=root+'48988d6a1c32eeaa__5387-receipt-v2.json';wf=root+'6c4c8cef569872ef__PHYSICAL-RECEIPT.json';scopefile=root+'174c3176718f4ac9__README.md'
  result=rd(rf);a=rd(ff);physical=rd(wf);candidate='b1ab650d36f59e5be682a813145b7c67e219e341'
  ck('own_selected_candidate',result['strongest_head']==a['candidate']['head']==physical['candidate_head']==candidate and F(result['strongest_kappa'])==F(a['kappa']))
  wordfile='late-uniform-source-extraction/files/5396/da5207429df7e4c6__WORD.json.gz';H=409549000000000000
  ck('own_strict_funding_receipt',a['endpoint_funded']and a['complete_bill_ready']and a['no_expanded_word_materialized'])
 else:
  rf=root+'4e4f0b144648ee25__RESULT.json';wf=root+'a9ac8960c41f867c__WORD-RECEIPT.json';ff=rf;scopefile=root+'38966d950e574afb__README.md';result=rd(rf);a=result['normal']['independent_fresh']['exact_funding']['result'];physical=rd(wf);candidate='329b2ff35d2994b11abbb59f770d12da75c494ac'
  ck('own_selected_candidate',result['head']==physical['head']==candidate and F(result['kappa'])==F(a['kappa']))
  other=result['optimized']['independent_fresh']['exact_funding']['result'];ck('independent_normal_optimized_math_agree',all(a[k]==other[k]for k in['H','N','kappa','uniform_saving','targets','paid','normalized_paid_upper']))
  correction=rd(root+'7954cde60f6de6cc__RESULT.json')['physical_formal_diagnostic_scope'];ck('formal_diagnostic_erratum_not_repurposed',not correction['actual_physical_nonzero_established']and not correction['physical_surjectivity_established']and not correction['reverse_zero_required_by_main_proof']and correction['positive_arbitrary_bridge_substitution_cancellation_unchanged'])
  wordfile='late-uniform-source-extraction/files/5392/a882d509237f178d__WORD.json.gz';H=31385200000000
 eta=F(a['uniform_saving']);kap=F(a['kappa']);ck('own_selected_H_and_positive_supplier',int(a['H'])==H and a['N']==f'2^{H}'and 0<kap<eta<1 and F(a['normalized_paid_upper'])<1)
 T={int(k):v for k,v in a['targets'].items()};P={int(k):v for k,v in a['paid'].items()};ck('own_complete_raw_rankmass',sum(T.values())==a['productive_count']and sum(P.values())==a['paid_count']and sum(k*v for k,v in T.items())-sum(k*v for k,v in P.items())==a['rank_mass_surplus']==752)
 b=(R/wordfile).read_bytes();raw=gzip.decompress(b);word=json.loads(raw);canonical=(json.dumps(word,sort_keys=True,separators=(',',':'))+'\n').encode();ck('own_word_compressed_commitment',hashlib.sha256(b).hexdigest()==physical['word_sha256']);ck('own_word_payload_commitment',hashlib.sha256(canonical).hexdigest()==physical['word_payload_sha256']);ck('own_word_Git_blob_commitment',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==physical['word_git_blob'])
 source[wordfile]=hs(wordfile);program=word['programs']['backward']if'programs'in word else word['backward'];adds=[]
 owned={tuple(z)for z in(word['owned']['backward']if'owned'in word else word['owned_roles'])}
 for i,e in enumerate(program):
  if e[0]=='scalar'and e[1][0]=='add':
   z=e[1]
   if len(z)==5 and z[1][0]==z[2][0]=='L'and 0<=z[1][1]<224 and 0<=z[2][1]<224 and z[1]!=z[2]and z[4]>0 and abs(z[3])==z[4]and tuple(z[1])not in owned and tuple(z[2])not in owned:adds.append(dict(event_index=i,instruction=e))
 ck('four_actual_public_main_unit_ADDs',len(adds)>=4)
 ck('selected_unit_DEN_and_actual_owned_exclusion',all(e['instruction'][1][4]>0 and abs(F(e['instruction'][1][3],e['instruction'][1][4]))==1 and all(tuple(z)not in owned for z in e['instruction'][1][1:3])for e in adds[:4]))
 invoice=a['invoice']if pr==5395 else result['normal']['independent_fresh']['literal_invoice']['result']
 if pr==5399:ck('own_controller_uses_backward',invoice['controller']['counts']['backward']>=1)
 else:ck('own_physical_controller_complete',len(physical['controller']['backward_stages'])>=1)
 ck('fixed_degree8_reference',ref['status']=='closed_conditional_degree8_source_upper'and ref['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8');ck('exact_prefix_cancellation',H>73 and 8*(1<<69)==1<<72)
 deps=['source-committed-reviewed-lowers.md','late-uniform-source-extraction/source-manifest.json','reviewed-selected-native-lowers.md','optimized-gmp-degree8-upper.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
 o=dict(schema='own-source-committed-review-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=head,selected_candidate_head=candidate,H=str(H),N=f'2^{H}',tensor_power=1024,kappa=str(kap),eta_uniform=str(eta),model='xag-straightline-v1',baseline_extension_id=ref['baseline_extension_id'],selected_result_file=rf,own_funding_receipt_file=ff,own_word_commitment_file=wf,selected_literal_file=wordfile,selected_literal_sha256=hs(wordfile),recovered_word_exactly_own_committed_bytes=True,parameter_transfer_from_recovery_archive=False,source_scope_file=scopefile,selected_literal_ADDs=adds[:4],available_literal_complex_ADD_count=len(adds),used_boundary_complex_ADD_count=4,active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),upper=None,whole_sufficient_upper_derived=False,native_full_engine_replayed_here=False,all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,scope='Own source-selected unreduced full-field/native/complete controller enhancement family at positive multiplicity and width>=2 when active; identical repaired optimizedGMP when inactive.',statistic='Earliest possible strict win in this declared source-selected literal enhancement family',formal_nonzero_cut_claim_used=False,retained_contracts=['Own complete required physical entry/output-frame/absolute-phase/all-column/owned/spectator native endpoint and literal complete controller, not established by source scalar statistics or formal nonzero-cut diagnostics.','Own source physically realized strict winning uniform supplier, chronological integer compiler/fullfields and source complete-template applicability. Exact own stored evidence is authenticated, not freshly rerun original native/phase/validation engines here.','Same prescribed unreduced dense arithmetic macros and repaired optimizedGMP correctness/finite-kernel halting.'],source_sha256=source,dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks,formal_status='Conditional AI-assisted written mathematics and exact source/byte/arithmetic checks; not Lean or independent human acceptance.')
 (R/f'pr{pr}-source-committed-literal-lower.json').write_text(json.dumps(o,indent=2)+'\n');summ.append(dict(pr=pr,H=str(H),checks=len(checks),lower=o['input_bits']))
print(json.dumps(summ,indent=2))
