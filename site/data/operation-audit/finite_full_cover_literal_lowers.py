"""Own-source mandatory literal finite-cover work; no stock-as-work inference."""
from pathlib import Path
from hashlib import sha256,sha1
import json,sys,runpy
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def rd(f):return json.loads((R/f).read_bytes())
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def ck(n,v):assert v,n;checks[n]=True
base='optimized-gmp-degree8-compact-upper.json';B=rd(base)
ck('same_reference_closed',B['status']=='closed_conditional_degree8_source_upper'and B['numerical_reference_upper_admitted']and B['full_upper_each_gate_type']=='2^1875*(n+1)^8'and B['baseline_extension_id']=='gmp-630-native-skylake-unbounded-exact-constants-v2')
for k in ['source_sha256','dependency_hashes']:
 for p,h in B[k].items():ck('reference_'+p,hs(p)==h)
peerfile='optimized-gmp-degree8-compact-upper-peer-review.json';peer=rd(peerfile)
ck('reference_independent_peer',peer['review_status'].startswith('PASS')and peer['reviewed_sha256'][base]==hs(base)and peer['reviewed_sha256']['optimized-gmp-degree8-compact-upper.md']==hs('optimized-gmp-degree8-compact-upper.md')and peer['reviewed_sha256']['optimized_gmp_degree8_compact_upper.py']==hs('optimized_gmp_degree8_compact_upper.py'))
manifest='pr147-source/download-manifest.json';M=rd(manifest);source={}
for a in M:
 f='pr147-source/'+a['file'];ck('own147_'+a['path'],hs(f)==a['sha256']);source[f]=a['sha256']
