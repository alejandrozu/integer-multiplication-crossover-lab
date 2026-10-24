"""Public plot chronology adapter retaining the complete original primary receipt."""
from pathlib import Path
from hashlib import sha256
import json
R=Path(__file__).resolve().parent
rd=lambda n:json.loads((R/n).read_bytes());hs=lambda n:sha256((R/n).read_bytes()).hexdigest()
c=rd('pr1175-final-mixed-source/chronology-primary-receipt.json');p=rd('pr1175-native-cost-source/api-pr1175.json');m=rd('pr1175-native-cost-source/api-merge-commit.json');h=rd('pr1175-native-cost-source/api-own-head-commit.json');a=rd('pr1175-native-cost-source/chronology-api-inputs.json')
assert all(c['checks'].values())and c['source_revision_merge_commit']==m['sha']==p['merge_commit_sha']and c['own_head']==h['sha']==p['head']['sha']and c['source_revision_included_at_merge']==p['merged_at']
for x in a.values():assert hs(x['file'])==x['sha256']==c['source_sha256'][x['file']]
parents=[x['sha']for x in m['parents']];assert parents[5]==h['sha']and len(parents)==23
out=dict(schema='source-selected-corrected-kappa-plot-chronology/1',pr=1175,own_head=h['sha'],source_head=h['sha'],merged_at=p['merged_at'],merge_commit_sha=m['sha'],merge_parents=parents,source_committed_at=h['commit']['committer']['date'],actual_own_selected_kappa=c['actual_own_selected_kappa'],frozen_metadata_kappa=c['frozen_metadata_kappa'],original_primary_receipt='pr1175-final-mixed-source/chronology-primary-receipt.json',source_sha256={**c['source_sha256'],'pr1175-final-mixed-source/chronology-primary-receipt.json':hs('pr1175-final-mixed-source/chronology-primary-receipt.json')},script_sha256=hs(Path(__file__).name),scope=c['scope'])
(R/'pr1175-final-mixed-source/plot-chronology-primary-receipt.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS own1175plotchronology adapter')
