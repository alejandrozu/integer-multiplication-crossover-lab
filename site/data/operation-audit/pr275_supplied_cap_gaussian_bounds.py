"""Own PR275 supplied-cap selection, chronology and a newly counted Gaussian bound."""
from pathlib import Path
from hashlib import sha1,sha256
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
head='524375c61b75dc10cef68a71d504e79e7e7f138c';own=rd('pr275-cap-source/own-manifest.json');ownfiles={a['path']:a['file']for a in own};up=rd(ownfiles['research/finite-assembly-pr799/UPSTREAM.json']);manifest=rd(ownfiles['research/finite-assembly-pr799/MANIFEST.json'])['files'];expected=rd(ownfiles['research/finite-assembly-pr799/EXPECTED.json']);kappa=F(expected['target']);frozen_metadata=F('46942230864663/62500000000000000')
for a in own:ck('actual_own_primary_'+a['path'],a['own_head']==head and hs(a['file'])==a['sha256']and '/'+head+'/'in a['primary_url'])
for key in ['UPSTREAM.json','EXPECTED.json','verify.py','README.md']:ck('actual_own_manifest_'+key,manifest[key]==hs(ownfiles['research/finite-assembly-pr799/'+key]))
ck('own_selected_target_not_old_fixture',kappa==F('207704331708695884480429/125000000000000000000000000')and kappa==F(expected['assembly']['target'])and kappa!=frozen_metadata)
ck('quoted_fixture_preserved',next(a for a in rd('remaining-record-audit/complete-audit-queue.json')['rows']if a['pr']==275)['quoted_kappa_fraction']==str(frozen_metadata))
vr=(R/ownfiles['research/finite-assembly-pr799/verify.py']).read_text(encoding='utf8')
ck('actual_verifier_selects_799_source',"package = upstream / 'research/gauge44-frames-x'"in vr and "os.environ['WITNESS_SPEC'] = str(package / 'data/SPEC.json')"in vr and "read(upstream / 'research/community-frontier799-audit/RESULT.json')"in vr and "owner['paid_profile']"in vr and "target = assembly.greatest_grid_target(c, b, grid)"in vr)
declared=rd('pr275-cap-source/declared-parent-manifest.json');files={a['path']:a['file']for a in declared}
for a in declared:
 p=a['path'];raw=(R/a['file']).read_bytes();pin=up['files'][p];ck('own_declared_immutable_input_'+p,a['declaring_head']==head and a['declared_commit']==up['commit']=='f567884aeb8851b6e794af1184119a3bfbe1e631'and sha256(raw).hexdigest()==a['sha256']==pin['sha256']and len(raw)==pin['bytes']and sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin['git_blob'])
selected=rd(files['research/gauge44-frames-x/data/SPEC.json']);pm=rd(files['research/gauge44-frames-x/MANIFEST.json'])
ck('actual_selected_parent_manifest',pm['data/SPEC.json']==hs(files['research/gauge44-frames-x/data/SPEC.json']))
ck('actual_selected_plan_and_owners',selected['data']['plan_sha256']==hs(files['research/gauge44-frames-x/data/PLAN.json'])and selected['data']['owners_sha256']==hs(files['research/gauge44-frames-x/data/OWNERS.json.gz']))
native=rd('pr799-finite-controller-native.json');native_peer=rd('pr799-finite-controller-peer-review.json');source_peer=rd('pr799-finite-controller-source-peer-review.json')
ck('named_own799_native_theorem_closed',native['status'].startswith('closed_conditional')and native_peer['reviewed_sha256']['pr799-finite-controller-native.json']==hs('pr799-finite-controller-native.json')and source_peer['reviewed_sha256']['pr799-finite-controller-native.json']==hs('pr799-finite-controller-native.json'))
for group in ['source_sha256','dependency_hashes']:
 for p,h in native[group].items():ck('named_native_'+p,hs(p)==h)
for suffix,p in [('__SPEC.json','research/gauge44-frames-x/data/SPEC.json'),('__PLAN.json','research/gauge44-frames-x/data/PLAN.json'),('__OWNERS.json.gz','research/gauge44-frames-x/data/OWNERS.json.gz')]:
 hits=[v for path,v in native['source_sha256'].items()if path.startswith('older-reviewed-source/799/')and path.endswith(suffix)];ck('exact_source_selected_native_input_'+suffix,len(hits)==1 and hits[0]==hs(files[p]))
