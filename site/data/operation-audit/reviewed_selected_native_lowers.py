"""Own selected validation capsules; source-specific literal lower endpoints only."""
from pathlib import Path
from fractions import Fraction as F
import gzip,hashlib,json
R=Path(__file__).resolve().parent
REVIEW_CLOSED=True
CONFIG={
5384:dict(H=31385200000000,kappa='60447/20000000',result='e3f4ccec6d55a564__RESULT.json',word='c0bc63a81aa03371__WORD.json.gz',scope='789651d37f0003da__README.md'),
5396:dict(H=409549000000000000,kappa='605334953/200000000000',result='aef661be51025a0c__RESULT.json',word='da5207429df7e4c6__WORD.json.gz',scope='40bda2b7c17ac754__PROOF.md'),
5400:dict(H=38569300000000000,kappa='302728823/100000000000',result='9fe3dfc1cc74ac4d__RESULT.json',word='267c3cc51495ad8b__WORD.json.gz',scope='797e0b873ee9a6e3__PROOF.md')}
def read(p):
    raw=(R/p).read_bytes();return json.loads(gzip.decompress(raw)if str(p).endswith('.gz')else raw)
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
manifest='late-uniform-source-extraction/source-manifest.json'
allfiles=read(manifest)['files'];outputs=[]
baseline=read('optimized-gmp-degree8-upper.json')
for pr,cfg in CONFIG.items():
    checks={}
    def ck(k,v):
        assert v,f'{pr}: {k}'
        checks[k]=True
    items=[x for x in allfiles if x['pr']==pr];head=items[0]['head'];root=f'late-uniform-source-extraction/files/{pr}/'
    by={x['local_path']:x for x in items}
    for i,x in enumerate(items):
        raw=(R/x['local_path']).read_bytes()
        ck('own_source_'+str(i),x['head']==head and x['status']=='authenticated_own_head_bytes'and head in x['url']and hashlib.sha256(raw).hexdigest()==x['sha256'])
        ck('own_blob_'+str(i),hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['git_blob_sha1'])
    resultfile=root+cfg['result'];wordfile=root+cfg['word'];scopefile=root+cfg['scope']
    ck('actual_own_inputs_present',all(p in by for p in[resultfile,wordfile,scopefile]))
    result=read(resultfile);a=result['arithmetic'];word=read(wordfile)
    H=int(a['compiler']['H']);eta=F(a['compiler']['uniform_saving']);kappa=F(a['kappa'])
    ck('own_selected_tuple',H==cfg['H']and a['compiler']['N']==f'2^{H}'and kappa==F(cfg['kappa']))
    ck('strict_positive_source_supplier',0<kappa<eta<1 and F(a['strictification']['normalized_paid_upper'])<1)
    ck('actual_source_outer_funds_own_supplier',F(a['outer']['parameters']['complex_uniform_saving'])==eta)
    T={int(k):v for k,v in a['targets'].items()};P={int(k):v for k,v in a['paid'].items()}
    ck('complete_raw_profile',sum(T.values())==a['productive_fields']and sum(P.values())==a['paid_calls']and sum(k*v for k,v in T.items())-sum(k*v for k,v in P.items())==a['rank_mass_surplus']==752)
    ck('whole_backward_native_called',a['full_backward']>=1)
    canonical=hashlib.sha256((json.dumps(word,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
    wanted=result['local_word_sha256']if pr==5400 else result['word_payload_sha256']
    ck('actual_selected_word_payload',canonical==wanted)
    adds=[dict(event_index=i,instruction=e)for i,e in enumerate(word['programs']['backward'])if e[0]=='scalar'and e[1][0]=='add'and len(e[1])==5 and e[1][1][0]==e[1][2][0]=='L'and 0<=e[1][1][1]<224 and 0<=e[1][2][1]<224 and e[1][1]!=e[1][2]and abs(e[1][3])==e[1][4]]
    ck('four_distinct_public_field_unit_ADDs',len(adds)>=4)
    if pr==5396:
        other=read(root+'41d9ecf561d52262__RESULT.json')
        ck('distinct_reviewed_5383_not_selected',F(other['arithmetic']['kappa'])!=kappa and int(other['arithmetic']['compiler']['H'])==31385200000000 and other['word_payload_sha256']!=wanted)
    ck('same_fixed_reference',baseline['status']=='closed_conditional_degree8_source_upper'and baseline['baseline_extension_id']=='gmp-630-native-skylake-unbounded-exact-constants-v2'and baseline['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8')
    ck('exact_prefix_cancellation',H>73 and 8*(1<<69)==1<<72 and 8==1<<3)
    deps=[manifest,'reviewed-selected-native-lowers.md','optimized-gmp-degree8-upper.md','optimized-gmp-degree8-upper.json','changed-native-p16-boundary-lowers.md']
    out=dict(schema='own-reviewed-selected-p16-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=head,model='xag-straightline-v1',baseline_extension_id=baseline['baseline_extension_id'],H=str(H),N=f'2^{H}',tensor_power=a['strictification']['power'],kappa=str(kappa),eta_uniform=str(eta),algorithm_relation='Independent validation of its own selected literal construction; no new-construction credit inferred.',selected_result_file=resultfile,selected_result_sha256=hs(resultfile),selected_literal_file=wordfile,selected_literal_sha256=hs(wordfile),selected_word_canonical_sha256=canonical,source_scope_file=scopefile,source_scope_sha256=hs(scopefile),used_boundary_complex_ADD_count=4,available_literal_complex_ADD_count=len(adds),selected_literal_ADDs=adds[:4],active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),upper=None,whole_sufficient_upper_derived=False,native_full_engine_replayed_here=False,all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,scope='Own selected complete unreduced raw controller/native word with full field/spectator ranges when active, stored width at least two; identical optimized GMP when inactive.',statistic='Earliest possible strict win in the specified own-source literal enhancement family',retained_contracts=['Own source native arbitrary-input required entry/output frames, absolute phase, all-column whole-job/owned/spectator and actual changed caller semantics. Stored validation evidence is authenticated, not a freshly rerun original native or validation engine here.','Own physically realized strict winning uniform compiler at the selected H, literal raw occurrences/boundary instructions retained, no materialized enormous uniform-word claim.','Prescribed unreduced dense ADD macros and the same fixed reference correctness/finite-kernel halting contracts.'],formal_status='Conditional AI-assisted written mathematics and exact source/arithmetic checks; not Lean or independent human verification.',source_hashes={x['local_path']:x['sha256']for x in items},dependency_hashes={p:hs(p)for p in deps},proof_file='reviewed-selected-native-lowers.md',script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
    (R/f'pr{pr}-reviewed-selected-literal-lower.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');outputs.append(dict(pr=pr,checks=len(checks),H=str(H),lower=out['input_bits']))
print(json.dumps(dict(status='PASS_CLOSED_CONDITIONAL'if REVIEW_CLOSED else'PASS_PENDING_REVIEW',rows=outputs),indent=2))
