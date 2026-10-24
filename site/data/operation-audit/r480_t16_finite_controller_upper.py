"""Own-source whole bounds for the selected r480 T16 controllers."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True
checks={};prefix=''
def ck(n,v):assert v,prefix+n;checks[prefix+n]=True
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def read(p):return json.loads((R/p).read_bytes())
def identity(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [enc(v)for v in o]
    return o
census=read('r480-t16-owner-invoice.json')
ck('own_whole_census_current_script',census['script_sha256']==hs('r480_t16_owner_invoice.py'))
ck('own_whole_roles_invoices_complete',census['status']=='own_source_numeric_role_invoice_checked' and all(census['checks'].values()))
for p,h in census['source_sha256'].items():ck('own_primary_'+p,hs(p)==h)
for p,h in census['dependency_hashes'].items():ck('own_dependency_'+p,hs(p)==h)
native=read('r480-selected-native-recovery.json')
ck('actual_selected_native_recovery',native['script_sha256']==hs('r480_selected_native_recovery.py') and native['native_scalar_allcolumn_replayed'] and all(native['checks'].values()))
for p,h in native['source_sha256'].items():ck('native_primary_'+p,hs(p)==h)
for p,h in native['dependency_hashes'].items():ck('native_dependency_'+p,hs(p)==h)
endpoint=R/'pr4535-upper-source/endpoint.py'
ck('parameterized_outer_source',hs('pr4535-upper-source/endpoint.py')=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
ns={'__name__':'own_r480_outer','__file__':str(endpoint)};exec(compile(endpoint.read_bytes(),str(endpoint),'exec'),ns)
lemma=R/'pr531_finite_controller_upper.py';names={'divup','series_log_ratio','logint','expint','powint','moment','branch'}
defs=[n for n in ast.parse(lemma.read_text()).body if isinstance(n,ast.FunctionDef)and n.name in names]
ck('exact_finite_lemma_utilities',{n.name for n in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(lemma),'exec'),globals())
SCALE=1<<384;ln2=series_log_ratio(2,1)
old1042=read('older-reviewed-source/1042-manifest.json');result1042='older-reviewed-source/'+next(x['file']for x in old1042 if x['path']=='research/gauge44-slots-t16/RESULT.json')
price1094='pr1094-source/files/research/complex-t16-rare-pattern-exchanges/PRICE.json'
bit=read('older-reviewed-source/799/pr589-pinned-EXPECTED.json')['nine']['bit_lower']
ck('own_both_BIT_citations',F(read(result1042)['bit_lower'])==F(read(price1094)['prices']['native']['outer']['bit_c'])==F(bit))
native_recurrence_contracts=[
 'Own exact arbitrary-input phase/normalized-wrapper, common-label/mutable-source and all-size unequal-child realization interfaces remain explicit fixed-protocol hypotheses.',
 'Exact earlier own-SPEC canonical/program hashes are recovered from a later archive; only identical earlier selected bytes are reused. No later owner/profile or rank supplier is substituted.',
 'All704 native scalar input columns, private clears, actual wrapper sweeps, dyadic Horner/prefix counts and each own whole T16 role/window/chart/profile were freshly checked; no full phase or Lean replay is claimed.',
 'The parent numeric realization uses an independently window-matched primary geometry fixture and source direct-sum lift. Own historical PLAN, call order, windows, profile and owner bytes are bound; historical parent provenance metadata byte identity is not claimed.',
 'Completed Gaussian children have semantic norm one under the endpoint contract. Own finite router/literal/C0 inequalities,512-bit payload and16469 row allowance fund the typed precision interface.',
 'Same direct Gaussian/fine-prime/finite-section/boundary/recovery analytic contracts, exact candidate-only Fermat helper and repaired unlimited optimized-GMP correctness/halting assumptions.'
]
rows=[]
for pr in [1042,1094]:
    prefix=str(pr)+'_';invoice=read(f'pr{pr}-r480-own-finite-invoice.json');plan=read(f'pr{pr}-r480-own-numeric-plan.json')
    ck('own_invoice_identity',invoice==census['invoices'][str(pr)])
    ck('own_numeric_PLAN_hash',identity(plan)==invoice['numeric_plan_sha256'] and plan['historical_parent_provenance_byte_identity_claimed'] is False)
    ck('own_complete_calls_and_native_word',len(plan['complete_calls'])==144 and plan['selected_program_semantic_sha256']==native['selected_program_semantic_sha256'])
    ck('own_source_independent_roles_controls',census['role_receipts'][str(pr)]['roles']==69120 and len(census['controls'][str(pr)])==6)
    m=73;Wlive=14336;physical=14850;P={int(k):v for k,v in invoice['paid_profile'].items()};mass=sum(r*n for r,n in P.items())
    group=2**(36*36)
    for i in range(1,37):group*=2**(2*i)-1
    stock=group*physical;streamed=group*mass;G=2**30000;Esource=2**100000;C0=2**210000
    ck('own_stock_rank_and_prefix',mass==1041408 and m*Wlive-mass==5120 and invoice['prefix_bits']==397 and invoice['charged_prefix_bits']==512 and invoice['physical_row_coefficient']==16469)
    ck('own_complete_finite_constants',invoice['router_bits']<30000 and invoice['literal_bits']<100000 and invoice['retained_previous_invoice'] is None and 32*m*(streamed+Esource)**2<C0)
    expected={'kappa':invoice['own_record_kappa'],'complex_lower':invoice['own_complex_lower'],'bit_lower':bit}
    fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(F(expected['kappa'])+F(expected['complex_lower']))/2
    earlyiv=moment(eta_early);recordiv=moment(eta_record)
    ck('own_coarse_moment',earlyiv[1]<F(1695000,1696009)<1)
    ck('own_record_moment_and_slack',F(expected['kappa'])<eta_record<F(expected['complex_lower']) and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
    early=branch('early',eta_early,earlyiv,F(1,5000),10000,10001,((1<<54)+10000)//10001)
    record=branch('record',eta_record,recordiv,F(expected['kappa']),10**8,400000001,2**59)
    for kind,o in [('early',early),('record',record)]:
        X=int(o['A'])*int(o['E']);Q=o['Q'];reserve_degree=10**6*Q;workexp=int(o['allsize_work_coefficient_exponent'])
        ck(kind+'_full_stopped_stock_tail',F(X,Q)-10>reserve_degree*(X+3).bit_length()+1000)
        ck(kind+'_complete_precision_and_coefficient_tail',F(int(o['E']),Q)>workexp+220000+1040*(X+3).bit_length()+100)
    ownnative=dict(schema='own-r480-t16-finite-native/1',pr=pr,own_head=invoice['own_head'],native_coordinate_rank=73,not_uniform_2_to_H=True,selected_program_semantic_sha256=native['selected_program_semantic_sha256'],own_invoice=invoice,numeric_plan_sha256=identity(plan),source_roles=census['role_receipts'][str(pr)],native_record_saving=str(eta_record),coarse_moment_interval=[str(v)for v in earlyiv],record_moment_interval=[str(v)for v in recordiv],full_phase_engine_rerun=False,retained_contracts=native_recurrence_contracts)
    deps=['r480-t16-finite-controller-upper.md','r480_selected_native_recovery.py','r480-selected-native-recovery.json','r480-selected-native-recovery.md','r480_t16_owner_invoice.py','r480-t16-owner-invoice.json',f'pr{pr}-r480-own-numeric-plan.json',f'pr{pr}-r480-own-finite-invoice.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','pr531-finite-controller-peer-review.json','candidate-fermat-helper.json','candidate-fermat-helper.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py',result1042,price1094,'older-reviewed-source/799/pr589-pinned-EXPECTED.json']
    dep={p:hs(p)for p in deps};primary={**census['source_sha256'],**native['source_sha256']}
    for kind,o in [('native',ownnative),('record-upper',record),('early-upper',early)]:
        o.update(schema='own-r480-t16-finite-controller-'+kind+'/1',pr=pr,own_head=invoice['own_head'],source_head=invoice['own_head'],status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks.copy(),source_sha256=primary,dependency_hashes=dep,meaningful_lower=None,source_equivalent_numeric_realization=True,historical_parent_provenance_byte_identity_claimed=False)
        if kind=='early-upper':o.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-r480-finite-controller-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-r480-finite-controller-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],piecewise_description='Use unchanged repaired GMP below the sufficient early gate, the own counted early schedule until its quantified own record tail, and its own record schedule thereafter. This chosen policy is not a natural crossover lower bound.')
        (R/f'pr{pr}-r480-finite-controller-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
    rows.append(dict(pr=pr,own_head=invoice['own_head'],kappa_record=expected['kappa'],early_upper_certificate=f'pr{pr}-r480-finite-controller-early-upper.json',record_upper_certificate=f'pr{pr}-r480-finite-controller-record-upper.json',native_certificate=f'pr{pr}-r480-finite-controller-native.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None))
out=dict(schema='own-r480-t16-whole-upper-bundle/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'r480-t16-finite-controller-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'rows':rows},indent=2))
