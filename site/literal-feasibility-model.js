(function(root){
  'use strict';
  function validate(c){
    if(c?.schema!=='pr4470-literal-feasibility-range/1'||c?.status!=='closed_conditional_literal_family_feasibility_range'||c?.model!=='xag-straightline-v1')throw Error('Literal feasibility proof is unavailable');
    if(c.H!=='64215200000000'||c.lower!=='2^(2^64215199999996-2^69+1022)'||c.upper!=='2^(M_N^1400000001/256)'||c.reference_upper_per_type!=='2^(2^73)*(n+1)^16')throw Error('Unrecognized counted endpoints');
    if(c.baseline_extension_id!=='gmp-630-native-skylake-unbounded-exact-constants-v2'||c.source_upper_lower_transfers_to_corrected_reference!==true)throw Error('Incomplete unlimited reference');
    if(c.arbitrary_switch_used_as_lower!==false||c.validity_gate_used_as_necessary_lower!==false||c.API_limit_used!==false||c.exact_first_crossing_known!==false||c.covers_all_PR4470_implementations!==false)throw Error('Crossover scope is invalid');
    if(c.requires_unreduced_literal_core!==true||c.requires_same_reference_when_inactive!==true||c.retained_PR_native_analytic_recovery_contracts!==true||c.ordinary_finite_native_halting_and_correctness_contract!==true)throw Error('Required contracts are missing');
    return true;
  }
  function tariff(c,rho){
    validate(c);const r=OperationModel.tariff(String(rho)),a=BigInt(r.numerator),b=BigInt(r.denominator);
    let num=b+3n*a,den=b+a;function gcd(x,y){while(y){const r=x%y;x=y;y=r}return x}
    const g=gcd(num,den);num/=g;den/=g;
    if(!(num>den&&num<3n*den))throw Error('Tariff is not positive');
    return {numerator:String(num),denominator:String(den),rootMultiplier:(Number(num)/Number(den))**(1/16)};
  }
  function lowerPlot(c){validate(c);return Math.log2(64215199999996)}
  const api={validate,tariff,lowerPlot};
  if(typeof module==='object'&&module.exports)module.exports=api;root.LiteralFeasibilityModel=api;
})(typeof globalThis==='object'?globalThis:this);
