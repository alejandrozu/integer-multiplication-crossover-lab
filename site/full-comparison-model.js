(function(root){
  'use strict';
  const A=1000000000000000n,KNUM=60403n,KDEN=20000000n;
  function gcd(a,b){while(b){const r=a%b;a=b;b=r}return a}
  function priceFactor(baseline,rho){
    const r=OperationModel.tariff(String(rho)),a=BigInt(r.numerator),b=BigInt(r.denominator);
    let num,den;
    if(baseline==='hvh'){num=512n*(a+b);den=216n*b+378n*a}
    else if(baseline==='gmp'){num=1024n*(a+b);den=2n*b+3n*a}
    else throw Error('Unknown whole-circuit reference');
    const d=gcd(num,den);num/=d;den/=d;
    return {numerator:num.toString(),denominator:den.toString(),log2:OperationModel.log2Integer(num.toString())-OperationModel.log2Integer(den.toString())};
  }
  function validate(c){
    if(c?.model!=='xag-straightline-v1'||c?.subject!=='whole_integer_multiplication')throw Error('Whole-circuit model mismatch');
    if(c?.complete_candidate_upper!==true||c?.crossover_established!==true||c?.status!=='closed_conditional_sufficient_upper_bound')throw Error('The complete conditional bound has not passed its closure gates');
    if(c?.input_bound?.A!==A.toString()||c?.kappa!=='60403/20000000')throw Error('Unrecognized exact comparison parameters');
    if(KNUM*A-101n*KDEN<=10n*KDEN)throw Error('Compressed comparison failed');
    return true;
  }
  function comparison(c,baseline,rho){validate(c);return {baseline,price:priceFactor(baseline,rho),A:A.toString(),inputUpper:'2^(Mbar^1000000000000000)',Mbar:'2^(33010*4^(2^64215200000000))',log2Log2InputUpper:'33010000000000000000*2^(2*2^64215200000000)',conditional:true,exactFirstCrossing:false,validForEveryLargerInput:true,universalTariffBound:true,scaledRatioExponentAtBound:{numerator:(101n*KDEN-KNUM*A).toString(),denominator:KDEN.toString()}}}
  const api={A:A.toString(),kappa:Number(KNUM)/Number(KDEN),validate,priceFactor,comparison};
  if(typeof module==='object'&&module.exports)module.exports=api;root.FullComparisonModel=api;
})(typeof globalThis==='object'?globalThis:this);
