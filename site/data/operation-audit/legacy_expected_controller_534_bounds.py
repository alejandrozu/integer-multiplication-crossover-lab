"""Own pre-SPEC534 direct Gaussian finite bound; no retained prior invoice."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import ast,gzip,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
checks={}
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def rd(p):
    b=(R/p).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return{str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(tuple,list)):return[enc(v)for v in o]
    return o
inp=rd('legacy-expected-controller-534-inputs.json');S='legacy-expected-controller-source/534/';D='legacy-expected-controller-534-derived/'
ck('actual_own_pre_SPEC_component',inp['pr']==534 and inp['own_head']=='3e148183cbf124fcaba4d3c2d609133ff2edd518'and inp['checks_passed']==87 and all(inp['checks'].values())and inp['script_sha256']==hs('legacy_expected_controller_534_inputs.py')and inp['source_selection_by_literal_verifier']and not inp['complete_historical_global_verifier_PASS_claimed']and not inp['original_phase_engines_freshly_replayed'])
primary=dict(inp['source_sha256']);dep=dict(inp['dependency_hashes'])
for p,h in primary.items():ck('own_source_'+p,hs(p)==h)
for p,h in dep.items():ck('source_component_'+p,hs(p)==h)
for a in inp['outputs']:ck('own_fresh_output_'+a['file'],hs(a['file'])==a['sha256']);dep[a['file']]=a['sha256']
M=rd(S+'MANIFEST.json')['sha256'];sm=rd(S+'source-manifest.json');e=rd(S+'EXPECTED.json');v=(R/S/'verify_fast.py').read_text()
ck('literal_own_selector_not_kappa_equivalence',sm['own_head']==inp['own_head']and sm['MANIFEST_sha256']==hs(S+'MANIFEST.json')==hs(sm['MANIFEST_primary']['file'])and "local = root/'evidence/local'"in v and "root/'inputs/OWNERS.json.gz'"in v and "root/'inputs/OWNER-PLAN.json'"in v and "expected = read(root/'EXPECTED.json')"in v)
primary[sm['MANIFEST_primary']['file']]=sm['MANIFEST_sha256']
for a in sm['files']:ck('own_manifest_primary_'+a['relative'],a['own_head']==inp['own_head']and inp['own_head']in a['primary_url']and a['exact_own_manifest_payload']and hs(a['file'])==a['sha256']==M[a['relative']])
own=inp['own_owner_receipt'];inv=inp['own_invoice'];control=inp['own_controller_receipt'];nc=rd(D+'fresh-scalar-only-census.json');template=rd(D+'hosted/GLOBAL-TEMPLATE.json.gz');parent=rd(D+'base/split-centres/GLOBAL-TEMPLATE.json.gz');can=rd(inp['selected_canonical_file'])
ck('entire_selected_complete_template',template==rd(S+'evidence/hosted/GLOBAL-TEMPLATE.json.gz')and own['template_sha256']==inv['template_sha256']==e['global_template_content_sha256'])
ck('complete_actual_owner_and_seven_negative_controls',control['complete_invocations']==72 and len(control['mutations_rejected'])==7 and control['mutation_controls_run']and own['hosted_residuals']==36288 and own['actual_helper_owner_charts']==36288 and own['all_live_owners_per_call_distinct']and control['one_owner_per_complete_invocation'])
ck('fresh_own_invoice_not_prior_allowance',inv['retained_prior_overcharge']is None and inp['retained_previous_invoice']is None and all(inv['strict_checks'].values())and "if retained_invoice is not None:"in(R/S/'code/invoice_final.py').read_text())
ck('own_native_local_geometry',can['v']==112 and can['h']==9 and can['R']==504 and len(can['centers'])==8)
for orient,z in nc.items():
    q=inv['local'][orient]
    ck(orient+'_actual_scalar_only_fullcolumns',z['scalar_specialization_columns_checked']and z['native_canonical_frame_catalog_checked']and not z['operator_valued_endpoint_proved_by_this_census']and z['all_scalar_coefficients_dyadic']and z['private_centres_and_coefficient_work_clear']and z['columns']==728 and z['helpers']==504)
    ck(orient+'_fresh_actual_primitives_prefix',z['real_component_primitives']==q['real_component_primitives']and z['scalar_macros']==q['macros']and z['coefficient_work_primitives']==q['coefficient_work_primitive_count']and z['prefix_bits']==q['prefix_bits']and z['prefix_l1']==q['prefix_l1']and z['pre_wrappers']==z['post_wrappers']==152 and z['paid_profile']==e['local_profile'])
ck('actual_helper_initial_final_widths',[can['h']-len(can['frames'][f])for f in can['start'][224:]]==nc['forward']['widths']==nc['backward']['widths']and sum(bool(f)for f in can['start'][224:])==inv['entering_helpers']==152)
m=73;Wlive=own['live'];P={int(k):v for k,v in own['paid_profile'].items()};mass=sum(k*v for k,v in P.items())
ck('own_complete_rank_profile_surplus_halving',own['paid_profile']==e['global_profile']and mass==own['rank_mass']==e['rank_mass']and m*Wlive-mass==own['deficit']==e['deficit']==2560 and m*m>2*max(P)**2 and max(P)<m)
ck('own_physical_stock',Wlive==inv['live']==e['live']==7168 and own['physical']==inv['physical']==e['physical']==Wlive+504+8+2==7682)
compiler=64*(m+1)**3;children=sum(int(x)for x in nc['forward']['paid_profile'].values());macros=max(z['scalar_macros']for z in nc.values());adapters=16*(macros+children+728+8)+64*m
ck('fresh_full_native_adapter_allowance',compiler==inv['compiler']and adapters==inv['local_adapters']and max(z['real_component_primitives']for z in nc.values())+adapters*compiler==inv['local_primitive_bound']<2**48)
calls=template['calls'];bridges=sum(a['kind']=='bridge'for a in template['execution_schedule']);vports=112;replicas=8;stages=9;shifts=4*vports*replicas;moves=2*shifts;bridge_adds=2*vports*bridges
parent_live=parent['live'];parent_physical=parent['physical'];banks,rem=divmod(parent_live-2*vports*4*replicas,stages)
ck('own_parent_geometry_complete_calls',not rem and banks>=0 and parent_physical==parent_live+504+8+2 and len(calls)==stages*replicas==72 and bridges==72)
scalar=sum(nc[a['orientation']]['real_component_primitives']for a in calls);wrapper=2*len(calls)*152*2*(m-1)
nonlocal_items=4*vports*replicas*stages+2*vports*replicas*stages+2*len(calls)*504+sum(x['replicas']for x in parent['idle_children'])+stages*banks+bridge_adds+shifts+moves+parent_live+parent_physical+wrapper
outside=8*nonlocal_items+64*m;parent_cost=scalar+bridge_adds+shifts+moves+parent_live+(len(calls)*adapters+outside)*compiler+64*parent_physical
rebased=parent_cost+65*(inv['physical']-parent_physical)+(Wlive-parent_live);used=max(rebased,parent_cost)
ck('direct_reconstruction_of_entire_fresh_invoice',inv['wrapper_elementary_factors_charged']==wrapper and parent_cost==inv['unhosted_pervertex']and rebased==inv['hosted_rebased_pervertex']and used==inv['conservative_pervertex_used'])
ck('own_global_payload_row_guard',max(z['prefix_bits']for z in nc.values())+37+len(calls)+bridges+4==inv['global_prefix_bits']==e['global_prefix_bits']==225<inv['charged_prefix_bits']==512 and inv['row_prefix_extra']==1024)
group=2**1296
for i in range(1,37):group*=2**(2*i)-1
stock=group*inv['physical'];streamed=group*mass;logical=group*used+64;router=compiler*(logical+1)*(stock+1)**2;literal=2*2**30000*stock**2+8*streamed+4*stock+4+32*m;Esource=2**100000
ck('own_complete_stock_router_literal',stock.bit_length()==inv['finite']['physical_stock_bits']and router.bit_length()==inv['finite']['router_bits']and literal.bit_length()==inv['finite']['literal_bits']and logical<2**6050 and router<2**30000 and literal<Esource)
ck('own_source_height_tape_and_row',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000 and 2*stock.bit_length()+9909+252+1024==inv['finite']['physical_row_coefficient']<20161)
component=rd('gaussian-only-parameter-ledger.json');ck('closed_Gaussian_only_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed']and component['invented_BIT_saving']is None and not component['bounded_schur_lemma']['arbitrary_scale_free_H_theorem_used'])
for p,h in component['dependency_hashes'].items():ck('component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('frozen_reduced_Gaussian',R/'gaussian_only_parameter_ledger.py');reduced=importlib.util.module_from_spec(sp);sp.loader.exec_module(reduced)
names={'divup','series_log_ratio','logint','expint','powint','moment'};p=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(p.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names];ck('pure_exact_series_only',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(p),'exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
fallback=32*m*m*sum(P.values());kappa=F(e['kappa']);eta_early=F(1,1000);eta_record=(kappa+F(e['complex_lower']))/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
ck('own_coarse_taxed_moment',earlyiv[1]<F(1695000,1696009)<1)
record_quantified=recordiv[1]<1 and 1-recordiv[1]>F(1,2**100)
ck('own_record_taxed_moment_or_explicit_failure',kappa<eta_record<F(e['complex_lower'])and((record_quantified and recordiv[1]<1)or recordiv[0]>1))
for name,iv in [('early',earlyiv)]+([('record',recordiv)]if record_quantified else[]):
    reciprocal=ceil(1/(1-iv[1]));coeff=2**32*m**4*(Esource+stock+streamed+1)**2*(1+reciprocal)**2*20162**2;ck(name+'_own_allsize_work_coefficient',reciprocal<2**100 and coeff<2**220000)
early=reduced.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001)
record=reduced.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)if record_quantified else None
for kind,o in [('early',early)]+([('record',record)]if record_quantified else[]):ck(kind+'_fresh_all32_Gaussian_and_seven_runtime_rows',len(o['checks'])==32 and all(o['checks'].values())and not o['ordinary_BIT_supplier_consumed']and 'bit_saving'not in json.dumps(o['new_outer_parameters']))
contracts=component['component_source_interfaces_required']+[
 'Own534 completed native all-input Gaussian/helper endpoints, exact required entry/output frames and absolute phases, normalised residual wrappers and identity on spectators are substantive retained interfaces. Scalar-only specialization and finite frame checks do not prove these operator identities.',
 'The own all-size compiler, common-label/mutable-basis owned realisation, normalized completed-child height, restored-row/tape and analytic recovery contracts remain conditional exactly as qualified in the own README. The source bounded73-axis binary-affine/even-quadratic-Z4 finite phase grammar is required for the charged universal compiler tariff.',
 'The fresh original source preparation, complete owner/controller audit with seven mutations and no-prior-invoice full recount were actually executed. No full original global verifier, all-edge phase engine or predecessor cold replay is claimed.',
 'This is a newly counted direct Gaussian/Fermat XAG realization of the own selected complete complex construction. The original optional BIT supplier is neither consumed nor assigned an invented saving.',
 'The preserved finite fallback density tax is not adjustable. Full stopped-child reserve u^(1000000*Q), per-coordinate40e direct tensor fallback and all seven actual operation rows are included by the independently closed finite component.'
]
deps=['legacy-expected-controller-534-bounds.md','legacy-expected-controller-534-inputs.md','legacy-expected-controller-534-inputs.json','legacy_expected_controller_534_inputs.py','fetch_legacy_expected_controller_sources.py','finite_selected_program_census.py','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
dep.update({p:hs(p)for p in deps})
native=dict(native_coordinate_rank=73,own_input_certificate='legacy-expected-controller-534-inputs.json',own_invoice=inv,own_role_receipt=own,actual_own_source_stages=inp['actual_own_source_stages'],scalar_only_specialization_not_operator_proof=True,operator_phase_proved=False,coarse_moment_interval=list(map(str,earlyiv)),record_moment_interval=list(map(str,recordiv)),attempted_record_saving=str(eta_record),native_record_saving=str(eta_record)if record_quantified else None,inherited_fallback_tax_denominator='10000000000000000',inherited_fallback_tax_removed=False)
for kind,o in [('native',native)]+([('record-upper',record)]if record_quantified else[])+[('early-upper',early)]:
    o.update(schema='own-pre-SPEC-selected-direct-Gaussian-'+kind+'/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',pr=534,own_head=inp['own_head'],source_head=inp['own_head'],kappa_record=str(kappa),early_effective_kappa='1/5000'if kind=='early-upper'else None,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',meaningful_lower=None,actual_first_crossing_known=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,record_tail_quantified=record_quantified,source_equivalent_numeric_realization=True,retained_previous_invoice=None,original_global_verifier_full_PASS_claimed=False,original_phase_engines_freshly_replayed=False,retained_contracts=contracts,source_sha256=primary,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks=checks.copy(),whole_instance_checks_passed=len(checks))
    if kind=='early-upper':o.update(record_tail_certificate='pr534-legacy-expected-finite-record-upper.json'if record_quantified else None,record_tail_certificate_sha256=hs('pr534-legacy-expected-finite-record-upper.json')if record_quantified else None,record_tail_upper_log2log2_integer=record['upper_log2log2_integer']if record_quantified else None,record_tail_scope='Own534 record exponent freshly quantified by the new direct Gaussian circuit.'if record_quantified else'Own534 record exponent is provenance only; its inherited taxed moment does not close a record tail.',piecewise_description='The counted early circuit has the stated sufficient domain. Its chosen switch is not a natural lower bound; a separately priced own record circuit supplies the quantified tail when indicated.')
    (R/f'pr534-legacy-expected-finite-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks_passed=len(checks),status='closed'if REVIEW_CLOSED else'pending_independent_AI_review',pr=534,record_tail_quantified=record_quantified,early_P=early['upper_log2log2_integer'],record_P=record['upper_log2log2_integer']if record_quantified else None),indent=2))
