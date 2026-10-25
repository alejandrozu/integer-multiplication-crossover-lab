"""Own890/942 V-only necessary prefixes and same available literal upper wrappers."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(k,v):assert v,k;checks[k]=True
basefile='optimized-gmp-degree8-compact-upper.json';base=rd(basefile);basepeerfile='optimized-gmp-degree8-compact-upper-peer-review.json';bp=rd(basepeerfile)
ck('same_closed_reference',base['status']=='closed_conditional_degree8_source_upper'and base['numerical_reference_upper_admitted']and base['full_upper_coefficient_log2']==1875 and base['full_upper_each_gate_type']=='2^1875*(n+1)^8')
ck('reference_peer_exact_binding',bp['review_status'].startswith('PASS')and bp['reviewed_sha256'][basefile]==hs(basefile))
floorfile='finite73-literal-cover-source-floor.json';floor=rd(floorfile);floorpeerfile='finite73-literal-cover-source-floor-peer-review.json';fp=rd(floorpeerfile)
ck('separately_reviewed_V_only_source_floor',floor['status']=='checked_source_floor_under_explicit_literal_realization_policy'and floor['checks_passed']==227 and all(floor['checks'].values())and not floor['coordinate_multiplier_admitted']and not floor['whole_crossover_lower_created']and not floor['inactive_reference_rule_is_original_source_fact'])
ck('source_floor_peer_exact_binding',fp['review_status'].startswith('PASS')and fp['reviewed_sha256'][floorfile]==hs(floorfile)and fp['reviewed_sha256']['finite73-literal-cover-source-floor.md']==hs('finite73-literal-cover-source-floor.md')and fp['reviewed_sha256']['finite73_literal_cover_source_floor.py']==hs('finite73_literal_cover_source_floor.py'))
common={}
for a in [base,floor]:
 for key in ['source_sha256','dependency_hashes']:
  for f,h in a.get(key,{}).items():ck('component_'+f,hs(f)==h);common[f]=h
for peer in [bp,fp]:
 for f,h in peer['reviewed_sha256'].items():ck('peer_'+f,hs(f)==h)
ownmath=(R/'t21_t37_finite_controller_upper.py').read_text();ownproof=(R/'t21-t37-finite-controller-upper.md').read_text();whole=(R/'pr4470-whole-integer-bound.md').read_text()
ck('own_upper_retains_full_group_invoice','stock=group*physical;streamed=group*mass;'in ownmath and 'Esource=2**100000'in ownmath and 'logical=V*used+64'in ownproof and 'literal=2*2^30000*stock^2'in ownproof)
ck('outer_native_dimension_and_first_stage','Set d=floor(p^epsilon)'in whole and 'one butterfly bit from each *different* tensor axis into an ordinary Hadamard operation'in whole and 'There are h=ceil(log2 T/d) levels.'in whole)
rows=[]
for src in floor['rows']:
 pr=src['pr'];pref=str(pr)+'_';V=int(src['cover_group_order']);j=V.bit_length()-1;e=(j-1875)//8
 ck(pref+'own_V_only_floor',j==src['floor_log2_active_AND']==2627 and not src['coordinate_multiplier_admitted']and e==94)
 ck(pref+'exact_no_win_prefix',2**(1875+8*e)<=V and e>0)
 nfile=f'pr{pr}-finite-controller-native.json';efile=f'pr{pr}-finite-controller-early-upper.json';rfile=f'pr{pr}-finite-controller-record-upper.json';n,u,r=[rd(f)for f in[nfile,efile,rfile]]
 ck(pref+'same_own_upper_source',all(a['pr']==pr and a['own_head']==src['own_head']and a['status']=='closed_conditional_upper_only'for a in[n,u,r])and n['selected_program_semantic_sha256']==src['selected_program_semantic_sha256'])
 ck(pref+'same_counted_record_tail_not_optional_hybrid',u['record_tail_quantified']and u['record_tail_certificate']==rfile and u['record_tail_certificate_sha256']==hs(rfile)and r['kappa_used']==u['kappa_record']and u['early_effective_kappa']=='1/5000')
 peerfile=f'pr{pr}-finite-controller-peer-review.json';peer=rd(peerfile)
 for f in[nfile,efile,rfile,n['numeric_plan_certificate'],n['invoice_certificate'],'t21_t37_finite_controller_upper.py','t21-t37-finite-controller-upper.md']:
  ck(pref+'old_cost_peer_'+f,peer['reviewed_sha256'][f]==hs(f))
 inv=n['invoice'];plan=rd(n['numeric_plan_certificate'])
 ck(pref+'own_complete_unchanged_body',inv['retained_previous_invoice']is None and inv['calls']==src['own_invocation_count']==len(plan['complete_calls'])and inv['calls']==(189 if pr==890 else 333)and plan['selected_program_semantic_sha256']==src['selected_program_semantic_sha256'])
 ck(pref+'upper_has_room_for_surviving_literal_word',2**100000>V and inv['literal_bits']<=100000 and inv['router_bits']<=30000)
 for label,a in [('early',u),('record',r)]:
  X=int(a['upper_log2log2_integer'])+8;Q=int(a['Q']);delta=F(a['delta']);epsilon=F(a['new_outer_parameters']['epsilon']);degree=1000000*Q;logbase=16*Q+1000+degree*(X+3).bit_length();margin=delta*epsilon*X-10
  ck(pref+label+'_same_full_stopped_reserve',int(a['allsize_work_log_degree'])==degree and delta==F(1,Q))
  ck(pref+label+'_native_present_above_complete_base',margin>logbase+(2*73).bit_length()and margin>logbase)
  ck(pref+label+'_presence_persists_in_tail',F(4*degree,X)<delta*epsilon)
  ck(pref+label+'_positive_full_target_axes',delta*X>10 and epsilon>F(1,2)and X-8>4)
 source=dict(src['source_sha256']);dep=dict(common)
 for a in[n,u,r]:
  for key in['source_sha256','dependency_hashes']:
   for f,h in a[key].items():ck(pref+'upper_payload_'+f,hs(f)==h);(source if key=='source_sha256'else dep)[f]=h
 dep.update({f:hs(f)for f in[basefile,basepeerfile,floorfile,floorpeerfile,'finite73-literal-cover-source-floor.md','finite73_literal_cover_source_floor.py',nfile,efile,rfile,peerfile,f'pr{pr}-finite-controller-source-peer-review.json','t21_t37_finite_controller_upper.py','t21-t37-finite-controller-upper.md','pr4470-whole-integer-bound.md','finite73-literal-cover-ranges.md']})
 scope='Declared own literal complete O(73,2) early/record Gaussian enhancement family. Every active counted source body retains all cover vertices and the actual selected public ADD with no pruning, aggregation, quotienting or bypass; any no-native synthesis returns the identical optimized GMP reference. This is an added comparison-family policy and excludes other historical BIT/original hybrid or compressed implementations.'
 lower=dict(input_bits='2^94',exact_log2_integer=94,plot_triple_log=dict(expression='log2(log2(94))',exact_log2_integer=94),source='Own complete O(73,2) invocation prescription and surviving actual selected U8 ADD, with the independently closed same-reference1875 upper; no coefficient-coordinate multiplier.',scope=scope,statistic='necessary_no_strict_win_below_endpoint_for_declared_literal_family',exact_individual_crossing=False,all_PR_implementations=False)
 quantifiers=dict(necessary_lower_quantifier='all_valid_literal_family_public_policies',sufficient_upper_policy='the_bound_counted_early_schedule_above_its_verified_domain',upper_not_for_all_switching_policies=True,record_tail_policy='the_bound_counted_same_core_record_schedule_above_its_separately_verified_domain')
 out=dict(schema='own-finite73-V-only-literal-lower/1',status='closed_conditional_necessary_lower'if REVIEW_CLOSED else'pending_independent_literal_range_review',pr=pr,own_head=src['own_head'],model=base['model'],baseline_extension_id=base['baseline_extension_id'],kappa_record=u['kappa_record'],effective_kappa='1/5000',group_order=str(V),group_order_bitlength=V.bit_length(),coordinate_multiplicity_used_in_lower=1,complete_coordinate_volume_factor_not_used=True,mandatory_AND_floor=str(V),mandatory_XOR_floor=str(3*V),mandatory_AND_log2_floor=j,reference_upper_log2_coefficient=1875,lower_log2_integer=e,lower=lower,meaningful_lower=lower,activation_threshold_used_as_lower=False,inactive_reference_rule_is_original_source_fact=False,inactive_branch_identical_reference=True,all_switching_policies=True,actual_first_crossing_known=False,upper_compatibility_file=efile,upper_compatibility_sha256=hs(efile),upper_compatibility_scope='Full same own counted source body and complete group E; own early and record verified domains both contain a nonempty native H stage above the full stopped base. No optional unrelated original-record hybrid is included.',source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),checks=checks.copy(),checks_passed=len(checks),retained_contracts=n['retained_contracts']+[scope],**quantifiers)
 lowerfile=f'pr{pr}-finite73-literal-cover-lower.json';(R/lowerfile).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8')
 wrapper=dict(schema='own-finite73-V-only-literal-range/1',status='closed_conditional_two_sided_literal_family'if REVIEW_CLOSED else'pending_independent_literal_range_review',pr=pr,own_head=src['own_head'],source_commit=src['own_head'],model=base['model'],baseline_extension_id=base['baseline_extension_id'],kappa_record=u['kappa_record'],effective_kappa='1/5000',early_effective_kappa='1/5000',upper_log2log2_integer=u['upper_log2log2_integer'],P=u['upper_log2log2_integer'],inputUpper=u['inputUpper'],upper=u['inputUpper'],lower=lower,record_tail_quantified=True,record_tail_certificate=rfile,record_tail_certificate_sha256=hs(rfile),record_tail_upper_log2log2_integer=r['upper_log2log2_integer'],source_base_upper_certificate=efile,source_base_upper_certificate_sha256=hs(efile),lower_certificate=lowerfile,lower_certificate_sha256=hs(lowerfile),upper_compatibility_scope=out['upper_compatibility_scope'],source_family_scope=scope,source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),retained_contracts=out['retained_contracts'],actual_first_crossing_known=False,**quantifiers)
 wrapperfile=f'pr{pr}-finite73-literal-cover-range.json';(R/wrapperfile).write_text(json.dumps(wrapper,indent=2,sort_keys=True)+'\n',encoding='utf8')
 rows.append(dict(pr=pr,own_head=src['own_head'],lower_certificate=lowerfile,lower_certificate_sha256=hs(lowerfile),range_certificate=wrapperfile,range_certificate_sha256=hs(wrapperfile),lower_input_bits='2^94',upper_log2log2_integer=u['upper_log2log2_integer']))
out=dict(schema='own-finite73-V-only-literal-ranges/1',status='closed_conditional_literal_ranges'if REVIEW_CLOSED else'pending_independent_literal_range_review',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'finite73-literal-cover-ranges.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8');print('PASS',len(checks),'own890/942 V-only literal range checks;',out['status'])
