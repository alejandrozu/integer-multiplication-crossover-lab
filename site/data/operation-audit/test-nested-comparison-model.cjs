/* Independent exact-fraction/scientific-contract audit of the site model.
 * The mathematical plotted ceiling is proved without materializing M_N:
 * log2p >=8+t(A*m-8), hence log_M p>=t(A-1) when m>8,t>=1,
 * because the difference numerator is t(m-8)+8>0.
 */
'use strict';
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');
const here=__dirname,dist=path.resolve(here,'../site/dist');
const context=vm.createContext({console});
for(const f of ['operation-model.js','full-comparison-model.js','nested-comparison-model.js'])
  vm.runInContext(fs.readFileSync(path.join(dist,f),'utf8'),context,{filename:f});
const model=context.NestedComparisonModel;
const audit=fs.existsSync(path.join(dist,'data/operation-audit'))?path.join(dist,'data/operation-audit'):here;
const c=JSON.parse(fs.readFileSync(path.join(audit,'pr4470-nested-comparison.json'),'utf8'));
let checks=0;
function ck(v,msg){assert(v,msg);checks++;}
function rejects(fn,msg){assert.throws(fn,undefined,msg);checks++;}
ck(model.validate(c)===true,'Actual tightened certificate accepted');
for(const [f,expected] of Object.entries(c.hashes)){
  const raw=fs.readFileSync(path.join(audit,f));
  ck(crypto.createHash('sha256').update(raw).digest('hex')===expected,'Published proof hash matches '+f);
}
for(const [key,value] of [
  ['model','old-model'],['H','128'],['N','2^128'],['M_N','2^128'],['A','1000000000000000'],['kappa','1/3'],
  ['status','pending'],['linear_guard_review_closed',false],
  ['native_contracts_retained',false],['hw_runtime_crossover',true],
  ['coefficient_each_gate_type',100],['inputUpper','2^(Mbar^1000000000000000)'],
  ['log2log2U','old-cutoff'],['rigorous_reference_comparisons',['hvh']]
])rejects(()=>model.validate({...c,[key]:value}),'Reject mismatched '+key);

for(const rho of ['0.000000000000000000000000000001','0.001','0.1','1','10','1000','1000000000000000000000000000000']){
  for(const b of ['hvh','gmp']){
    const r=model.comparison(c,b,rho),num=BigInt(r.price.numerator),den=BigInt(r.price.denominator);
    ck(num>0n&&den>0n&&num<512n*den,'Exact price factor lies in(0,512)');
    ck(r.conditional===true&&!r.exactFirstCrossing&&!r.hardwareRuntime,'Scientific scope flags');
    ck(r.inputUpper==='2^(M_N^1400000001/256)','New cutoff, not frozen old cutoff');
    ck(Number.isFinite(r.price.log2),'Finite displayed logprice');
  }
}
for(const rho of ['0','-1','NaN','Infinity','1e3','abc',''])
  rejects(()=>model.comparison(c,'hvh',rho),'Invalid tariff '+rho);
rejects(()=>model.comparison(c,'unknown','1'),'Unknown reference');
for(const t of [0,-1,0.999,NaN,undefined,Infinity,'1'])rejects(()=>model.plotCeiling(t),'Outside certified input domain');

for(const m of [9n,128n,33010n,1000000n])for(const [tn,td] of [[1n,1n],[11n,10n],[6n,5n],[1000n,1n]]){
  ck(tn*(m-8n)+8n*td>0n,'Exact transformed-input exponent inequality');
}
for(const [tn,td] of [[1n,1n],[11n,10n],[6n,5n]]){
  const num=20000000n*td-60403n*1400000000n*tn,den=20000000n*td;
  const expected=Number(num)/Number(den),actual=model.plotCeiling(Number(tn)/Number(td));
  ck(Math.abs(actual-expected)<1e-8,'Rounded graph agrees with exact rational ceiling');
  ck(actual<0,'Graph certifies strict comparison throughout displayed valid tail');
}
const result={status:'PASS',checks,scope:'Actual new certificate, exact tariff factors, input-coordinate inequality and plot arithmetic. Not a proof of retained native hypotheses.'};
fs.writeFileSync(path.join(here,'pr4470-nested-model-audit.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
