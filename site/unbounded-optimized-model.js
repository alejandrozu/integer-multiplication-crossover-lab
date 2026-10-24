(function(root){
  'use strict';
  function validate(c){
    if(c?.schema!=='pr4470-unbounded-optimized-comparison/1'||c?.status!=='closed_conditional_sufficient_upper_bound'||c?.model!=='xag-straightline-v1')throw Error('Unbounded comparison proof is unavailable');
    if(c.A!=='1400000001'||c.kappa!=='60403/20000000'||c.H!=='64215200000000'||c.N!=='2^64215200000000'||c.M_N!=='2^(9HN)')throw Error('Unrecognized candidate parameters');
    if(c.inputUpper!=='2^(M_N^1400000001/256)'||c.log2log2U!=='809111520577936800000000N-8'||c.inputLowerGeneral!=='2')throw Error('Bound parameters do not match');
    if(c.hybridExactL!=='2^(M_N^1400000001/256-1)+1'||c.natural_first_crossing_known!==false||c.natural_eventual_threshold_known!==false)throw Error('First-crossing scope does not match');
    if(c.proof_domain_first_integer!==c.hybridExactL)throw Error('The exact precision endpoint does not match');
    if(c.lowerAND!==2||c.lowerXOR!==3||c.n_min!=='2^80'||c.coefficient_each_gate_type!==1)throw Error('Operation envelopes do not match');
    if(c.unbounded_FFT_termination_closed!==true)throw Error('The unbounded FFT recursion is not closed');
    if(c.baseline_unbounded_extension?.full_tuned_MUL_table_entries!==227||c.native_contracts_retained!==true||c.linear_guard_review_closed!==true||c.hw_runtime_crossover!==false)throw Error('Reference or proof scope does not match');
    return true;
  }
  function gcd(a,b){while(b){const r=a%b;a=b;b=r}return a}
  function price(c,rho){
    validate(c);const r=OperationModel.tariff(String(rho)),a=BigInt(r.numerator),b=BigInt(r.denominator);
    let num=512n*(a+b),den=2n*b+3n*a;const d=gcd(num,den);num/=d;den/=d;
    if(!(num>0n&&den>0n&&num<256n*den))throw Error('Positive-tariff bound failed');
    return {numerator:String(num),denominator:String(den),log2:OperationModel.log2Integer(String(num))-OperationModel.log2Integer(String(den))};
  }
  function plotCeiling(t){if(typeof t!=='number'||!Number.isFinite(t)||t<1)throw Error('Outside the plotted proof domain');return 1-(60403/20000000)*1400000000*t}
  const api={validate,price,plotCeiling};
  if(typeof module==='object'&&module.exports)module.exports=api;root.UnboundedOptimizedModel=api;
})(typeof globalThis==='object'?globalThis:this);
