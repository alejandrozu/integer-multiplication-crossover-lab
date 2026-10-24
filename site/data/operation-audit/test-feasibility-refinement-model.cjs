'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
global.OperationModel=require('../site/dist/operation-model.js');
const model=require('../site/dist/feasibility-refinement-model.js');
const c=JSON.parse(fs.readFileSync(path.join(__dirname,'literal-feasibility-refinement-v2.json')));
assert(model.validate(c));
for(const [file,hash]of Object.entries(c.proof_inputs_sha256))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,file))).digest('hex'),hash,file);
assert.equal(c.upper_log2log2_integer,'125861792269956681793310401189063');
assert(model.integerLog2(c.upper_log2log2_integer)>106.63&&model.integerLog2(c.upper_log2log2_integer)<106.64);
for(const [rho,num,den]of [['1','2','1'],['0.001','1003','1001'],['1000','3001','1001']]){const t=model.tariff(c,rho);assert.equal(t.numerator,num);assert.equal(t.denominator,den);assert(t.rootMultiplier>1&&t.rootMultiplier<3**(1/8));}
for(const key of ['interval_is_narrow_or_realistic','API_limit_used','chosen_switch_used_as_lower','precision_proof_gate_used_as_necessary_lower']){const b=structuredClone(c);b[key]=true;assert.throws(()=>model.validate(b));}
const bad=structuredClone(c);bad.upper_log2log2_integer=String(BigInt(c.upper_log2log2_integer)+1n);assert.throws(()=>model.validate(bad));
const transfer=structuredClone(c);transfer.rows.find(r=>r.pr===4610).upper=c.rows[0].upper;assert.throws(()=>model.validate(transfer));
const overclaim=structuredClone(c);overclaim.rows[0].all_implementations_of_PR=true;assert.throws(()=>model.validate(overclaim));
console.log(JSON.stringify({passed:true,rows:c.rows.length,source_hashes:Object.keys(c.proof_inputs_sha256).length,tariffs:3,unproved_claim_mutations_rejected:true}));
const v3=JSON.parse(fs.readFileSync(path.join(__dirname,'literal-feasibility-refinement-v3.json')));
assert(model.validate(v3));
for(const [file,hash]of Object.entries(v3.proof_inputs_sha256))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,file))).digest('hex'),hash,file);
const own=v3.rows.find(r=>r.pr===4610);
assert.equal(own.upper_log2log2_integer,'75595828000242989051763406588679201189081');
assert.equal(own.tensor_power_used_for_lower,1);
assert.equal(own.upper_uses_completed_tensor_power,1024);
assert(model.integerLog2(own.upper_log2log2_integer)>135&&model.integerLog2(own.upper_log2log2_integer)<137);
for(const key of ['E','Eguard','A','upper_log2log2_integer']){const b=structuredClone(v3);b.rows.find(r=>r.pr===4610)[key]=String(BigInt(own[key])+1n);assert.throws(()=>model.validate(b));}
const copied=structuredClone(v3);copied.rows.find(r=>r.pr===4610).upper=v3.rows[0].upper;assert.throws(()=>model.validate(copied));
console.log(JSON.stringify({passed:true,schema:3,own_source_upper_witnesses:2,source_hashes:Object.keys(v3.proof_inputs_sha256).length,parameter_and_transfer_mutations_rejected:true}));

const v4=JSON.parse(fs.readFileSync(path.join(__dirname,'literal-feasibility-refinement-v4.json')));
assert(model.validate(v4));
for(const [file,hash]of Object.entries(v4.proof_inputs_sha256))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,file))).digest('hex'),hash,file);
assert.equal(v4.rows.length,8);assert.equal(v4.rows.filter(r=>r.upper).length,4);
assert.equal(v4.rows.find(r=>r.pr===4359).core_c_hex,'0x8');
assert.equal(v4.rows.find(r=>r.pr===4359).lower,'2^(2^276540184358-2^69)');
assert.equal(v4.rows.find(r=>r.pr===4470).early_effective_kappa,'1/500');
assert(model.integerLog2(v4.upper_log2log2_integer)>72&&model.integerLog2(v4.upper_log2log2_integer)<73);
for(const pr of [4470,4479,4535,4610]){const b=structuredClone(v4);b.rows.find(r=>r.pr===pr).upper_log2log2_integer=String(BigInt(b.rows.find(r=>r.pr===pr).upper_log2log2_integer)+1n);assert.throws(()=>model.validate(b));}
const invented=structuredClone(v4);invented.rows.find(r=>r.pr===4565).upper=v4.rows[1].upper;assert.throws(()=>model.validate(invented));
console.log(JSON.stringify({passed:true,schema:4,source_specific_lowers:8,source_specific_uppers:4,earlier_p3_and_retuned_branch:true}));
const v5=JSON.parse(fs.readFileSync(path.join(__dirname,'literal-feasibility-refinement-v5.json')));
assert(model.validate(v5));
for(const [file,hash]of Object.entries(v5.proof_inputs_sha256))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,file))).digest('hex'),hash,file);
assert.equal(v5.rows.length,13);assert.equal(v5.rows.filter(r=>r.upper).length,12);
assert.equal(v5.rows.find(r=>r.pr===5413).core_c_hex,'0x95a0');
for(const p of v5.rows){for(const key of ['H','core_c_hex','lower']){const b=structuredClone(v5);b.rows.find(r=>r.pr===p.pr)[key]+='1';assert.throws(()=>model.validate(b));}if(p.upper)for(const key of ['E','Eguard','A','upper_log2log2_integer','Klog_upper']){const b=structuredClone(v5);b.rows.find(r=>r.pr===p.pr)[key]=String(BigInt(p[key])+1n);assert.throws(()=>model.validate(b));}}
for(const rho of ['0.001','1','1000'])assert(model.tariff(v5,rho).rootMultiplier>1);
console.log(JSON.stringify({passed:true,schema:5,source_specific_lowers:13,source_specific_uppers:12,source_hashes:Object.keys(v5.proof_inputs_sha256).length,own_parameter_mutations_rejected:true}));
