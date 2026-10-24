'use strict';
const assert=require('node:assert/strict');
const C=require('../site/dist/operation-model.js');
let pairs=0;
for(let width=1;width<=6;width++)for(let x=0;x<2**width;x++)for(let y=0;y<2**width;y++){
 let and=0,xor=0;const AND=(a,b)=>(and++,a&b),XOR=(a,b)=>(xor++,a^b);
 let sum=XOR(x&1,y&1),carry=AND(x&1,y&1);
 for(let i=1;i<width;i++){const a=x>>i&1,b=y>>i&1,p=XOR(a,b);sum|=XOR(p,carry)<<i;carry=XOR(AND(a,b),AND(p,carry))}
 sum|=carry<<width;assert.equal(sum,x+y);assert.deepEqual(C.counts(and,xor),C.ripple(width));pairs++;
}
assert.deepEqual(C.weighted(C.counts(10,20),'0.25'),{numerator:'1500',denominator:'100'});
assert.equal(C.compare(C.counts(10,20),C.counts(20,10),'0.25'),-1);
assert.equal(C.compare(C.counts(10,20),C.counts(20,10),'1'),0);
assert.equal(C.compare(C.counts(10,20),C.counts(20,10),'4'),1);
assert.deepEqual(C.criticalTariff(C.counts(10,20),C.counts(20,10)),{kind:'boundary',numerator:'10',denominator:'10',candidateWins:'below'});
assert.equal(C.criticalTariff(C.counts(20,20),C.counts(10,10)).kind,'never');
assert.equal(C.criticalTariff(C.counts(10,10),C.counts(20,20)).kind,'always');
assert.equal(C.criticalTariff(C.counts(10,10),C.counts(10,20)).kind,'always');
assert.equal(C.criticalTariff(C.counts(10,20),C.counts(10,10)).kind,'never');
assert.equal(C.criticalTariff(C.counts(10,20),C.counts(10,20)).kind,'tie');
assert.equal(C.log2Integer((2n**1000n).toString()),1000);
assert.equal(C.log2Weighted(C.counts(1024,1024),'1'),11);
assert.equal(C.completeComparison({model:C.MODEL,subject:'controller',countClosure:'complete'},{model:C.MODEL,subject:'whole_integer_multiplication',countClosure:'complete'}).ready,false);
assert.equal(C.completeComparison({model:C.MODEL,subject:'whole_integer_multiplication',countClosure:'incomplete'},{model:C.MODEL,subject:'whole_integer_multiplication',countClosure:'complete'}).ready,false);
assert.equal(C.completeComparison({model:C.MODEL,subject:'whole_integer_multiplication',countClosure:'complete'},{model:C.MODEL,subject:'whole_integer_multiplication',countClosure:'complete'}).ready,true);
assert.throws(()=>C.counts(9007199254740992,1));assert.throws(()=>C.tariff('0'));assert.throws(()=>C.ripple(0));
assert.throws(()=>C.scale({model:'other',and:'1',xor:'1'},2));
assert.throws(()=>C.weighted(C.counts(1,1),{numerator:'-2',denominator:'1'}));
assert.throws(()=>C.weighted(C.counts(1,1),{numerator:'2',denominator:'0'}));
assert.equal(C.mixedLayerThreshold(64,'1').fSufficient,'266');
assert.equal(C.mixedLayerThreshold(1000000,'1').fSufficient,'267');
for(const w of [2,3,8,64,1000000])for(const rho of ['0.001','0.1','1','10','1000'])assert(BigInt(C.mixedLayerThreshold(w,rho).fSufficient)<=271n);
assert(271n*12032n>3258860n);
assert.equal(C.mixedLayerUniform('0.001').fSufficient,'259');
assert.equal(C.mixedLayerUniform('1').fSufficient,'267');
assert.equal(C.mixedLayerUniform('1000').fSufficient,'271');
for(const rho of ['0.001','0.1','1','10','1000'])for(const w of [2,8,64,1000000])assert(BigInt(C.mixedLayerThreshold(w,rho).fSufficient)<=BigInt(C.mixedLayerUniform(rho).fSufficient));
for(const [rho,offset] of [['0.001','1947'],['0.1','1946'],['1','1944'],['10','1942'],['1000','1941']]){const r=C.baselineSufficientExponent(rho);assert.equal(r.offset,offset);assert(r.exactIntegerInequality&&r.previousDoesNotCertify)}
assert.equal(C.baselineSufficientExponent('1').log2InputBits,'7137398073256634897664758526207831208354');
let negationInputs=0;
for(let width=2;width<=8;width++)for(let x=0;x<2**width;x++){
 let and=0,xor=0;const AND=(a,b)=>(and++,a&b),XOR=(a,b)=>(xor++,a^b);let result=x&1,prefix=x&1;
 for(let i=1;i<width;i++){const a=x>>i&1,s=XOR(a,prefix);result|=s<<i;if(i<width-1)prefix=XOR(s,AND(a,prefix))}
 assert.equal(result,(-x)&(2**width-1));assert.deepEqual(C.counts(and,xor),C.counts(width-2,2*width-3));negationInputs++;
}
console.log(JSON.stringify({passed:true,exhaustive_negation_inputs:negationInputs,mixed_layer_tariff_bound:'f <= 271 under the documented component assumptions'}));
console.log(JSON.stringify({passed:true,exhaustive_adder_input_pairs:pairs,comparisons_and_scope_checks:true,scope:'Reference circuit and exact rational cost engine only; not a full PR4470 proof.'}));
