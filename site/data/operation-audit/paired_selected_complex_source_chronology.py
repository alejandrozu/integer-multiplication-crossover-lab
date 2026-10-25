"""Own545 selected-composition correction, preserving frozen baseline quote."""
from pathlib import Path
from hashlib import sha256
import json,sys,urllib.request
R=Path(__file__).resolve().parent;D=R/'paired-complex-selection-source/545';head='376426f3b2b26ab430d10baf16bbd9ff42990a7c';checks={};prim=[]
def ck(k,v):assert v,k;checks[k]=True
def hs(f):return sha256(f.read_bytes()).hexdigest()
def get(path,name):
    f=D/name;url='https://api.github.com/repos/CrocSwap/integer-mult-bounds/'+path
    if not f.exists():
        assert '--fetch'in sys.argv,'Run --fetch once to obtain immutable primary chronology inputs'
        f.write_bytes(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'own-paired-complex-chronology'}),timeout=90).read())
    prim.append(dict(primary_url=url,file=f.relative_to(R).as_posix(),sha256=hs(f),bytes=f.stat().st_size));return json.loads(f.read_bytes())
p=get('pulls/545','chronology-pull.json');s=get('git/commits/'+head,'chronology-source-git-commit.json');m=get('git/commits/'+p['merge_commit_sha'],'chronology-merge-git-commit.json');parents=[a['sha']for a in m['parents']]
ck('actual_own_PR_head',p['number']==545 and p['head']['sha']==s['sha']==head)
ck('actual_included_source_merge',p['merged']and p['merged_at']and p['merge_commit_sha']==m['sha']and head in parents)
ck('source_committed_before_actual_merge',s['committer']['date']<=p['merged_at'])
e=json.loads((D/'EXPECTED.json').read_bytes());frozen='1584931111785787/1000000000000000000';actual='793733736881443/500000000000000000'
ck('actual_selected_composition_vs_preserved_baseline',e['kappa']['pr535']['kappa']==actual and e['pr535']['kappa']==frozen and e['kappa']['pr535']['binding_component']=='complex')
out=dict(schema='own-source-version-primary-chronology/1',pr=545,source_head=head,own_head=head,merged_at=p['merged_at'],merge_commit_sha=m['sha'],merge_parents=parents,merge_parent_number=parents.index(head)+1,source_committed_at=s['committer']['date'],source_included_at_actual_merge=True,frozen_metadata_kappa=frozen,actual_own_selected_kappa=actual,source_selected_kappa_correction=True,primary_receipts=prim,source_sha256={a['file']:a['sha256']for a in prim},checks=checks,checks_passed=len(checks),script_sha256=hs(Path(__file__)),scope='Own545 complete primary535 composition target from EXPECTED.kappa.pr535 differs from the historical parser quote of EXPECTED.pr535, which is explicitly the cited535 baseline. Preserve both. Source existed at actual merge; no backdating or new accepted-record truth is inferred.')
(D/'chronology.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('PASS',len(checks),'own545 selected-composition/source chronology checks; parent',parents.index(head)+1,'of',len(parents))
