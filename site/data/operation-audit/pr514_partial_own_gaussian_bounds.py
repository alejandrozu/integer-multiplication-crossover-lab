"""Own PR514 rank73 supplier with actual120 data slots and16 private centres."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import ast,gzip,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def rd(p):
 b=(R/p).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [enc(v)for v in o]
 return o
binding_file='pr514-selected-native-source-bindings.json';own=rd(binding_file)
ck('exact_own_source_binding',own['schema']=='own-partial-kernel92-source-native-bindings/1'and own['status']=='passed_own_source_and_actual_prior_full_replay_binding'and own['pr']==514 and own['own_head']=='246bfacd4cb4072836ae3147099f548bb728229f'and own['script_sha256']==hs('pr514_selected_native_source_bindings.py')and all(own['checks'].values()))
for group in ['source_sha256','dependency_hashes']:
 for p,h in own[group].items():ck('own_bound_'+p,hs(p)==h)
ck('actual_new_dimensions_not_later_native',(own['native_coordinate_rank'],own['native_data_slots'],own['native_helpers'],own['native_complete_columns'])==(73,120,560,800)and not own['numerical_cutoff_transferred']and not own['expensive_engines_rerun_by_this_binding'])
ck('prior_exact_own13_original_stages',own['full_original_514_stages_actually_previously_executed']==13 and rd(own['full_replay_receipt'])['exit_code']==0)
import finite_selected_program_census_v120 as nativec
program=rd(own['own_local_programs_file']);canonical=rd(own['own_canonical_file']);census=nativec.census(program,v=120,canonical=canonical)
ck('actual_selected_native_semantics',nativec.identity(program)==own['selected_program_semantic_sha256']and sha256(gzip.decompress((R/own['own_canonical_file']).read_bytes())).hexdigest()==own['selected_canonical_payload_sha256']and {o:nativec.identity(es)for o,es in program.items()}==own['selected_orientation_sha256'])
ck('actual120_data_and560_helpers',canonical['v']==120 and canonical['h']==9 and canonical['R']==560 and len(canonical['start'])==len(canonical['final'])==800)
inv=own['own_invoice'];ck('exact_complete_own_invoice',rd(own['own_invoice_file'])==inv and hs(own['own_invoice_file'])==own['own_invoice_sha256']and all(inv['strict_checks'].values()))
for o,c in census.items():
 a=inv['local'][o]
 ck(o+'_fresh_complete_scalar_and_frame_census',c['columns']==800 and c['helpers']==560 and c['scalar_specialization_columns_checked']and c['native_canonical_frame_catalog_checked']and c['native_monotone_frame_checks']==23549 and not c['operator_valued_endpoint_proved_by_this_census'])
 for key,old in [('events','events'),('scalar_macros','macros'),('real_component_primitives','real_component_primitives'),('coefficient_work_primitives','coefficient_work_primitive_count'),('prefix_l1','prefix_l1'),('prefix_bits','prefix_bits')]:ck(o+'_fresh_own_'+key,F(c[key])==F(a[old]))
 ck(o+'_all_own_dirty_inputs_restored_and_private_clear',a['all_exact_columns']==800 and a['all_560_dirty_helper_columns_restored']and a['private_centres_and_coefficient_work_cleared']and c['private_centres_and_coefficient_work_clear'])
P={int(k):v for k,v in own['own_full_profile'].items()};m=73;Wlive=own['productive_live'];physical=own['physical_families'];mass=sum(k*v for k,v in P.items())
ck('own_complete_physical_rank_and_halving',Wlive==7680 and physical==8258 and mass==own['rank_mass']==558144 and m*Wlive-mass==own['rank_surplus']==2496 and max(P)==48 and m*m>2*max(P)**2)
localP=census['forward']['paid_profile'];ck('both_own_native_paid_profiles',localP==census['backward']['paid_profile'])
compiler=64*74**3;adapters=16*(max(c['scalar_macros']for c in census.values())+sum(localP.values())+800+16)+64*73
ck('fresh120_16_adapter_tariff',adapters==inv['local_adapters']==394512 and compiler==inv['compiler'])
ck('fresh_complete_local_primitive_tariff',max(c['real_component_primitives']for c in census.values())+compiler*adapters==inv['local_primitive_bound']<2**48)
fin=inv['finite'];ck('own72_calls512_prefix_and_full_row',inv['complete_invocation_sweeps']==inv['bridge_sweeps']==72 and inv['global_prefix_bits']==206<inv['charged_prefix_bits']==512 and inv['row_prefix_extra']==1024 and fin['physical_row_coefficient']==16467<fin['retained_row_coefficient']==20161)
ck('own_finite_literal_router_height_envelopes',fin['router_bits']<fin['G_exponent']==30000 and fin['literal_bits']<fin['E_exponent']==100000 and fin['required_C0_bits']<fin['C0_exponent']==210000 and fin['halving_integer_inequality']==[73**2,2*48**2])
group=2**(36*36)
for j in range(1,37):group*=2**(2*j)-1
stock=group*physical;streamed=group*mass;Esource=2**100000
ck('fresh_complete_semantic_guard',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
names={'divup','series_log_ratio','logint','expint','powint','moment'};defs=[a for a in ast.parse((R/'pr531_finite_controller_upper.py').read_bytes()).body if isinstance(a,ast.FunctionDef)and a.name in names];ck('exact_pure_interval_engine',{a.name for a in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),'own514_fresh_exact_moment','exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1);fallback=32*m*m*sum(P.values())
kappa=F(own['kappa_record']);native_lower=F(own['complex_lower']);eta_early=F(1,1000);eta_record=(kappa+native_lower)/2
ck('own_selected_record_and_native_endpoint',kappa==F('1391523459591829/1000000000000000000')and native_lower==F('139346249534416215349/100000000000000000000000')and 0<kappa<eta_record<native_lower)
earlyiv=moment(eta_early);recordiv=moment(eta_record)
ck('fresh_early_taxed_moment',earlyiv[1]<F(1695000,1696009)<1)
ck('fresh_own_record_taxed_moment',recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
for tag,iv in [('early',earlyiv),('record',recordiv)]:
 reciprocal=ceil(1/(1-iv[1]));coefficient=2**32*m**4*(Esource+stock+streamed+1)**2*(1+reciprocal)**2*20162**2
 ck(tag+'_complete_own_allsize_coefficient',reciprocal<2**100 and coefficient<2**220000)
component=rd('gaussian-only-parameter-ledger.json');ck('closed_reduced_arithmetic_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed'])
for p,h in component['dependency_hashes'].items():ck('arithmetic_component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('own514_only_reduced_Gaussian_arithmetic',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
early=G.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001);record=G.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)
for tag,o in [('early',early),('record',record)]:
 ck(tag+'_fresh_all32_ledger_runtime_guards',len(o['checks'])==32 and all(o['checks'].values()))
 ck(tag+'_no_BIT_parameter_or_operation',not o['ordinary_BIT_supplier_consumed']and'bit_saving'not in o['new_outer_parameters'])
 ck(tag+'_own_input_width_mapping',int(o['upper_log2log2_integer'])==int(o['A'])*int(o['E'])-8)
contracts=own['retained_contracts']+[
 'The dimension-independent rank73 finite-interface proof in pr514-partial-own-gaussian-bounds.md is used with the actual120-data,560-helper,16-private-centre ledger. The later112/504/8 native theorem is not imported. Every own monomial/Clifford map is bounded73-axis binary affine/even-quadratic Z4 with exactly recorded absolute phase and full owed normalization/copy/clear work.',
 'The completed exact Gaussian endpoint has semantic norm1; this is a retained operator interface, not a new field inferred from scalar replay or a claim that transient prefix gains are1.',
 'Concrete normalized Gaussian accretivity, finite LDU/narrow row-gap/cyclic-border and fine-prime/rounding/recovery interfaces; repaired reference correctness and finite-kernel halting. No arbitrary-scale accretive theorem is used.'
]
deps=['pr514-partial-own-gaussian-bounds.md',binding_file,'pr514_selected_native_source_bindings.py','finite_selected_program_census_v120.py','finite_selected_program_census.py','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
dep={p:hs(p)for p in deps};dep.update(own['dependency_hashes'])
base=dict(pr=514,own_head=own['own_head'],source_head=own['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(kappa),native_coordinate_rank=73,native_data_slots=120,native_dirty_helpers=560,native_complete_columns=800,native_private_centres=16,not_uniform_2_to_H=True,later112_native_substituted=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,native_engine_expensively_rerun_here=False,own_original13stages_previously_executed=True,scalar_specialization_freshly_checked=True,universal_operator_endpoint_proved_by_new_scalar_census=False,source_sha256=own['source_sha256'],dependency_hashes=dep,script_sha256=hs(Path(__file__).name),retained_contracts=contracts,checks_passed=len(checks),checks=checks)
rf='pr514-partial-own-gaussian-record-upper.json';ro=dict(base,**record,schema='own-partial-kernel92-Gaussian-record-upper/1');(R/rf).write_text(json.dumps(enc(ro),indent=2)+'\n',encoding='utf8')
ef='pr514-partial-own-gaussian-early-upper.json';eo=dict(base,**early,schema='own-partial-kernel92-Gaussian-early-upper/1',early_effective_kappa='1/5000',record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='New counted direct Gaussian/Fermat realization of the actual own120-data partial-kernel92 source at its own record exponent; no original optional BIT circuit replay.',piecewise_description='Identical repaired reference below early sufficient gate, then counted early source-core branch and separately quantified own-record branch. These switches are not crossover lower bounds.');(R/ef).write_text(json.dumps(enc(eo),indent=2)+'\n',encoding='utf8')
nf='pr514-partial-own-gaussian-native.json';no=dict(base,schema='own-partial-kernel92-Gaussian-native-parameters/1',source_binding=own,own_invoice=inv,fresh_actual120_native_census=census,own_full_profile=P,coarse_moment_interval=[str(v)for v in earlyiv],native_record_saving=str(eta_record),record_moment_interval=[str(v)for v in recordiv],inherited_fallback_tax_denominator='10000000000000000',inherited_fallback_tax_removed=False);(R/nf).write_text(json.dumps(enc(no),indent=2)+'\n',encoding='utf8')
out=dict(schema='own-partial-kernel92-Gaussian-cost-audit/1',pr=514,own_head=own['own_head'],status='closed_conditional_case'if REVIEW_CLOSED else'pending_independent_AI_review',native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'pr514-partial-own-gaussian-bounds.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf8')
print('PASS',len(checks),'own514 actual120/16 native and full-Gaussian cost checks')
