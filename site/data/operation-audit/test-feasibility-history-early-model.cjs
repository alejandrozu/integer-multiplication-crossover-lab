'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),model=require(path.join(root,'site/dist/feasibility-history-early-model.js'));
const d=JSON.parse(fs.readFileSync(path.join(root,'site/dist/data/feasibility-history-pr147.json'))),e=d.early_finite_extension;
assert(model.validate(d));assert.equal(d.entries.length,595);assert.equal(model.rows(d,'bounded').length,14);
assert.equal(d.coverage.entries_with_meaningful_lower,13);assert.equal(d.coverage.entries_with_conditional_upper,13);assert.equal(d.coverage.entries_with_two_sided_bounds,12);
const p=d.entries.find(p=>p.pr===147);assert.equal(p.meaningful_lower_bound,null);assert.equal(p.actual_crossover,null);assert.equal(p.conditional_upper.input_bits,'2^(2^21992431578775544)');assert.equal(e.original_record_tail_quantified,false);
const legacy=JSON.parse(fs.readFileSync(path.join(root,'site/dist/data/feasibility-history-v5.json')));for(const p of d.entries){const old=legacy.entries.find(x=>x.pr===p.pr);for(const key of ['accepted_at','created_at','title','kappa_fraction','author'])assert.equal(p[key],old[key])}
assert(model.ordinate(p)>54&&model.ordinate(p)<55);
for(const axis of ['date','kappa'])assert.deepEqual(model.bestUpperSteps(d.entries,axis).map(p=>p.pr),[147]);
assert.deepEqual(model.strictFamilyImprovements(d).map(p=>[p.earlier,p.later]),[[4416,4483],[4416,4533]]);
const cert=fs.readFileSync(path.join(__dirname,e.certificate_file));assert.equal(crypto.createHash('sha256').update(cert).digest('hex'),e.certificate_sha256);assert.equal(JSON.parse(cert).status,'closed_conditional_upper_only');
for(const key of ['E','A','P']){const b=structuredClone(d);b.early_finite_extension[key]=String(BigInt(e[key])+1n);assert.throws(()=>model.validate(b))}
const b=structuredClone(d);b.early_finite_extension.original_record_tail_quantified=true;assert.throws(()=>model.validate(b));
const wrong=structuredClone(d);wrong.entries.find(p=>p.pr===147).conditional_upper.log2log2_input_bits='2';assert.throws(()=>model.validate(wrong));
console.log(JSON.stringify({passed:true,entries:595,lower:13,upper:13,intervals:12,upper_only:147,best_audited_upper:147,unchanged_strict_pairs:2,original_tail_quantified:false}));
