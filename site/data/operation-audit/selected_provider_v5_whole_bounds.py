"""Own1178 exact reconstructed native and full finite Gaussian circuit bound."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
ADMITTED={1178}
checks={};prefix=''
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def rd(p):return json.loads((R/p).read_bytes())
def ck(n,v):assert v,prefix+n;checks[prefix+n]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [enc(v)for v in o]
    return o
component=rd('gaussian-only-parameter-ledger.json')
ck('closed_reduced_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed']and component['invented_BIT_saving']is None)
for p,h in component['dependency_hashes'].items():ck('reduced_component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('frozen_gaussian_reduced_component',R/'gaussian_only_parameter_ledger.py');reduced=importlib.util.module_from_spec(sp);sp.loader.exec_module(reduced)
names={'divup','series_log_ratio','logint','expint','powint','moment'};source=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(source.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names];ck('pure_exact_interval_functions',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(source),'exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
screen=rd('selected-provider-dispatch-v5.json');sm={r['pr']:r for r in screen['rows']};ck('frozen_source_dispatcher',screen['script_sha256']==hs('selected_provider_dispatch_v5.py'))
native_recovery=rd('pr1178-exact-selected-native-recovery.json')
ck('own_exact_native_reconstruction',native_recovery['status']=='passed_exact_selected_semantic_and_orientation_reconstruction'and native_recovery['script_sha256']==hs('recover_pr1178_selected_native.py')and all(native_recovery['checks'].values())and all(a['exit_code']==0 for a in native_recovery['steps']))
for path,digest in native_recovery['source_sha256'].items():ck('own_native_source_'+path,hs(path)==digest)
for artifact in native_recovery['outputs']:ck('own_native_derived_'+artifact['file'],hs(artifact['file'])==artifact['sha256'])
for p,h in screen['source_sha256'].items():ck('frozen_source_input_'+p,hs(p)==h)
for p,h in screen['dependency_hashes'].items():ck('source_module_'+p,hs(p)==h)
review=rd('selected-provider-review-evidence-screen.json');rm={r['pr']:r for r in review['rows']};scope=rd('selected-provider-canonical-contradiction-scope-read.json');scm={r['pr']:r for r in scope['rows']}
ck('canonical_semantic_scope_review',scope['source_screen_sha256']==hs('selected-provider-review-evidence-screen.json')and scope['summary']['exhibited_selected_native_frame_phase_counterexamples_found']==0)
rows=[]
for pr in sorted(ADMITTED):
    prefix=str(pr)+'_';entry=sm[pr];ck('complete_own_numeric_inputs',entry['status']=='source_numeric_inputs_checked_not_yet_whole_cost_certificate')
    cr=rd(entry['own_census_file']);ck('own_census_and_SPEC',hs(entry['own_census_file'])==entry['own_census_sha256']and hs(cr['own_SPEC_file'])==cr['own_SPEC_sha256']and cr['own_head']==entry['own_head'])
    provenance_file=f'selected-provider-v2-discovered-source/{pr}/manifest.json';provenance=rd(provenance_file)
    own_sources=[a for a in provenance['files']if a['file']==cr['own_SPEC_file']and a['sha256']==cr['own_SPEC_sha256']]
    ck('new_exact_own_commit_primary_provenance',provenance['own_head']==cr['own_head']and len(own_sources)==1 and own_sources[0]['primary_url']=='https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/'+cr['own_head']+'/'+own_sources[0]['path'])
    primary={cr['own_SPEC_file']:cr['own_SPEC_sha256']};cached={}
    for kind,a in cr['own_physical_artifacts'].items():ck('own_'+kind,hs(a['file'])==a['sha256']==a['own_SPEC_expected_sha256']);primary[a['file']]=a['sha256']
    plan_source=cr['own_physical_artifacts']['PLAN']
    ck('own_exact_compressed_PLAN_transform',plan_source['status']=='authenticated_own_SPEC_derived_bytes'and hs(plan_source['source_compressed_file'])==plan_source['source_compressed_sha256']and hashlib.sha256(__import__('gzip').decompress((R/plan_source['source_compressed_file']).read_bytes())).hexdigest()==plan_source['sha256'])
    primary[plan_source['source_compressed_file']]=plan_source['source_compressed_sha256']
    for n in cr['selected_native_censuses']:
        ck(n['provider']+'_selected_program_census',hs(n['program_file'])==n['program_file_sha256']and hs(n['census_file'])==n['census_sha256']);primary[n['program_file']]=n['program_file_sha256'];cached[n['census_file']]=n['census_sha256']
        if n['canonical_file']:ck(n['provider']+'_optional_canonical',hs(n['canonical_file'])==n['canonical_file_sha256']);primary[n['canonical_file']]=n['canonical_file_sha256']
    rev=rm[pr];ck('own_canonical_review',rev['own_head']==entry['own_head']and any(x['own_head_present_in_record']for x in rev['matched_review_rows']))
    for x in rev['matched_review_rows']:ck('canonical_primary_'+x['source_file'],hs(x['source_file'])==x['source_sha256']);primary[x['source_file']]=x['source_sha256']
    if any(x['literal_potential_contradiction_anchors']for x in rev['matched_review_rows']):ck('flagged_review_individually_read',pr in scm and scm[pr]['manual_scope_read'])
    ck('shared_historical_false_general_theorem_not_imported',pr not in scope['summary']['shared_analytic_qualification_entries']and not component['bounded_schur_lemma']['arbitrary_scale_free_H_theorem_used'])
    inv=cr['invoice'];role=cr['role_receipt'];m=73;Wlive=inv['live'];P={int(k):v for k,v in role['profile'].items()};mass=sum(k*v for k,v in P.items())
    group=2**(36*36)
    for i in range(1,37):group*=2**(2*i)-1
    stock=group*inv['physical'];streamed=group*mass;Esource=2**100000
    ck('positive_raw_surplus_and_halving',mass==role['rank_mass']and m*Wlive-mass==role['rank_surplus']>0 and max(P)<m and m*m>2*max(P)**2)
    ck('own_complete_work_stock_and_row',len(cr['negative_controls'])==6 and inv['retained_previous_invoice']is None and inv['router_bits']<30000 and inv['literal_bits']<100000 and role['physical_row_coefficient']<20161 and role['prefix_bits']<role['charged_prefix_bits'])
    ck('own_semantic_height',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
    fallback=32*m*m*sum(P.values());eta_early=F(1,1000);kappa=F(cr['kappa_record']);eta_record=(kappa+F(cr['complex_lower']))/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
    ck('own_early_moment',earlyiv[1]<F(1695000,1696009)<1)
    ck('own_record_interior_moment',kappa<eta_record<F(cr['complex_lower'])and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
    for kind,iv in [('early',earlyiv),('record',recordiv)]:
        bound=ceil(1/(1-iv[1]));coeff=2**32*m**4*(Esource+stock+streamed+1)**2*(1+bound)**2*20162**2
        ck(kind+'_own_allsize_work_coefficient',bound<2**100 and coeff<2**220000)
    early=reduced.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001)
    record=reduced.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)
    for kind,o in [('early',early),('record',record)]:
        ck(kind+'_fresh_all_reduced_and_runtime_checks',len(o['checks'])==32 and all(o['checks'].values()))
        ck(kind+'_no_BIT_parameter_or_operation',not o['ordinary_BIT_supplier_consumed']and'bit_saving'not in json.dumps(o['new_outer_parameters']))
    contracts=cr['retained_interfaces']+component['component_source_interfaces_required']+['The exact own selected source core is realized by this new direct Gaussian/Fermat circuit; original optional BIT admission is neither assumed nor executed. Missing canonical catalogue is explicit; scalar specialization does not prove the operator endpoint.']
    ownnative=dict(pr=pr,own_head=cr['own_head'],native_coordinate_rank=73,own_complete_census_file=entry['own_census_file'],own_complete_census_sha256=entry['own_census_sha256'],selected_native_censuses=cr['selected_native_censuses'],canonical_catalogue_absent_for=cr['canonical_catalogue_absent_for'],operator_phase_proved=False,own_invoice=inv,own_role_receipt=role,coarse_moment_interval=[str(x)for x in earlyiv],record_moment_interval=[str(x)for x in recordiv],native_record_saving=str(eta_record),ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,retained_contracts=contracts)
    deps=['selected-provider-v5-whole-upper.md','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-source-peer-review.json','selected-provider-dispatch-v5.json','selected-provider-dispatch-v5-inputs.json','selected_provider_dispatch_v5.py','finite_selected_program_census.py','finite_actual_owner_census.py','selected-provider-review-evidence-screen.json','selected-provider-canonical-contradiction-scope-read.json',entry['own_census_file'],'pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
    deps+=['gaussian-only-parameter-ledger-peer-review.json',provenance_file,'selected-provider-v2-discovered-source.json','pr1178-exact-selected-native-recovery.json','recover_pr1178_selected_native.py','pr1178-native-recovery-source/1178-manifest.json','pr1178-native-recovery-source/native-dependencies-manifest.json','pr1178-native-recovery-source/extra-primary-manifest.json']
    dep={p:hs(p)for p in deps};dep.update(cached)
    dep.update(native_recovery['source_sha256'])
    for kind,o in [('native',ownnative),('record-upper',record),('early-upper',early)]:
        o.update(schema='own-selected-direct-gaussian-'+kind+'/1',pr=pr,own_head=cr['own_head'],source_head=cr['own_head'],model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=cr['kappa_record'],early_effective_kappa='1/5000'if kind=='early-upper'else None,source_equivalent_numeric_realization=True,historical_parent_provenance_byte_identity_claimed=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,meaningful_lower=None,actual_first_crossing_known=False,retained_contracts=contracts,source_sha256=primary,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks=checks.copy(),whole_instance_checks_passed=len(checks))
        if kind=='early-upper':o.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-recovered-x54-finite-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-recovered-x54-finite-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Own record exponent is quantified by the new direct Gaussian realization of the same selected source core; literal historical dual-supplier implementation is not claimed.',piecewise_description='Existence witness with unchanged repaired GMP below early sufficient gate, own counted direct Gaussian early branch, then own counted direct Gaussian record tail. Chosen switches are not natural lower bounds.')
        (R/f'pr{pr}-recovered-x54-finite-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
    rows.append(dict(pr=pr,own_head=cr['own_head'],kappa_record=cr['kappa_record'],native_certificate=f'pr{pr}-recovered-x54-finite-native.json',early_upper_certificate=f'pr{pr}-recovered-x54-finite-early-upper.json',record_upper_certificate=f'pr{pr}-recovered-x54-finite-record-upper.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],canonical_catalogue_absent_for=cr['canonical_catalogue_absent_for'],meaningful_lower=None))
    print('PASS own direct Gaussian whole bound',pr,flush=True)
ck('exact_one_own_X54_set',set(r['pr']for r in rows)==ADMITTED)
out=dict(schema='own-selected-direct-gaussian-upper-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,script_sha256=hs(Path(__file__).name))
(R/'selected-provider-v5-whole-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n');print(json.dumps(dict(status=out['status'],checks=len(checks),points=len(rows)),indent=2))
