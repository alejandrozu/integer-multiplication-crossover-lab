'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=__dirname;
globalThis.OperationModel=require('../site/dist/operation-model.js');
const m=require('../site/dist/literal-feasibility-model.js');
const c=JSON.parse(fs.readFileSync(path.join(root,'pr4470-literal-feasibility-range.json')));
assert(m.validate(c));
for(const [file,hash] of Object.entries(c.proof_input_sha256))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,file))).digest('hex'),hash,file);
for(const [rho,num,den] of [['0.001','1003','1001'],['1','2','1'],['1000','3001','1001']]){
  const p=m.tariff(c,rho);assert.equal(p.numerator,num);assert.equal(p.denominator,den);assert(p.rootMultiplier>1&&p.rootMultiplier<3**(1/16));
}
for(const field of ['arbitrary_switch_used_as_lower','validity_gate_used_as_necessary_lower','API_limit_used','exact_first_crossing_known','covers_all_PR4470_implementations']){const bad=structuredClone(c);bad[field]=true;assert.throws(()=>m.validate(bad),/scope/)}
for(const field of ['requires_unreduced_literal_core','requires_same_reference_when_inactive','ordinary_finite_native_halting_and_correctness_contract']){const bad=structuredClone(c);bad[field]=false;assert.throws(()=>m.validate(bad),/contracts/)}
assert.throws(()=>m.tariff(c,'0'));
assert(m.lowerPlot(c)>45&&m.lowerPlot(c)<47);
console.log(JSON.stringify({passed:true,source_hash_bindings:true,exact_tariffs:true,overclaim_mutations_rejected:true}));