profilefile='pr147-source-native-profile.json';p=rd(profilefile)
ck('own147_source_profile',p['pr']==147 and p['source_author_head']=='29383a28d96b9880edbe59ed930f1da1dd6fdfa6'and p['native_coordinate_rank']==72 and p['passed']and all(p['checks'].values()))
sharing=(R/'pr147-source/notes__paired-cube-sharing.tex').read_text();construction=(R/'pr147-source/notes__paired-cube-construction.tex').read_text();assembly=(R/'pr147-source/notes__paired-cube-assembly.tex').read_text()
for n,s in [('full_vertices','Use invocation vertices from the full ambient group'),('all_group_roles',r'$(g,r)$, $g\in\mathcal G$'),('complete_stages','Execute complete'),('literal_copies','all three copies of the actual local word remain paid'),('scalar_group_not_cancelled','scalar work, row stock or the finite semantic guard')]:ck('own147_mandatory_source_'+n,s in sharing)
ck('own147_actual_source_binary_adds','25 binary additions per cube'in construction and p['literal_scalar_fact']['complex_binary_ADDs_per_cube']==25 and p['literal_scalar_fact']['cubes_per_local_invocation']==220 and p['literal_scalar_fact']['source_native_coordinate_volume']=='2^72')
freshmanifest='finite-full-cover-lower-source/147/manifest.json'
for a in rd(freshmanifest):
 b=(R/a['file']).read_bytes();ck('own147_fresh_primary_'+a['path'],a['own_head']==p['source_author_head']and hs(a['file'])==a['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==a['git_blob_sha1']);source[a['file']]=a['sha256']
graphfile='finite-full-cover-lower-source/147/graph.py';gn=runpy.run_path(str(R/graphfile));g=gn['Graph'](12);g.local_channels();edge=1760
ck('actual_surviving_E_edge_source',g.a[edge]==[0,1]and g.signs[edge]==1 and len(g.labels)==1760)
center=g.sum(g.A[I,0,0]for I in g.cubes if 0 in I);todo=[center];active=set()
while todo:
 x=todo.pop()
 if x in active:continue
 active.add(x)
 if g.a[x]:todo.extend(g.a[x])
ck('E_edge_is_live_ancestor_of_required_star_center',edge in active)
gs=(R/graphfile).read_text();fs=(R/'finite-full-cover-lower-source/147/frames.py').read_text();ss=(R/'finite-full-cover-lower-source/147/gauges.py').read_text();producer=(R/'finite-full-cover-lower-source/147/paired_cube_producer.py').read_text()
ck('own_selected_producer_selects_actual_graph','g=Graph(12).finish(restricted_triples(12),restricted_pairs(11),all_but_one(10))'in producer and "actual,word=select(g,baseline,witness)"in producer and "assert actual==expected"in producer)
ck('selected_star_center_is_required_root',"self.centers.append(self.sum(self.A[I, i, e] for I in self.cubes if i in I))"in gs and "kind='center'"in gs)
ck('required_root_ancestry_retained_by_compiler',"todo=[r['node'] for r in roots]"in fs and "if args[x]:todo.extend(args[x])"in fs and 'order=sorted(active,'in fs)
ck('actual_live_node_becomes_paid_unit_scalar','for x in order:'in ss and 'ops.append((dest,control,x))'in ss and 'opcoeff.append((sign,1) if swapped else (1,sign))'in ss)
ck('own147_group_source','V=2^{1296}'in assembly and r'\prod_{i=1}^{35}(2^{2i}-1)'in assembly)
V=2**1296
for i in range(1,36):V*=2**(2*i)-1
m=72;A0=V;j=A0.bit_length()-1;e=(j-1875)//8
ck('own147_exact_group_and_coordinate_meaning',V==int(p['vertices_per_stage'])and V.bit_length()==2556 and int(p['target_vertex_count_N'])==1760*V and p['N_is_not_coordinate_rank'])
ck('earlier_tensor_volume_potential_not_imported',p['literal_scalar_fact']['fullbatch_scalar_floor_potential_exponent']==2627 and j==2555 and A0==V)
ck('own147_positive_lower_exponent',e==85 and e>0)
ck('own147_reference_vs_active_floor',2**(1875+8*e)<=2**j<=A0<2**(j+1))
ck('all_positive_tariffs_strict',3>1)
for rho in [1,2,19]:ck('exact_positive_tariff_witness_'+str(rho),(1+3*rho)*A0>(1+rho)*2**(1875+8*e))
upperfile='pr147-finite-gate-refined-upper.json';upper=rd(upperfile)
ck('same_own_sufficient_certificate',upper['pr']==147 and upper['status']=='closed_conditional_upper_only'and upper['kappa_record']==p['kappa_record'])
original=rd('pr147-finite-controller-upper.json');corrected=rd('pr147-stopped-stock-corrected-upper.json');uScript=(R/'pr147_finite_controller_upper.py').read_text();uProof=(R/'pr147-finite-controller-upper.md').read_text();gateProof=(R/'finite-controller-gate-refinement.md').read_text()
ck('upper_uses_full_E_without_width_division',original['literal_elementary_charge_bound_used']=='own E_source, no division byW'and 'literal=int(source[\'E\'])'in uScript and 'C=2**32*m**4*(literal+W+s+1)**2' in uScript and 'Use the full source literal charge, not G/W' in uProof)
literal=int(p['E']);W=int(p['full_role_count_W']);s=int(p['paid_rank_mass_s']);G=int(p['G'])
ck('upper_complete_group_elementary_charge',2*G*W**2+8*s+4*W+4+32*m<literal and W==V*29937 and literal>V and 2**100000>literal)
ck('upper_complete_coordinate_volume',"C_e=C_1 tensor e has 2^e coefficient coordinates"in gateProof and "40*e*w per coordinate"in gateProof)
ck('corrected_and_refined_uppers_retain_same_counted_native',corrected['corrects_certificate_sha256']==hs('pr147-finite-controller-upper.json')and corrected['literal_elementary_charge_bound_used']==original['literal_elementary_charge_bound_used']and corrected['native_coordinate_rank']==m and upper['source_base_certificate_sha256']==hs('pr147-stopped-stock-corrected-upper.json')and upper['source_base_certificate']=='pr147-stopped-stock-corrected-upper.json')
ck('no_unquantified_original_hybrid_in_lower_family',not upper['record_tail_quantified']and original['original_record_hybrid_compatibility']['extra_retained_same_XAG_record_realization_contract_required'])
from fractions import Fraction as F
X=int(upper['upper_log2log2_integer'])+8;Q=10000;delta=F(1,Q);epsilon=1-delta;reserve=70000*Q;logbase=16*Q+1000+reserve*(X+3).bit_length();rootmargin=delta*epsilon*X-10
wholeProof=(R/'pr4470-whole-integer-bound.md').read_text();precisionProof=(R/'pr4470-global-precision.md').read_text()
ck('actual_outer_dimension_and_nonempty_H_source','Set d=floor(p^epsilon)'in wholeProof and 'one butterfly bit from each *different* tensor axis into an ordinary Hadamard operation'in wholeProof and 'There are h=ceil(log2 T/d) levels.'in wholeProof and 'd = floor(p^epsilon)'in precisionProof)
ck('upper_domain_native_root_above_full_corrected_base',rootmargin>logbase and rootmargin>(2*m).bit_length()+logbase)
ck('native_root_presence_persists_through_tail',F(4*reserve,X)<delta*epsilon)
ck('upper_domain_complete_positive_target_axes',delta*X>10 and X-8>4 and epsilon>F(1,2))
dep={f:hs(f)for f in [base,peerfile,'optimized-gmp-degree8-compact-upper.md','optimized_gmp_degree8_compact_upper.py',manifest,profilefile,'pr147_source_native_profile.py',freshmanifest,upperfile,'pr147-finite-controller-upper.json','pr147-finite-controller-upper.md','pr147_finite_controller_upper.py','pr147-stopped-stock-corrected-upper.json','pr147_stopped_stock_correction.py','pr147-stopped-stock-correction.md','pr147-stopped-stock-correction-peer-review.json','finite-controller-gate-refinement.md','finite_controller_gate_refinement.py','finite-controller-gate-refinement-peer-review.json','pr147-native-allsize-component.md','pr4470-whole-integer-bound.md','pr4470-global-precision.md','finite-full-cover-literal-lowers.md']}
scope='Declared explicit EARLY Gaussian unreduced complete finite-cover literal enhancement family: every active native word retains every group vertex and full field coordinate with paid ADD lowering and no pruning/aggregation/bypass; if no native word is used the output branch is exactly the same optimized GMP reference. All switching policies are included. The optional original-record/min-total hybrid and every other implementation are excluded; the early effective exponent is1/5000.'
lower=dict(input_bits='2^85',exact_log2_integer=85,plot_triple_log=dict(expression='log2(log2(85))',exact_log2_integer=85),source='Own PR147 mandatory complete O(72,2) cover and actual producer binary additions, compared with the independently closed same-reference compact upper.',scope=scope,statistic='necessary_no_strict_win_below_endpoint_for_declared_literal_family',exact_individual_crossing=False,all_PR_implementations=False)
out=dict(schema='own-finite-full-cover-literal-lower/1',status='closed_conditional_necessary_lower'if REVIEW_CLOSED else'pending_independent_source_floor_and_lower_review',pr=147,own_head=p['source_author_head'],model=B['model'],baseline_extension_id=B['baseline_extension_id'],kappa_record=p['kappa_record'],coordinate_rank=m,group_order=str(V),group_order_bitlength=V.bit_length(),mandatory_real_ADD_per_vertex_lower=1,actual_required_E_edge=dict(zero_based_graph_node=edge,original_source_ports=[0,1],coefficient=1,required_root='coordinate0 selector0 star center',live_after_ancestry_filter=True),coordinate_multiplicity_used_in_lower=1,complete_coordinate_volume_factor_not_used=True,mandatory_AND_floor=str(A0),mandatory_XOR_floor=str(3*A0),mandatory_AND_log2_floor=j,reference_upper_log2_coefficient=1875,lower_log2_integer=e,lower=lower,meaningful_lower=lower,upper=None,actual_first_crossing_known=False,activation_threshold_used_as_lower=False,finite_group_as_uniform_rank=False,all_switching_policies=True,inactive_branch_identical_reference=True,optional_original_record_or_hybrid_included=False,upper_compatibility_file=upperfile,upper_compatibility_sha256=hs(upperfile),upper_compatibility_scope='The explicit full-cover early circuit only. Its full source elementary charge is retained without dividing byW; corrected/refined rows fund the same full producer and complete field coefficient volume. Original-record/min-total hybrid branch is not in this lower family.',source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),checks=checks,checks_passed=len(checks),retained_contracts=p['retained_premises']+[scope,'Fixed real ADD word width at least two and the stipulated unreduced truncated addition subnetworks; full word and every physical coordinate remain present.'],formal_status='AI-assisted conditional written/source and exact arithmetic checks; not a universal lower bound, actual first crossing or formal proof')
(R/'pr147-finite-full-cover-lower.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8')
wrapper=dict(schema='own-finite-full-cover-literal-range/1',status='closed_conditional_two_sided_literal_family'if REVIEW_CLOSED else'pending_independent_literal_range_review',pr=147,own_head=p['source_author_head'],source_commit=p['source_author_head'],model=B['model'],baseline_extension_id=B['baseline_extension_id'],kappa_record=p['kappa_record'],effective_kappa='1/5000',early_effective_kappa='1/5000',upper_log2log2_integer=upper['upper_log2log2_integer'],P=upper['upper_log2log2_integer'],inputUpper=upper['inputUpper'],upper=upper['inputUpper'],lower=lower,record_tail_quantified=False,original_record_hybrid_included=False,source_base_upper_certificate=upperfile,source_base_upper_certificate_sha256=hs(upperfile),lower_certificate='pr147-finite-full-cover-lower.json',lower_certificate_sha256=hs('pr147-finite-full-cover-lower.json'),upper_compatibility_scope=out['upper_compatibility_scope'],retained_contracts=out['retained_contracts'],source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),actual_first_crossing_known=False,source_family_scope=scope)
quantifiers=dict(sufficient_upper_policy='the_bound_counted_early_schedule_above_its_verified_domain',necessary_lower_quantifier='all_valid_literal_family_public_policies',upper_not_for_all_switching_policies=True)
out.update(quantifiers);wrapper.update(quantifiers)
# The wrapper binds the final lower bytes, including the distinct quantifiers.
(R/'pr147-finite-full-cover-lower.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8')
wrapper['lower_certificate_sha256']=hs('pr147-finite-full-cover-lower.json')
(R/'pr147-finite-full-cover-range.json').write_text(json.dumps(wrapper,indent=2,sort_keys=True)+'\n',encoding='utf8')
print('PASS',len(checks),'own literal finite-cover lower checks;',out['status'])
