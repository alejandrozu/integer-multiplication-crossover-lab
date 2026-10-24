"""Exhaustive own-source dispatcher for the selected-provider discovery cohort.

Selection requires the own SPEC's exact record value, not a title heuristic.
Byte recoveries are discovery only until each own digest is rechecked. Missing
or ambiguous interfaces are reported; they are never counted as priced.
"""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import argparse,gzip,hashlib,importlib.util,json,sys,urllib.request
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'selected-provider-dispatch-v22-source';D.mkdir(exist_ok=True)
ap=argparse.ArgumentParser();ap.add_argument('--fetch',action='store_true');ap.add_argument('--execute',action='store_true');ap.add_argument('--refresh-inputs',action='store_true');args=ap.parse_args()
def hs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_bytes())
def ident(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def require(v,why):
    if not v:raise ValueError(why)
def module(name):
    s=importlib.util.spec_from_file_location(name,R/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
nativec=module('finite_selected_program_census');ownerc=module('finite_actual_owner_census_v2')
snapshot=R/'selected-provider-dispatch-v22-inputs.json'
if args.refresh_inputs or not snapshot.exists():
    raise ValueError('V22 requires frozen actual own-selector preparation, not mutable discovery')
    paths=['remaining-record-audit/cost-coverage-ledger.json','remaining-record-audit/complete-audit-queue.json','selected-native-byte-recoveries.json','selected-native-derived-byte-recoveries.json'];raw={p:(R/p).read_bytes()for p in paths};docs={p:json.loads(b)for p,b in raw.items()}
    l,q,b,d=[docs[p]for p in paths];selectedrows=[x for x in l['rows']if x.get('source_family')=='selected_provider_controller'];ids={x['pr']for x in selectedrows};sources={}
    for row in b['rows']:
        for pin in row['declared_pins']:
            for match in pin.get('matched_actual_bytes',[]):
                for z in match['source']:sources.setdefault(z['file'],dict(file=z['file'],sha256=z['sha256'],origin='immutable_Git_primary_archive',primary=z))
    for row in d['rows']:
        for pin in row['recoveries']:
            for match in pin['matched_derived_bytes']:
                z=match['source'];sources.setdefault(z['file'],dict(file=z['file'],sha256=z['file_sha256'],origin='derived_reconstruction_exact_own_commitment',primary=z))
    snap=dict(schema='selected-provider-dispatch-frozen-inputs/1',cohort_rows=selectedrows,claim_metadata=[dict(pr=x['pr'],quoted_kappa_fraction=x.get('quoted_kappa_fraction'))for x in q['rows']if x['pr']in ids],actual_native_archive_sources=list(sources.values()),original_input_sha256={p:hashlib.sha256(v).hexdigest()for p,v in raw.items()},scope='Filtered byte-for-byte field snapshot of the structural cohort and claim metadata plus exact native archive source receipts. Later ledger edits do not change this audit universe.')
    snapshot.write_text(json.dumps(snap,indent=2)+'\n')
snap=rd(snapshot)
for f,h in snap['original_input_sha256'].items():require(hs(R/f)==h,'frozen V22 source SHA '+f)
ledger={'rows':snap['cohort_rows']};qm={x['pr']:x for x in snap['claim_metadata']}
# Build an actual finite-byte index. Index claims are not trusted as equality:
# each file is read, hashed and canonically rehashed here.
actual={};actual_sources={};native_paths=set();verified_actual={};actual_program_pairs={}
for s in snap['actual_native_archive_sources']:
    path=R/s['file'];require(hs(path)==s['sha256'],'native archive SHA mismatch');native_paths.add(s['file'])
for ix,path in enumerate(sorted(native_paths),1):
    obj=rd(R/path);digest=ident(obj);actual.setdefault(digest,path);actual_sources[path]=hs(R/path)
    if isinstance(obj,dict)and set(obj)=={'forward','backward'}:actual_program_pairs.setdefault(tuple(ident(obj[o])for o in ['backward','forward']),path)
    if ix%100==0:print('indexed actual finite files',ix,'/',len(native_paths),flush=True)

def selected(row):
    q=qm[row['pr']];quoted=q.get('quoted_kappa_fraction');candidates=[]
    for a in row['verified_components']:
        if not a.get('path','').endswith('/SPEC.json'):continue
        require(hs(R/a['file'])==a['sha256'],'own SPEC primary SHA mismatch')
        s=rd(R/a['file'])
        if not isinstance(s,dict)or not all(k in s for k in ['providers','dispatch','data','expected']):continue
        ex=s['expected']
        try:match=quoted is not None and F(ex['kappa'])==F(quoted)
        except(KeyError,ValueError,TypeError):match=False
        if match:candidates.append((a,s))
    groups={}
    for a,s in candidates:groups.setdefault(a['sha256'],[]).append((a,s))
    require(groups,'no own SPEC with exact independently recorded claim kappa')
    require(len(groups)==1,'multiple distinct own SPECs match claim; selectedness unresolved')
    a,s=next(iter(groups.values()))[0]
    require(isinstance(s['dispatch'],list)and all(isinstance(z,list)and len(z)==3 for z in s['dispatch']),'unsupported own dispatch schema')
    require({z[2]for z in s['dispatch']}<=set(s['providers']),'dispatch names missing from own registry')
    return a,s

def fetch_one(task):
    pr,head,root,kind,want=task;out=D/str(pr);out.mkdir(exist_ok=True);cache=out/(kind+'.json')
    if cache.exists():
        receipt=rd(cache)
        if receipt.get('sha256')==want and hs(R/receipt['file'])==want:return receipt
    names={'PLAN':['data/PLAN.json','PLAN.json'],'OWNERS':['data/OWNERS.json.gz','OWNERS.json.gz']}
    errors=[]
    for name in names[kind]:
        path=root+'/'+name;url='https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/'+head+'/'+path
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'IntegerCostAudit/1.0'}),timeout=40)as f:data=f.read()
            digest=hashlib.sha256(data).hexdigest()
            if digest!=want:errors.append(dict(path=path,sha256=digest,status='digest_does_not_match_own_SPEC'));continue
            dest=out/(digest[:12]+'__'+PurePosixPath(path).name);dest.write_bytes(data)
            r=dict(pr=pr,own_head=head,path=path,url=url,file=dest.relative_to(R).as_posix(),sha256=digest,bytes=len(data),own_SPEC_expected_sha256=want,status='authenticated_own_SPEC_declared_bytes')
            cache.write_text(json.dumps(r,indent=2)+'\n');return r
        except Exception as e:errors.append(dict(path=path,error=type(e).__name__+': '+str(e)))
    r=dict(pr=pr,own_head=head,kind=kind,status='unavailable_own_hash_bound_artifact',expected_sha256=want,attempts=errors);cache.write_text(json.dumps(r,indent=2)+'\n');return r

