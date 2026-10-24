"""Supplemental exact own275 source selection and merge-chronology audit."""
from pathlib import Path
from hashlib import sha1,sha256
from fractions import Fraction as F
from datetime import datetime
import json,subprocess,sys
R=Path(__file__).resolve().parent;checks={}
def ck(k,v):assert v,k;checks[k]=True
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):return json.loads((R/f).read_bytes())
files=['pr275-supplied-cap-gaussian-bounds.md','pr275_supplied_cap_gaussian_bounds.py','pr275-supplied-cap-gaussian-bounds.json']+[f'pr275-supplied-cap-gaussian-{t}.json'for t in['native','early-upper','record-upper']]
before={f:hs(f)for f in files};run=subprocess.run([sys.executable,'-X','utf8',str(R/'pr275_supplied_cap_gaussian_bounds.py')],cwd=R,text=True,encoding='utf8',capture_output=True)
ck('fresh79_cost_checks',run.returncode==0 and 'PASS 79'in run.stdout);ck('all6_frozen_proof_bytes_unchanged',all(hs(f)==h for f,h in before.items()))
n=rd('pr275-supplied-cap-gaussian-native.json');e=rd('pr275-supplied-cap-gaussian-early-upper.json');record=rd('pr275-supplied-cap-gaussian-record-upper.json');own=rd('pr275-cap-source/own-manifest.json');declared=rd('pr275-cap-source/declared-parent-manifest.json');paths={a['path']:a['file']for a in own+declared};head='524375c61b75dc10cef68a71d504e79e7e7f138c';base='f567884aeb8851b6e794af1184119a3bfbe1e631'
pins={f:hs(f)for f in files};pins['pr275-supplied-cap-gaussian-peer-review.json']=hs('pr275-supplied-cap-gaussian-peer-review.json')
for f in['pr275-cap-source/own-manifest.json','pr275-cap-source/declared-parent-manifest.json','pr275-cap-source/chronology-primary-receipt.json','remaining-record-audit/complete-audit-queue.json']:pins[f]=hs(f)
for a in own:
 ck('own_exact_'+a['path'],a['own_head']==head and hs(a['file'])==a['sha256']and'/'+head+'/'in a['primary_url']);pins[a['file']]=a['sha256']
up=rd(paths['research/finite-assembly-pr799/UPSTREAM.json']);mf=rd(paths['research/finite-assembly-pr799/MANIFEST.json']);expected=rd(paths['research/finite-assembly-pr799/EXPECTED.json']);spec=rd(paths['research/gauge44-frames-x/data/SPEC.json'])
for k in['EXPECTED.json','UPSTREAM.json','verify.py','README.md']:ck('actual_own_MANIFEST_'+k,mf['files'][k]==hs(paths['research/finite-assembly-pr799/'+k]))
for a in declared:
 raw=(R/a['file']).read_bytes();p=up['files'][a['path']]
 ck('exact_own_declared_parent_'+a['path'],up['commit']==base==a['declared_commit']and a['declaring_head']==head and sha256(raw).hexdigest()==a['sha256']==p['sha256']and len(raw)==p['bytes']and sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==p['git_blob']);pins[a['file']]=a['sha256']
target=F('207704331708695884480429/125000000000000000000000000');old=F('46942230864663/62500000000000000');q=next(a for a in rd('remaining-record-audit/complete-audit-queue.json')['rows']if a['pr']==275)
ck('source_target_and_frozen_fixture_separate',F(expected['target'])==F(expected['assembly']['target'])==F(e['kappa_record'])==target and F(q['quoted_kappa_fraction'])==F(e['frozen_metadata_kappa'])==old and old!=target)
vr=(R/paths['research/finite-assembly-pr799/verify.py']).read_text(encoding='utf8');ck('actual_own_selection_is_799_application',"package = upstream / 'research/gauge44-frames-x'"in vr and"os.environ['WITNESS_SPEC'] = str(package / 'data/SPEC.json')"in vr and"target = assembly.greatest_grid_target(c, b, grid)"in vr)
native=rd('pr799-finite-controller-native.json');ck('same_named799_native_not_its_cutoff',native==n['own_native_theorem_facts']and n['own_selected_SPEC_sha256']==hs(paths['research/gauge44-frames-x/data/SPEC.json'])and spec['providers']['gauge44']['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']==native['selected_program_semantic_sha256'])
for suffix,path in[('__SPEC.json','research/gauge44-frames-x/data/SPEC.json'),('__PLAN.json','research/gauge44-frames-x/data/PLAN.json'),('__OWNERS.json.gz','research/gauge44-frames-x/data/OWNERS.json.gz')]:
 hits=[h for f,h in native['source_sha256'].items()if f.startswith('older-reviewed-source/799/')and f.endswith(suffix)];ck('exact_complete799_'+suffix,hits==[hs(paths[path])])
