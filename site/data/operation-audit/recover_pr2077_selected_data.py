"""Reconstruct all three actual own2077 data byte strings from four moves."""
from pathlib import Path
from hashlib import sha256,sha1
import json,subprocess,sys,tempfile,urllib.request
R=Path(__file__).resolve().parent;P=R/'pr2077-vacancy-chain-source';D=P/'selected-base';D.mkdir(exist_ok=True);checks={}
def hs(p):return sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(p.read_bytes())
def ck(n,v):assert v,n;checks[n]=True
receipt=rd(P/'source-receipt.json');M=rd(P/'MANIFEST.json');sources={}
ck('own_complete_source_inventory',receipt['own_head']=='407712103b605a662a89a56f9c42b93dca69126b'and receipt['inventory_matches_own_MANIFEST']and receipt['script_sha256']==hs(R/'fetch_pr2077_own_source.py')and {a['relative']:a['sha256']for a in receipt['files']}==M)
for a in receipt['files']:ck('own_source_'+a['relative'],hs(R/a['file'])==a['sha256']);sources[a['file']]=a['sha256']
binding=rd(P/'SOURCES.json');pins=rd(P/'INPUTS.json');base=binding['base_commit'];basefiles=[]
for name in['OWNERS.json.gz','PLAN.json','SPEC.json']:
 path='research/complex-t16-rare-pattern-exchanges/data/'+name;want=pins[path];rec=next(a for a in binding['files']if a['path']==path);ck('own_INPUTS_SOURCE_join_'+name,rec['sha256']==want)
 dest=D/name;url=f'https://raw.githubusercontent.com/CrocSwap/integer-mult-bounds/{base}/{path}'
 if not dest.exists()or hs(dest)!=want:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'OwnSelectedDataRecovery/1.0'}),timeout=90)as response:b=response.read()
  dest.write_bytes(b)
 b=dest.read_bytes();ck('actual_pinned_base_SHA_'+name,sha256(b).hexdigest()==want);ck('pinned_base_SHA_and_Git_blob_'+name,hs(dest)==want and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==rec['git_blob'])
 a=dict(path=path,source_commit=base,file=dest.relative_to(R).as_posix(),sha256=want,git_blob=rec['git_blob'],primary_url=url);basefiles.append(a);sources[a['file']]=want
with tempfile.TemporaryDirectory(prefix='own2077-data-')as tmp:
 T=Path(tmp);parent=T/'research/complex-t16-rare-pattern-exchanges/data';parent.mkdir(parents=True)
 for a in basefiles:(parent/Path(a['path']).name).write_bytes((R/a['file']).read_bytes())
 g={'__name__':'own2077_actual_builder','__file__':str(P/'build.py')};exec(compile((P/'build.py').read_bytes(),str(P/'build.py'),'exec'),g);blobs=g['derive'](T)
 for name,b in zip(['OWNERS.json.gz','PLAN.json','SPEC.json'],blobs):ck('exact_entire_own_reconstructed_'+name,b==(P/'data'/name).read_bytes()and sha256(b).hexdigest()==M['data/'+name])
v=(P/'verify.py').read_text();ck('actual_own_entrypoint_reconstruction_and_selector',"blobs=mod.derive(main)"in v and"for name in ('OWNERS.json.gz','PLAN.json','SPEC.json')"in v and"source/'verify_t16.py'"in v and"research/community-frontier1094-audit/selected-replay.tar.gz"in v)
s=rd(P/'data/SPEC.json');c=rd(P/'CANDIDATE.json');ck('actual_own_target_not_frozen_baseline',s['expected']['kappa']==c['expected_updates']['kappa']=='418166011373521/250000000000000000'and c['baseline_kappa']=='836330098538459/500000000000000000')
out=dict(schema='own2077-exact-selected-data-reconstruction/1',status='actual_own_build_full_data_bytes_recovered_no_runtime_claim',pr=2077,own_head=receipt['own_head'],own_source_receipt_file='pr2077-vacancy-chain-source/source-receipt.json',own_source_receipt_sha256=hs(P/'source-receipt.json'),source_sha256=sources,selected_base_inputs=basefiles,own_selected_data={name:dict(file=(P/'data'/name).relative_to(R).as_posix(),sha256=hs(P/'data'/name))for name in['OWNERS.json.gz','PLAN.json','SPEC.json']},actual_own_kappa=s['expected']['kappa'],frozen_baseline_quote=c['baseline_kappa'],original_global_verifier_or_native_phase_replayed=False,whole_runtime_bound_claimed=False,checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__)))
(R/'pr2077-exact-selected-data-recovery.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own2077 exact source-generated data checks')
