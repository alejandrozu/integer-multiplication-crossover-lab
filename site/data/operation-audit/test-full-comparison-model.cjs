'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..');
require(path.join(root,'site/dist/operation-model.js'));
const model=require(path.join(root,'site/dist/full-comparison-model.js'));
const cert=JSON.parse(fs.readFileSync(path.join(__dirname,'pr4470-whole-integer-bound.json'),'utf8'));
assert.equal(model.validate(cert),true);
assert.throws(()=>model.validate({...cert,complete_candidate_upper:false}),/closure/);
assert.throws(()=>model.validate({...cert,subject:'component'}),/mismatch/);
assert.throws(()=>model.priceFactor('unrecognized','1'),/Unknown/);
const expected={hvh:['512','297'],gmp:['2048','5']};
let checks=0;
for(const baseline of ['hvh','gmp']){
 const one=model.priceFactor(baseline,'1');assert.deepEqual([one.numerator,one.denominator],expected[baseline]);
 let previous;
 for(let i=-60;i<=60;i++){
  const rho=(10**(i/20)).toPrecision(12),x=model.comparison(cert,baseline,rho),r=x.price;
  assert(BigInt(r.numerator)>0n&&BigInt(r.denominator)>0n);
  assert(BigInt(r.numerator)<512n*BigInt(r.denominator));
  if(previous)assert(BigInt(r.numerator)*BigInt(previous.denominator)<=BigInt(previous.numerator)*BigInt(r.denominator));
  assert.equal(x.inputUpper,'2^(Mbar^1000000000000000)');
  assert.equal(x.exactFirstCrossing,false);assert.equal(x.conditional,true);
  assert.equal(x.validForEveryLargerInput,true);previous=r;checks++;
 }
}
assert.equal(model.comparison(cert,'hvh','0.001').scaledRatioExponentAtBound.numerator,'-60402999997980000000');
console.log(JSON.stringify({passed:true,positive_tariff_comparisons:checks,exact_rho_one_factors:expected,conditional_not_first_crossing:true}));