cohort=[x for x in ledger['rows']if x.get('source_family')=='selected_provider_controller'];selections={};screen=[];tasks=[]
for row in cohort:
    entry=dict(pr=row['pr'],own_head=row['own_head'],url=row['url'],title=row['title'],historical_streams=row['claimed_record_status'].get('streams',[]),historical_record_candidate=bool(row['claimed_record_status'].get('streams')),numeric_bound_completed=False)
    try:
        authority,s=selected(row);parent=PurePosixPath(authority['path']).parent;root=str(parent.parent if parent.name=='data'else parent)
        entry.update(selected_SPEC_file=authority['file'],selected_SPEC_sha256=authority['sha256'],selected_package=root,kappa_record=s['expected']['kappa'])
        require(all(k in s['data']for k in ['plan_sha256','owners_sha256']),'own PLAN/OWNERS digest interface missing')
        need=[];native=[]
        for pid in sorted({z[2]for z in s['dispatch']}):
            p=s['providers'][pid];sem=p.get('artifact_semantic_sha256',{});w=sem.get('CANONICAL-WORD.json.gz');g=sem.get('LOCAL-PROGRAMS.json.gz')
            if w is None:
                ownrec=snap['recovered_own_native_selection'][str(row['pr'])][pid]
                require(ownrec['orientation_sha256']==p['program_hashes'] and ownrec['own_RAW_content_sha256']==s['build']['providers'][pid]['word_content_sha256'],'own exact RAW/orientation recovery join')
                w=ownrec['canonical_sha256'];g=ownrec['program_sha256']
            pf=actual.get(g)
            # Some own SPECs bind only the two orientation words. In that case
            # both hashes must identify one actual complete program object.
            if g is None and set(p.get('program_hashes',{}))=={'backward','forward'}:pf=actual_program_pairs.get(tuple(p['program_hashes'][o]for o in ['backward','forward']))
            missing=[]if pf else['program']
            native.append(dict(provider=pid,canonical_digest=w,program_digest=g,canonical_file=actual.get(w),program_file=pf,program_binding='own_semantic_and_orientation_hashes'if g else'own_both_orientation_hashes',canonical_catalogue_available=w in actual,missing=missing))
            need+= [pid+':'+name for name in missing]
        entry.update(native_provider_bindings=native,missing_selected_native_bytes=need)
        selections[row['pr']]=(authority,s,entry)
        if need:entry['status']='selected_native_bytes_missing'
        else:entry['status']='selected_native_bytes_resolved_owner_checks_pending'
        for kind,key in [('PLAN','plan_sha256'),('OWNERS','owners_sha256')]:tasks.append((row['pr'],row['own_head'],root,kind,s['data'][key]))
    except Exception as e:entry.update(status='own_selection_or_interface_unresolved',blocker=str(e)or type(e).__name__)
    screen.append(entry)
