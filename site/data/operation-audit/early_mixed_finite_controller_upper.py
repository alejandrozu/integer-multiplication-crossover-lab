"""Own-source full upper instantiations for nine selected mixed native words."""
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
census=read('early-mixed-owner-invoice.json');native=read('early-mixed-native-components.json')
for key,obj,script in [('owner',census,'early_mixed_owner_invoice.py'),('native',native,'early_mixed_native_components.py')]:
    ck(key+'_fresh_script',obj['script_sha256']==hs(script)and all(obj['checks'].values()))
    for k in ['source_sha256','dependency_hashes']:
        for p,h in obj[k].items():ck(key+'_'+k+'_'+p,hs(p)==h)
for p,h in native['derived_selected_bytes_sha256'].items():ck('actual_native_'+p,hs(p)==h)
endpoint=R/'pr4535-upper-source/endpoint.py';ns={'__name__':'own_mixed_outer','__file__':str(endpoint)}
ck('parameterized_outer_source',hs('pr4535-upper-source/endpoint.py')=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15')
exec(compile(endpoint.read_bytes(),str(endpoint),'exec'),ns)
lemma=R/'pr531_finite_controller_upper.py';names={'divup','series_log_ratio','logint','expint','powint','moment','branch'}
defs=[n for n in ast.parse(lemma.read_text()).body if isinstance(n,ast.FunctionDef)and n.name in names]
ck('named_conditional_finite_utilities',{n.name for n in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(lemma),'exec'),globals())
SCALE=1<<384;ln2=series_log_ratio(2,1)
bitpath='remaining-record-audit/artifacts/543/06eccee9f6b7__EXPECTED.json';bitreceipt='remaining-record-audit/artifacts/543/fetch-cdef8d301b07fff6.json'
brec=read(bitreceipt);ck('actual_own_cited_BIT_primary',brec['head']=='2065fe4f72a914d907f1046603f5a36f17018535'and brec['api_own_blob_verified']and hs(bitpath)==brec['sha256']=='06eccee9f6b77e140833df83407e7996dc948c17d49b0779ab171fbe463fd28d')
bit=read(bitpath)['nine']['bit_lower']
native_recurrence_contracts=[
 'Own arbitrary-input operator-valued native phase, normalized-wrapper, ascending typed-helper and whole Gaussian endpoint contracts remain explicit; scalar specialization is not their proof.',
 'Exact own selected canonical/program/orientation hashes, actual scalar/frame incidence and dyadic Horner/prefix counts are checked independently. Derived objects are rebuilt from earlier hash-pinned recipes, sometimes using exact matching later archive bytes; no later supplier is imported.',
 'Each own PLAN/order/dispatch/OWNERS/window, complete role namespace, residual/spectator chart, primitive/wrapper invoice and no-prior-invoice finite stock is freshly checked.',
 'The counted parent is a primary-fixture source-equivalent numeric realization matching own physical windows; historical parent provenance metadata byte identity is not claimed.',
 'Common-label, mutable-source, arbitrary-input owned restore and all-size unequal-child occupied-row batching remain fixed-protocol hypotheses; completed Gaussian children have norm one under the endpoint contract.',
 'Own C0=2^210000 and actual512-bit payload fund the semantic precision reserve. Same direct analytic fine-prime/boundary/recovery, candidate-only Fermat helper and repaired unlimited GMP correctness/halting interfaces.'
]
rows=[]
for cr in census['rows']:
    pr=cr['pr'];prefix=str(pr)+'_';invoice=read(f'pr{pr}-mixed-own-finite-invoice.json');plan=read(f'pr{pr}-mixed-own-numeric-plan.json')
    ck('own_invoice_and_numeric_PLAN',invoice==cr['invoice']and identity(plan)==invoice['numeric_plan_sha256']and not plan['historical_parent_provenance_byte_identity_claimed'])
    ck('own_complete_role_controls',len(cr['negative_controls'])==6 and cr['role_receipt']['roles']==sum(next(x for x in native['rows']if x['pr']==pr and x['provider']==c['provider'])['selected_local_census']['forward']['helpers']for c in plan['selected_calls']))
    m=73;Wlive=invoice['live'];physical=invoice['physical'];P={int(k):v for k,v in invoice['paid_profile'].items()};mass=sum(r*n for r,n in P.items())
    group=2**(36*36)
    for i in range(1,37):group*=2**(2*i)-1
    stock=group*physical;streamed=group*mass;G=2**30000;Esource=2**100000;C0=2**210000
    ck('own_rank_stock_prefix',mass==invoice['paid_rank_mass']and m*Wlive-mass==invoice['rank_surplus']and invoice['prefix_bits']<invoice['charged_prefix_bits']==512 and invoice['physical_row_coefficient']<20161)
    ck('own_finite_constants',invoice['retained_previous_invoice']is None and 32*m*(streamed+Esource)**2<C0 and 2*(streamed+Esource)+18<C0)
    spec=read(cr['own_SPEC_file']);expected={'kappa':invoice['own_record_kappa'],'complex_lower':invoice['own_complex_lower'],'bit_lower':bit}
    ap=next(x for x in read('early-mixed-provider-source/own-packages-manifest.json')if x['pr']==pr and x['logical_path']=='code/assemble.py')
    ck('own_explicit_BIT_citation',"'research/e8-bit-r420/EXPECTED.json'"in(R/'early-mixed-provider-source'/ap['file']).read_text()and"'2065fe4f72a914d907f1046603f5a36f17018535'"in(R/'early-mixed-provider-source'/ap['file']).read_text())
    fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(F(expected['kappa'])+F(expected['complex_lower']))/2
    earlyiv=moment(eta_early);recordiv=moment(eta_record)
    ck('own_early_moment',earlyiv[1]<F(1695000,1696009)<1)
    ck('own_record_moment_slack',F(expected['kappa'])<eta_record<F(expected['complex_lower'])and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
    early=branch('early',eta_early,earlyiv,F(1,5000),10000,10001,((1<<54)+10000)//10001)
    record=branch('record',eta_record,recordiv,F(expected['kappa']),10**8,400000001,2**59)
    for kind,o in [('early',early),('record',record)]:
        X=int(o['A'])*int(o['E']);Q=o['Q'];reserve_degree=10**6*Q;workexp=int(o['allsize_work_coefficient_exponent'])
        ck(kind+'_full_stopped_stock_tail',F(X,Q)-10>reserve_degree*(X+3).bit_length()+1000)
        ck(kind+'_full_precision_coefficient_tail',F(int(o['E']),Q)>workexp+220000+1040*(X+3).bit_length()+100)
    ownnative=dict(pr=pr,own_head=invoice['own_head'],native_coordinate_rank=73,not_uniform_2_to_H=True,own_invoice=invoice,numeric_plan_sha256=identity(plan),selected_natives=[dict(provider=x['provider'],canonical=x['canonical_semantic_sha256'],program=x['program_semantic_sha256'])for x in native['rows']if x['pr']==pr],native_record_saving=str(eta_record),coarse_moment_interval=[str(v)for v in earlyiv],record_moment_interval=[str(v)for v in recordiv],full_phase_engine_rerun=False,retained_contracts=native_recurrence_contracts)
    deps=['early-mixed-finite-controller-upper.md','early_mixed_native_components.py','early-mixed-native-components.json','early_mixed_owner_invoice.py','early-mixed-owner-invoice.json','finite_selected_program_census.py','finite_actual_owner_census.py',f'pr{pr}-mixed-own-numeric-plan.json',f'pr{pr}-mixed-own-finite-invoice.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','pr531-finite-controller-peer-review.json','candidate-fermat-helper.json','candidate-fermat-helper.md','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json','pr4535-upper-source/endpoint.py',bitpath,bitreceipt]
    dep={p:hs(p)for p in deps};primary={**census['source_sha256'],**native['source_sha256']}
    for kind,o in [('native',ownnative),('record-upper',record),('early-upper',early)]:
        o.update(schema='own-mixed-finite-controller-'+kind+'/1',pr=pr,own_head=invoice['own_head'],source_head=invoice['own_head'],status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks.copy(),source_sha256=primary,dependency_hashes=dep,meaningful_lower=None,source_equivalent_numeric_realization=True,historical_parent_provenance_byte_identity_claimed=False)
        if kind=='early-upper':o.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-mixed-finite-controller-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-mixed-finite-controller-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],piecewise_description='Unchanged repaired GMP below the sufficient early gate, own counted early realization until the own quantified record tail, then own counted record realization; chosen switches are not natural lower bounds.')
        (R/f'pr{pr}-mixed-finite-controller-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n')
    rows.append(dict(pr=pr,own_head=invoice['own_head'],kappa_record=expected['kappa'],early_upper_certificate=f'pr{pr}-mixed-finite-controller-early-upper.json',record_upper_certificate=f'pr{pr}-mixed-finite-controller-record-upper.json',native_certificate=f'pr{pr}-mixed-finite-controller-native.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],meaningful_lower=None))
out=dict(schema='own-mixed-whole-upper-bundle/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'early-mixed-finite-controller-upper.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps(dict(status=out['status'],checks=len(checks),rows=rows),indent=2))
