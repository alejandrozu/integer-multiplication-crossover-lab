(function(root){
  'use strict';
  const A=1400000001n,KNUM=60403n,KDEN=20000000n;
  function validate(c){
    if(c?.model!=='xag-straightline-v1'||String(c?.A)!==String(A)||c?.kappa!=='60403/20000000')throw Error('Unrecognized nested comparison parameters');
    if(c?.status!=='closed_conditional_sufficient_upper_bound'||c?.linear_guard_review_closed!==true||c?.native_contracts_retained!==true)throw Error('The nested conditional proof has not closed');
    if(c?.H!=='64215200000000'||c?.N!=='2^64215200000000'||c?.M_N!=='2^(9HN)')throw Error('The selected inventory bound does not match');
    if(c?.hw_runtime_crossover!==false)throw Error('The circuit result must not be presented as a hardware crossover');
    if(c?.coefficient_each_gate_type!==1||c?.inputUpper!=='2^(M_N^1400000001/256)'||c?.log2log2U!=='809111520577936800000000N-8')throw Error('The nested cost or input bound does not match');
    if(!['hvh','generic_gmp'].every(b=>c?.rigorous_reference_comparisons?.includes(b)))throw Error('Missing reference proof');
    if(KNUM*(A-1n)<=KDEN)throw Error('The common bound does not prove the comparison');
    return true;
  }
  function comparison(c,baseline,rho){
    validate(c);
    return {price:FullComparisonModel.priceFactor(baseline,rho),A:String(A),
      inputUpper:'2^(M_N^1400000001/256)',
      conditional:true,exactFirstCrossing:false,hardwareRuntime:false};
  }
  // For t>=1 and U=2^(M_N^A/256), log_M_N(p)>=t(A-1).
  // Both exact positive-tariff price factors are <512<M_N.
  function plotCeiling(t){if(typeof t!=='number'||!Number.isFinite(t)||t<1)throw Error('Outside the certified domain');return 1-Number(KNUM)/Number(KDEN)*Number(A-1n)*t}
  const api={A:String(A),kappa:Number(KNUM)/Number(KDEN),validate,comparison,plotCeiling};
  if(typeof module==='object'&&module.exports)module.exports=api;
  root.NestedComparisonModel=api;
})(typeof globalThis==='object'?globalThis:this);