ck('selected_actual_native_not_stale_archive',native['stale_native_evidence_rejected']and native['selected_native_scalar_and_frame_engine_freshly_executed']and native['reported_RESULT_spec_hash_matches_own_SPEC']is False and native['selected_program_semantic_sha256']==selected['providers']['gauge44']['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz'])
chron=rd('pr275-cap-source/chronology-primary-receipt.json')
for a in chron['primary_sources']:ck('chronology_primary_'+a['file'],hs(a['file'])==a['sha256'])
pr=rd('pr275-cap-source/current-pull275-api.json');commit=rd('pr275-cap-source/source-head-commit-api.json');merge=rd('pr275-cap-source/actual-merge-commit-api.json')
ck('actual_source_head_in_actual_merge',pr['number']==275 and pr['merged']and pr['head']['sha']==head and pr['merge_commit_sha']==merge['sha']=='fadae6f469e0d5c9c03bbe047a4d383dac254448'and merge['parents'][1]['sha']==head and commit['sha']==head)
ck('actual_selected_revision_before_merge',commit['commit']['committer']['date']=='2026-10-13T11:43:12Z'and commit['commit']['committer']['date']<pr['merged_at']=='2026-10-16T15:51:16Z'and 'Apply finite assembly to source-bound PR799 caps'in commit['commit']['message'])
P={int(k):v for k,v in native['paid_profile'].items()};m=73;Wlive=native['productive_live_families'];mass=sum(k*v for k,v in P.items())
ck('own_selected_full_profile_same_native',selected['expected']['global_profile']=={str(k):v for k,v in P.items()}and selected['expected']['live']==Wlive==7168 and selected['expected']['physical']==native['physical_families']==7682 and mass==native['paid_rank_mass']and m*Wlive-mass==native['rank_surplus']>0 and 2*max(P)**2<m*m)
ck('complete_named_native_costs',native['source_G_upper']=='2^30000'and native['source_E_upper']=='2^100000'and native['source_C0']=='2^210000'and native['source_row_coefficient']<20161 and native['source_global_prefix_bits']<512)
names={'divup','series_log_ratio','logint','expint','powint','moment'};tree=ast.parse((R/'pr531_finite_controller_upper.py').read_bytes());defs=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in names];ck('pure_exact_interval_engine',{n.name for n in defs}==names);exec(compile(ast.Module(body=defs,type_ignores=[]),'frozen_exact_moment','exec'),globals());SCALE=1<<384;ln2=series_log_ratio(2,1);fallback=32*m*m*sum(P.values())
eta_early=F(1,1000);eta_record=(kappa+F(selected['expected']['complex_lower']))/2;earlyiv=moment(eta_early);recordiv=moment(eta_record)
ck('new_early_and_record_moments',earlyiv[1]<1 and kappa<eta_record<F(selected['expected']['complex_lower'])and recordiv[1]<1 and 1-recordiv[1]>F(1,2**100))
group=2**(36*36)
for i in range(1,37):group*=2**(2*i)-1
stock=group*native['physical_families'];streamed=group*mass;Esource=2**100000
ck('complete_own_semantic_guard',32*m*(streamed+Esource)**2<2**210000)
for tag,iv in [('early',earlyiv),('record',recordiv)]:
 reciprocal=ceil(1/(1-iv[1]));coefficient=2**32*m**4*(Esource+stock+streamed+1)**2*(1+reciprocal)**2*20162**2;ck(tag+'_complete_allsize_coefficient',reciprocal<2**100 and coefficient<2**220000)
