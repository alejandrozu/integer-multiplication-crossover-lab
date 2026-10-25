"""Separate smaller degree-eight source upper; frozen reference algorithms unchanged."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json,re
R=Path(__file__).resolve().parent;REVIEW_CLOSED=True;checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(n,v):assert v,n;checks[n]=True
model='xag-straightline-v1';baseline='gmp-630-native-skylake-unbounded-exact-constants-v2'
dep={};source={}
def bind(f):dep[f]=hs(f);return rd(f)
def peer(f,targets):
 a=bind(f);ck('peer_PASS_'+f,a['review_status'].startswith('PASS'))
 for t in targets:ck('peer_bound_'+f+'_'+t,a['reviewed_sha256'][t]==hs(t))
 for p,h in a['reviewed_sha256'].items():ck('peer_payload_'+f+'_'+p,hs(p)==h)
 return a
old=bind('optimized-gmp-upper-recurrence.json');degree=bind('optimized-gmp-degree8-upper.json')
ck('frozen_original_recurrence',hs('optimized-gmp-upper-recurrence.json')=='0ae22a2306d99ee19391082bf0902dad6008c182c71cd1e489ab29adb28226ff'and old['full_upper_closed']and old['native_nonrecursive_census_closed'])
ck('same_reference_identity',old['baseline_extension_id']==baseline==degree['baseline_extension_id'])
for p,h in old['source_sha256'].items():
 p='optimized-gmp-upper-source/'+p;ck('unchanged_original_source_'+p,hs(p)==h);source[p]=h
for p in ['optimized-gmp-upper-recurrence.md','optimized-gmp-degree8-upper.md','optimized-gmp-semantic-repair.json','optimized-gmp-unbounded-source/audit.json']:
 dep[p]=hs(p)
ck('same_multiword_semantic_repair',hs('optimized-gmp-semantic-repair.json')==old['semantic_repair_sha256'])
ck('same_original_native_selector',hs('optimized-gmp-unbounded-source/audit.json')==old['baseline_audit_sha256'])
control=bind('optimized-gmp-finite-control-v2.json');op=bind('optimized-gmp-opcode-arity.json');native=bind('optimized-gmp-native-loop-bound.json')
ck('closed_control',control['status']=='closed_conditional_source_control_component'and all(control['checks'].values())and control['script_sha256']==hs('optimized_gmp_finite_control_v2.py')and control['proof_sha256']==hs('optimized-gmp-finite-control-v2.md'))
ck('closed_opcode',op['status']=='closed_source_bound_native_opcode_arity_component'and all(op['checks'].values())and op['script_sha256']==hs('optimized_gmp_opcode_arity.py')and op['proof_sha256']==hs('optimized-gmp-opcode-arity.md'))
ck('closed_native',native['status']=='closed_conditional_component'and all(native['checks'].values())and native['script_sha256']==hs('audit_optimized_gmp_native_loops.py'))
ck('same_component_source_archive',control['archive_sha256']==native['archive_sha256']=='a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898')
ck('component_baseline_identity',control['model']==op['model']==model and control['baseline_extension_id']==op['baseline_extension_id']==baseline)
for a in [control,op,native]:
 for key in ['source_sha256','dependency_hashes']:
  for p,h in a.get(key,{}).items():ck('component_payload_'+p,hs(p)==h);source[p]=h
for p in ['optimized_gmp_finite_control_v2.py','optimized-gmp-finite-control-v2.md','optimized_gmp_opcode_arity.py','optimized-gmp-opcode-arity.md','audit_optimized_gmp_native_loops.py','optimized-gmp-native-loop-bound.md']:
 dep[p]=hs(p)
peer('optimized-gmp-opcode-arity-peer-review.json',['optimized-gmp-opcode-arity.json','optimized-gmp-opcode-arity.md','optimized_gmp_opcode_arity.py'])
peer('optimized-gmp-native-loop-bound-peer-review.json',['optimized-gmp-native-loop-bound.json','optimized-gmp-native-loop-bound.md','audit_optimized_gmp_native_loops.py'])
peer('optimized-gmp-finite-control-v2-secondary-peer-review.json',['optimized-gmp-finite-control-v2.json','optimized-gmp-finite-control-v2.md','optimized_gmp_finite_control_v2.py'])
# Root's independent primary control receipt is mandatory once this component closes.
primary='optimized-gmp-finite-control-v2-peer-review.json'
if (R/primary).exists():peer(primary,['optimized-gmp-finite-control-v2.json','optimized-gmp-finite-control-v2.md','optimized_gmp_finite_control_v2.py'])
else:ck('primary_control_peer_pending_only_in_unclosed_draft',not REVIEW_CLOSED)
m0=2**14;Bexp=1740;Lexp=1872;Dexp=1280
ck('finite_source_boundary',control['analysis_boundary_limbs']==m0 and control['initial_normalized_rank_upper']==m0+2)
ck('all_native_dimensions_paid',control['array_and_native_dimension_upper']==int(native['dimension_upper_inclusive'])==2**22)
ck('complete_source_step_bound',control['sourcefaithful_word_instruction_steps_strict_power2_upper']==864 and 309+144+400==853<864)
ck('complete_opcode_step_bound',op['instruction_input_bits_upper']==op['instruction_output_bits_upper']==768 and op['data_instruction_per_type_gates_power2_upper']==800 and op['finite_step_per_type_gates_power2_upper']==870)
ck('finite_run_gate_coefficient',864+870==1734 and 64*2**1734==2**Bexp)
ck('finite_halt_output_and_initial_state_slack',2**1734+8*2**870+2**80<2**Bexp)
census=old['source_census_review']
ck('unchanged_structural_position_factors',census['nonrecursive_positions']=='2^128*(x+1)^4'and census['word_instruction_positions_per_call']=='2^256*(x+1)^2'and census['local_memory_mux_factor']=='2^32*(x+1)^2')
ck('original_loose_data_estimate_only_replaced',census['non_ADD_opcode_gate_bound']=='2^8192 per gate type'and 128+256+800+32==1216<Dexp==op['candidate_nonrecursive_D_power2'])
mp='optimized-gmp-finite-leaf-source/mpn/generic/mul.c';mtext=(R/mp).read_text();hp='optimized-gmp-finite-leaf-source/mpn/x86_64/skylake/gmp-mparam.h';htext=(R/hp).read_text()
thresholds={k:int(v)for k,v in re.findall(r'#define\s+((?:MUL|SQR)_[A-Z0-9_]+THRESHOLD)\s+(\d+)',htext)}
for p in [mp,hp]:source[p]=hs(p)
ck('actual_nonFFT_chunk_thresholds',thresholds['MUL_TOOM22_THRESHOLD']==26 and thresholds['MUL_TOOM33_THRESHOLD']==73 and thresholds['MUL_FFT_THRESHOLD']==6272 and thresholds['SQR_FFT_THRESHOLD']==4224)
for name,anchor in [('basecase500','#define MUL_BASECASE_MAX_UN 500'),('X2_shorter','BELOW_THRESHOLD (vn, MUL_TOOM33_THRESHOLD)'),('nonFFT_OR','BELOW_THRESHOLD ((un + vn) >> 1, MUL_FFT_THRESHOLD) ||'),('nonFFT_shorter','BELOW_THRESHOLD (3 * vn, MUL_FFT_THRESHOLD)'),('X3_chunk','mpn_toom63_mul (ws, up, 2 * vn, vp, vn, scratch)'),('X3_remainder','/* vn / 2 <= un < 2.5vn */'),('balanced44_ratio','#define TOOM44_OK(an,bn) (12 + 3 * an < 4 * bn)')]:ck('actual_nonFFT_source_'+name,anchor in mtext)
ck('selected_no_mul2_basecase_exception','#undef HAVE_NATIVE_mpn_mul_2'in htext and'|| vn == 1'in mtext)
ck('X2_complete_chunks_finite',3*(thresholds['MUL_TOOM33_THRESHOLD']-1)<m0)
ck('nonFFT_average_arm_whole_input_finite',2*thresholds['MUL_FFT_THRESHOLD']<m0)
short=(thresholds['MUL_FFT_THRESHOLD']-1)//3
ck('nonFFT_shorter_arm_chunks_and_remainders_finite',short==2090 and 2*short<m0 and F(5,2)*short<m0 and F(4,3)*short<m0)
ck('balanced_nonFFT_and_modF_base_jobs_finite',max(thresholds['MUL_FFT_THRESHOLD'],thresholds['SQR_FFT_THRESHOLD'],404+2)<m0)
crt=(F(9,8)*(1+F(1,m0)))**8/(1-F(1,256));restart=8*24*F(9,16)**8;block=8*F(12,128)
ck('active_child_mass',F(16,128)==F(1,8))
ck('CRT_root_mass_at_new_boundary',crt<3)
ck('restart_source_rank_domain',F(m0+1,2)+17<=F(9,16)*(m0+2)and F(263,2)+17==F(9,16)*(263+1))
ck('four_length_variants_restart_mass',restart<2)
ck('blocking_mass',block==F(3,4))
leaf=F(2**(Bexp+128),2**Lexp);nonrec=F(2**Dexp,2**Lexp)
ck('finite_starting_cases',Bexp<Lexp)
ck('local_leaf_charge',leaf==F(1,16)<F(1,4))
ck('nonrecursive_charge',nonrec<F(1,4))
ck('T_induction_budget',F(1,8)+leaf+nonrec<1)
ck('ordinary_F_induction_budget',crt+restart+leaf+nonrec<8)
ck('blocking_F_induction_budget',block+leaf+nonrec<8)
ck('unchanged_algorithmic_cutoffs',str(2**20)==old['finite_leaf_cutoff_limbs']==degree['finite_leaf_cutoff_limbs']and not control['source_algorithm_or_threshold_changed']and not op['source_algorithm_or_threshold_changed'])
ck('final_bitlength_mapping',Lexp+3==1875)
proof='optimized-gmp-degree8-compact-upper.md';dep[proof]=hs(proof)
out=dict(schema='same-optimized-GMP-compact-degree8-source-upper/1',status='closed_conditional_degree8_source_upper'if REVIEW_CLOSED else'pending_independent_combined_source_induction_review',model=model,baseline_extension_id=baseline,reference_algorithm_changed=False,reference_circuit_compilation_contract_changed=False,finite_analysis_boundary_limbs=m0,previous_frozen_analysis_boundary_limbs=2**20,algorithmic_dispatch_cutoff_changed=False,finite_step_count_power2_upper=864,finite_step_gate_count_power2_upper=870,finite_leaf_pertype_gate_count_power2_upper=Bexp,unbounded_nonrecursive_pertype_gate_count_coefficient_power2=Dexp,induction_L_power2=Lexp,full_upper_each_gate_type='2^1875*(n+1)^8',full_upper_coefficient_log2=1875,exponent=8,retains_all_four_length_variants=True,actual_instruction_counts_claimed=False,numerical_reference_upper_admitted=REVIEW_CLOSED,source_family_endpoints_changed=False,meaningful_lower_claimed=False,exact_budget_fractions=dict(active_child=str(F(1,8)),CRT_roots=str(crt),four_variant_restarts=str(restart),blocking=str(block),local_finite_leaves=str(leaf),nonrecursive=str(nonrec)),source_sha256=source,dependency_hashes=dep,script_sha256=hs(Path(__file__).name),proof_sha256=hs(proof),checks_passed=len(checks),checks=checks,retained_contracts=control['retained_contracts']+old['retained_assumptions']+['Fixed-data opcode refinement and actual native source preconditions, with source-faithful call/cursor compilation as pinned in the three components; no arbitrary compiler or pinned machine binary claim.','Explicit unbounded public indices and data-dependent local memory/carry selection remain charged by the original structural factors.','No published source-family endpoint is modified by this separate reference-bound component.'],formal_status='AI-assisted conditional written source proof and exact checks; not a formal source translation, Lean proof, independent human review, practical cost count or first crossing')
(R/'optimized-gmp-degree8-compact-upper.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8')
print('PASS',len(checks),'combined degree8 compact source-upper checks;',out['status'])
