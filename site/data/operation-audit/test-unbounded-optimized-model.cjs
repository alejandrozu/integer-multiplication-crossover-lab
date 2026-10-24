/* Test the published proof contract, exact tariff arithmetic and scope. */
'use strict';
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');
const here=__dirname,dist=path.resolve(here,'../site/dist');
const audit=fs.existsSync(path.join(dist,'data/operation-audit'))?path.join(dist,'data/operation-audit'):here;
const context=vm.createContext({console});
for(const f of ['operation-model.js','unbounded-optimized-model.js'])vm.runInContext(fs.readFileSync(path.join(dist,f),'utf8'),context,{filename:f});
const m=context.UnboundedOptimizedModel,c=JSON.parse(fs.readFileSync(path.join(audit,'pr4470-unbounded-optimized-comparison.json'),'utf8'));
let checks=0;
function ck(v,s){assert(v,s);checks++}
function bad(fn,s){assert.throws(fn,undefined,s);checks++}
const sha=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
ck(m.validate(c),'Accept actual unlimited-input certificate');
for(const [f,h] of Object.entries(c.source_sha256))ck(sha(path.join(audit,'optimized-gmp-unbounded-source',f))===h,'Native source binding '+f);
for(const [f,h] of Object.entries(c.bound_inputs_sha256))ck(sha(path.join(audit,f))===h,'Candidate/proof binding '+f);
for(const [k,v] of [['status','pending'],['model','wall-clock'],['A','1'],['kappa','1/3'],['H','128'],['N','2^128'],['M_N','2^128'],['inputLowerGeneral','1000000'],['inputUpper','unknown'],['log2log2U','unknown'],['hybridExactL','2'],['natural_first_crossing_known',true],['natural_eventual_threshold_known',true],['lowerAND',1],['lowerXOR',1],['n_min','2^2'],['coefficient_each_gate_type',100],['native_contracts_retained',false],['linear_guard_review_closed',false],['hw_runtime_crossover',true]])bad(()=>m.validate({...c,[k]:v}),'Reject altered '+k);
bad(()=>m.validate({...c,unbounded_FFT_termination_closed:false}),'Reject an unclosed unbounded recurrence');
bad(()=>m.validate({...c,baseline_unbounded_extension:{...c.baseline_unbounded_extension,full_tuned_MUL_table_entries:0}}),'Reject a different source profile');
for(const r of ['0.000000000000000000000000001','0.001','0.1','1','10','1000','1000000000000000000000000000']){
  const p=m.price(c,r),a=BigInt(p.numerator),b=BigInt(p.denominator);
  ck(a<256n*b&&3n*a>512n*b,'Exact price interval');
  ck(Number.isFinite(p.log2),'Displayed price is finite');
}
const one=m.price(c,'1');ck(one.numerator==='1024'&&one.denominator==='5','Default optimized factor');
for(const r of ['0','-1','NaN','Infinity','1e3','abc',''])bad(()=>m.price(c,r),'Reject invalid tariff');
for(const t of [0,.999,-1,NaN,Infinity,undefined,'1'])bad(()=>m.plotCeiling(t),'Reject unresolved plot domain');
for(const [a,b] of [[1n,1n],[11n,10n],[6n,5n]]){
  const exact=Number(20000000n*b-60403n*1400000000n*a)/Number(20000000n*b);
  ck(Math.abs(m.plotCeiling(Number(a)/Number(b))-exact)<1e-8,'Plot agrees with exact rational ceiling');
  ck(exact<0,'Strict comparison throughout the plotted valid tail');
}
const result={status:'PASS',checks,scope:'Source/proof hashes, exact circuit tariffs, invalid certificates and first-crossing scope. Not a physical runtime theorem.'};
fs.writeFileSync(path.join(here,'pr4470-unbounded-model-audit.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
