"""Source/alias/callee witnesses for the finite native-loop component."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,re,tarfile
R=Path(__file__).resolve().parent;S=R/'optimized-gmp-native-loop-audit-source';S.mkdir(exist_ok=True)
REVIEW_CLOSED=True;checks={}
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(p.read_bytes())
def ck(k,v):assert v,k;checks[k]=True
archive=R/'gmp-6.3.0.tar.xz';ah='a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898'
ck('exact_GMP_archive',hs(archive)==ah)
manifest_file='optimized-gmp-finite-leaf-source/expanded-static-manifest-v2.json';manifest=rd(R/manifest_file)
ck('expanded_manifest_archive',manifest['archive_sha256']==ah)
asm={a['path']:a for a in manifest['source_manifest']if a['path'].endswith('.asm')}
ck('complete123_native_files',len(asm)==123)
with tarfile.open(archive,'r:xz')as tar:
    macros=[]
    for name in ['mpn/asm-defs.m4','mpn/x86_64/x86_64-defs.m4','mpn/x86_64/dos64.m4','mpn/x86_64/darwin.m4','mpn/x86_64/missing-call.m4','mpn/x86_64/missing-inline.m4']:
        data=tar.extractfile('gmp-6.3.0/'+name).read();p=S/Path(name).name
        if p.exists():ck('retained_exact_macro_'+name,p.read_bytes()==data)
        else:p.write_bytes(data)
        macros.append(dict(path=name,file=p.relative_to(R).as_posix(),sha256=hs(p),bytes=len(data),archive_member='gmp-6.3.0/'+name))
text={}
for path,a in asm.items():ck('source_'+path,hs(R/a['file'])==a['sha256']);text[path]=(R/a['file']).read_text()
includes={p:['mpn/'+t for t in re.findall(r"include_mpn\(`([^']+)'\)",s)]for p,s in text.items()}
for p,tt in includes.items():ck('all_include_targets_present_'+p,all(t in asm for t in tt))
def visit(p,stack=()):
    ck('include_acyclic_'+p,p not in stack)
    for t in includes[p]:visit(t,stack+(p,))
for p in asm:visit(p)
def body(p):return text[p]+''.join(body(t)for t in includes[p])
calls={p:re.findall(r'\b(?:T?CALL)\(\s*(mpn_[A-Za-z0-9_]+)\s*\)',s)for p,s in text.items()}
ck('exact_native_callee_set',{t for tt in calls.values()for t in tt}=={'mpn_add_n','mpn_invert_limb','mpn_gcd_11'})
ck('at_most_two_static_call_occurrences',max(map(len,calls.values()))<=2)
for target,paths in {'mpn_add_n':['mpn/x86_64/aors_n.asm','mpn/x86_64/core2/aors_n.asm','mpn/x86_64/coreihwl/aors_n.asm','mpn/x86_64/coreisbr/aors_n.asm'],'mpn_invert_limb':['mpn/x86_64/invert_limb.asm'],'mpn_gcd_11':['mpn/x86_64/gcd_11.asm','mpn/x86_64/core2/gcd_11.asm','mpn/x86_64/coreisbr/gcd_11.asm']}.items():
    ck('callee_is_native_leaf_'+target,all(not any(calls[q]for q in [p,*includes[p]])for p in paths))
    ck('callee_no_indirect_call_'+target,all(not re.search(r'^\s*call[qwl]?\s+\*',body(p),re.M)for p in paths))
ck('no_bare_external_or_indirect_calls',not any(re.search(r'^\s*call[qwl]?\s',s,re.M)for s in text.values()))
ck('no_bare_external_tail_call',not any(re.search(r'^\s*jmp\s+(?:mpn_|GSYM)',s,re.M)for s in text.values()))
emulation=(S/'missing-call.m4').read_text();emu_targets=re.findall(r'\bcall\s+(__gmp_[a-z]+)',emulation)
ck('exact_optional_fixed_emulation_targets',set(emu_targets)=={'__gmp_adox','__gmp_adcx','__gmp_mulx'}and len(emu_targets)==3)
ck('all_fixed_emulation_bodies_present',all('PROLOGUE('+s+')'in text['mpn/x86_64/missing.asm']for s in emu_targets))
ck('fixed_emulation_has_no_calls_or_jumps',not re.search(r'^\s*(?:call|j[a-z]+)\b',text['mpn/x86_64/missing.asm'],re.M))
generator_bounds={'mpn/x86_64/coreibwl/sbpi1_bdiv_r.asm':dict(max_iterations=9,anchor="define(`MAX_SPECIAL', 8)",site='forloop(i,eval(MAX_SPECIAL+1),9,'),'mpn/x86_64/gcd_11.asm':dict(max_iterations=127,anchor='deflit(MAXSHIFT, 7)',site='forloop(i,1,MASK,'),'mpn/x86_64/gcd_22.asm':dict(max_iterations=255,anchor='deflit(MAXSHIFT, 8)',site='forloop(i,1,MASK,'),'mpn/x86_64/invert_limb_table.asm':dict(max_iterations=256,anchor='forloop(i,256,512-1,',site='forloop(i,256,512-1,'),'mpn/x86_64/mod_34lsub1.asm':dict(max_iterations=2,anchor='define(UNROLL,3)',site='forloop(i,1,UNROLL-1,')}
ck('all_five_ASM_forloop_sites_explicitly_bounded',{p for p,s in text.items()if 'forloop('in s}==set(generator_bounds))
for p,g in generator_bounds.items():ck('fixed_m4_generator_'+p,g['anchor']in text[p]and g['site']in text[p]and text[p].count('forloop(')==1 and g['max_iterations']<=256)
ck('mod34_unroll_only_four_plain_add_adc_instructions',bool(re.search(r"forloop\(i,1,UNROLL-1,`dnl\s+add[^\n]+\n\s+adc[^\n]+\n\s+adc[^\n]+\n\s+adc[^\n]+\n'\)",text['mpn/x86_64/mod_34lsub1.asm'])))
quad={'mul_basecase','mullo_basecase','sqr_basecase','redc_1','sbpi1_bdiv_r'}
division={'bdiv_dbm1c','bdiv_q_1','div_qr_1n_pi1','div_qr_2n_pi1','div_qr_2u_pi1','dive_1','divrem_1','divrem_2','mod_1_1','mod_1_2','mod_1_4','mod_34lsub1','mode1o'}
linear={'aorrlsh1_n','aorrlsh2_n','aorrlshC_n','aorrlsh_n','aors_err1_n','aors_err2_n','aors_err3_n','aors_n','aorsmul_1','cnd_aors_n','cnd_add_n','cnd_sub_n','com','com-palignr','copyd','copyd-palignr','copyi','copyi-palignr','hamdist','logops_n','lshift','lshiftc','lshift-movdqu2','lshiftc-movdqu2','lshsub_n','mul_1','mul_2','addmul_1','addmul_2','popham','popcount','rsh1aors_n','rshift','rshift-movdqu2','sqr_diag_addlsh1','sublsh1_n','sublsh2_n','sublshC_n'}
rows=[]
for p,a in asm.items():
    stem=Path(p).stem
    if stem in quad:category='quadratic_size_and_optional_carry';depth=3
    elif stem in division:category='division_reduction_size_and_quotient_carry';depth=3
    elif stem=='sec_tabselect':category='table_entries_times_limb_blocks';depth=2
    elif stem in ['gcd_11','gcd_22']:category='odd_binary_GCD_bitlength_descent';depth=0
    elif stem in ['invert_limb','invert_limb_table','missing']:category='fixed_refinement_static_data_or_simulation';depth=0
    else:ck('explicit_linear_body_class_'+p,stem in linear);category='linear_size_alignment_and_optional_carry';depth=2
    labels={};branches=[];lines=text[p].splitlines()
    for i,l in enumerate(lines,1):
        for lab in re.findall(r'L\(([^)]+)\):',l):labels.setdefault(lab,[]).append(i)
        q=re.search(r'\b(j[a-z]+)\s+L\(([^)]+)\)',l)
        if q:
            prior=[x for x in labels.get(q[2],[])if x<=i]
            if prior:branches.append(dict(line=i,opcode=q[1],target=q[2],target_line=max(prior),source_context=lines[max(0,i-5):i]))
    rows.append(dict(path=p,file=a['file'],sha256=a['sha256'],bytes=a['bytes'],class_name=category,source_review_max_nested_size_passes=depth,reserved_nested_size_passes=6,include_targets=includes[p],native_callees=calls[p],local_backward_branch_witnesses=branches,indirect_local_dispatch_lines=[dict(line=i,text=l.strip())for i,l in enumerate(lines,1)if re.search(r'\bjmp\s+\*',l)]))
cg='optimized-gmp-finite-leaf-source/mpn/generic/gcd_22.c';g=(R/cg).read_text();ck('explicit_odd_GCD_precondition','ASSERT (u0 & v0 & 1)'in g)
ck('assembly_GCD_difference_minimum_progress',all('cmovc' in body(p)and('bsf'in body(p)or'shr'in body(p))for p in asm if Path(p).stem in ['gcd_11','gcd_22']))
ck('static_native_and_macro_text_below_2power20',sum(a['bytes']for a in asm.values())+sum(a['bytes']for a in macros)<2**20)
ck('each_effective_source_below_2power20',max(len(body(p))for p in asm)<2**20)
M=2**22;local=2**32*(M+16)**6
ck('local_loop_envelope_below_2power170',local<2**170)
ck('callee_inclusive_native_below_2power172',3*local<2**172)
ck('looped_call_multiplicity_paid',2**32*((M+16)**3+2*(M+16)**5)<3*local)
ck('GCD_384_passes_dominated',384*2**32<local)
call_composition=dict(D='2^22+16',C='2^32',caller_own_steps_strict_upper='C*D^3',each_static_callsite_visits_upper='D^3',each_native_callee_steps_strict_upper='C*D^2',total_steps_strict_upper='C*(D^3+2*D^5)<3*C*D^6<2^172',static_call_count_is_not_runtime_call_count=True)
out=dict(schema='same-optimized-GMP-finite-native-source-loop-bound/1',status='closed_conditional_component'if REVIEW_CLOSED else'pending_independent_semantic_source_review',archive_sha256=ah,input_manifest_file=manifest_file,input_manifest_sha256=hs(R/manifest_file),rows=rows,macro_sources=macros,native_source_files=len(rows),class_counts=dict(Counter(a['class_name']for a in rows)),native_routine_callee_graph_depth=1,optional_straightline_instruction_emulation_microcall_depth=1,max_explicit_routine_call_occurrences=2,optional_emulation_microcalls_charged_in_static_pass_reserve=True,dimension_upper_inclusive=str(M),static_acyclic_pass_instruction_reserve='2^32',reserved_nested_size_passes=6,native_instruction_steps_strict_upper='2^172',odd_double_limb_GCD_passes_upper=256,odd_single_limb_GCD_passes_upper=128,checks=checks,checks_passed=len(checks),dependency_hashes={cg:hs(R/cg),'optimized-gmp-native-loop-bound.md':hs(R/'optimized-gmp-native-loop-bound.md')},script_sha256=hs(Path(__file__)),retained_required_interfaces=['Valid documented native arithmetic and allocated-array preconditions','C caller separately proves every public array/table/quotient/loop dimension including carry/sentinel region is at most2^22','Selected64-bit no-nails x86-64 configuration; standard fixed instruction macros and aliases, not arbitrary user m4 redefinitions'],scope='Source-backed native call/include/loop component only. Per-file progress classifications and fixed2^32 macro/static expansion reserve are semantic proof obligations separately reviewed, not conclusions of lexical line counting. Saved source backward branches/contexts support that review. No measured runtime/state-space bound, C recursion count, opcode XAG tariff, complete multiplication upper or numerical crossover is claimed.')
out['looped_native_call_composition']=call_composition
out['fixed_ASM_m4_generator_bounds']=generator_bounds
(R/'optimized-gmp-native-loop-bound.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'native source/closure/loop arithmetic checks;',len(rows),'ASMfiles; closedconditionalcomponent')
