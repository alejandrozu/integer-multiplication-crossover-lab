"""Fresh per-PR moment, stopped reserve and whole cost instantiations."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
ADMITTED_PRS={592,600,622,623,624,625,1018,1082,1063,1297,1319,1130,1124,3338,3413}
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
screen=rd('selected-provider-dispatch.json');screenhash=hs('selected-provider-dispatch.json')
review=rd('selected-provider-review-evidence-screen.json');reviewmap={r['pr']:r for r in review['rows']}
scope=rd('selected-provider-canonical-contradiction-scope-read.json');scopemap={r['pr']:r for r in scope['rows']}
ck('canonical_review_scope_binding',scope['source_screen_sha256']==hs('selected-provider-review-evidence-screen.json')and scope['summary']['exhibited_selected_native_frame_phase_counterexamples_found']==0)
ck('dispatcher_script',screen['script_sha256']==hs('selected_provider_dispatch.py'))
for p,h in screen['source_sha256'].items():ck('dispatcher_input_'+p,hs(p)==h)
for p,h in screen['dependency_hashes'].items():ck('dispatcher_module_'+p,hs(p)==h)
endpoint=R/'pr4535-upper-source/endpoint.py';ns={'__name__':'selected_provider_own_outer','__file__':str(endpoint)}
ck('outer_parameter_source',hs('pr4535-upper-source/endpoint.py')=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
exec(compile(endpoint.read_bytes(),str(endpoint),'exec'),ns)
names={'divup','series_log_ratio','logint','expint','powint','moment','branch'};lemma=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(lemma.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names]
ck('named_finite_arithmetic',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(lemma),'exec'),globals())
SCALE=1<<384;ln2=series_log_ratio(2,1);rows=[]
for entry in screen['rows']:
    pr=entry['pr'];prefix=str(pr)+'_';row=dict(pr=pr,own_head=entry['own_head'],dispatch_status=entry['status'],numeric_bound_completed=False)
    if entry['status']!='source_numeric_inputs_checked_not_yet_whole_cost_certificate':row.update(status='source_cost_obligation_open',blocker=entry.get('blocker')or entry.get('missing_selected_native_bytes')or entry.get('physical_artifact_blockers')or entry['status']);rows.append(row);continue
    if pr not in ADMITTED_PRS:row.update(status='source_cost_obligation_open',blocker='Not admitted in this frozen batch: own auxiliary admission proof remains unresolved at this snapshot. A later separately proved extension must use new certificates.');rows.append(row);continue
    try:
        rev=reviewmap[pr];ck('own_canonical_review_head',rev['own_head']==entry['own_head']and any(z['own_head_present_in_record']for z in rev['matched_review_rows']))
        for z in rev['matched_review_rows']:ck('canonical_primary_'+z['source_file'],hs(z['source_file'])==z['source_sha256'])
        if any(z['literal_potential_contradiction_anchors']for z in rev['matched_review_rows']):ck('flagged_review_semantically_read',pr in scopemap and scopemap[pr]['manual_scope_read']and scopemap[pr]['own_head']==entry['own_head'])
        ck('shared_analytic_qualification_not_silently_assumed',pr not in scope['summary']['shared_analytic_qualification_entries'])
        cr=rd(entry['own_census_file']);ck('own_census_bytes',hs(entry['own_census_file'])==entry['own_census_sha256']and cr['own_head']==entry['own_head'])
        ck('own_SPEC_bytes',hs(cr['own_SPEC_file'])==cr['own_SPEC_sha256'])
        for kind,a in cr['own_physical_artifacts'].items():ck('own_'+kind+'_hash',hs(a['file'])==a['sha256']==a['own_SPEC_expected_sha256'])
        for n in cr['selected_native_censuses']:
            ck(n['provider']+'_actual_program_and_census',hs(n['program_file'])==n['program_file_sha256']and hs(n['census_file'])==n['census_sha256'])
            if n['canonical_file']:ck(n['provider']+'_actual_canonical',hs(n['canonical_file'])==n['canonical_file_sha256'])
        bp=f'selected-provider-dispatch-source/{pr}/own-bit-citation.json';bit=rd(bp);ck('own_auxiliary_citation',bit['status']=='own_citation_authenticated'and bit['own_head']==entry['own_head'])
        for p,h in bit['source_sha256'].items():ck('own_auxiliary_'+p,hs(p)==h)
        invoice=cr['invoice'];role=cr['role_receipt'];m=73;Wlive=invoice['live'];physical=invoice['physical'];P={int(k):v for k,v in role['profile'].items()};mass=sum(k*v for k,v in P.items())
        group=2**(36*36)
        for i in range(1,37):group*=2**(2*i)-1
        stock=group*physical;streamed=group*mass;G=2**30000;Esource=2**100000;C0=2**210000
        ck('own_complete_profile_and_finite_stock',mass==role['rank_mass']and 73*Wlive-mass==role['rank_surplus']and invoice['retained_previous_invoice']is None and invoice['router_bits']<30000 and invoice['literal_bits']<100000 and role['physical_row_coefficient']<20161)
        ck('positive_raw_surplus_and_source_halving_class',role['rank_surplus']>0 and max(P)<m and m*m>2*max(P)**2)
        ck('own_semantic_height',32*m*(streamed+Esource)**2<C0 and 2*(streamed+Esource)+18<C0)
        ck('complete_own_owner_controls',len(cr['negative_controls'])==6 and role['checked_whole_helper_widths']==role['roles']==role['checked_busy_family_windows'])
        expected={'kappa':cr['kappa_record'],'complex_lower':cr['complex_lower'],'bit_lower':bit['bit_lower']}
        fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(F(expected['kappa'])+F(expected['complex_lower']))/2
        earlyiv=moment(eta_early);recordiv=moment(eta_record)
        ck('own_early_moment',earlyiv[1]<F(1695000,1696009)<1)
        ck('own_interior_record_moment',F(expected['kappa'])<eta_record<F(expected['complex_lower'])and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
        native_recurrence_contracts=cr['retained_interfaces']+['Own complete dyadic scalar/phase grammar and actual selected source costs are separately bound; missing canonical catalogue is explicit, not a claimed native GF2 or phase replay.','Completed native child maps have norm one under that full endpoint contract. Fixed all-size occupied-row, constructive group/compiler, analytic fine-prime/boundary/recovery and repaired unlimited GMP correctness/halting contracts remain explicit.']
        early=branch('early',eta_early,earlyiv,F(1,5000),10000,10001,((1<<54)+10000)//10001)
        record=branch('record',eta_record,recordiv,F(expected['kappa']),10**8,400000001,2**59)
        for kind,o in [('early',early),('record',record)]:
            X=int(o['A'])*int(o['E']);Q=o['Q'];degree=10**6*Q;workexp=int(o['allsize_work_coefficient_exponent'])
            ck(kind+'_full_stopped_stock_tail',F(X,Q)-10>degree*(X+3).bit_length()+1000)
            ck(kind+'_precision_coefficient_tail',F(int(o['E']),Q)>workexp+220000+1040*(X+3).bit_length()+100)
        ownnative=dict(pr=pr,own_head=cr['own_head'],native_coordinate_rank=73,not_uniform_2_to_H=True,selected_native_censuses=cr['selected_native_censuses'],canonical_catalogue_absent_for=cr['canonical_catalogue_absent_for'],operator_phase_proved=False,own_complete_census_file=entry['own_census_file'],own_complete_census_sha256=entry['own_census_sha256'],own_invoice=invoice,own_role_receipt=role,coarse_moment_interval=[str(v)for v in earlyiv],record_native_saving=str(eta_record),record_moment_interval=[str(v)for v in recordiv],retained_contracts=native_recurrence_contracts)
        deps=['selected-provider-batch-upper.md','selected_provider_dispatch.py','selected-provider-dispatch-inputs.json','selected-provider-dispatch.json','selected-provider-review-evidence-screen.json','selected-provider-canonical-contradiction-scope-read.json','finite_selected_program_census.py','finite_actual_owner_census.py',entry['own_census_file'],bp,'pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','pr531-finite-controller-peer-review.json','candidate-fermat-helper.json','candidate-fermat-helper.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py']
        dep={p:hs(p)for p in deps};primary={cr['own_SPEC_file']:cr['own_SPEC_sha256'],**{a['file']:a['sha256']for a in cr['own_physical_artifacts'].values()},**bit['source_sha256']}
        primary.update({z['source_file']:z['source_sha256']for z in rev['matched_review_rows']})
        for n in cr['selected_native_censuses']:
            primary[n['program_file']]=n['program_file_sha256']
            if n['canonical_file']:primary[n['canonical_file']]=n['canonical_file_sha256']
            dep[n['census_file']]=n['census_sha256']
        for kind,o in [('native',ownnative),('record-upper',record),('early-upper',early)]:
            o.update(schema='own-dispatched-selected-finite-'+kind+'/1',pr=pr,own_head=cr['own_head'],source_head=cr['own_head'],status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks.copy(),source_sha256=primary,dependency_hashes=dep,meaningful_lower=None,source_equivalent_numeric_realization=True,historical_parent_provenance_byte_identity_claimed=False)
            if kind=='early-upper':o.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-dispatched-finite-controller-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-dispatched-finite-controller-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],piecewise_description='Existence witness: unchanged repaired GMP below the sufficient early gate, own counted early realization until its quantified own record gate, then own counted record realization. No natural lower bound is inferred from these switches.')
            (R/f'pr{pr}-dispatched-finite-controller-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
        row.update(status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',numeric_bound_completed=REVIEW_CLOSED,kappa_record=cr['kappa_record'],canonical_catalogue_absent_for=cr['canonical_catalogue_absent_for'],native_certificate=f'pr{pr}-dispatched-finite-controller-native.json',early_upper_certificate=f'pr{pr}-dispatched-finite-controller-early-upper.json',record_upper_certificate=f'pr{pr}-dispatched-finite-controller-record-upper.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None)
        print('PASS own dispatched whole-cost instantiation',pr,flush=True)
    except(Exception)as e:row.update(status='whole_cost_or_auxiliary_obligation_open',blocker=str(e)or type(e).__name__)
    rows.append(row)
ck('dispatcher_snapshot_not_changed_during_job',hs('selected-provider-dispatch.json')==screenhash)
ck('exact_admitted_PR_set',set(r['pr']for r in rows if 'early_upper_certificate'in r)==ADMITTED_PRS)
out=dict(schema='own-selected-provider-whole-cost-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,dispatch_sha256=screenhash,script_sha256=hs(Path(__file__).name),summary=dict(cohort=len(rows),passing_instantiations=sum('early_upper_certificate'in r for r in rows),closed_upper_count=sum(r['numeric_bound_completed']for r in rows),remaining_obligations=sum('early_upper_certificate'not in r for r in rows)))
(R/'selected-provider-batch-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n');print(json.dumps(out['summary'],indent=2))
