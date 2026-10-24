"""Fresh own1154/1176 actual native/whole-owner/invoice inputs.

The original dynamic provider selection is preserved. A new explicit numerical
PLAN registry records those same calls; it is not claimed to be a historical
committed whole PLAN. No old billed amount or cutoff is imported.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import copy,gzip,hashlib,importlib.util,json,subprocess,sys
R=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)
def hs(f):return hashlib.sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 p=R/f;b=p.read_bytes();return json.loads(gzip.decompress(b)if p.suffix=='.gz'else b)
def ident(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def module(n):
 s=importlib.util.spec_from_file_location(n,R/(n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
nativec=module('finite_selected_program_census');ownerc=module('finite_actual_owner_census_v2')
manifest=rd('kernel-demotions-source/manifest.json');checks={}
own_heads={x['pr']:x['own_head_sha']for x in rd('remaining-record-audit/complete-audit-queue.json')['rows']}
def ck(n,v):assert v,n;checks[n]=True
ck('complete_own_source_inventories',manifest['source_inventories_exact'])
for a in manifest['objects']:ck('primary_'+a['file'],hs(a['file'])==a['sha256'])
D=R/'kernel-demotions-counted-source';D.mkdir(exist_ok=True)
rows=[]
for pr,V in[(1154,5),(1176,3)]:
 pre=str(pr)+'_';assets=[x for x in manifest['objects']if x['pr']==pr]
 def a(rel):return next(x for x in assets if x['relative']==rel)
 def obj(rel):return rd(a(rel)['file'])
 pkg=manifest['packages'][str(pr)];M=rd(pkg['MANIFEST_file']);ver=a('verify.py');vs=(R/ver['file']).read_text()
 ck(pre+'complete_actual_own_manifest_and_head',pkg['own_head']==own_heads[pr]and hs(pkg['MANIFEST_file'])==pkg['MANIFEST_sha256']and {x['relative']:x['sha256']for x in assets}==M and all(x['own_head']==pkg['own_head']for x in assets))
 ck(pre+'own_manifest_entrypoint',M['verify.py']==ver['sha256'])
 oldspecpath='vendor/pr1117/data/SPEC.json'if pr==1154 else'vendor/pr1148/SPEC.json'
 oldspec=obj(oldspecpath);oldprovider=oldspec['providers']['gauge44']
 ck(pre+'dynamic_actual_source_selector',"local/check_local.py"in vs and"data/DISPATCH.json"in vs and oldspecpath in vs and("audit_mixed.py"in vs if pr==1154 else"audit_candidate.py"in vs))
 oldnative=R/'kernel-demotions-old-selected-native'/str(pr);oldnative.mkdir(parents=True,exist_ok=True)
 oldcanonical=a('local/data/OLD-CANONICAL-WORD.json.gz');(oldnative/'CANONICAL-WORD.json.gz').write_bytes((R/oldcanonical['file']).read_bytes())
 emitter=a('local/vendor/hpe_emit_local.py')
 cp=subprocess.run([sys.executable,'-I','-B',str(R/emitter['file']),str(oldnative)],capture_output=True,text=True,timeout=120)
 ck(pre+'unchanged_old_emitter_exit',cp.returncode==0)
 oldprogramfile=(oldnative/'LOCAL-PROGRAMS.json.gz').relative_to(R).as_posix();oldprogram=rd(oldprogramfile)
 ck(pre+'old_selected_complete_program_and_orientations',ident(oldprogram)==oldprovider['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and{o:ident(oldprogram[o])for o in oldprogram}==oldprovider['program_hashes'])
 providers={};nativecost={};bindings=[];source={a['file']:a['sha256']for a in assets}
 for k in range(V+1):
  pid=str(k);wp=oldcanonical['file']if k==0 else f'kernel-demotions-fresh-replay/{pr}/provider-{k}/native/CANONICAL-WORD.json.gz'
  pf=oldprogramfile if k==0 else f'kernel-demotions-fresh-replay/{pr}/provider-{k}/native/LOCAL-PROGRAMS.json.gz'
  w,program=rd(wp),rd(pf)
  if k:
   ew=obj(f'local/data/EXPECTED-{k}-CANONICAL-WORD.json.gz');ck(pre+pid+'_own_expected_canonical',w==ew)
   emitted=R/'kernel-demotions-counted-source'/str(pr)/('fresh-emitted-'+pid);emitted.mkdir(parents=True,exist_ok=True);(emitted/'CANONICAL-WORD.json.gz').write_bytes((R/wp).read_bytes())
   er=subprocess.run([sys.executable,'-I','-B',str(R/emitter['file']),str(emitted)],capture_output=True,text=True,timeout=120)
   ck(pre+pid+'_own_unchanged_emitter_reproduces_full_program',er.returncode==0 and rd((emitted/'LOCAL-PROGRAMS.json.gz').relative_to(R))==program)
   replay=rd(f'kernel-demotions-fresh-replay/{pr}/provider-{k}/native/INDEPENDENT-LOCAL-REPLAY.json')
   ck(pre+pid+'_fresh_complete_program_binding',replay['canonical_word_sha256']==hs(wp)and replay['local_programs_sha256']==hs(pf))
  else:ck(pre+'old_expected_canonical',ident(w)==oldprovider['artifact_semantic_sha256']['CANONICAL-WORD.json.gz'])
  c=nativec.census(program,canonical=w);f=c['forward'];ck(pre+pid+'_native_dimensions',(w['v'],w['h'],w['R'],f['columns'])==(112,9,480,704))
  first=2*w['v'];initial=[len(w['frames'][i])for i in w['start'][first:]];final=[len(w['frames'][i])for i in w['final'][first:]]
  ck(pre+pid+'_actual_partial_helper_ranks',[b-a for a,b in zip(initial,final)]==f['widths']and all(ownerc.basis(w['frames'][i]+w['frames'][j])==ownerc.basis(w['frames'][j])for i,j in zip(w['start'][first:],w['final'][first:])))
  p=dict(columns=f['columns'],helpers=f['helpers'],widths=f['widths'],paid_profile={int(r):n for r,n in f['paid_profile'].items()},prefix_bits=max(x['prefix_bits']for x in c.values()),entering_flags=[bool(x)for x in initial],initial_helper_ranks=initial,final_helper_ranks=final)
  adapter=16*(max(x['scalar_macros']for x in c.values())+sum(p['paid_profile'].values())+f['columns']+8)+64*73
  ck(pre+pid+'_full_event_adapter_allowance',all(x['events']<adapter for x in c.values()))
  providers[pid]=p;nativecost[pid]=dict(local=c,adapters=adapter)
  dest=D/str(pr)/('provider-'+pid+'-census.json');dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(c,indent=2)+'\n',encoding='utf8')
  bindings.append(dict(provider=pid,canonical_file=wp,canonical_file_sha256=hs(wp),semantic_canonical_sha256=ident(w),program_file=pf,program_file_sha256=hs(pf),semantic_program_sha256=ident(program),orientation_sha256={o:ident(program[o])for o in program},census_file=dest.relative_to(R).as_posix(),census_sha256=hs(dest.relative_to(R)),initial_helper_ranks=initial,final_helper_ranks=final,entering_flags=p['entering_flags']))
  source.update({wp:hs(wp),pf:hs(pf)})
 planrel='vendor/pr1117/data/PLAN.json'if pr==1154 else'data/PLAN.json';plan=copy.deepcopy(obj(planrel));plan.update(K=4,M=73,L=9,live=896*plan['T'])
 changes=obj('data/DISPATCH.json');order=[tuple(x)for x in plan['order']];dispatch={call:'0'for call in order};seen=set()
 for z in changes:
  call=tuple(z['call']);ck(pre+'dispatch_time_'+str(z['time']),call==order[z['time']]and call not in seen and 1<=z['variant']<=V);seen.add(call);dispatch[call]=str(z['variant'])
 roles=obj('data/OWNERS.json.gz');parentowners='vendor/pr1117/data/OWNERS.json.gz'if pr==1154 else'vendor/pr1148/OWNERS.json.gz';edits=obj('data/EDITS-FROM-PR1117.json'if pr==1154 else'data/EDITS-FROM-PR1148.json');rebuilt=obj(parentowners);edited=set()
 for z in edits:
  i=z['index'];ck(pre+'own_literal_owner_edit_'+str(i),i not in edited and rebuilt[i]==z['before']);edited.add(i);rebuilt[i]=z['after']
 ck(pre+'entire_own_owner_edit_result',rebuilt==roles and len(roles)==69120)
 proto=obj('inputs/ROUND20-PARENT-TEMPLATE.json.gz');phases=obj('inputs/DATA-PHASES.json');ports=rd(oldcanonical['file'])['ports'];ctx=ownerc.context(proto,phases,ports,plan,roles,dispatch,providers);role=ownerc.audit(ctx,roles);neg=ownerc.controls(ctx,roles)
 expected=obj('expected/EXACT-PRICE.json');sourceaudit=rd(f'kernel-demotions-fresh-replay/{pr}/OWNER-AUDIT.json')
 ck(pre+'own_complete_profile_mass_deficit',role['profile']=={int(r):n for r,n in expected['profile'].items()}and role['profile']=={int(r):n for r,n in sourceaudit['profile'].items()}and role['rank_mass']==sourceaudit['rank_mass']and role['rank_surplus']==sourceaudit['deficit'])
 ck(pre+'own_owner_geometry_agreement',role['cross_replica_helpers']==sourceaudit['cross_replica']and role['actual_73_axis_charts']==sourceaudit['actual_73column_sigmas']and role['idle']=={int(r):n for r,n in sourceaudit['idle_profile'].items()})
 ck(pre+'own_payload_and_row',role['prefix_bits']<role['charged_prefix_bits']and role['physical_row_coefficient']<20161)
 stageorient={c['stage']:c['orientation']for c in proto['calls']};plan['provider_registry']={pid:dict(ports=ports,widths=p['widths'],orientation_program_sha256=next(b['orientation_sha256']for b in bindings if b['provider']==pid),actual_paid_profile=p['paid_profile'])for pid,p in providers.items()};plan['provider_calls']=[dict(time=t,stage=s,replica=r,provider=dispatch[s,r],orientation=stageorient[s],local_program_sha256=plan['provider_registry'][dispatch[s,r]]['orientation_program_sha256'][stageorient[s]])for t,(s,r)in enumerate(order)];plan['per_call_widths']=[dict(time=t,stage=s,replica=r,widths=providers[dispatch[s,r]]['widths'])for t,(s,r)in enumerate(order)]
 plan['numeric_realization_provenance']='New explicit complete native registry and original own literal call order/windows/dispatch. This is not claimed to be a historically committed whole PLAN.'
 planfile=f'kernel-demotions-counted-source/{pr}/NUMERIC-PLAN.json';(R/planfile).write_text(json.dumps(plan,sort_keys=True,separators=(',',':'))+'\n',encoding='utf8')
 scalar=wrappers=0
 for s,r in order:
  z=nativecost[dispatch[s,r]]['local'][stageorient[s]];scalar+=z['real_component_primitives'];wrappers+=(z['pre_wrappers']+z['post_wrappers'])*144
 T=plan['T'];groups=(T+7)//8;live=role['live'];physical=role['physical'];parentlive=11704*groups-896*(8*groups-T);parentphysical=parentlive+514;parentidle=16128*groups;banks=504*groups;calls=role['calls'];helpers=role['helpers_max'];bridges=2*112*role['bridges'];shifts=4*112*T;moves=2*shifts;adapters=max(z['adapters']for z in nativecost.values());compiler=64*74**3
 items=4*112*T*9+2*112*T*9+2*calls*helpers+parentidle+9*banks+bridges+shifts+moves+parentlive+parentphysical+wrappers;outside=8*items+64*73
 work=scalar+bridges+shifts+moves+parentlive+(calls*adapters+outside)*compiler+64*parentphysical;usedwork=max(work,work+65*(physical-parentphysical)+(live-parentlive));group=2**(36*36)
 for i in range(1,37):group*=2**(2*i)-1
 stock=group*physical;streamed=group*role['rank_mass'];logical=group*usedwork+64;router=compiler*(logical+1)*(stock+1)**2;literal=2*2**30000*stock**2+8*streamed+4*stock+4+32*73
 ck(pre+'own_finite_compiler_budget',logical<2**6050 and router<2**30000 and literal<2**100000)
 ck(pre+'own_semantic_height',32*73*(streamed+2**100000)**2<2**210000 and 2*(streamed+2**100000)+18<2**210000)
 invoice=dict(selected_real=scalar,wrapper_factors=wrappers,adapters=adapters,parent_live=parentlive,parent_physical=parentphysical,parent_banks=banks,parent_idle=parentidle,nonlocal_items=items,outside=outside,unhosted_work=work,complete_work=usedwork,retained_previous_invoice=None,physical=physical,live=live,stock_bits=stock.bit_length(),router_bits=router.bit_length(),literal_bits=literal.bit_length(),G='2^30000',E='2^100000',C0='2^210000')
 file=f'kernel-demotions-counted-source/{pr}/own-census.json';out=dict(schema='own-kernel-demotions-complete-counted-census/1',pr=pr,own_head=pkg['own_head'],kappa_record=expected['kappa'],complex_lower=expected['complex_lower'],selected_native_censuses=bindings,role_receipt=role,negative_controls=neg,provider_counts=dict(Counter(dispatch.values())),invoice=invoice,numeric_PLAN_file=planfile,numeric_PLAN_sha256=hs(planfile),historical_complete_PLAN_byte_identity_claimed=False,source_equivalent_numeric_realization=True,actual_source_finite_replay_observed=True,literal_original_timeout_command_PASS_claimed=False,execution_only_timeout_wrapper_disclosed=True,operator_phase_globally_proved=False,source_sha256=source,source_manifest_file='kernel-demotions-source/manifest.json',source_manifest_sha256=hs('kernel-demotions-source/manifest.json'),dependency_hashes={f:hs(f)for f in ['finite_selected_program_census.py','finite_actual_owner_census_v2.py']},script_sha256=hs(Path(__file__).name))
 (R/file).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');rows.append(dict(pr=pr,own_head=pkg['own_head'],own_census_file=file,own_census_sha256=hs(file)));print('PASS own native/owner/no-prior invoice',pr,flush=True)
(R/'kernel-demotions-counted-source-censuses.json').write_text(json.dumps(dict(schema='own-kernel-demotions-census-batch/1',rows=rows,checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__).name)),indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own input checks')