component=rd('gaussian-only-parameter-ledger.json');ck('closed_noBIT_component',component['status']=='closed_conditional_mathematical_component'and component['script_sha256']==hs('gaussian_only_parameter_ledger.py')and all(component['checks'].values())and not component['ordinary_BIT_supplier_consumed'])
sp=importlib.util.spec_from_file_location('own275_reduced_gaussian',R/'gaussian_only_parameter_ledger.py');G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
early=G.finite_branch(F(1,5000),eta_early,10000,10001,((1<<54)+10000)//10001);record=G.finite_branch(kappa,eta_record,10**8,400000001,2**59,record=True)
for tag,o in [('early',early),('record',record)]:ck(tag+'_all32_outer_runtime_gate_checks',len(o['checks'])==32 and all(o['checks'].values())and not o['ordinary_BIT_supplier_consumed']and 'bit_saving'not in o['new_outer_parameters'])
deps=['pr275-supplied-cap-gaussian-bounds.md','pr275-cap-source/own-manifest.json','pr275-cap-source/declared-parent-manifest.json','pr275-cap-source/chronology-primary-receipt.json','remaining-record-audit/complete-audit-queue.json','pr799-recovered-finite-controller.md','pr799_recovered_finite_controller.py','pr799-finite-controller-native.json','pr799-finite-controller-peer-review.json','pr799-finite-controller-source-peer-review.json','gaussian-only-parameter-ledger.md','gaussian-only-parameter-ledger.json','gaussian_only_parameter_ledger.py','gaussian-only-parameter-ledger-peer-review.json','gaussian-only-parameter-ledger-source-peer-review.json','pr531_finite_controller_upper.py','candidate-fermat-helper.json','optimized-gmp-degree8-upper.json','optimized-gmp-semantic-repair.json']
dep={p:hs(p)for p in deps};dep.update(native['dependency_hashes']);source={a['file']:a['sha256']for a in own+declared};source.update({a['file']:a['sha256']for a in chron['primary_sources']})
base=dict(pr=275,own_head=head,source_head=head,model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',status='closed_conditional_upper_only'if REVIEW_CLOSED else'pending_independent_AI_review',kappa_record=str(kappa),frozen_metadata_kappa=str(frozen_metadata),source_selected_kappa_correction=True,source_selected_kappa_correction_basis='Own actual merged-head799-application EXPECTED target, own manifest/verifier/UPSTREAM binding and actual merge second parent; old parser chose historical433fixture. Frozen metadata is preserved, not rewritten.',source_revision_committed_at=commit['commit']['committer']['date'],source_revision_included_at_merge=pr['merged_at'],source_revision_merge_commit=merge['sha'],native_coordinate_rank=73,native_same_selected_source_theorem='pr799-finite-controller-native.json',native_same_selected_source_theorem_sha256=hs('pr799-finite-controller-native.json'),native_engine_independently_rerun_here=False,ordinary_BIT_supplier_consumed=False,invented_BIT_saving=None,source_equivalent_numeric_realization=True,historical_literal_dual_supplier_rerun=False,meaningful_lower=None,actual_first_crossing_known=False,retained_contracts=native['retained_contracts']+component['component_source_interfaces_required'],source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)
rf='pr275-supplied-cap-gaussian-record-upper.json';r=dict(base,**record,schema='own-source-selected-cap-gaussian-record-upper/1');(R/rf).write_text(json.dumps(enc(r),indent=2)+'\n',encoding='utf8')
ef='pr275-supplied-cap-gaussian-early-upper.json';e=dict(base,**early,schema='own-source-selected-cap-gaussian-early-upper/1',early_effective_kappa='1/5000',record_tail_quantified=True,record_tail_certificate=rf,record_tail_certificate_sha256=hs(rf),record_tail_upper_log2log2_integer=record['upper_log2log2_integer'],record_tail_scope='New counted direct Gaussian realization of the exact own explicitly selected799 core at this own application target; no historical original dual-supplier replay.',piecewise_description='Unchanged repaired GMP below early gate, counted same-core early branch then quantified own-record branch. No chosen switch supplies a natural lower.');(R/ef).write_text(json.dumps(enc(e),indent=2)+'\n',encoding='utf8')
nf='pr275-supplied-cap-gaussian-native.json';n=dict(base,schema='own-source-selected-cap-native-parameters/1',own_selected_SPEC=files['research/gauge44-frames-x/data/SPEC.json'],own_selected_SPEC_sha256=hs(files['research/gauge44-frames-x/data/SPEC.json']),paid_profile=P,own_native_theorem_facts=native,early_moment=[str(x)for x in earlyiv],record_moment=[str(x)for x in recordiv],native_record_saving=str(eta_record),record_tail_quantified=True);(R/nf).write_text(json.dumps(enc(n),indent=2)+'\n',encoding='utf8')
out=dict(schema='own-source-selected-cap-gaussian-cost-audit/1',status='closed_conditional_case'if REVIEW_CLOSED else'pending_independent_AI_review',pr=275,own_head=head,kappa_record=str(kappa),frozen_metadata_kappa=str(frozen_metadata),source_selected_kappa_correction=True,checks_passed=len(checks),checks=checks,native_certificate=nf,early_upper_certificate=ef,record_upper_certificate=rf,script_sha256=hs(Path(__file__).name));(R/'pr275-supplied-cap-gaussian-bounds.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own275 exact-source/chronology and fresh full-cost checks')
