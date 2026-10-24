'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p)));
const model=require(path.join(root,'site/dist/feasibility-history-early-model.js'));
const data=read('site/dist/data/feasibility-history.json'),before=read('site/dist/data/feasibility-history-pr147.json');
assert(model.validate(data));
assert.equal(data.entries.length,before.entries.length);
const adapters=model.extensions(data),ids=new Set(adapters.map(e=>e.pr));
assert(ids.has(147));assert.equal(ids.size,adapters.length);
for(const pr of ids)assert(model.rows(data,'leaders').some(p=>p.pr===pr));
const sha=file=>crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,file))).digest('hex');
for(const e of adapters){
  assert.equal(sha(e.certificate_file),e.certificate_sha256);
  assert(e.peer_review_file);assert.equal(sha(e.peer_review_file),e.peer_review_sha256);
  const peer=read('operation-audit/'+e.peer_review_file);
  assert.equal(peer.reviewed_sha256[e.certificate_file],e.certificate_sha256);
  const cert=read('operation-audit/'+e.certificate_file);
  assert(cert.status.startsWith('closed_conditional'));
  assert.equal(cert.inputUpper,`2^(2^${e.P})`);
  const p=data.entries.find(p=>p.pr===e.pr);
  assert.equal(p.meaningful_lower_bound,null);assert.equal(p.actual_crossover,null);
  assert(model.ordinate(p)>54&&model.ordinate(p)<55);
  assert.equal(p.conditional_upper.source,'data/operation-audit/'+e.certificate_file);
  if(e.pr===147){assert(e.correction_notice);assert.equal(e.supersedes_adapter_file,'pr147-crossover-plot-adapter.json');assert.equal(sha(e.supersedes_adapter_file),e.supersedes_adapter_sha256)}
  if(e.original_record_tail_quantified){
    assert.equal(sha(e.record_certificate_file),e.record_certificate_sha256);
    const tail=read('operation-audit/'+e.record_certificate_file);
    assert(tail.status.startsWith('closed_conditional'));
    assert(BigInt(e.record_P)>BigInt(e.P));assert.equal(tail.inputUpper,e.record_upper);
  }
  for(const key of ['E','A','P']){
    const altered=structuredClone(data);altered.finite_family_extensions.find(x=>x.pr===e.pr)[key]=String(BigInt(e[key])+1n);
    assert.throws(()=>model.validate(altered));
  }
  const falseLower=structuredClone(data);falseLower.entries.find(x=>x.pr===e.pr).meaningful_lower_bound={input_bits:'2'};
  assert.throws(()=>model.validate(falseLower));
}
for(const p of data.entries){
  const old=before.entries.find(x=>x.pr===p.pr);assert(old);
  for(const key of ['accepted_at','created_at','title','kappa_fraction','author','historical_status'])assert.deepEqual(p[key],old[key]);
  if(!ids.has(p.pr)){assert.deepEqual(p.conditional_upper,old.conditional_upper);assert.deepEqual(p.meaningful_lower_bound,old.meaningful_lower_bound)}
}
const low=data.entries.filter(p=>p.meaningful_lower_bound).length,up=data.entries.filter(p=>p.conditional_upper).length;
const intervals=data.entries.filter(p=>p.meaningful_lower_bound&&p.conditional_upper).length;
assert.equal(data.coverage.entries_with_meaningful_lower,low);assert.equal(data.coverage.entries_with_conditional_upper,up);
assert.equal(data.coverage.entries_with_two_sided_bounds,intervals);assert.equal(intervals,12);assert.equal(low,13);
assert.equal(model.rows(data,'bounded').length,13+adapters.length);
for(const axis of ['date','kappa'])assert.deepEqual(model.bestUpperSteps(data.entries,axis).map(x=>x.pr),[147]);
assert.deepEqual(model.strictFamilyImprovements(data).map(p=>[p.earlier,p.later]),[[4416,4483],[4416,4533]]);
assert.equal(data.entries.filter(p=>p.actual_crossover!==null).length,0);
console.log(JSON.stringify({passed:true,entries:data.entries.length,finite_upper_only:[...ids],lower:low,upper:up,intervals,actual_crossings:0,old_metadata_and_bounds_preserved:true}));