chron=rd('pr275-cap-source/chronology-primary-receipt.json')
for a in chron['primary_sources']:ck('primary_API_exact_'+a['file'],hs(a['file'])==a['sha256']);pins[a['file']]=a['sha256']
pr=rd('pr275-cap-source/current-pull275-api.json');commit=rd('pr275-cap-source/source-head-commit-api.json');merge=rd('pr275-cap-source/actual-merge-commit-api.json')
ck('actual_pull_head_and_actual_merge_second_parent',pr['number']==275 and pr['merged']is True and pr['head']['sha']==commit['sha']==head and pr['merge_commit_sha']==merge['sha']==chron['merge_commit_sha']and len(merge['parents'])==2 and merge['parents'][1]['sha']==head)
ck('source_revision_did_not_exist_at_PR_creation',datetime.fromisoformat(pr['created_at'].replace('Z','+00:00'))<datetime.fromisoformat(commit['commit']['committer']['date'].replace('Z','+00:00'))<datetime.fromisoformat(pr['merged_at'].replace('Z','+00:00')))
ck('actual_included_at_merge_date_not_creation',pr['merged_at']==chron['merged_at']==e['source_revision_included_at_merge']=='2026-10-16T15:51:16Z'and commit['commit']['committer']['date']==e['source_revision_committed_at']=='2026-10-13T11:43:12Z')
ck('required_visible_correction_scope',e['source_selected_kappa_correction']and'Frozen metadata is preserved'in e['source_selected_kappa_correction_basis'])
ck('new_Gaussian_only_realization_scope',not e['historical_literal_dual_supplier_rerun']and not e['native_engine_independently_rerun_here']and not e['ordinary_BIT_supplier_consumed']and e['meaningful_lower']is None and not e['actual_first_crossing_known'])
for group in['source_sha256','dependency_hashes']:
 for f,h in e[group].items():ck('all_cost_source_deps_'+f,hs(f)==h);pins[f]=h
peer=rd('pr275-supplied-cap-gaussian-peer-review.json');ck('independent_math_peer_binds_actual_upper_and_record',peer['reviewed_sha256']['pr275-supplied-cap-gaussian-early-upper.json']==hs('pr275-supplied-cap-gaussian-early-upper.json')and peer['reviewed_sha256']['pr275-supplied-cap-gaussian-record-upper.json']==hs('pr275-supplied-cap-gaussian-record-upper.json'))
out=dict(schema='own-source-and-primary-chronology-supplemental-review/1',pr=275,own_head=head,review_status='PASS_actual_merged_head_source_cap_and_explicit_chronology_correction',scope='Separate AI-assisted source/hash/primary-API chronology audit, alongside the separately authored independent mathematical peer. This author also prepared the cost adaptation; this receipt does not claim a second independent human or proof-kernel review.',actual_source_selected_kappa=str(target),frozen_metadata_kappa=str(old),mandatory_visible_source_correction=True,source_revision_committed_at=e['source_revision_committed_at'],source_revision_included_at_merge=e['source_revision_included_at_merge'],source_revision_merge_commit=e['source_revision_merge_commit'],source_was_included_by_actual_merge_second_parent=True,creation_date_not_used_for_later_revision=True,mathematical_or_native_engines_replayed_here=False,fast_cost_replay=run.stdout.strip(),material_findings_remaining=[],reviewed_sha256=pins,checks_passed=len(checks),checks=checks,reproducer_sha256=hs(Path(__file__).name))
(R/'pr275-supplied-cap-gaussian-source-peer-review.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own275 exact source and primary merge-chronology supplemental checks')
