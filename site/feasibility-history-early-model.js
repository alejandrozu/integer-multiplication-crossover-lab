(function(root){
  'use strict';
  const base=typeof module==='object'&&module.exports?require('./feasibility-history-model.js'):root.FeasibilityHistoryModel;
  const refinement=typeof module==='object'&&module.exports?require('./feasibility-refinement-model.js'):root.FeasibilityRefinementModel;
  function extensions(data){return data.finite_family_extensions||(data.early_finite_extension?[data.early_finite_extension]:[])}
  function legacyData(data){const ids=new Set(extensions(data).map(p=>p.pr));return ids.size?{...data,entries:data.entries.map(p=>ids.has(p.pr)?{...p,conditional_upper:null,cost_status:'not_costed'}:p)}:data}
  function validate(data){
    base.validate(legacyData(data));const seen=new Set();
    for(const e of extensions(data)){
      const p=data.entries.find(p=>p.pr===e.pr),A=10001n,E=BigInt(e.E),P=A*E-8n;
      if(![2199023255552n,((1n<<54n)+A-1n)/A].includes(E))throw Error('Unrecognized finite gate');
      if(e.schema!=='source-bound-finite-controller-plot-extension/1'||![147,531,535,588,596,617,626,741,799,890,942,1042,1094].includes(e.pr)||seen.has(e.pr)||e.model!=='xag-straightline-v1'||e.baseline_extension_id!=='gmp-630-native-skylake-unbounded-exact-constants-v2'||e.E!==String(E)||e.A!==String(A)||e.P!==String(P)||e.native_rank!==(e.pr===147?72:73)||e.effective_kappa!=='1/5000'||!e.certificate_file||!/^[a-f0-9]{64}$/.test(e.certificate_sha256)||e.exact_first_crossing_known!==false||typeof e.original_record_tail_quantified!=='boolean')throw Error('Unrecognized finite-source upper extension');
      seen.add(e.pr);
      if(e.pr===147&&e.original_record_tail_quantified!==false)throw Error('Unquantified PR147 original record tail');
      if(e.original_record_tail_quantified&&(!e.record_certificate_file||!/^[a-f0-9]{64}$/.test(e.record_certificate_sha256)||!e.record_upper||!e.record_P||BigInt(e.record_P)<=P))throw Error('Missing own quantified record tail');
      if(!p||p.meaningful_lower_bound!==null||p.actual_crossover!==null||p.cost_status!=='conditional_finite_source_upper_only'||p.conditional_upper?.input_bits!==`2^(2^${P})`||p.conditional_upper.log2log2_input_bits!==String(P)||p.conditional_upper.plot_triple_log.exact_log2log2_integer!==String(P)||p.conditional_upper.source!==`data/operation-audit/${e.certificate_file}`)throw Error('Finite source point differs from its certificate');
    }return true;
  }
  function rows(data,filter='leaders'){
    validate(data);if(filter==='bounded')return data.entries.filter(p=>p.meaningful_lower_bound||p.conditional_upper);
    const selected=new Set(base.rows(legacyData(data),filter).map(p=>p.pr));if(filter==='leaders')for(const e of extensions(data))selected.add(e.pr);return data.entries.filter(p=>selected.has(p.pr));
  }
  const api={...base,validate,rows,extensions,strictFamilyImprovements:data=>{validate(data);return base.strictFamilyImprovements(legacyData(data))},ordinate:p=>p.upper_only_finite_source&&p.conditional_upper?refinement.integerLog2(p.conditional_upper.log2log2_input_bits):base.ordinate(p)};
  if(typeof module==='object'&&module.exports)module.exports=api;root.FeasibilityHistoryModel=api;
})(typeof globalThis==='object'?globalThis:this);
