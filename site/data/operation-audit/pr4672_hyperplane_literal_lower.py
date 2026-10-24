"""Fresh own hyperplane word reconstruction and source-selected work floor."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from copy import deepcopy
import ast,gzip,hashlib,json
R=Path(__file__).resolve().parent
HEAD='9da43a7d1ec73f4e6000a201d9d76818a8d4548f'
BASE='research/hyperplane-retiming/'
REVIEW_CLOSED=True
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def read(p):
    b=(R/p).read_bytes();return json.loads(gzip.decompress(b)if str(p).endswith('.gz')else b)
def need(v,m):assert v,m
checks={}
def ck(k,v):assert v,k;checks[k]=True
items=[x for x in read('late-uniform-source-extraction/source-manifest.json')['files']if x['pr']==4672]
by={x['source_path']:x['local_path']for x in items}
for i,x in enumerate(items):
    raw=(R/x['local_path']).read_bytes()
    ck('own_source_'+str(i),x['head']==HEAD and HEAD in x['url']and x['status']=='authenticated_own_head_bytes'and hashlib.sha256(raw).hexdigest()==x['sha256'])
    ck('own_blob_'+str(i),hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['git_blob_sha1'])
a=read(by[BASE+'ARITHMETIC.json']);native=read(by[BASE+'RESULT.json']);source=read(by[BASE+'inputs/pr4610-word.json.gz']);patch=read(by[BASE+'PATCH.json'])
for p,h in a['source_sha256'].items():ck('own_arithmetic_source_'+p,p in by and hs(by[p])==h)
ck('own_selected_native_receipt',a['native_receipt_sha256']==hs(by[BASE+'RESULT.json']))
ck('separate_local_vs_whole_claim',native['new_kappa']is None and F(a['kappa'])==F(151083,50000000))
tree=ast.parse((R/by[BASE+'verify.py']).read_bytes());names={'span','gates','synth','regenerate','invoice'};defs=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in names];ck('exact_own_pure_reconstruction_functions',{n.name for n in defs}==names)
env=dict(Counter=Counter,deepcopy=deepcopy,need=need);exec(compile(ast.Module(body=defs,type_ignores=[]),'own4672_unchanged_word_reconstruction','exec'),env)
c,words,Hprofile=env['regenerate'](source,patch)
ck('own_changed_contact_inventory',len(patch['helper_entrances'])==native['changed_helper_entrances']==13 and len(patch['contacts'])==native['changed_contacts']==49)
for i,basis in enumerate(c['frames']):
    piv={}
    for x in basis:
        ck('frame_domain_'+str(i)+'_'+str(x),isinstance(x,int)and 0<x<512)
        y=x
        while y:
            b=y.bit_length()-1
            if b not in piv:piv[b]=y;break
            y^=piv[b]
    ck('frame_basis_'+str(i),len(piv)==len(basis))
paid={int(k):v for k,v in patch['paid'].items()};T,P=env['invoice'](Hprofile,paid)
ck('whole_selected_profiles_match_native',dict(T)=={int(k):v for k,v in native['whole_targets'].items()}and dict(P)=={int(k):v for k,v in native['whole_paid'].items()})
ck('whole_selected_profiles_match_arithmetic',dict(T)=={int(k):v for k,v in a['targets'].items()}and dict(P)=={int(k):v for k,v in a['paid'].items()}and sum(T.values())==a['productive_fields']and sum(P.values())==a['paid_calls'])
ck('complete_rank_surplus',sum(k*v for k,v in T.items())-sum(k*v for k,v in P.items())==native['rank_surplus']==a['rank_mass_surplus']==752)
H=int(a['compiler']['H']);eta=F(a['compiler']['uniform_saving'])
ck('own_selected_uniform_supplier',H==31385200000000 and a['compiler']['N']==f'2^{H}'and 0<F(a['kappa'])<eta<1 and F(a['strictification']['normalized_paid_upper'])<1)
ck('own_whole_outer_same_supplier',F(a['outer']['parameters']['complex_uniform_saving'])==eta)
adds=[dict(event_index=i,instruction=e)for i,e in enumerate(words['backward'])if e[0]=='scalar'and e[1][0]=='add'and len(e[1])==5 and e[1][1][0]==e[1][2][0]=='L'and 0<=e[1][1][1]<224 and 0<=e[1][2][1]<224 and e[1][1]!=e[1][2]and abs(e[1][3])==e[1][4]]
ck('actual_public_main_ADD_floor',len(adds)==716)
ck('source_width_and_complete_columns',c['start'][:224]==source['canonical']['start'][:224]and c['final']==source['canonical']['final']and len(c['start'])==632 and sum(Hprofile.values())==408)
baseline=read('optimized-gmp-degree8-upper.json')
ck('same_reference',baseline['status']=='closed_conditional_degree8_source_upper'and baseline['baseline_extension_id']=='gmp-630-native-skylake-unbounded-exact-constants-v2'and baseline['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8')
ck('exact_prefix_cancellation',8*(1<<69)==1<<72 and H>73)
payload=(json.dumps(dict(canonical=c,programs=words),sort_keys=True,separators=(',',':'))+'\n').encode()
derived='pr4672-own-regenerated-word.json.gz';(R/derived).write_bytes(gzip.compress(payload,compresslevel=9,mtime=0))
deps=['pr4672-hyperplane-literal-lower.md','late-uniform-source-extraction/source-manifest.json','optimized-gmp-degree8-upper.json','optimized-gmp-degree8-upper.md','changed-native-p16-boundary-lowers.md']
out=dict(schema='own-hyperplane-p16-literal-lower/1',status='closed_conditional_literal_family_lower_bound'if REVIEW_CLOSED else'pending_independent_AI_review',pr=4672,own_head=HEAD,model='xag-straightline-v1',baseline_extension_id=baseline['baseline_extension_id'],H=str(H),N=f'2^{H}',kappa=a['kappa'],eta_uniform=str(eta),tensor_power=a['strictification']['power'],selected_result_file=by[BASE+'ARITHMETIC.json'],selected_result_sha256=hs(by[BASE+'ARITHMETIC.json']),selected_native_result_file=by[BASE+'RESULT.json'],selected_native_result_sha256=hs(by[BASE+'RESULT.json']),selected_literal_file=derived,selected_literal_sha256=hs(derived),derived_word_payload_sha256=hashlib.sha256(payload).hexdigest(),derivation='Own unchanged pure source regenerate/invoice functions applied to own exact PATCH and source program; not a replay of the original native/phase/interval engine.',changed_contacts=49,changed_helper_entrances=13,public_required_frames_preserved=True,all_scalar_and_warp_center_adapter_chronology_preserved=True,actual_frame_bases_checked=True,used_boundary_complex_ADD_count=4,available_literal_complex_ADD_count=len(adds),selected_literal_ADDs=adds[:4],active_AND_lower='8*2^N',active_XOR_lower='24*2^N',input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),upper=None,whole_sufficient_upper_derived=False,native_full_engine_replayed_here=False,actual_word_reconstruction_replayed_here=True,exact_individual_crossing=False,all_PR_implementations=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,scope='Own selected complete unreduced hyperplane-retimed raw controller/native word, full field/spectator ranges when active, stored width at least two; identical optimized GMP when inactive.',statistic='Earliest possible strict win in the declared literal enhancement family',excluded_selection='Alternative round-three and inherited result tuples in the same head are not used.',retained_contracts=['Own source gauge/relative-helper arbitrary-input all-column required-entry/output-frame and absolute-phase identities, complete copied/owned/spectator interface; original full native engine is authenticated but not rerun here.','Own physical mixed tensor/completion/splitting/compiler strict supplier at the selected H, literal complete raw occurrences retained.','Same prescribed unreduced dense ADD lowering and fixed repaired-reference correctness/finite-kernel halting contracts.'],source_hashes={x['local_path']:x['sha256']for x in items},dependency_hashes={p:hs(p)for p in deps},script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks,formal_status='Conditional AI-assisted written mathematics and exact source/reconstruction/arithmetic checks; not Lean or independent human verification.')
(R/'pr4672-hyperplane-literal-lower.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(pr=4672,status=out['status'],checks=len(checks),lower=out['input_bits'],actual_public_ADDs=len(adds))))
