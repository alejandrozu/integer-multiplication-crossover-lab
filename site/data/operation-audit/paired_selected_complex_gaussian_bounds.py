"""Own543/545 explicitly selected complete535 core, newly counted Gaussian tails."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256,sha1
import ast,base64,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={};prefix=''
def rd(f):return json.loads((R/f).read_bytes())
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def ck(k,v):assert v,prefix+k;checks[prefix+k]=True
def ceil(q):return -(-q.numerator//q.denominator)
def enc(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return{str(k):enc(v)for k,v in o.items()}
    if isinstance(o,(tuple,list)):return[enc(v)for v in o]
    return o
root535='older-reviewed-source/535/research/post-center-rank4-global/';nfile='pr535-finite-controller-native.json';n=rd(nfile);oldM=rd(root535+'MANIFEST.json')['sha256'];oldE=rd(root535+'EXPECTED.json')
ck('closed_exact_selected_native_component',n['status']=='closed_conditional_upper_only'and n['pr']==535 and n['source_head']=='8b758a103915179322766bed5798f9b6e7198011'and n['native_coordinate_rank']==73 and n['script_sha256']==hs('older_reviewed_finite_controllers.py'))
for p,h in n['source_sha256'].items():ck('selected535_source_'+p,hs(p)==h)
for p,h in n['dependency_hashes'].items():ck('selected535_dependency_'+p,hs(p)==h)
for pf in['pr535-finite-controller-peer-review.json','pr535-finite-controller-source-peer-review.json']:
    q=rd(pf);ck(pf+'_closed',q['status']in['independent_AI_peer_review_pass_conditional','independent_AI_source_peer_review_pass_conditional']and all(q['reviewed_sha256'][f]==hs(f)for f in[nfile,'older-reviewed-finite-controllers.md','older_reviewed_finite_controllers.py']))
component=rd('gaussian-only-parameter-ledger.json');ck('closed_reduced_Gaussian_only',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed']and component['invented_BIT_saving']is None)
for p,h in component['dependency_hashes'].items():ck('reduced_component_'+p,hs(p)==h)
sp=importlib.util.spec_from_file_location('frozen_reduced_component',R/'gaussian_only_parameter_ledger.py');reduced=importlib.util.module_from_spec(sp);sp.loader.exec_module(reduced)
names={'divup','series_log_ratio','logint','expint','powint','moment'};p=R/'pr531_finite_controller_upper.py';defs=[x for x in ast.parse(p.read_text()).body if isinstance(x,ast.FunctionDef)and x.name in names];ck('pure_interval_arithmetic_only',{x.name for x in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),str(p),'exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1)
sources=rd('paired-complex-selection-source/manifest.json');supplier=rd('paired-complex-selection-source/supplier-manifests.json');rows=[]
for case in sources['rows']:
    pr=case['pr'];prefix=str(pr)+'_';S=f'paired-complex-selection-source/{pr}/';primary={};dep={}
    ck('own_two_explicit_primary_compositions',pr in[543,545]and case['own_head']=={543:'2065fe4f72a914d907f1046603f5a36f17018535',545:'376426f3b2b26ab430d10baf16bbd9ff42990a7c'}[pr])
    mf=next(a for a in case['primary_files']if a['relative'].startswith('MANIFEST.'));mb=(R/mf['file']).read_bytes()
    if mf['relative'].endswith('.json'):z=json.loads(mb);M=z.get('files',z.get('sha256',z))
    else:M={line.split('  ',1)[1]:line.split('  ',1)[0]for line in mb.decode().splitlines()if line.strip()}
    for f,h in case['changed_file_receipts'].items():ck('own_changed_file_API_'+f,hs(f)==h);primary[f]=h
    for a in case['primary_files']:
        b=(R/a['file']).read_bytes();blob=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();ck('own_primary_'+a['relative'],a['pr']==pr and a['own_head']==case['own_head']and case['own_head']in a['primary_url']and hs(a['file'])==a['sha256']and blob==a['git_blob_sha1']and(a['relative']==mf['relative']or M[a['relative']]==a['sha256'])and(a['API_own_blob_verified']or a['own_API_authenticated_MANIFEST_payload']));primary[a['file']]=a['sha256']
    ck('own_MANIFEST_actual_API_blob',mf['API_own_blob_verified'])
    choice=next(a for a in rd(S+'data/complex-b.json')['suppliers']if a['name']=='pr535');cited=rd(S+choice['receipt']);e=rd(S+'EXPECTED.json');krow=e['nine']['kappa']['pr535']if pr==543 else e['kappa']['pr535'];target=F(krow['kappa']);b=F(choice['b'])
    ck('actual_primary_complete_complex_choice',choice['pr']==535 and choice['role']=='primary'and choice['field']=='complex_lower'and choice['receipt']=='data/complex/pr535/EXPECTED.json'and b==F(cited['complex_lower'])==F(oldE['complex_lower'])and krow['binding_component']=='complex'and F(krow['complex_lower'])==b and target==F(793733736881443,500000000000000000))
    if pr==543:
        pin=rd(S+'SOURCE-pr535.json');v=(R/S/'verify.sh').read_text();c=(R/S/'code/cited.py').read_text()
        ck('literal_own543_selector_and_cited_commit',pin['commit']==choice['commit']==n['source_head']and pin['source'].endswith('/535')and 'nine $WORD $R $WD $WD $D/selection9-r420.json pr535,pr531'in v and '$PY $C/cited.py $HERE'in v and 'for s in t["suppliers"]:'in c)
        for f,a in pin['identical'].items():
            payload=(R/S/f).read_bytes();ck('own535_receipt_Gitblob_'+f,sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()==a['blob'])
    else:
        v=(R/S/'verify.py').read_text();ck('literal_own545_selector_and_cited_commit',choice['commit']=='25f9b7c2310d40c9efdfbe368a40ba6e74d3b0a2'and "emit_audit_assemble(WORD, WD, bit, HOST, AD, ['pr535', str(HERE / 'data/complex-b.json')])"in v and "r['kappa']['pr535']['kappa'] == e['kappa']['pr535']['kappa']"in v and sha1(b'blob '+str(len((R/S/choice['receipt']).read_bytes())).encode()+b'\0'+(R/S/choice['receipt']).read_bytes()).hexdigest()==choice['receipt_git_blob'])
    correction={}
    if pr==545:
        cf=S+'chronology.json';chron=rd(cf);prim={}
        ck('source_correction_chronology_checked',chron['pr']==545 and chron['own_head']==case['own_head']and chron['actual_own_selected_kappa']==str(target)and chron['frozen_metadata_kappa']==e['pr535']['kappa']and chron['script_sha256']==hs('paired_selected_complex_source_chronology.py')and all(chron['checks'].values()))
        for a in chron['primary_receipts']:ck('correction_primary_'+a['file'],hs(a['file'])==a['sha256']and len((R/a['file']).read_bytes())==a['bytes']);primary[a['file']]=a['sha256'];prim[Path(a['file']).name]=rd(a['file'])
        actualpull=prim['chronology-pull.json'];actualsource=prim['chronology-source-git-commit.json'];actualmerge=prim['chronology-merge-git-commit.json']
        ck('actual_eighth_of43_source_at_merge',actualpull['head']['sha']==actualsource['sha']==chron['own_head']and actualpull['number']==545 and actualpull['merged']and actualpull['merged_at']==chron['merged_at']and actualpull['merge_commit_sha']==actualmerge['sha']==chron['merge_commit_sha']and[a['sha']for a in actualmerge['parents']]==chron['merge_parents']and chron['merge_parents'][7]==case['own_head']and len(chron['merge_parents'])==43 and actualsource['committer']['date']==chron['source_committed_at']<=chron['merged_at'])
        dep[cf]=hs(cf);dep['paired_selected_complex_source_chronology.py']=hs('paired_selected_complex_source_chronology.py')
        correction=dict(source_selected_kappa_correction=True,frozen_metadata_kappa=chron['frozen_metadata_kappa'],actual_own_selected_kappa=str(target),source_kappa_correction_primary_receipt=cf,source_revision_included_at_merge=chron['merged_at'],source_revision_merge_commit=chron['merge_commit_sha'],source_revision_committed_at=chron['source_committed_at'],source_selected_kappa_correction_basis='Own EXPECTED.kappa.pr535 and literal verifier select the complete primary composition. The frozen parser instead quoted own EXPECTED.pr535, explicitly the cited535 baseline. Both values are preserved; actual ownhead is eighth of43 merge parents.',source_selected_kappa_correction_note='The quoted historical baseline remains visible. This new cost realization uses the actual own selected composition target at its authenticated merge date, without backdating or adjudicating a new accepted exponent record.',new_accepted_exponent_record_claimed=False)
    selected={a['path'].rsplit('/',1)[-1]:a for a in supplier['rows']if a['source_head']==choice['commit']}
    for name,a in selected.items():
        raw=(R/a['file']).read_bytes();api=rd(a['GitContents_response']);ck('actual_cited535_API_'+name,a['API_blob_verified']and a['source_pr']==535 and a['source_head']==choice['commit']and choice['commit']in a['primary_url']and hs(a['file'])==a['sha256']and hs(a['GitContents_response'])==a['GitContents_response_sha256']and base64.b64decode(api['content'])==raw and sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==api['sha']==a['git_blob_sha1']);primary[a['file']]=a['sha256'];primary[a['GitContents_response']]=a['GitContents_response_sha256']
    selectedM=rd(selected['MANIFEST.json']['file'])['sha256'];selectedE=rd(selected['EXPECTED.json']['file'])
    ck('complete52item_selected_supplier_MANIFEST_exact_equality',len(selectedM)==52 and selectedM==oldM and selectedE==cited==oldE)
    for f,h in selectedM.items():ck('actual_selected535_full_payload_'+f,hs(root535+f)==h);primary[root535+f]=h
    ck('actual_selected_entire_native_and_physical_receipt_identity',cited['canonical_word_content_sha256']==oldE['canonical_word_content_sha256']and cited['raw_word_content_sha256']==oldE['raw_word_content_sha256']and cited['global_template_content_sha256']==oldE['global_template_content_sha256']and cited['global_profile']=={str(k):v for k,v in n['paid_profile'].items()})
    m=73;P={int(k):v for k,v in n['paid_profile'].items()};Wlive=n['productive_live_families'];mass=sum(k*v for k,v in P.items());group=2**1296
    for i in range(1,37):group*=2**(2*i)-1
    stock=group*n['physical_families'];streamed=group*mass;Esource=2**100000
    ck('same_exact_selected_native_budget_not_old_upper',n['paid_rank_mass']==mass and m*Wlive-mass==n['rank_surplus']==2560 and m*m>2*max(P)**2 and max(P)<m and n['source_G_upper']=='2^30000'and n['source_E_upper']=='2^100000'and n['source_C0']=='2^210000'and n['source_row_coefficient']<20161 and stock.bit_length()==n['physical_stock_bitlength'])
    ck('complete_source_height_no_field_cancellation',32*m*(streamed+Esource)**2<2**210000 and 2*(streamed+Esource)+18<2**210000)
    fallback=32*m*m*sum(P.values());eta_early=F(1,1000);eta_record=(target+b)/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
    ck('fresh_own_early_and_record_taxed_moments',earlyiv[1]<F(1695000,1696009)<1 and target<eta_record<b and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
    for label,iv in [('early',earlyiv),('record',recordiv)]:
        rec=ceil(1/(1-iv[1]));coeff=2**32*m**4*(Esource+stock+streamed+1)**2*(1+rec)**2*20162**2;ck(label+'_full_allsize_work_coefficient',rec<2**100 and coeff<2**220000)
    early=reduced.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001);record=reduced.finite_branch(target,eta_record,10**8,400000001,2**59,record=True)
    for label,o in [('early',early),('record',record)]:ck(label+'_fresh32and50_2_7_and_actual_seven_rows',len(o['checks'])==32 and all(o['checks'].values())and not o['ordinary_BIT_supplier_consumed']and 'bit_saving'not in json.dumps(o['new_outer_parameters']))
    contracts=n['retained_contracts']+component['component_source_interfaces_required']+[
      'This NEW direct Gaussian/Fermat XAG realization executes the complete complex supplier explicitly named primary by the own paired construction. The changed own BIT circuit is wholly UNUSED: no claim is made to price it or to attribute the resulting runtime to its optimization.',
      'Both actually cited535 source heads have the exact complete52item MANIFEST of the separately closed535 native/physical/invoice component. Every actual selected source payload is rechecked; this is full serialized source identity, not equality of kappa, a histogram or an old upper.',
      'Required normalized Gaussian/native absolute-phase, entry/output frames, arbitrary-input helper/spectator restore, common-label/owned all-size compiler/row/tape and analytic contracts remain substantive explicit premises. No fresh original BIT/native-phase/global verifier run is claimed.',
      'All inherited fallback density tax, per-coefficient40e direct fallback, full u^(1000000Q) stopped reserve, concrete-scale Schur and all actual seven operation rows are retained. The optional BIT argument/saving is absent from this reduced branch.'
    ]
    deps=['paired-selected-complex-gaussian-bounds.md','paired-complex-selection-source/manifest.json','paired-complex-selection-source/supplier-manifests.json','fetch_paired_complex_selection_sources.py','fetch_paired_complex_supplier_manifests.py',S+'source-manifest.json',nfile,'pr535-finite-controller-peer-review.json','pr535-finite-controller-source-peer-review.json','older-reviewed-finite-controllers.md','older_reviewed_finite_controllers.py','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','pr531-finite-controller-upper.md','pr531_finite_controller_upper.py','candidate-fermat-helper.json','pr4470-global-precision.md','pr4470-boundary-recovery.md','pr4470-whole-integer-bound.md','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
    dep.update({p:hs(p)for p in deps});dep.update(n['dependency_hashes']);primary.update(n['source_sha256'])
    native=dict(selected_supplier_pr=535,selected_supplier_head=choice['commit'],complete_selected_MANIFEST_equality=True,selected_complete_source_payload_count=52,selected_native_component=nfile,selected_native_component_sha256=hs(nfile),native_coordinate_rank=73,productive_live_families=Wlive,physical_families=n['physical_families'],paid_profile=P,paid_rank_mass=mass,rank_surplus=2560,coarse_moment_interval=list(map(str,earlyiv)),record_moment_interval=list(map(str,recordiv)),native_record_saving=str(eta_record),inherited_fallback_tax_removed=False)
    for kind,o in [('native',native),('record-upper',record),('early-upper',early)]:
        o.update(schema='own-paired-selected-complete-complex-Gaussian-'+kind+'/1',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',pr=pr,own_head=case['own_head'],source_head=case['own_head'],kappa_record=str(target),early_effective_kappa='1/5000'if kind=='early-upper'else None,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',meaningful_lower=None,ordinary_BIT_supplier_consumed=False,changed_own_BIT_circuit_priced=False,changed_own_BIT_benefit_attributed=False,invented_BIT_saving=None,record_tail_quantified=True,original_global_verifier_full_PASS_claimed=False,retained_contracts=contracts,source_sha256=primary,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),whole_instance_checks=checks.copy(),whole_instance_checks_passed=len(checks),**correction)
        if kind=='early-upper':o.update(record_tail_certificate=f'pr{pr}-paired-selected-complex-record-upper.json',record_tail_certificate_sha256=hs(f'pr{pr}-paired-selected-complex-record-upper.json'),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='Own paired-construction record exponent freshly funded by the explicitly selected complete complex Gaussian realization; original changed BIT runtime/benefit not priced.',piecewise_description='Use the counted early source-core circuit above its sufficient gate, and the separately counted own record source-core circuit above its verified record gate. A chosen switch is not a natural lower bound.')
        (R/f'pr{pr}-paired-selected-complex-{kind}.json').write_text(json.dumps(enc(o),indent=2)+'\n',encoding='utf8')
    rows.append(dict(pr=pr,own_head=case['own_head'],native_certificate=f'pr{pr}-paired-selected-complex-native.json',early_upper_certificate=f'pr{pr}-paired-selected-complex-early-upper.json',record_upper_certificate=f'pr{pr}-paired-selected-complex-record-upper.json',upper_log2log2_integer=early['upper_log2log2_integer'],record_tail_quantified=True,changed_own_BIT_circuit_priced=False))
out=dict(schema='own-paired-selected-complete-complex-Gaussian-batch/1',status='closed_conditional_batch'if REVIEW_CLOSED else'pending_independent_AI_review',rows=rows,checks_passed=len(checks),checks=checks,script_sha256=hs(Path(__file__).name))
(R/'paired-selected-complex-gaussian-bounds.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own paired explicit complex selections',len(rows),out['status'])
