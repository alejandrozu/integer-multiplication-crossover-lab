"""Exact arithmetic/source witnesses for the revised finite-control proof.

The source-case and progress catalogue is a written, peer-reviewed obligation,
not a conclusion of a lexical parser. No numerical reference upper is emitted.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import ast,json,re,tarfile
R=Path(__file__).resolve().parent;D=R/'optimized-gmp-finite-leaf-source';REVIEW_CLOSED=True
checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
def ck(k,v):assert v,k;checks[k]=True
def ceil(q):return -(-q.numerator//q.denominator)
archive='gmp-6.3.0.tar.xz';ah='a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898'
ck('same_original_source_archive',hs(archive)==ah)
lexfile='inventory_optimized_gmp_all_helpers.py';ns={'re':re};module=ast.parse((R/lexfile).read_text())
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n,ast.FunctionDef)and n.name in['clean','nopre','functions','macros','calls']],type_ignores=[]),'<pure source helpers>','exec'),ns)
fdefs={};mac={};raw={}
with tarfile.open(R/archive)as t:
 for a in t.getmembers():
  p=a.name.removeprefix('gmp-6.3.0/')
  if not a.isfile()or not((p.startswith('mpn/generic/')and p.endswith('.c'))or p in['gmp-impl.h','gmp-h.in','longlong.h']):continue
  b=t.extractfile(a).read();raw[p]=b;s=ns['clean'](b.decode('utf8',errors='replace'))
  for name,body,line in ns['functions'](s):fdefs.setdefault(name,[]).append(dict(path=p,body=body,line=line))
  for name,bodies in ns['macros'](s).items():mac.setdefault(name,[]).extend(dict(path=p,body=b)for b in bodies)
product=lambda n:bool(re.fullmatch(r'mpn_(?:mul|mul_n|sqr|mul_fft|nussbaumer_mul|(?:mul|sqr)mod_b[kn]*[mp]1|toom\w*_(?:mul|sqr))',n))
transforms={'mpn_fft_fft','mpn_fft_fftinv','mpn_fft_mul_modF_K','mpn_mul_fft_internal','mpn_mul_fft_full'}
def excluded(n):return product(n)or n in transforms
terminal={'ASSERT','ASSERT_ALWAYS','ASSERT_LIMB','ASSERT_ALWAYS_LIMB','ASSERT_MPN','ASSERT_ALWAYS_MPN','TRACE','ASSERT_NOCARRY','ASSERT_CARRY','ASSERT_MPN_ZERO_P','umul_ppmm','smul_ppmm','udiv_qrnnd','udiv_qrnnd_preinv','udiv_rnnd_preinv','add_ssaaaa','sub_ddmmss','ADDC_LIMB','SUBC_LIMB','binvert_limb','invert_limb','count_leading_zeros','count_trailing_zeros','MPN_COPY','MPN_COPY_INCR','MPN_COPY_DECR','MPN_ZERO','MPN_FILL','MPN_INCR_U','MPN_DECR_U','mpn_incr_u','mpn_decr_u','TMP_ALLOC_LIMBS','TMP_BALLOC_LIMBS','TMP_SALLOC_LIMBS','TMP_BALLOC_MP_PTRS','TMP_BALLOC_TYPE','__GMP_ALLOCATE_FUNC_LIMBS','__GMP_FREE_FUNC_LIMBS','__GMPN_CMP','__GMPN_ADD_1','__GMPN_SUB_1','__GMPN_AORS','__GMPN_AORS_1','__GMPN_COPY','__GMPN_COPY_REST'}
index_only={'mpn_mulmod_bknp1_itch','mpn_mulmod_bnm1_itch','mpn_sqrmod_bknp1_itch','mpn_sqrmod_bnm1_itch'}
macrocycles=[];external_calls=[];indirect_calls=[];terminal_macro_seen=set()
def indirect(text,path,through):
 for token in re.findall(r'\(\s*\*\s*([A-Za-z_]\w*)\s*\)\s*\(',text):indirect_calls.append(dict(token=token,path=path,through_macro=through))
def audit_terminal(n,path,seen=()):
 key=(n,path)
 if key in terminal_macro_seen or n in seen:return
 terminal_macro_seen.add(key)
 ms=[a for a in mac.get(n,[])if a['path']==path]or[a for a in mac.get(n,[])if not a['path'].endswith('.c')]
 for a in ms:
  indirect(a['body'],a['path'],n)
  for token in re.findall(r'\b([A-Za-z_]\w*)\s*\(',a['body']):
   if token in mac:audit_terminal(token,path,seen+(n,))
   elif token not in fdefs:external_calls.append(dict(token=token,path=a['path'],through_macro=n))
  # Object macros such as TMP_FREE have no argument parentheses, but their
  # runtime contents must still enter the explicit external-call audit.
  for token in sorted(set(re.findall(r'\b[A-Za-z_]\w*\b',a['body']))&mac.keys()):audit_terminal(token,path,seen+(n,))
def resolve(text,path,seen=()):
 targets=[];sites=0;indirect(text,path,seen[-1]if seen else None)
 for token in sorted(set(re.findall(r'\b[A-Za-z_]\w*\b',text))&mac.keys()):audit_terminal(token,path)
 for n in re.findall(r'\b([A-Za-z_]\w*)\s*\(',text):
  if n in terminal:audit_terminal(n,path);targets.append('LEAF::'+n);sites+=1;continue
  fs=fdefs.get(n,[]);local=[a for a in fs if a['path']==path]
  if local:targets.extend(a['path']+'::'+n for a in local);sites+=1;continue
  if n.startswith('mpn_')and fs:targets.extend(a['path']+'::'+n for a in fs);sites+=1;continue
  if n in index_only:sites+=1;continue
  ms=[a for a in mac.get(n,[])if a['path']==path]or[a for a in mac.get(n,[])if not a['path'].endswith('.c')]
  if ms and all('__MPN'in a['body']for a in ms)and n.startswith('mpn_'):
   targets.append('LEAF::'+n);sites+=1;continue
  if ms:
   if n in seen:macrocycles.append(seen+(n,));continue
   sub=[resolve(a['body'],path,seen+(n,))for a in ms]
   for tt,cc in sub:targets.extend(tt)
   sites+=sum(cc for tt,cc in sub)
  elif n.startswith(('mpn_','_mpn_')):
   # The only absent optional native symbol is the unselected subrsh
   # alternative. The complete fallback body is independently present.
   ck('unselected_optional_native_'+n,n=='mpn_subrsh');sites+=1;targets.append('LEAF::'+n)
  else:external_calls.append(dict(token=n,path=path,through_macro=seen[-1]if seen else None))
 return sorted(set(targets)),sites
roots=['mpn_mul','mpn_mul_n','mpn_sqr','mpn_mul_fft','mpn_mulmod_bnm1','mpn_sqrmod_bnm1','mpn_mulmod_bknp1','mpn_sqrmod_bknp1','mpn_nussbaumer_mul']
one_loop={'mpn_fft_best_k','mpn_add_n_sub_n','mpn_add_n','mpn_sub_n','mpn_sqr_basecase','mpn_addmul_1','mpn_mul_1','mpn_lshift','mpn_bdiv_dbm1c','mpn_rshift','mpn_divexact_by3c','mpn_toom_eval_pm2rexp','mpn_toom_eval_pm1','mpn_submul_1','mpn_pi1_bdiv_q_1','mpn_divexact_1','mpn_toom_eval_pm2','mpn_toom_interpolate_7pts','mpn_toom_eval_pm2exp','mpn_mul_basecase','_mpn_modbnp1_kn','_mpn_crt','mpn_mod_34lsub1','mpn_mod_1s_2p','mpn_mod_1_norm','mpn_mod_1s_4p_cps','mpn_mod_1_unnorm','mpn_mod_1s_4p','mpn_mod_1s_2p_cps','mpn_mod_1_1p','mpn_mul_fft_decompose','mpn_com','mpn_lshiftc','abs_sub_n','mpn_mul_fft_lcm'}
two_loop={'mpn_fft_initl','_mpn_modbknp1dbnp1_n'}
todo=[a['path']+'::'+n for n in roots for a in fdefs[n]];nodes={};sourcepins={lexfile:hs(lexfile)}
while todo:
 key=todo.pop()
 if key in nodes or key.startswith('LEAF::'):continue
 p,n=key.split('::');bodies=[a for a in fdefs[n]if a['path']==p];calls=set();parts=[]
 for a in bodies:
  tt,ss=resolve(a['body'],p);calls.update(tt);loops=bool(re.search(r'\b(?:for|while)\s*\(',a['body']))
  if not excluded(n):ck('every_ordinary_loop_has_named_progress_case_'+key,not loops or n in one_loop|two_loop)
  ck('expanded_semantic_calls_below_2power16_'+key,ss<2**16)
  parts.append(dict(line=a['line'],body_sha256=sha256(a['body'].encode()).hexdigest(),source_bytes=len(a['body'].encode()),expanded_semantic_call_sites_upper=ss))
 f=D/p;f.parent.mkdir(parents=True,exist_ok=True)
 if f.exists():ck('exact_cached_source_'+p,f.read_bytes()==raw[p])
 else:f.write_bytes(raw[p])
 sourcepins[f.relative_to(R).as_posix()]=sha256(raw[p]).hexdigest()
 nodes[key]=dict(path=p,name=n,calls=sorted(calls),parts=parts,separately_charged_product_or_transform=excluded(n),ordinary_loop_coordinates=2 if n in two_loop else 1 if n in one_loop else 0)
 todo.extend(sorted(calls-nodes.keys()))
ck('no_unresolved_semantic_macro_cycle',not macrocycles)
external_calls=[dict(token=t,path=p,through_macro=m)for t,p,m in sorted({(a['token'],a['path'],a['through_macro']or'')for a in external_calls})]
indirect_calls=[dict(token=t,path=p,through_macro=m)for t,p,m in sorted({(a['token'],a['path'],a['through_macro']or'')for a in indirect_calls})]
external_classes={}
def classify(tokens,label):
 for token in tokens.split():external_classes[token]=label
classify('if for while return sizeof switch __asm__ asm __attribute__ __volatile__ mode _Pragma','C_syntax_cast_asm_or_compiletime_pragma_local_work_charged')
classify('__builtin_expect','branch_hint_identity_local_control_charged')
classify('__builtin_clzl __builtin_clzll __builtin_ctzl __builtin_ctzll','bounded_64bit_word_builtin_in_terminal_tariff')
classify('__UMULH __builtin_alpha_umulh _int_mult_upper _leadz _m64_xmahu','unselected_non_x86_architecture_fixed_word_intrinsic_alternative')
classify('__ALLOCA __gmp_tmp_alloc __gmp_tmp_debug_alloc __gmp_tmp_reentrant_alloc __gmp_tmp_debug_free __gmp_tmp_debug_mark __gmp_tmp_free __gmp_tmp_mark __gmp_tmp_reentrant_free','private_public_sized_allocation_metadata_under_existing_OS_exclusion')
classify('__gmp_assert_fail','unreachable_failure_on_documented_valid_inputs')
classify('CB OP','formal_macro_parameter_bound_to_plus_minus_and_word_carry_comparison')
classify('__gmpn_mod_1_1p __gmpn_mod_1_1p_cps mpn_mod_1_1p_1 mpn_mod_1_1p_2 mpn_mod_1_1p_cps_1 mpn_mod_1_1p_cps_2','unselected_TUNE_PROGRAM_BUILD_alternative')
classify('mpn_subrsh','unselected_HAVE_NATIVE_alternative_explicit_fallback_counted')
classify('printf','disabled_TRACE_diagnostic_not_a_runtime_reference_call')
for a in external_calls:
 ck('external_call_token_has_explicit_class_'+a['token'],a['token']in external_classes)
 a['classification']=external_classes[a['token']]
ck('no_opaque_indirect_arithmetic_function_call',not indirect_calls)
ck('no_external_libc_copy_clear_call_in_reachable_closure',not({'memcpy','memmove','memset','__builtin_memcpy','__builtin_memmove','__builtin_memset'}&{a['token']for a in external_calls}))
gh=raw['gmp-h.in'].decode();gi=raw['gmp-impl.h'].decode();fft_text=raw['mpn/generic/mul_fft.c'].decode()
ck('actual_macro_carry_callback_bindings',all(s in re.sub(r'\\\s*\n',' ',gh)for s in['__GMPN_AORS_1(cout, dst, src, n, v, +, __GMPN_ADDCB)','__GMPN_AORS_1(cout, dst, src, n, v, -, __GMPN_SUBCB)']))
ck('actual_TRACE_compiletime_elision','#ifdef TRACE\n#undef TRACE\n#define TRACE(x) x'in fft_text and '#define TRACE(x)\n'in fft_text)
def trace_ranges(body):
 out=[]
 for a in re.finditer(r'\bTRACE\s*\(',body):
  i=a.end();depth=1
  while depth and i<len(body):depth+=(body[i]=='(')-(body[i]==')');i+=1
  ck('balanced_TRACE_call',depth==0);out.append((a.start(),i))
 return out
for key,node in nodes.items():
 for b in[z['body']for z in fdefs[node['name']]if z['path']==node['path']]:
  spans=trace_ranges(b)
  ck('all_printfs_are_disabled_TRACE_arguments_'+key,all(any(lo<=m.start()<hi for lo,hi in spans)for m in re.finditer(r'\bprintf\s*\(',b)))
ordinary={k:a for k,a in nodes.items()if not a['separately_charged_product_or_transform']}
memo={};stack=[];dimension=2**22;d=dimension+16
def bound(k):
 if k.startswith('LEAF::'):return 2**180
 if k not in ordinary:return 0
 if k in memo:return memo[k]
 a=ordinary[k]
 if a['name']=='mpn_sqr_basecase':memo[k]=2**240;return memo[k]
 ck('ordinary_graph_acyclic_'+k,k not in stack);stack.append(k)
 child=max([2**180]+[bound(c)for c in a['calls']]);b=d**a['ordinary_loop_coordinates']*(2**64+2**16*child)
 stack.pop();memo[k]=b;return b
for k in ordinary:ck('ordinary_helper_below_2power400_'+k,bound(k)<2**400)
ck('generic_square_linear_self_budget',32*d*(2**64+2**16*2**180)<2**240)
nativefile='optimized-gmp-native-loop-bound.json';native=rd(nativefile)
ck('independently_closed_native_component',native['status']=='closed_conditional_component'and native['native_instruction_steps_strict_upper']=='2^172'and int(native['dimension_upper_inclusive'])==dimension and all(native['checks'].values())and native['script_sha256']==hs('audit_optimized_gmp_native_loops.py'))
sourcepins[nativefile]=hs(nativefile);sourcepins['audit_optimized_gmp_native_loops.py']=hs('audit_optimized_gmp_native_loops.py')
for r in native['rows']:ck('native_payload_'+r['path'],hs(r['file'])==r['sha256'])
native_text='\n'.join((R/r['file']).read_text()for r in native['rows'])
native_symbols=set(re.findall(r'\bmpn_[A-Za-z0-9_]+\b',re.sub(r'^\s*C(?:\s|$).*','',native_text,flags=re.M)))
inline_array={'mpn_add','mpn_sub','mpn_add_1','mpn_sub_1','mpn_cmp','mpn_neg','mpn_zero_p','mpn_incr_u','mpn_decr_u'}
optional_disabled={'mpn_addmul_2s','mpn_addmul_3','mpn_addmul_4','mpn_addmul_5','mpn_addmul_6','mpn_sqr_diagonal','mpn_subrsh','mpn_sublsh_n'}
leaf_classes={}
for leaf in sorted({c[6:]for a in nodes.values()for c in a['calls']if c.startswith('LEAF::')}):
 if leaf in optional_disabled:
  ck('optional_native_branch_has_no_selected_body_'+leaf,leaf not in native_symbols)
  ck('optional_native_branch_is_guarded_'+leaf,any(('HAVE_NATIVE_'+leaf)in b.decode()for p,b in raw.items()if p.startswith('mpn/generic/')))
  leaf_classes[leaf]='unselected_HAVE_NATIVE_alternative_no_runtime_callee_asserted'
 elif leaf in inline_array:leaf_classes[leaf]='documented_inline_array_scan_native_pass_and_carry_wrapper'
 elif leaf.startswith('mpn_'):
  ck('selected_native_alias_present_'+leaf,leaf in native_symbols)
  leaf_classes[leaf]='selected_native_body_or_fixed_native_alias'
 else:leaf_classes[leaf]='fixed_word_array_or_public_allocation_macro_separate_written_case'
for p in['gmp-impl.h','gmp-h.in','longlong.h']:
 f=D/p
 if f.exists():ck('exact_macro_header_'+p,f.read_bytes()==raw[p])
 else:f.write_bytes(raw[p])
 sourcepins[f.relative_to(R).as_posix()]=sha256(raw[p]).hexdigest()
header='optimized-gmp-finite-leaf-source/mpn/x86_64/skylake/gmp-mparam.h';h=(R/header).read_text();th={k:int(v)for k,v in re.findall(r'#define\s+((?:MUL|SQR)_[A-Z0-9_]+(?:THRESHOLD|SIZE))\s+(\d+)',h)};sourcepins[header]=hs(header)
ck('actual_MODF_floors',th['MUL_FFT_MODF_THRESHOLD']==404 and th['SQR_FFT_MODF_THRESHOLD']==400)
ck('actual_balanced_FFT_floors',th['MUL_FFT_THRESHOLD']==6272 and th['SQR_FFT_THRESHOLD']==4224)
ck('actual_small_Toom_thresholds',[th[n]for n in['MUL_TOOM22_THRESHOLD','MUL_TOOM33_THRESHOLD','MUL_TOOM44_THRESHOLD','SQR_TOOM2_THRESHOLD','SQR_TOOM3_THRESHOLD','SQR_TOOM4_THRESHOLD']]==[26,73,208,32,117,336])
fft=raw['mpn/generic/mul_fft.c'].decode();bkp=raw['mpn/generic/mulmod_bknp1.c'].decode();impl=raw['gmp-impl.h'].decode()
for name,anchor,text in[
 ('below_MODF_special_split','else if (MPN_MULMOD_BKNP1_USABLE (n, k, MUL_FFT_MODF_THRESHOLD))',fft),
 ('one_majority_full_product','mpn_mul_n (tp, tp + (k - 1) * n * 2, tp + (k - 1) * n * 3, (k - 1) * n)',bkp),
 ('minority_recursion_only','_mpn_mulmod_bnp1_tp (hp + (n + 1) * 2, hp, hp + n + 1, n, hp + (n + 1) * 2)',bkp),
 ('minority_rank_divides_by_k','rn /= k;',bkp),
 ('small_modular_top_correction','for (; (hl = *(rp += k * n)) != 0; )',bkp),
 ('valid_odd_k','ASSERT (k > 2);',bkp),
 ('linear_modular_scratch','return rn << 2;',impl)]:ck('source_anchor_'+name,anchor in text)
def minor_leaves(n):return 1 if n<3 else 1+minor_leaves(n//3)
ck('all_small_BKNP1_chains_at_most_six_full_leaves',max(minor_leaves(n)for n in range(1,404))<=6)
ck('special_majority_products_cannot_restart_full_FFT',404<min(th['MUL_FFT_THRESHOLD'],th['SQR_FFT_THRESHOLD']))
initial=(1<<14)+2;rootmax=ceil(F(9,8)*(initial+1));ck('rounded_root_envelope',rootmax<18440)
ck('array_shift_carry_and_table_dimension_envelope',128*(rootmax+1)<dimension and 32*(rootmax+1)<dimension and 2*rootmax*64<dimension)
audit=rd('optimized-gmp-unbounded-source/audit.json')
ck('actual_fft_tables_fit_dimension',all(len(audit['profiles']['tigerlake_native']['tables'][k])<2**16 for k in['MUL','SQR']))
for m in range(128,initial+1):
 ck('measure_shrink_'+str(m),max(F((m+1)//2+3),F(m,2)+18,F(3,8)*(m+1)+1,F(7,16)*m+2,F(5,9)*m+1)<=F(3,4)*(m+1))
mul=raw['mpn/generic/mul.c'].decode()
ck('actual_X2_remaining_rectangle_Toom_source','/* vn <= un < 3vn */'in mul and 'mpn_toom42_mul (ws, up, un, vp, vn, scratch)'in mul)
ck('actual_X3_remaining_full_product_source','/* vn / 2 <= un < 2.5vn */'in mul and 'mpn_mul (ws, up, un, vp, vn)'in mul and 'un -= 2 * vn;'in mul)
ck('X3_two_piece_rank_envelope',1-2*F(2,9)==F(5,2)*F(2,9)==F(5,9)and F(2,5)<F(5,9))
ck('coalesced_BKNP1_and_restarts_child_count',all(F(27,4)*(m+1)+24<64*(m+1)for m in range(128,initial+1)))
ck('top_correction_two_round_algebra',all((x**q-1)%(x+1)==0 and x*((x**q-1)//(x+1))<x**q for x in[2,4,16,2**64]for q in[2,4,6,12,16]))
tree=1;front=1;ledger=[]
for i in range(17):
 rank=ceil(F(initial+1)*F(3,4)**i);front*=64*rank;tree+=front;ledger.append(dict(level=i,measure=rank,population=str(front)))
ck('seventeen_large_levels',F(initial+1)*F(3,4)**17<=128)
ck('large_product_population',tree<2**284)
small=sum(64**j for j in range(5));ck('four_small_levels',small<2**25)
for m in range(1,128):
 n=m
 for i in range(3):n=(n+1)//2+2
 ck('small_Toom_rank_'+str(m),n<26)
ck('all_finite_product_nodes',tree*small<2**309)
ck('finite_transform_controller_count_reserve',32*6*rootmax*16*2**16*6*4<2**64)
ck('per_product_word_sites_and_helper_calls',2**64*(2**64+2**16*2**400)<2**144*2**400)
ck('complete_finite_instruction_steps',309+144+400==853<864)
proof='optimized-gmp-finite-control-v2.md'
out=dict(schema='same-optimized-GMP-finite-source-control-component/2',status='closed_conditional_source_control_component'if REVIEW_CLOSED else'pending_independent_source_control_review',model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',archive_sha256=ah,source_algorithm_or_threshold_changed=False,analysis_boundary_limbs=2**14,initial_normalized_rank_upper=initial,array_and_native_dimension_upper=dimension,sourcefaithful_word_instruction_steps_strict_power2_upper=864,product_nodes_strict_power2_upper=309,ordinary_helper_steps_strict_power2_upper=400,per_product_outer_multiplier_power2=144,source_graph=nodes,terminal_case_classification=leaf_classes,external_call_token_audit=external_calls,indirect_function_pointer_audit=indirect_calls,ordinary_helper_bitlengths={k:v.bit_length()for k,v in memo.items()},large_tree_ledger=ledger,checks=checks,checks_passed=len(checks),source_sha256=sourcepins,proof_sha256=hs(proof),script_sha256=hs(Path(__file__).name),retained_contracts=['Same source-faithful native/circuit call/cursor compilation interface and fixed64-bit code-text allowance; not an arbitrary C compiler or a new source compiler choice','Valid documented arithmetic, allocated scratch and carry/sentinel regions; private OS allocation/circuit generation excluded as before','Exact original native64-bit no-nails selector, thresholds and v2 carry repair'],numerical_reference_upper_claimed=False,meaningful_lower_claimed=False,remaining_obligations=['Bind separate closed native-loop and opcode components and reprove the unlimited degree8 induction before admitting a new reference bound.'])
(R/'optimized-gmp-finite-control-v2.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf8');print('PASS',len(checks),'revised finite source-control checks; no numerical reference upper')
