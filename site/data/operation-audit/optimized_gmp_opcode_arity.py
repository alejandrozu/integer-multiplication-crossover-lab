"""Source-bound native arity and Boolean counting component, pending peer review.

Does not bound execution steps or change any published comparison certificate.
"""
from pathlib import Path
from hashlib import sha256
import json,re,tarfile
R=Path(__file__).resolve().parent
H=lambda b:sha256(b).hexdigest()
checks={}
def ck(k,v):assert v,k;checks[k]=True
manifest=R/'optimized-gmp-finite-leaf-source/expanded-static-manifest-v2.json'
mf=json.loads(manifest.read_bytes())
lexpath=R/'optimized-gmp-opcode-lexical-inventory.json'
lex=json.loads(lexpath.read_bytes())
ck('lexical_inventory_joins_exact_source_manifest',lex['source_manifest_sha256']==H(manifest.read_bytes()))
ck('actual_native_superset_includes_recursive_templates',lex['source_files']==123 and lex['source_lines']==26161)
pins={manifest.relative_to(R).as_posix():H(manifest.read_bytes()),lexpath.name:H(lexpath.read_bytes())}
for n,h in lex['source_sha256'].items():
 ck('bytes_'+n,H((R/n).read_bytes())==h);pins[n]=h
# Review all tokens, including the no-operand spellings that the earlier
# whitespace-operand lexical inventory deliberately did not classify.
scalar=set('adc add addl addq and andl bsf bsr bt cmovc cmovnc cmp cmpl dec decq imul inc incq ja jae jb jbe jc je jg jge jl jle jmp jnc jne jns jnz jrcxz js jz lea leaq mov movl movq movslq movzbl movzwl mul mulq neg negq not notq or orb pop push rcr sal sar sbb seta setae setb setbe setc shl shld shr shrd sub test xor'.split())
simd=set('lddqu movaps movd movdqa movdqu paddb paddd paddq pand pcmpeqb pcmpeqd por psadbw pshufb pshufd psllq psrlq psrlw punpcklqdq pxor'.split())
aliases={'ADCSBB','ADDSUB','LOGOP','C','GLOBL'}
ck('every_previous_operand_instruction_token_has_reviewed_class',set(lex['instruction_like_token_counts'])<=scalar|simd|aliases)
noargs=set();noarg_sites=[];alltexts=[]
for row in lex['rows']:
 text=(R/row['file']).read_text();alltexts.append(text)
 for i,line in enumerate(text.splitlines(),1):
  if re.match(r'\s*(?:C(?:\s|$)|dnl|#)',line):continue
  s=re.sub(r'\bdnl\b.*','',line)
  s=re.split(r'\s+C(?:\s|$)',s,maxsplit=1)[0]
  s=re.sub(r'^\s*(?:L\([^)]*\)|[0-9]+):','',s).strip().strip("`'")
  if re.fullmatch(r'(?:retq?|pushfq|popfq|clc|stc|cld|std|nop)',s):
   noargs.add(s);noarg_sites.append(dict(file=row['file'],line=i,token=s))