if args.fetch:
    with ThreadPoolExecutor(max_workers=6)as pool:
        for i,res in enumerate(pool.map(fetch_one,tasks),1):
            if i%20==0:print('source fetch',i,'/',len(tasks),flush=True)

old=rd(R/'older-reviewed-source/535-manifest.json');proto=rd(R/'older-reviewed-source'/next(x['file']for x in old if x['path']=='research/post-center-rank4-global/inputs/ROUND20-PARENT-TEMPLATE.json.gz'))
dm=rd(R/'t21-t37-cost-source/manifest.json')
def data(suffix):return R/'t21-t37-cost-source'/next(x['file']for x in dm if x.get('path','').endswith(suffix)and'error'not in x)
phases=rd(data('/work/complex-nine-native/DATA-PHASES.json'));baseword=rd(data('/split-centres/CANONICAL-WORD.json.gz'))
cache=D/'native-census-cache';cache.mkdir(exist_ok=True)
receipts=[]
for entry in screen:
    pr=entry['pr']
    if pr not in selections:continue
    authority,s,_=selections[pr];art={}
    for kind in ['PLAN','OWNERS']:
        p=D/str(pr)/(kind+'.json')
        if p.exists():
            r=rd(p)
            if r.get('status')=='authenticated_own_SPEC_declared_bytes'and hs(R/r['file'])==r['sha256']:art[kind]=r
    entry['own_physical_artifacts']=art
    if len(art)<2:entry['physical_artifact_blockers']=[k for k in ['PLAN','OWNERS']if k not in art]
    if not args.execute or entry.get('missing_selected_native_bytes')or len(art)<2:continue
    try:
        providers={};nativecost={};nativechecks=[]
        for z in entry['native_provider_bindings']:
            pid=z['provider'];p=s['providers'][pid];w=rd(R/z['canonical_file'])if z['canonical_file']else None;program=rd(R/z['program_file']);key=ident([z['canonical_digest']if w is not None else None,ident(program),hs(R/'finite_selected_program_census.py')]);cp=cache/(key+'.json')
            if cp.exists():c=rd(cp)
            else:
                c=nativec.census(program,canonical=w);cp.write_text(json.dumps(c,indent=2)+'\n')
            require((w is None or ident(w)==z['canonical_digest'])and(z['program_digest']is None or ident(program)==z['program_digest']),'own semantic native digest')
            require({o:v['sha256']for o,v in c.items()}==p['program_hashes'],'own actual two orientation hashes')
            f=c['forward']
            if w is not None:require(w['ports']==baseword['ports']and all(ownerc.basis(w['frames'][a])==ownerc.basis(baseword['frames'][b])for a,b in zip(w['center_frames'],baseword['center_frames'])),'different native physical port/centre geometry')
            if 'complete_contract'in p:contract=p['complete_contract']
            else:
                require(ident(f['widths'])==p['width_digest']and dict(Counter(f['widths']))=={int(k):v for k,v in p['inventory'].items()},'own raw-schema whole-width digest and inventory')
                local=p.get('expected_local')or{o:p['expected_local.'+o]for o in ['backward','forward']}
                contract=dict(widths=f['widths'],local=local,new_adapter_realization_not_historical_complete_contract=True)
            require(f['widths']==contract['widths']and {int(k):v for k,v in f['paid_profile'].items()}=={int(k):v for k,v in p['expected_profile'].items()},'own width/profile contract mismatch')
            # JSON caches use string profile keys; normalize only after equality.
            providers[pid]=dict(columns=f['columns'],helpers=f['helpers'],widths=f['widths'],paid_profile={int(k):v for k,v in f['paid_profile'].items()},prefix_bits=max(v['prefix_bits']for v in c.values()))
            require(w is not None,'actual canonical catalogue required for helper-entry census in this cohort')
            first=2*w['v'];entry_ranks=[len(w['frames'][i])for i in w['start'][first:]]
            require(len(entry_ranks)==f['helpers']and all(type(x)is int and 0<=x<=9 for x in entry_ranks),'own actual canonical initial helper dimensions')
            final_ranks=[len(w['frames'][i])for i in w['final'][first:]]
            require(len(final_ranks)==f['helpers']and [b-a for a,b in zip(entry_ranks,final_ranks)]==f['widths'],'own helper productive width equals actual final-minus-initial rank')
            require(all(ownerc.basis(w['frames'][a]+w['frames'][b])==ownerc.basis(w['frames'][b])for a,b in zip(w['start'][first:],w['final'][first:])),'own initial helper subspace lies in final subspace')
            providers[pid].update(entering_flags=[bool(x)for x in entry_ranks],initial_helper_ranks=entry_ranks,final_helper_ranks=final_ranks)
            require(sum(providers[pid]['entering_flags'])==p['entering']and sum(entry_ranks)==p['entrance'],'own actual canonical entering-helper count/rank')
            adapter=16*(max(v['scalar_macros']for v in c.values())+sum(providers[pid]['paid_profile'].values())+f['columns']+8)+64*73
            if 'local_adapters'in contract:require(adapter==contract['local_adapters'],'own actual adapter invoice mismatch')
            require(all(v['events']<adapter for v in c.values()),'native event count exceeds full Clifford/adapter envelope')
            for o,v in c.items():
                e=contract['local'][o];require(v['real_component_primitives']==e['real_component_primitives']and F(v['prefix_l1'])==F(e['prefix_l1']),'own scalar/prefix contract mismatch')
                if 'macros'in e:require(v['scalar_macros']==e['macros']and v['events']==e['events']and v['coefficient_work_primitives']==e['coefficient_work_primitive_count'],'own complete local source primitive/macro/event bill')
            nativecost[pid]=dict(local=c,adapters=adapter);nativechecks.append(dict(provider=pid,census_file=cp.relative_to(R).as_posix(),census_sha256=hs(cp),canonical_file=z['canonical_file'],canonical_file_sha256=hs(R/z['canonical_file'])if w is not None else None,program_file=z['program_file'],program_file_sha256=hs(R/z['program_file']),program_binding=z['program_binding'],canonical_GF2_catalogue_freshly_checked=w is not None,physical_entry_output_absolute_phase_contract_freshly_proved=False,initial_helper_ranks=providers[pid]['initial_helper_ranks'],final_helper_ranks=providers[pid]['final_helper_ranks'],entering_flags=providers[pid]['entering_flags']))
        plan=rd(R/art['PLAN']['file']);roles=rd(R/art['OWNERS']['file']);dispatch={(a,b):p for a,b,p in s['dispatch']};stageorient={c['stage']:c['orientation']for c in proto['calls']}
        for pid,p in s['providers'].items():
            if pid not in providers:continue
            reg=plan['provider_registry'][pid]
            require(reg['ports']==baseword['ports']and reg['widths']==providers[pid]['widths']and reg['orientation_program_sha256']==p['program_hashes']and reg['actual_paid_profile']==p['expected_profile'],'own complete PLAN provider registry')
        require(plan['order']==s['call_order'],'own exact call order')
        require(plan['provider_calls']==[dict(time=t,stage=a,replica=b,provider=dispatch[a,b],orientation=stageorient[a],local_program_sha256=s['providers'][dispatch[a,b]]['program_hashes'][stageorient[a]])for t,(a,b)in enumerate(plan['order'])],'own complete dispatch/orientation/program calls')
        require(len(plan['per_call_widths'])==len(plan['order'])and all(set(z)<=set(['stage','replica','widths','time'])and z['stage']==a and z['replica']==b and z['widths']==providers[dispatch[a,b]]['widths']and('time'not in z or z['time']==t)for t,(z,(a,b))in enumerate(zip(plan['per_call_widths'],plan['order']))),'own per-call whole-helper widths')
        rolekey=ident(dict(PLAN=art['PLAN']['sha256'],OWNERS=art['OWNERS']['sha256'],providers=providers,parent=ident(proto),phases=ident(phases),module=hs(R/'finite_actual_owner_census_v2.py')));rolecache=D/'owner-census-cache';rolecache.mkdir(exist_ok=True);rp=rolecache/(rolekey+'.json')
        if rp.exists():rr=rd(rp);role=rr['role'];neg=rr['negative_controls']
        else:
            ctx=ownerc.context(proto,phases,baseword['ports'],plan,roles,dispatch,providers);role=ownerc.audit(ctx,roles);neg=ownerc.controls(ctx,roles)
            rp.write_text(json.dumps(dict(input_fingerprint=rolekey,role=role,negative_controls=neg,scope='Pure owner component reused only at exact complete PLAN/OWNERS/program-width-profile/parent-phase/module input equality; own source selection and cost parameters remain separate.'),indent=2)+'\n')
        # Restore integer keys after a JSON cache load.
        for name in ['profile','idle']:role[name]={int(k):v for k,v in role[name].items()}
        ex=s['expected']
        for actual,expected in [('live','live'),('physical','physical'),('roles','hosted_residuals'),('rank_mass','rank_mass'),('rank_surplus','deficit'),('cross_replica_helpers','cross_replica_helper_roles'),('actual_73_axis_charts','actual_73column_sigmas')]:
            if expected in ex:require(role[actual]==ex[expected],'own expected '+expected)
        declared=ex.get('entering_helper_roles');actual=role['actual_nonzero_start_frame_roles'];legacy=role['width_below_9_roles']
        meter=dict(source_declared_entering_helper_roles=declared,actual_nonzero_start_frame_roles=actual,width_below_9_roles=legacy,source_declared_meter_style='not_declared_in_own_expected'if declared is None else'actual_initial_nonzero_frames'if declared==actual else'legacy_width_below_9'if declared==legacy else'unreproduced_descriptive_metadata',source_declared_counter_matches_actual=None if declared is None else declared==actual,used_by_new_cost_stock_or_precision=False)
        require(role['rank_surplus']==73*ex['live']-ex['rank_mass'],'own exact live/mass surplus')
        require(role['profile']=={int(k):v for k,v in ex['global_profile'].items()}and role['idle']=={int(k):v for k,v in ex['idle_remainder_profile'].items()},'own full paid/idle profile')
        # Explicit padded T8 direct-sum parent, charged even for clipped groups.
        # The physical touch windows above are independently checked literally.
        T=plan['T'];groups=(T+7)//8;live=role['live'];physical=role['physical'];parentlive=11704*groups-896*(8*groups-T);parentphysical=parentlive+514;parentidle=16128*groups;banks=504*groups
        scalar=wrappers=0
        for a,b in plan['order']:
            z=nativecost[dispatch[a,b]]['local'][stageorient[a]];scalar+=z['real_component_primitives'];wrappers+=(z['pre_wrappers']+z['post_wrappers'])*144
        calls=role['calls'];helpers=role['helpers_max'];bridges=2*112*role['bridges'];shifts=4*112*T;moves=2*shifts;adapters=max(z['adapters']for z in nativecost.values());compiler=64*74**3
        items=4*112*T*9+2*112*T*9+2*calls*helpers+parentidle+9*banks+bridges+shifts+moves+parentlive+parentphysical+wrappers;outside=8*items+64*73
        work=scalar+bridges+shifts+moves+parentlive+(calls*adapters+outside)*compiler+64*parentphysical;usedwork=max(work,work+65*(physical-parentphysical)+(live-parentlive))
        group=2**(36*36)
        for i in range(1,37):group*=2**(2*i)-1
        stock=group*physical;streamed=group*role['rank_mass'];logical=group*usedwork+64;router=compiler*(logical+1)*(stock+1)**2;literal=2*2**30000*stock**2+8*streamed+4*stock+4+32*73
        require(logical<2**6050 and router<2**30000 and literal<2**100000,'finite constructor budget beyond named finite lemma')
        require(32*73*(streamed+2**100000)**2<2**210000 and 2*(streamed+2**100000)+18<2**210000,'semantic height reserve beyond named finite lemma')
        require(role['physical_row_coefficient']<20161,'own row constant exceeds named20,161 allowance')
        invoice=dict(selected_real=scalar,wrapper_factors=wrappers,adapters=adapters,parent_live=parentlive,parent_physical=parentphysical,parent_banks=banks,parent_idle=parentidle,nonlocal_items=items,outside=outside,unhosted_work=work,complete_work=usedwork,retained_previous_invoice=None,physical=physical,live=live,stock_bits=stock.bit_length(),router_bits=router.bit_length(),literal_bits=literal.bit_length(),G='2^30000',E='2^100000',C0='2^210000')
        out=dict(schema='own-selected-provider-dispatch-census/1',pr=pr,own_head=entry['own_head'],own_SPEC_file=authority['file'],own_SPEC_sha256=authority['sha256'],kappa_record=s['expected']['kappa'],complex_lower=s['expected'].get('complex_lower'),selected_native_censuses=nativechecks,own_physical_artifacts=art,role_receipt=role,negative_controls=neg,invoice=invoice,source_equivalent_numeric_parent=True,own_source_selector_file=(D/str(pr)/'actual-own-selector.json').relative_to(R).as_posix(),own_source_selector_sha256=hs(D/str(pr)/'actual-own-selector.json'),historical_complete_native_contract_field_invented=False,new_full_adapter_realization_charged=True,original_full_global_verifier_PASS_claimed=False,historical_parent_byte_identity_claimed=False,operator_phase_proved=False,descriptive_entering_counter=meter,canonical_catalogue_absent_for=[z['provider']for z in nativechecks if not z['canonical_GF2_catalogue_freshly_checked']],retained_interfaces=['Own full required physical entry/output-frame and absolute-phase operator-valued native endpoint, including normalized monomial wrappers and ascending typed helper paths; not inferred from scalar specialization or profiles','All unexpanded adapter/phase operations are bounded73-axis binary affine/even-quadratic Z4 monomial grammar, with no hidden arbitrary scalar coefficients or denominators; each full operation is charged the universal64*74^3 source tariff','Common-label/mutable-source/owned restore and all-size occupied-row interface','Fixed constructive group/compiler and direct analytic transfer contracts'],numeric_bound_completed=False,status='source_numeric_inputs_checked_not_yet_whole_cost_certificate')
        dest=D/str(pr)/'own-census.json';dest.write_text(json.dumps(out,indent=2)+'\n');entry.update(status=out['status'],own_census_file=dest.relative_to(R).as_posix(),own_census_sha256=hs(dest),role_count=role['roles'],actual_native_words=len(providers));receipts.append(out)
        print('PASS selected-provider numeric inputs',pr,flush=True)
    except Exception as e:entry.update(status='own_source_numeric_interface_blocked',blocker=str(e)or type(e).__name__)
summary=dict(entries=len(screen),historical_candidates=sum(x['historical_record_candidate']for x in screen),statuses=dict(Counter(x['status']for x in screen)),native_payload_files=len(native_paths),own_numeric_censuses=len(receipts),numeric_upper_certificates_created=0)
out=dict(schema='selected-provider-exhaustive-dispatch/1',scope='Every entry of the pinned structural selected_provider_controller cohort; this is not a proof that the historical record universe is complete.',summary=summary,rows=screen,source_sha256={'selected-provider-dispatch-v22-inputs.json':hs(snapshot)},original_filtered_input_sha256=snap['original_input_sha256'],dependency_hashes={p:hs(R/p)for p in ['finite_selected_program_census.py','finite_actual_owner_census_v2.py']},script_sha256=hs(Path(__file__)),no_automatic_equivalence_transfer=True)
(R/'selected-provider-dispatch-v22.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary,indent=2))
