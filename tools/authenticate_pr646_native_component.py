"""Authenticate a closed prior native receipt without claiming a new native run."""
from pathlib import Path,PurePosixPath
from hashlib import sha256
import argparse,gzip,json,sys
sys.set_int_max_str_digits(0)
PEER='pr646-signed-root-K480-finite-source-peer-review.json'
PEER_SHA='fd25d2adb38d843d8ab55886b0d1dba7118797ce606515144ea523f2c2b65ad0'
HEAD='cdfe8273bb5054e0a837a3594309c6262e995b1f'
def authenticate(folder):
 folder=Path(folder).resolve();checked={}
 def path(n):
  q=PurePosixPath(n);assert not q.is_absolute()and '..'not in q.parts and ':'not in n and '\\'not in n
  p=(folder/n).resolve();assert p.is_relative_to(folder);return p
 def hs(n):return sha256(path(n).read_bytes()).hexdigest()
 def rd(n):
  b=path(n).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
 def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 def ck(k,v):assert v,k;checked[k]=True
 ck('frozen_source_peer_exact',hs(PEER)==PEER_SHA);peer=rd(PEER)
 ck('prior_AI_source_review_attests_actual_corrected_native_run',peer['pr']==646 and peer['own_head']==HEAD and peer['review_status'].startswith('PASS')and peer['actual_corrected_native334_replay_executed_by_this_reviewer']is True)
 for f,h in peer['reviewed_sha256'].items():ck('exact_prior_review_binding_'+f,hs(f)==h)
 rf='late-cold-mixed-native-byte-recovery-646.json';r=rd(rf);producer='recover_signed_root_646_native_bytes.py'
 ck('closed_exact_own646_prior_native_receipt',r['pr']==646 and r['own_head']==HEAD and r['status']=='passed_actual_source_constructors_scalar_frame_wrapper_engines'and r['checks_passed']==334 and all(r['checks'].values())and r['script_sha256']==hs(producer)and bool(r['steps'])and all(a['exit_code']==0 for a in r['steps'])and not r['original_complete_source_package_replay_claimed'])
 for label in['source_sha256','retained_base_sha256','dependency_hashes']:
  for f,h in r[label].items():ck('exact_prior_native_'+label+'_'+f,hs(f)==h)
 for a in r['raw_intermediates']:
  b=path(a['file']).read_bytes();ck('whole_RAW_'+a['file'],sha256(b).hexdigest()==a['sha256']and sha256(gzip.decompress(b)).hexdigest()==a['decompressed_sha256'])
 for a in r['outputs']:ck('whole_native_output_'+a['file'],hs(a['file'])==a['sha256']and ident(rd(a['file']))==a['semantic_sha256'])
 sf='selected-provider-dispatch-v20-source/646/actual-own-selector.json';sel=rd(sf);s=rd(sel['SPEC_file']);nf='pr646-signed-root-K480-finite-native.json';n=rd(nf)
 ck('exact_own_selector_and_native_identity',sel['pr']==n['pr']==646 and sel['own_head']==n['own_head']==HEAD and sel['actual_literal_spec_driven_native_and_global_data_selection']and peer['reviewed_sha256'][sf]==hs(sf)and peer['reviewed_sha256'][nf]==hs(nf))
 c=rd(n['own_complete_census_file']);ck('complete_own_census_bound',n['dependency_hashes'][n['own_complete_census_file']]==peer['reviewed_sha256'][n['own_complete_census_file']]==hs(n['own_complete_census_file'])and c['pr']==646 and c['own_head']==HEAD)
 ck('all_own_selected_providers_present',set(s['providers'])=={a['provider']for a in c['selected_native_censuses']})
 for a in c['selected_native_censuses']:
  pid=a['provider'];p=s['providers'][pid];can=rd(a['canonical_file']);program=rd(a['program_file']);raw=s['build']['providers'][pid]['word_content_sha256']
  ck('own_complete_native_commitments_'+pid,ident(can)==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and ident(program)==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and{o:ident(w)for o,w in program.items()}==p['program_hashes']and any(z['provider']==pid and z['file']==a['program_file']and z['raw_content_sha256']==raw for z in r['outputs']))
 return dict(schema='closed-own646-native-receipt-authentication/1',passed=True,pr=646,own_head=HEAD,producer=producer,producer_sha256=hs(producer),recovery_file=rf,recovery_sha256=hs(rf),source_peer_file=PEER,source_peer_sha256=PEER_SHA,checks_passed=len(checked),checks=checked,fresh_native_constructor_or_controls_executed=False,prior_AI_source_review_execution_attestation_retained=True,authentication_tool_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),scope='Authenticates the existing closed AI-reviewed native execution receipt and its exact bound source, RAW and complete native outputs. This run does not repeat native constructors or destructive controls. Its historical execution attestation is retained from the cited source review. Whole cost schedules replay separately; universal operator/phase/allsize/analytic hypotheses are not discharged.')
if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--audit-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path);a=ap.parse_args();out=authenticate(a.audit_dir)
 if a.receipt:a.receipt.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
 print(json.dumps({k:out[k]for k in['passed','pr','checks_passed','fresh_native_constructor_or_controls_executed','recovery_sha256','source_peer_sha256']}))
