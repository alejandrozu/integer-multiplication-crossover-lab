"""Own890/942 active-body floor, not a crossover or automatic stock lower."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import gzip,json
R=Path(__file__).resolve().parent;checks={}
HEADS={890:'4b3bd8cbe8e3e81c44161017c9b72c905a8040a8',942:'1960cfa919a0945d0ca4cb14ea96237000037903'}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 b=(R/f).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ck(k,v):assert v,k;checks[k]=True
smf='t21-t37-cost-source/manifest.json';manifest=rd(smf)
own_paths={a['path']:a for a in manifest if'error'not in a}
for a in manifest:
 if 'error'not in a:ck('pinned_source_head_'+a['file'],a['head']==HEADS[a['pr']] and hs('t21-t37-cost-source/'+a['file'])==a['sha256'])
sf='older-reviewed-source/535-manifest.json';old=rd(sf);protoa=next(a for a in old if a['path']=='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz');protofile='older-reviewed-source/'+protoa['file'];proto=rd(protofile)
ck('literal_full_O73_cover_of_counted_parent',hs(protofile)==protoa['sha256']and proto['m']==73 and proto['cover']=='all matrices d in O(73,2), in lexicographic row order'and 'then every cover class d; each local invocation completes before the next.'in proto['loop_order'])
gate='finite-controller-gate-refinement.md'
emitter='t21-t37-cost-source/890-a7218fd96b28__emit_allcold.py';ev=(R/emitter).read_text()
ck('own890_retains_parent_and_entire_native_cover','t=copy.deepcopy(parent)'in ev and 'including its entire cover sweep and normalization wrappers'in ev and 'each local invocation completes before the next'in ev.lower())
invoice='t21-t37-cost-source/890-88e6a72fc94c__invoice_allcold.py';it=''.join((R/invoice).read_text().split());ck('own_source_group_counts_are_total_not_normalized_work','group=2**(half*half)'in it and 'group*=2**(2*i)-1'in it and 'group*physical'in it and 'group*used'in it)
prepare='t21-t37-cost-source/942-4fe738edc4c0__prepare.py';pv=(R/prepare).read_text()
ck('own942_explicitly_derives_all_runtime_files_from_own_T21_selection',"source=T21/'vendor/pr870/code'"in pv and "receipts['runtime/'+path.name]"in pv and "spec=read(T21/'data/SPEC.json')"in pv and "spec['call_order']=order"in pv)
ck('own942_source_transform_does_not_remove_cover_words','cover'not in pv and 'loop_order'not in pv)
predfile='t21-t37-cost-source/942-bd5fa93facf2__PREDECESSOR.json';pred=rd(predfile)
m942file='remaining-record-audit/artifacts/942/38907d05fdda__MANIFEST.json';m942=rd(m942file)
ck('own942_primary_MANIFEST_binds_actual_adapter_and_PREDECESSOR',m942['prepare.py']==hs(prepare) and m942['PREDECESSOR.json']==hs(predfile))
ck('own942_explicit_exact890_commit_selection',pred['pr']==890 and pred['commit']==HEADS[890] and all(v['unchanged'] for v in pred['packages'].values()) and 'Exact tracked bytes'in pred['copy_scope'])
recovery_file='u8-exact-earlier-selected-byte-recovery.json';recovery=rd(recovery_file);pf='u8-recovered-selected-native/LOCAL-PROGRAMS.json.gz';program=rd(pf)
ck('entire_actual_selected_U8_word',ident(program)=='a073d8d6a561cf5c8148d8b29ae2800bbe3978377c016b549edd7523eb3cf7e5'and any(a['file']==pf and a['sha256']==hs(pf)for a in recovery['outputs'])and all(recovery['checks'].values()))
selected_adds={}
for o,events in program.items():
 adds=[dict(event_index=i,event=e)for i,e in enumerate(events)if e[0]=='scalar'and e[1][0]=='add'and e[1][1][0]=='L'and e[1][2][0]=='L'and 0<=e[1][1][1]<224 and 0<=e[1][2][1]<224 and e[1][1]!=e[1][2]and e[1][4]>0 and abs(e[1][3])==e[1][4]]
 ck(o+'_actual_selected_event_and_public_ADD_counts',len(events)==24415 and len(adds)==489)
 ck(o+'_actual_public_unit_ADD_at_frame_zero',adds[0]['event_index']==3 and adds[0]['event'][-1]==0 and adds[0]['event'][1][4]==1)
 selected_adds[o]=dict(program_orientation_sha256=ident(events),actual_event_count=len(events),public_unit_ADD_count=len(adds),first_literal_add=adds[0])
V=2**(36*36)
for i in range(1,37):V*=2**(2*i)-1
ck('exact_odd_binary_orthogonal_group_order_bits',V.bit_length()==2628)
ck('V_only_floor_excludes_coordinate_multiplier',V.bit_length()-1==2627)
rows=[]
for pr in [890,942]:
 nfile=f'pr{pr}-finite-controller-native.json';n=rd(nfile);sfile=next(f for f in n['source_sha256']if f.endswith('__SPEC.json')and f.startswith('t21-t37-cost-source/890-'))if pr==890 else't21-t37-cost-source/890-0f075414217e__SPEC.json';s=rd(sfile)
 #942 own selection has a separately bound complete numericPLAN/owners and
 # the same exact native word; no890 profile, physical invoice or cutoff moves.
 ck(str(pr)+'_own_selected_program_and_native_rank',n['pr']==pr and n['own_head']==HEADS[pr] and n['native_coordinate_rank']==73 and n['selected_program_semantic_sha256']==ident(program))
 ck(str(pr)+'_own_complete_invocation_source',n['invoice']['calls']==(189 if pr==890 else 333)and n['invoice']['retained_previous_invoice']is None)
 ck(str(pr)+'_both_orientation_commitments',s['providers']['gauge44']['program_hashes']=={o:ident(v)for o,v in program.items()})
 peerfile=f'pr{pr}-finite-controller-peer-review.json';peer=rd(peerfile)
 ck(str(pr)+'_prior_closed_math_peer',peer['pr']==pr and peer['status']=='independent_AI_peer_review_pass_conditional' and peer['fresh_reproduction']['closed_certificates_byte_identically_reproduced'])
 for f in [nfile,n['invoice_certificate'],n['numeric_plan_certificate'],'t21_t37_owner_invoice.py','t21-t37-owner-invoice-workbench.json']:
  ck(str(pr)+'_closed_peer_binds_'+f,peer['reviewed_sha256'][f]==hs(f))
 src={nfile:hs(nfile),n['invoice_certificate']:hs(n['invoice_certificate']),n['numeric_plan_certificate']:hs(n['numeric_plan_certificate']),peerfile:hs(peerfile),pf:hs(pf),protofile:hs(protofile),emitter:hs(emitter),invoice:hs(invoice),gate:hs(gate),recovery_file:hs(recovery_file),prepare:hs(prepare),predfile:hs(predfile),m942file:hs(m942file),smf:hs(smf),sf:hs(sf)}
 for f,h in n['source_sha256'].items():ck(str(pr)+'_own_source_'+f,hs(f)==h);src[f]=h
 rows.append(dict(pr=pr,own_head=n['own_head'],native_coordinate_rank=73,selected_program_semantic_sha256=ident(program),native_selection_authority='own890 SPEC' if pr==890 else 'own942 MANIFEST-bound PREDECESSOR selecting exact890 head, plus own MANIFEST-bound runtime adapter; orientations checked in that selected890 SPEC',own_invocation_count=n['invoice']['calls'],cover_group='all matrices in O(73,2)',cover_group_order=str(V),cover_group_order_bit_length=V.bit_length(),coordinate_multiplier_admitted=False,actual_selected_public_ADDs=selected_adds,active_literal_real_ADD_floor='|O(73,2)|',active_pertype_AND_floor='|O(73,2)|',active_pertype_XOR_floor='3*|O(73,2)|',floor_log2_active_AND=2627,source_sha256=src))
out=dict(schema='own-finite73-literal-complete-cover-active-body-floor/1',status='checked_source_floor_under_explicit_literal_realization_policy',rows=rows,checks_passed=len(checks),checks=checks,whole_crossover_lower_created=False,required_realization_policy=['Execute the complete source orthogonal-group cover whenever using its native template, without cover quotienting or compression.','Retain at least one actual selected public scalar real ADD at each group vertex; no constant-folding, CSE, aggregation, native bypass or word pruning removes it.','Use guarded word width at least2 and the stipulated XAG ADD lowering. No coefficient-field coordinate factor is used.'],coordinate_multiplier_admitted=False,inactive_reference_rule_is_original_source_fact=False,comparison_family_may_add_explicit_inactive_exact_reference_policy=True,source_scope='The active source body floor is independent of a chosen sufficient proof/activation gate. Extending it to every input requires an explicitly fixed comparison-family rule for branches with no such native invocation. The original source does not prove that all no-cover small-input executions equal the reference. This is not an algorithm-independent or optimization-independent integer multiplication lower bound.',dependency_hashes={f:hs(f)for f in ['finite73-literal-cover-source-floor.md','t21-t37-owner-invoice-workbench.json','t21-t37-finite-controller-upper.md']},script_sha256=hs(Path(__file__)))
(R/'finite73-literal-cover-source-floor.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own890/942 source-native active-cover floor checks;no crossing bound')
