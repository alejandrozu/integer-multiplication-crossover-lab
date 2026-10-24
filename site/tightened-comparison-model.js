(function(root){
  'use strict';
  const A=1400000001n,KNUM=60403n,KDEN=20000000n;
  function validate(c){
    if(c?.model!=='xag-straightline-v1'||String(c?.A)!==String(A)||c?.kappa!=='60403/20000000')throw Error('Unrecognized refined comparison parameters');
    if(c?.status!=='closed_conditional_sufficient_upper_bound'||c?.linear_guard_review_closed!==true||c?.native_contracts_retained!==true)throw Error('The refined conditional proof has not closed');
    if(c?.coefficient_each_gate_type!==1||c?.inputUpper!=='2^(M_F^1400000001/256)'||c?.log2log2U!=='46214000033010Y-8')throw Error('The refined cost or input bound does not match');
    if(!['hvh','generic_gmp'].every(b=>c?.rigorous_reference_comparisons?.includes(b)))throw Error('Missing reference proof');
    if(c?.hw_runtime_crossover!==false)throw Error('The circuit result must not be presented as a hardware crossover');
    if(KNUM*(A-1n)<=KDEN)throw Error('The common bound does not prove the comparison');
    return true;
  }
  function comparison(c,baseline,rho){
    validate(c);
    return {price:FullComparisonModel.priceFactor(baseline,rho),A:String(A),
      inputUpper:'2^(M_F^1400000001/256)',
      log2log2Upper:'46214000033010*(F_(2N+2)-1)-8',
      conditional:true,exactFirstCrossing:false,hardwareRuntime:false};
  }
  // Price-uniform ceiling: for t>=1, log_M(p)>=t*(A-1),
  // while the exact price factor is <512<M. No giant integer is rounded.
  function plotCeiling(t){if(typeof t!=='number'||!Number.isFinite(t)||t<1)throw Error('Outside the certified domain');return 1-Number(KNUM)/Number(KDEN)*Number(A-1n)*t}
  const api={A:String(A),kappa:Number(KNUM)/Number(KDEN),validate,comparison,plotCeiling};
  if(typeof module==='object'&&module.exports)module.exports=api;
  root.TightenedComparisonModel=api;
})(typeof globalThis==='object'?globalThis:this);
