/* Own-source extensions keep the frozen historical model independently usable. */
(function(root){
 'use strict';
 const base=typeof module==='object'&&module.exports?require('./feasibility-history-early-model.js'):root.FeasibilityHistoryModel;
 const digest=/^[a-f0-9]{64}$/,commit=/^[a-f0-9]{40}$/;
 function extensions(data){return data.source_cost_extensions||[]}
 function historicalData(data){const map=new Map(extensions(data).map(e=>[e.pr,e]));return map.size?{...data,entries:data.entries.map(p=>map.has(p.pr)?{...p,...map.get(p.pr).previous_bound_fields}:p)}:data}
 function validate(data){
  base.validate(historicalData(data));const seen=new Set();
  for(const e of extensions(data)){
   if(e.schema!=='own-source-crossover-overlay/1'||seen.has(e.pr)||e.model!==data.model||e.baseline_extension_id!=='gmp-630-native-skylake-unbounded-exact-constants-v2'||!commit.test(e.source_commit)||!digest.test(e.certificate_sha256)||!digest.test(e.peer_review_sha256)||!e.certificate_file||!e.peer_review_file||!e.proof_file)throw Error('Unrecognized own-source cost extension');
   seen.add(e.pr);const p=data.entries.find(p=>p.pr===e.pr),b=e.previous_bound_fields;
   if(!p||p.actual_crossover!==null||!b||!['cost_status','conditional_upper','meaningful_lower_bound'].every(k=>Object.hasOwn(b,k)))throw Error('Missing own-source historical basis');
   if(e.source_selected_kappa_correction){
    if(!p.source_selected_kappa_correction||!p.frozen_kappa_metadata||p.kappa_fraction!==e.actual_own_selected_kappa||p.frozen_kappa_metadata.kappa_fraction!==e.frozen_metadata_kappa||p.kappa_status!=='authenticated_actual_merged_source_selection'||p.accepted_at!==e.source_revision_included_at_merge||!commit.test(e.source_revision_merge_commit)||!digest.test(e.source_kappa_correction_primary_sha256)||!e.source_selected_kappa_correction_basis||!e.source_peer_review_file)throw Error('Unbound source-selected kappa correction');
    for(const key of ['kappa_fraction','kappa_decimal','kappa_status','kappa_scope'])if(p.frozen_kappa_metadata[key]!==b[key])throw Error('Frozen source quote was not preserved');
   }
   if(!e.upper&&!e.lower)throw Error('Own-source extension has no bound');
   const hasLower=Boolean(e.lower||b.meaningful_lower_bound),status=e.upper?(hasLower?'conditional_own_source_range':'conditional_own_source_upper_only'):'conditional_own_source_lower_only';
   if(e.upper){
    if(!/^\d+$/.test(e.upper.exact_log2log2_integer)||BigInt(e.upper.exact_log2log2_integer)<=0n||e.upper.input_bits!==`2^(2^${e.upper.exact_log2log2_integer})`)throw Error('Unrecognized own-source upper encoding');
    if(p.conditional_upper?.input_bits!==e.upper.input_bits||p.conditional_upper.log2log2_input_bits!==e.upper.exact_log2log2_integer||p.conditional_upper.plot_triple_log.exact_log2log2_integer!==e.upper.exact_log2log2_integer||p.conditional_upper.source!==`data/operation-audit/${e.certificate_file}`)throw Error('Own-source point differs from its certificate');
   }else if(p.conditional_upper!==null||b.conditional_upper!==null)throw Error('A lower-only extension cannot assert an upper');
   if(p.cost_status!==status)throw Error('Own-source status differs from its bounds');
   if(e.lower){
    const lower=p.meaningful_lower_bound,plot=e.lower.plot_triple_log,coordinate=plot?.log2_of_integer,smallExponent=plot?.exact_log2_integer;
    const literalCover=coordinate===undefined&&Number.isSafeInteger(smallExponent)&&smallExponent>1&&e.lower.exact_log2_integer===smallExponent&&e.lower.input_bits===`2^${smallExponent}`&&plot.expression===`log2(log2(${smallExponent}))`&&e.lower.statistic==='necessary_no_strict_win_below_endpoint_for_declared_literal_family'&&e.necessary_lower_quantifier==='all_valid_literal_family_public_policies'&&e.upper_not_for_all_switching_policies===true;
    const tower=/^\d+$/.test(coordinate)&&BigInt(coordinate)>73n&&smallExponent===undefined;
    if(!digest.test(e.lower_certificate_sha256)||!e.lower_certificate_file||!(literalCover||tower)||e.lower.exact_individual_crossing!==false||e.lower.all_PR_implementations!==false||JSON.stringify(lower)!==JSON.stringify(e.lower)||lower.source!==`data/operation-audit/${e.lower_certificate_file}`)throw Error('Unrecognized own-source lower certificate');
   }else if(JSON.stringify(p.meaningful_lower_bound)!==JSON.stringify(b.meaningful_lower_bound))throw Error('An own-source upper does not imply a new lower');
   if(e.record_certificate_file&&(!digest.test(e.record_certificate_sha256)||!/^\d+$/.test(e.record_P)||BigInt(e.record_P)<BigInt(e.upper.exact_log2log2_integer)))throw Error('Missing own-source record-tail binding');
  }return true;
 }
 function rows(data,filter='leaders'){
  validate(data);const selected=new Set(base.rows(historicalData(data),filter).map(p=>p.pr));
  if(filter==='leaders'||filter==='bounded')for(const e of extensions(data))selected.add(e.pr);
  return data.entries.filter(p=>selected.has(p.pr));
 }
 function strictFamilyImprovements(data){
  validate(data);const result=[];
  for(const earlier of data.entries){
   const lower=earlier.meaningful_lower_bound?.input_bits,match=/^2\^\(2\^(\d+)-2\^69(?:\+(\d+))?\)$/.exec(lower||'');
   if(!match||BigInt(match[1])<=70n)continue;
   for(const later of data.entries){
    const p=later.conditional_upper?.log2log2_input_bits;
    if(!p||!/^\d+$/.test(p)||Date.parse(later.accepted_at)<=Date.parse(earlier.accepted_at)||BigInt(p)>BigInt(match[1])-1n)continue;
    result.push({earlier:earlier.pr,later:later.pr,lower,upper:later.conditional_upper.input_bits,proof:'P_later <= (H_earlier-3)-1, H_earlier-3>70, q_earlier>=0; hence U_later<L_earlier',all_positive_tariffs:true,scope:'Declared source-specific unreduced literal-core/GMP-fallback families under their retained contracts',source:'data/operation-audit/source-history-endpoint-ordering.md'});
   }
  }return result;
 }
 const api={...base,validate,rows,sourceExtensions:extensions,strictFamilyImprovements};
 if(typeof module==='object'&&module.exports)module.exports=api;root.FeasibilityHistoryModel=api;
})(typeof globalThis==='object'?globalThis:this);
