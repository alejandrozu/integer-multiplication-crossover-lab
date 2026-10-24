'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const model=require('../site/dist/feasibility-history-model.js');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'../site/dist/data/feasibility-history-v5.json')));
const cert=JSON.parse(fs.readFileSync(path.join(__dirname,'literal-feasibility-refinement-v5.json')));
assert.deepEqual(data.refinement_certificate,cert);
assert(model.validate(data));
assert.equal(data.coverage.entries_with_conditional_upper,12);
assert.equal(data.coverage.entries_with_meaningful_lower,13);
const own=new Map(cert.rows.map(p=>[p.pr,p]));
for(const p of data.entries){
  assert.equal(p.actual_crossover,null);
  assert.equal(p.acceptance_basis,'github_merged_at');
  const a=own.get(p.pr);
  if(!a){assert.equal(p.meaningful_lower_bound,null);assert.equal(p.conditional_upper,null);continue;}
  assert.equal(p.kappa_fraction,a.kappa);
  assert.equal(p.meaningful_lower_bound.input_bits,a.lower);
  if(a.upper){assert.equal(p.conditional_upper.input_bits,a.upper);assert.equal(p.conditional_upper.plot_triple_log.exact_log2log2_integer,a.upper_log2log2_integer);}
  else assert.equal(p.conditional_upper,null);
}
// Independent exact selection: no floating point is used for the proof pair.
const expected=[];
for(const e of data.entries){
  const a=own.get(e.pr);if(!a||BigInt(a.H)<=73n||a.q<0)continue;
  for(const l of data.entries){
    const b=own.get(l.pr);if(!b?.upper||Date.parse(l.accepted_at)<=Date.parse(e.accepted_at))continue;
    if(BigInt(b.upper_log2log2_integer)<=BigInt(a.H)-4n)expected.push([e.pr,l.pr]);
  }
}
assert.deepEqual(model.strictFamilyImprovements(data).map(p=>[p.earlier,p.later]),expected);
assert.deepEqual(expected,[[4416,4483],[4416,4533]]);
for(const axis of ['date','kappa']){
  const steps=model.bestUpperSteps(data.entries,axis);
  assert.equal(steps.at(-1).pr,4533);
  for(let i=1;i<steps.length;i++){assert(steps[i].x>steps[i-1].x);assert(BigInt(steps[i].P)<BigInt(steps[i-1].P));}
  assert.deepEqual(model.bestUpperSteps(data.entries.slice().reverse(),axis),steps);
}
assert.deepEqual(model.bestUpperSteps(data.entries,'date').map(p=>p.pr),[4359,4483,4533]);
assert.deepEqual(model.bestUpperSteps(data.entries,'kappa').map(p=>p.pr),[4359,4533]);
const tie=structuredClone(data);
tie.entries.find(p=>p.pr===4533).accepted_at=tie.entries.find(p=>p.pr===4416).accepted_at;
assert(!model.strictFamilyImprovements(tie).some(p=>p.later===4533));
const bad=structuredClone(data);bad.entries[0].actual_crossover='2';
assert.throws(()=>model.validate(bad),/Unverified crossover/);
// This offline test checks the bundled source-bound chart and its exact
// ordering. The workspace's broader metadata test independently reconciles
// every GitHub date/title against the frozen4911-PR inventory and delta.
console.log(JSON.stringify({passed:true,offline:true,entries:data.entries.length,source_bound_lowers:13,conditional_uppers:12,strict_family_pairs:expected,metadata_inventory_rescan:false}));
