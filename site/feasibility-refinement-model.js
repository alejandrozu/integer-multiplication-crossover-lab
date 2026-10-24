(function(root){
  'use strict';
  function integerLog2(s){const n=BigInt(s);if(n<=0n)throw Error('Nonpositive logarithm');const b=n.toString(2);return b.length<53?Math.log2(Number(n)):b.length-53+Math.log2(Number(BigInt('0b'+b.slice(0,53))))}
  function validate(c){
    if(c?.schema==='literal-construction-feasibility-refinement/5')return validateV5(c);
    if(!['literal-construction-feasibility-refinement/1','literal-construction-feasibility-refinement/2','literal-construction-feasibility-refinement/3','literal-construction-feasibility-refinement/4'].includes(c?.schema)||c.status!=='closed_conditional_refined_literal_family_bounds'||c.model!=='xag-straightline-v1')throw Error('Missing refined feasibility proof');
    if(c.baseline_extension_id!=='gmp-630-native-skylake-unbounded-exact-constants-v2'||c.reference_upper_per_type!=='2^(2^72+3)*(n+1)^8'||c.root_degree!==8)throw Error('Unexpected comparator or tariff degree');
    if(c.exact_crossovers_computed!==0||c.interval_is_narrow_or_realistic!==false||c.API_limit_used!==false||c.chosen_switch_used_as_lower!==false||c.precision_proof_gate_used_as_necessary_lower!==false)throw Error('Unsupported crossover claim');
    if(!c.retained_candidate_native_analytic_recovery_contracts||!c.retained_GMP_finite_native_correctness_halting_contracts)throw Error('Missing conditional contracts');
    const H=64215200000000n,m=145n**1024n,eq=H+1n+m*H*(H+33010n),et=H+4n+33010n*m*H*(H/4497n+3n);
    const guard=22n+66020n+BigInt((H/4497n+1n).toString(2).length)+BigInt((m*H+1n).toString(2).length);
    const v4=c.schema.endsWith('/4'),modern=!c.schema.endsWith('/1'),Q=v4?10000n:1400000000n,A=v4?10001n:1400000001n,E=modern?Q*(H+1n)+2n*H+66020n+guard+179200000000n+1048576n+1000n:eq+et+1400000000n*(H+1n)+1729n**12n+179200000000n+100n*H+1000n;
    if(c.E!==String(E)||c.upper_log2log2_integer!==String(A*E-8n))throw Error('Upper exponent does not reproduce');
    const ids=v4?[4359,4470,4479,4483,4533,4535,4565,4610]:[4470,4479,4483,4533,4535,4565,4610];
    if(c.rows?.length!==ids.length)throw Error('Incomplete refined construction set');
    for(const p of c.rows){
      if(!ids.includes(p.pr)||p.all_implementations_of_PR!==false||p.actual_first_crossing_known!==false||p.full_upper_transferred_from_other_PR!==false)throw Error('Invalid construction scope');
      const v=BigInt(p.tensor_power_used_for_lower),count=p.pr===4359?8n:630412n*(64620n**v-10928n**v)/53692n,j=count.toString(2).length-1,q=Math.floor((j-3)/8);
      if(BigInt(p.core_c_hex)!==count||p.j!==j||p.q!==q||p.lower!==`2^(2^${BigInt(p.H)-3n}-2^69${q===0?'':`+${q}`})`)throw Error('Lower endpoint does not reproduce');
      const expectedUpper=modern?`2^(2^${c.upper_log2log2_integer})`:'2^(2^(1400000001*E-8))';
      if(p.pr===4470){if(p.upper!==expectedUpper||p.upper_log2log2_integer!==c.upper_log2log2_integer)throw Error('Unproved upper transfer');if(v4&&p.early_effective_kappa!=='1/500')throw Error('Missing retuned exponent scope')}
      else if(p.pr===4610&&(c.schema.endsWith('/3')||v4)){
        const h=38569300000000000n,g=22n+66020n+BigInt((h/4497n+1n).toString(2).length)+BigInt((m*h+1n).toString(2).length),e=(v4?10000n:700000000000n)*(h+1n)+2n*h+66020n+g+179200000000n+1048576n+1000n,a=v4?10001n:2800000000001n,P=a*e-8n;
        if(p.H!==String(h)||p.E!==String(e)||p.Eguard!==String(g)||p.A!==String(a)||p.upper_log2log2_integer!==String(P)||p.upper!==`2^(2^${P})`||p.upper_source_certificate!==(v4?'pr-fixed-core-crossover-retuned-extensions.json':'pr4610-fermat-helper-upper.json')||(v4&&p.early_effective_kappa!=='1/500'))throw Error('PR4610 own upper does not reproduce');
      }else if(v4&&[4479,4535].includes(p.pr)){
        const compact=p.pr===4479,h=compact?558100005581n:1000000000000n,k=compact?43976n:66020n,g=compact?22n+k+BigInt((h/2995n+1n).toString(2).length)+BigInt((145n**682n*h+1n).toString(2).length):23n+k+BigInt((200000000000n+1n).toString(2).length)+h,e=10000n*(h+1n)+2n*h+k+g+179200000000n+1048576n+1000n,a=10001n,P=a*e-8n;
        if(p.H!==String(h)||p.E!==String(e)||p.Eguard!==String(g)||p.A!==String(a)||p.upper_log2log2_integer!==String(P)||p.upper!==`2^(2^${P})`||p.upper_source_certificate!=='pr-fixed-core-crossover-retuned-extensions.json'||p.early_effective_kappa!=='1/500')throw Error('Own-source upper does not reproduce');
      }else if(p.upper!==null)throw Error('Unproved upper transfer');
    }
    if(new Set(c.rows.map(p=>p.pr)).size!==ids.length)throw Error('Duplicate construction');
    return true;
  }
  function validateV5(c){
    if(c.status!=='closed_conditional_refined_literal_family_bounds'||c.model!=='xag-straightline-v1'||c.baseline_extension_id!=='gmp-630-native-skylake-unbounded-exact-constants-v2'||c.reference_upper_per_type!=='2^(2^72+3)*(n+1)^8'||c.root_degree!==8)throw Error('Unexpected v5 model or comparator');
    if(c.exact_crossovers_computed!==0||c.interval_is_narrow_or_realistic!==false||c.API_limit_used!==false||c.chosen_switch_used_as_lower!==false||c.precision_proof_gate_used_as_necessary_lower!==false||!c.retained_candidate_native_analytic_recovery_contracts||!c.retained_GMP_finite_native_correctness_halting_contracts)throw Error('Unsupported v5 scope');
    const heights={4359:'276540184361',4416:'16201843136005340321',4440:'10418370291022217',4441:'165315500000000',4447:'64215200000000',4470:'64215200000000',4479:'558100005581',4483:'2800000000',4533:'1587000000',4535:'1000000000000',4565:'11825387808',4610:'38569300000000000',5413:'38569300000000000'};
    const budgets={4359:[128,'362','pr4359-crossover-retuned-upper.json'],4416:[192439,'428188','p7-p17-record-crossover-bounds.json'],4440:[33277,'74103','p7-p17-record-crossover-bounds.json'],4441:[33292,'74121','p7-p17-record-crossover-bounds.json'],4447:[33292,'74118','p7-p17-record-crossover-bounds.json'],4470:[33010,'73475','pr4470-crossover-retuned-upper.json'],4479:[21988,'48962','pr-fixed-core-crossover-retuned-extensions.json'],4483:[33010,'2800066076','adaptive-p16-crossover-bounds.json'],4533:[33010,'1587066075','adaptive-p16-crossover-bounds.json'],4535:[33010,'1000000066081','pr-fixed-core-crossover-retuned-extensions.json'],4610:[33010,'73493','pr-fixed-core-crossover-retuned-extensions.json'],5413:[1048576,'2104625','pr5413-crossover-retuned-upper.json']};
    if(c.rows?.length!==13||new Set(c.rows.map(p=>p.pr)).size!==13)throw Error('Incomplete v5 set');
    for(const p of c.rows){
      if(p.H!==heights[p.pr]||p.all_implementations_of_PR!==false||p.actual_first_crossing_known!==false||p.full_upper_transferred_from_other_PR!==false)throw Error('Invalid own-source scope');
      const v=BigInt(p.tensor_power_used_for_lower),small=[4359,4416,4440,4441,4447].includes(p.pr),count=small?8n:p.pr===5413?38304n:630412n*(64620n**v-10928n**v)/53692n,j=count.toString(2).length-1,q=Math.floor((j-3)/8),H=BigInt(p.H);
      if(BigInt(p.core_c_hex)!==count||p.j!==j||p.q!==q||p.lower!==`2^(2^${H-3n}-2^69${q===0?'':`+${q}`})`)throw Error('V5 lower does not reproduce');
      if(p.pr===4565){if(p.upper!==null)throw Error('Unproved PR4565 upper');continue}
      const own=budgets[p.pr];if(String(p.Klog_upper)!==String(own[0])||p.Eguard!==own[1]||p.upper_source_certificate!==own[2])throw Error('Unauthenticated own-source budget');
      const K=BigInt(p.Klog_upper),G=BigInt(p.Eguard),E=10000n*(H+1n)+2n*H+2n*K+G+179200000000n+1048576n+1000n,P=10001n*E-8n;
      if(K<=0n||G<=0n||p.E!==String(E)||p.A!=='10001'||p.upper_log2log2_integer!==String(P)||p.upper!==`2^(2^${P})`||p.early_effective_kappa!=='1/500'||!p.upper_source_certificate||!p.native_source_certificate||!p.backup_record_upper_certificate||!p.backup_record_upper)throw Error('V5 own upper does not reproduce');
    }
    const main=c.rows.find(p=>p.pr===4470);if(c.E!==main.E||c.upper_log2log2_integer!==main.upper_log2log2_integer)throw Error('V5 pilot mismatch');return true;
  }
  function tariff(c,rho){validate(c);const r=OperationModel.tariff(String(rho)),a=BigInt(r.numerator),b=BigInt(r.denominator);let num=b+3n*a,den=b+a;const gcd=(x,y)=>{while(y){const z=x%y;x=y;y=z}return x},g=gcd(num,den);num/=g;den/=g;return{numerator:String(num),denominator:String(den),rootMultiplier:(Number(num)/Number(den))**(1/8)}}
  const api={validate,tariff,integerLog2};if(typeof module==='object'&&module.exports)module.exports=api;root.FeasibilityRefinementModel=api;
})(typeof globalThis==='object'?globalThis:this);