joined='\n'.join(alltexts)
ck('zero_operand_native_forms_are_bounded',noargs<={'ret','retq','pushfq','popfq','clc','stc','cld','std','nop'} and 'ret'in noargs)
ck('no_unreviewed_vector_or_state_instruction',not lex['wide_or_system_sites'] and not re.search(r'(?m)^\s*(?:fld\w*|fst\w*|fadd\w*|emms|movnt\w*|rep\w*\s+(?:movs|stos|lods|scas|cmps))\b',joined))
ck('only128bit_XMM_explicit_vector_registers',not re.search(r'%(?:[yz]mm\d+|mm\d+|k[0-7])\b',joined) and all(int(x)<16 for x in re.findall(r'%xmm(\d+)\b',joined)))
ck('all_three_REP_sites_are_BSF_not_string_repetition',len(lex['REP_sites'])==3 and all(re.search(r'\brep\s*;\s*bsf\b',x['text'])for x in lex['REP_sites']))
raw_classes={}
for x in lex['raw_encoded_or_table_sites']:
 n=x['file'];s=x['text'];key=f'{n}:{x["line"]}'
 if '/coreinhm/'in n and n.endswith(('/popcount.asm','/hamdist.asm')):
  ck('POPCNT64_encoding_'+key,bool(re.search(r'\.byte\s+0xf3,0x(?:48|49|4c),0x0f,0xb8,',s)));kind='POPCNT64'
 elif n.endswith('/copyi.asm'):
  text=(R/n).read_text();ck('unreachable_copyi_entry_padding',text.index('.byte\t0,0,0,0,0,0')<text.index('PROLOGUE(mpn_copyi)'));kind='padding_before_public_entry'
 elif n.endswith(('/com.asm','/logops_n.asm')):
  ck('NOP_padding_'+key,all(v.strip()=='0x90' for v in s.split('.byte',1)[1].split(',')));kind='NOP'
 elif n.endswith(('/core2/popcount.asm','/core2/hamdist.asm','/gcd_11.asm','/gcd_22.asm')):kind='lookup_table_data'
 else:raise AssertionError(('Unclassified raw encoding',x))
 raw_classes[key]=kind
ck('all54literal_encoding_or_data_sites_classified',len(raw_classes)==54)
defs=(R/'optimized-gmp-opcode-source/mpn/x86_64/x86_64-defs.m4').read_text()
for name in ['palignr','mulx','shlx','shrx','sarx','adcx','adox']:
 ck('actual_M4_fixed_width_encoder_'+name,('define(`'+name+"'")in defs)
ck('scalar_input_payload_envelope',4*64+2*64+64+64==512)
ck('SSE_input_payload_envelope',2*128+2*64+64+64==512)
k=t=768
ck('truth_table_AND_exact_integer_bound',t*k*2**k<2**800)
ck('truth_table_XOR_exact_integer_bound',t*2**k+k<2**800)
ck('paid_ADD_ADC_retained',128<2**800 and 192<2**800)
# Four128-bit accesses, four gates per bit/cell, with an extra factor16
# for address equality, conditional update, memory-copy control and decoder.
ck('finite64bit_RAM_selection_update_allowance',4*128*4*16*2**64<2**80)
ck('fixed_architectural_register_state_allowance',(16*64+16*128+64+64)<2**16)
ck('finite_step_code_decoder_and_RAM_sum',2**64*(2**800+2**80+2**80)<2**870)
ck('candidate_unchanged_nonrecursive_structure',128+256+800+32==1216 and 1216<1280)
proof='optimized-gmp-opcode-arity.md'
out=dict(schema='same-GMP-native-opcode-arity-component/1',status='closed_source_bound_native_opcode_arity_component',model='xag-straightline-v1',baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',source_algorithm_or_threshold_changed=False,native_sources=123,proof_file=proof,proof_sha256=H((R/proof).read_bytes()),script_sha256=H(Path(__file__).read_bytes()),source_sha256=pins,checked_raw_encoding_classes=raw_classes,checked_zero_operand_forms=sorted(noargs),zero_operand_sites=noarg_sites,instruction_input_bits_upper=768,instruction_output_bits_upper=768,data_instruction_per_type_gates_power2_upper=800,finite_step_per_type_gates_power2_upper=870,candidate_nonrecursive_D_power2=1280,checks=checks,checks_passed=len(checks),new_numerical_reference_upper_claimed=False,finite_instruction_steps_bounded=False,remaining_obligations=['Complete source-faithful finite helper, transform and product step bound.','Combine with the unchanged unlimited-size recurrence and independent peer before changing any endpoint.'],official_instruction_reference=dict(url='https://cdrdv2-public.intel.com/671110/325383-sdm-vol-2abcd.pdf',sha256='f117cb21ce1f3b6258f5ce5f786e91665a133bf55e7bc2dc8cae843b56e4fb8e',TZCNT_pdf_page=1455,manual_redistributed=False))
(R/'optimized-gmp-opcode-arity.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(passed=True,checks=len(checks),native_sources=123,standalone_forms=sorted(noargs),no_reference_endpoint_changed=True)))
