"""Own-source T21/T37 complete finite-controller and integer upper bounds."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
REVIEW_CLOSED=True
checks={};prefix=''
def ck(n,v):assert v,prefix+n;checks[prefix+n]=True
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def read(p):return json.loads((R/p).read_bytes())
def identity(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):enc(v) for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [enc(v) for v in o]
    return o
census=read('t21-t37-owner-invoice-workbench.json')
ck('fresh_owner_census_script_binding',census['script_sha256']==hs('t21_t37_owner_invoice.py'))
ck('fresh_owner_census_complete',census['status']=='source_numeric_and_whole_role_checks_verified' and all(census['checks'].values()))
for p,h in census['source_sha256'].items():ck('primary_'+p,hs(p)==h)
for p,h in census['dependency_hashes'].items():ck('owner_dependency_'+p,hs(p)==h)
ck('own_t21_full_owner_binding',census['owner21_byte_hash_matches_SPEC'] and census['role21']['roles']==95256 and len(census['omitted_edit_controls21'])==9)
ck('own_t37_full_owner_binding',census['role37']['roles']==167832 and len(census['omitted_edit_controls37'])==8)
ck('own_both_complete_bank_controls',len(census['bank_controls21'])==len(census['bank_controls37'])==8)

S=R/'t21-t37-cost-source';manifest=read('t21-t37-cost-source/manifest.json')
def primary(pr,suffix):
    return next(S/x['file'] for x in manifest if x.get('pr')==pr and x['path'].endswith(suffix) and 'error' not in x)
claim21=json.loads(primary(890,'/data/CLAIM.json').read_bytes())
claim37=json.loads(primary(942,'/CLAIM.json').read_bytes())
bit=read('older-reviewed-source/799/pr589-pinned-EXPECTED.json')
ck('same_source_bit_citation',F(claim21['bit_lower'])==F(claim37['bit_lower'])==F(bit['nine']['bit_lower']))
endpoint=R/'pr4535-upper-source/endpoint.py';ns={'__name__':'own_t21_t37_outer','__file__':str(endpoint)}
ck('parameterized_outer_source_pin',hs('pr4535-upper-source/endpoint.py')=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
exec(compile(endpoint.read_bytes(),str(endpoint),'exec'),ns)
lemma=R/'pr531_finite_controller_upper.py';names={'divup','series_log_ratio','logint','expint','powint','moment','branch'}
defs=[n for n in ast.parse(lemma.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in names]
ck('named_finite_lemma_utilities',{n.name for n in defs}==names)
exec(compile(ast.Module(body=defs,type_ignores=[]),str(lemma),'exec'),globals())
SCALE=1<<384;ln2=series_log_ratio(2,1)
native_recurrence_contracts=[
 'The source exact absolute-phase/normalized-wrapper and whole Gaussian endpoint contracts, together with common-label/mutable-source and all-size unequal-child realization interfaces, remain explicit hypotheses of the fixed comparison protocol.',
 'Actual selected native scalar/frame columns were replayed; own whole-owner physical windows/charts, padded parent banks and complete numeric invoices were checked afresh. Original full phase engines are not claimed rerun.',
 'The numeric PLAN is a newly checked source-equivalent realization with identical selected program/owner/order/window/profile semantics. It does not claim historical parent-template or PLAN provenance-string byte identity.',
 'Completed exact Gaussian children have semantic norm one under the source endpoint interface; own finite literal inequalities fund C0=2^210000 and the full own 512/1024 payload charges.',
 'Same direct Gaussian/fine-prime/finite-section/boundary/recovery analytic conditions, exact candidate-only Fermat helper, fixed XAG tariff and repaired unlimited optimized-GMP correctness/halting assumptions.'
]
rows=[]
for pr,claim,head in [(890,claim21,'4b3bd8cbe8e3e81c44161017c9b72c905a8040a8'),(942,claim37,'1960cfa919a0945d0ca4cb14ea96237000037903')]:
    prefix=str(pr)+'_'
    invoice=read(f'pr{pr}-own-finite-invoice.json');plan=read(f'pr{pr}-own-numeric-plan.json')
    ck('own_invoice_receipt_identity',invoice==census['invoices'][str(pr)])
    ck('own_numeric_plan_complete_binding',identity(plan)==invoice['numeric_plan_sha256'] and plan['own_head']==head and plan['historical_PLAN_byte_identity_claimed'] is False)
    m=73;Wlive=invoice['live'];physical=invoice['physical'];P={int(k):v for k,v in invoice['paid_profile'].items()}
    mass=sum(r*n for r,n in P.items());group=2**(36*36)
    for i in range(1,37):group*=2**(2*i)-1
    stock=group*physical;streamed=group*mass;G=2**30000;Esource=2**100000;C0=2**210000
    ck('own_rank_stock',mass==invoice['paid_rank_mass'] and 73*Wlive-mass==invoice['rank_surplus'] and physical==Wlive+514)
    ck('own_512_or_1024_payload',invoice['charged_prefix_bits']==(512 if pr==890 else 1024) and invoice['row_prefix_extra']==2*invoice['charged_prefix_bits'])
    ck('own_row_allowance',invoice['physical_row_coefficient']==(16469 if pr==890 else 17495)<20161)
    ck('own_whole_call_program_hashes',len(plan['complete_calls'])==invoice['calls'] and len({c['selected_program_sha256'] for c in plan['complete_calls']})==2)
    ck('own_finite_G_E_C0',invoice['router_bits']<=30000 and invoice['literal_bits']<=100000 and 32*73*(streamed+Esource)**2<C0 and 2*(streamed+Esource)+18<C0)
    ck('own_no_old_native_invoice_transfer',invoice['retained_previous_invoice'] is None)
    expected={'kappa':claim['kappa'],'complex_lower':claim['complex_lower'],'bit_lower':claim['bit_lower']}
    fallback=32*m*m*sum(P.values());eta_early=F(1,1000)
    eta_record=(F(expected['kappa'])+F(expected['complex_lower']))/2
    earlyiv=moment(eta_early);recordiv=moment(eta_record)
    ck('own_coarse_moment',earlyiv[1]<F(1695000,1696009)<1)
    ck('own_record_interior_moment',F(expected['kappa'])<eta_record<F(expected['complex_lower']) and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
    Eearly=((1<<54)+10000)//10001
    early=branch('early',eta_early,earlyiv,F(1,5000),10000,10001,Eearly)
    record=branch('record',eta_record,recordiv,F(expected['kappa']),10**8,400000001,2**59)
    for kind,o in [('early',early),('record',record)]:
        X=int(o['A'])*int(o['E']);Q=o['Q'];reserve_degree=10**6*Q;workexp=int(o['allsize_work_coefficient_exponent'])
        ck(kind+'_full_stopped_stock_tail',F(X,Q)-10>reserve_degree*(X+3).bit_length()+1000)
        ck(kind+'_work_semantic_and_precision_umbrella',F(int(o['E']),Q)>workexp+220000+1040*(X+3).bit_length()+100)
    native=dict(schema='own-t21-t37-numeric-native/1',status='source_numeric_and_whole_role_checks_verified',pr=pr,own_head=head,native_coordinate_rank=73,not_uniform_2_to_H=True,selected_program_semantic_sha256=plan['selected_program_semantic_sha256'],owners_content_sha256=plan['owners_content_sha256'],numeric_plan_sha256=identity(plan),invoice_certificate=f'pr{pr}-own-finite-invoice.json',numeric_plan_certificate=f'pr{pr}-own-numeric-plan.json',invoice=invoice,coarse_moment_interval=[str(v) for v in earlyiv],record_native_saving=str(eta_record),record_moment_interval=[str(v) for v in recordiv],full_phase_engine_rerun=False,retained_contracts=native_recurrence_contracts)
    deps=['t21-t37-finite-controller-upper.md','t21_t37_owner_invoice.py','t21-t37-owner-invoice-workbench.json',f'pr{pr}-own-finite-invoice.json',f'pr{pr}-own-numeric-plan.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','pr531-finite-controller-peer-review.json','candidate-fermat-helper.md','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py']
    deps.append('older-reviewed-source/799/pr589-pinned-EXPECTED.json')
    dependencies={p:hs(p) for p in deps}
    for name,o in [('native',native),('record-upper',record),('early-upper',early)]:
        o.update(pr=pr,own_head=head,source_head=head,schema='own-t21-t37-finite-controller-'+name+'/1',status='closed_conditional_upper_only' if REVIEW_CLOSED else 'pending_independent_AI_review',checks_passed=len(checks),source_sha256=census['source_sha256'],dependency_hashes=dependencies,script_sha256=hs(Path(__file__).name),source_equivalent_numeric_realization=True,historical_PLAN_byte_identity_claimed=False,meaningful_lower=None)
        if name=='early-upper':o.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-finite-controller-record-upper.json',record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_certificate_sha256=hs(f'pr{pr}-finite-controller-record-upper.json'),piecewise_description='Own unchanged repaired GMP below sufficient early gate, own counted early source-equivalent realization until quantified own record gate, then own counted record realization. The switch is not a natural crossover lower bound.')
        (R/f'pr{pr}-finite-controller-{name}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
    rows.append(dict(pr=pr,own_head=head,kappa_record=expected['kappa'],early_upper_certificate=f'pr{pr}-finite-controller-early-upper.json',record_upper_certificate=f'pr{pr}-finite-controller-record-upper.json',native_certificate=f'pr{pr}-finite-controller-native.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None))
out=dict(schema='own-t21-t37-whole-upper-bundle/1',status='closed_conditional_upper_only' if REVIEW_CLOSED else 'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'t21-t37-finite-controller-upper.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'rows':rows},indent=2))
