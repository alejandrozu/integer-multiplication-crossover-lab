(function(root){
  'use strict';
  const refinement=typeof module==='object'&&module.exports?require('./feasibility-refinement-model.js'):root.FeasibilityRefinementModel;
  function validate(data){
    if(data?.schema!=='integer-multiplication-feasibility-history/1'||data?.model!=='xag-straightline-v1'||!Array.isArray(data.entries))throw Error('Unrecognized feasibility history');
    const seen=new Set(),r=data.refinement_certificate;if(r)refinement.validate(r);
    for(const p of data.entries){
      if(!Number.isInteger(p.pr)||seen.has(p.pr)||(!p.historical_leader_candidate&&!(Number(p.kappa_decimal)>0))||!Number.isFinite(Date.parse(p.accepted_at)))throw Error('Invalid historical entry');
      seen.add(p.pr);
      if(p.acceptance_basis!=='github_merged_at'||p.actual_crossover!==null)throw Error('Unverified crossover or acceptance claim');
      const lowers=r?Object.fromEntries(r.rows.map(x=>[x.pr,x.lower])):{4470:'2^(2^64215199999996-2^69+1022)',4479:'2^(2^558100005577-2^69+681)',4483:'2^(2^2799999996-2^69+1)',4533:'2^(2^1586999996-2^69+1)',4535:'2^(2^999999999996-2^69+1)',4565:'2^(2^11825387804-2^69+1)'};
      if(p.meaningful_lower_bound&&(!lowers[p.pr]||p.meaningful_lower_bound.input_bits!==lowers[p.pr]||p.meaningful_lower_bound.all_PR4470_implementations!==false||p.meaningful_lower_bound.exact_individual_crossing!==false))throw Error('Unrecognized or overstated lower bound');
      const own=r?.rows.find(x=>x.pr===p.pr);
      if(p.pr!==4470&&p.meaningful_lower_bound&&!own?.upper&&(p.cost_status!=='conditional_literal_family_lower_only'||p.conditional_upper!==null||p.meaningful_lower_bound.full_upper_transferred!==false))throw Error('A descendant upper bound has not been proved');
      if(p.conditional_upper&&(p.cost_status!=='conditional_literal_family_range'||p.conditional_upper.input_bits!==(r?own?.upper:(p.pr===4470?'2^(M_N^1400000001/256)':null))||p.conditional_upper.model!==data.model))throw Error('Unrecognized crossover bound');
      if(r&&p.conditional_upper&&p.conditional_upper.plot_triple_log.exact_log2log2_integer!==own.upper_log2log2_integer)throw Error('Upper coordinate differs from its certificate');
    }
    return true;
  }
  function rows(data,filter='leaders'){
    validate(data);
    if(!['leaders','reviewed','bounded','all'].includes(filter))throw Error('Unknown history filter');
    if(filter==='reviewed')return data.entries.filter(p=>['historical_selected_or_reviewed_conditional_checkpoint_source','previous_selected_maintainer_reviewed_conditional_claim','latest_selected_maintainer_reviewed_conditional_claim'].includes(p.historical_status));
    return data.entries.filter(p=>filter==='all'||(filter==='leaders'?p.historical_leader_candidate||p.meaningful_lower_bound:p.meaningful_lower_bound||p.conditional_upper));
  }
  function ordinate(p){
    if(!p.conditional_upper)return null;
    const x=p.conditional_upper.plot_triple_log;
    if(x.exact_log2log2_integer)return refinement.integerLog2(x.exact_log2log2_integer);
    if(x.integer!=='64215200000000'||x.add_log2_of_integer!=='809111520577936800000000'||x.subtract_before_outer_log!=='8')throw Error('Unknown tower encoding');
    // log2(C*2^H-8) differs from H+log2(C) by <2^-H.
    // We display two decimal places, with a conservative upward round.
    return Math.ceil((Number(x.integer)+Math.log2(Number(x.add_log2_of_integer)))*100)/100;
  }
  function xValue(p,axis){if(axis==='date')return Date.parse(p.accepted_at);if(axis==='kappa')return Number(p.kappa_decimal)>0?Number(p.kappa_decimal):null;throw Error('Unknown chart axis')}
  function lowerOrdinate(p){if(!p.meaningful_lower_bound)return null;return Math.log2(Number(p.meaningful_lower_bound.plot_triple_log.log2_of_integer))}
  function fraction(p){const [a,b='1']=String(p.kappa_fraction||p.kappa_decimal).split('/');if(a.includes('.')){const [i,f]=a.split('.');return[BigInt(i+f),10n**BigInt(f.length)]}return[BigInt(a),BigInt(b)]}
  function compareKappa(a,b){const [an,ad]=fraction(a),[bn,bd]=fraction(b),d=an*bd-bn*ad;return d<0n?-1:d>0n?1:0}
  function bestUpperSteps(entries,axis){
    const ordered=entries.filter(p=>p.conditional_upper&&xValue(p,axis)!==null).slice().sort((a,b)=>(axis==='date'?Date.parse(a.accepted_at)-Date.parse(b.accepted_at):compareKappa(a,b))||a.pr-b.pr);
    const result=[];let best=null;
    for(let i=0;i<ordered.length;){let j=i+1;while(j<ordered.length&&(axis==='date'?ordered[j].accepted_at===ordered[i].accepted_at:compareKappa(ordered[j],ordered[i])===0))j++;
      const group=ordered.slice(i,j),winner=group.reduce((a,b)=>BigInt(a.conditional_upper.log2log2_input_bits)<=BigInt(b.conditional_upper.log2log2_input_bits)?a:b);
      if(!best||BigInt(winner.conditional_upper.log2log2_input_bits)<BigInt(best.conditional_upper.log2log2_input_bits)){best=winner;result.push({x:xValue(ordered[i],axis),pr:best.pr,y:ordinate(best),P:best.conditional_upper.log2log2_input_bits,source:best.conditional_upper.source})}i=j;
    }return result;
  }
  function strictFamilyImprovements(data){
    validate(data);const byId=new Map(data.refinement_certificate.rows.map(p=>[p.pr,p])),out=[];
    for(const earlier of data.entries){const a=byId.get(earlier.pr);if(!a||BigInt(a.H)<=73n||a.q<0)continue;
      for(const later of data.entries){const b=byId.get(later.pr);if(!b?.upper||Date.parse(later.accepted_at)<=Date.parse(earlier.accepted_at))continue;
        if(BigInt(b.upper_log2log2_integer)<=BigInt(a.H)-4n)out.push({earlier:earlier.pr,later:later.pr,lower:a.lower,upper:b.upper,proof:'P_later <= H_earlier-4; H_earlier>73; q_earlier>=0',all_positive_tariffs:true,scope:'Declared unreduced literal-core/GMP-fallback families only'});
      }
    }return out;
  }
  const api={validate,rows,ordinate,lowerOrdinate,xValue,compareKappa,bestUpperSteps,strictFamilyImprovements};
  if(typeof module==='object'&&module.exports)module.exports=api;
  root.FeasibilityHistoryModel=api;
})(typeof globalThis==='object'?globalThis:this);
