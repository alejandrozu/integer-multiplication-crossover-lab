"""Bind actual own1175 final source selection and included-at-merge chronology."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
R=Path(__file__).resolve().parent
rd=lambda n:json.loads((R/n).read_bytes());hs=lambda n:sha256((R/n).read_bytes()).hexdigest()
manifest=rd('pr1175-native-cost-source/chronology-api-inputs.json');checks={}
def ck(n,v):assert v,n;checks[n]=True
for n,a in manifest.items():ck(n,hs(a['file'])==a['sha256'])
pull=rd('pr1175-native-cost-source/api-pr1175.json');head=rd('pr1175-native-cost-source/api-own-head-commit.json');merge=rd('pr1175-native-cost-source/api-merge-commit.json');meta=rd('pr1175-native-cost-source/frozen-own-PR-metadata.json');snap=rd('selected-provider-dispatch-v8-inputs.json');sel=snap['selection_receipts'][0]
ck('actual_own_head',pull['number']==1175 and pull['head']['sha']==head['sha']==sel['own_head']==meta['headRefOid'])
ck('actual_merge',pull['merged']and pull['merge_commit_sha']==merge['sha']and pull['merged_at']==meta['mergedAt'])
ordinals=[i+1 for i,p in enumerate(merge['parents'])if p['sha']==head['sha']];ck('actual_own_head_in_octopus_merge',ordinals==[6])
claim=rd(sel['claim_file']);spec=rd(sel['authority_file']);result=rd(sel['result_file']);ck('actual_final_claim_package','research/gauge44-slots-mixed-arcflow'in claim['head_kappa_package']and F(claim['head_kappa'])==F(spec['expected']['kappa'])==F(result['kappa'])==F(sel['record_kappa']))
ck('fixture_different_preserved',F(sel['frozen_metadata_kappa'])!=F(sel['record_kappa']))
ck('source_date_before_merge_after_creation',pull['created_at']<head['commit']['committer']['date']<pull['merged_at'])
source={a['file']:a['sha256']for a in manifest.values()};source.update({sel[k+'_file']:sel[k+'_sha256']for k in ['authority','claim','manifest','verifier','result']});source.update({'pr1175-native-cost-source/frozen-own-PR-metadata.json':hs('pr1175-native-cost-source/frozen-own-PR-metadata.json'),'selected-provider-dispatch-v8-inputs.json':hs('selected-provider-dispatch-v8-inputs.json')})
out=dict(schema='own1175-selected-source-chronology/1',pr=1175,status='passed_actual_source_selection_and_merge_chronology',own_head=head['sha'],frozen_metadata_kappa=sel['frozen_metadata_kappa'],actual_own_selected_kappa=sel['record_kappa'],source_selected_kappa_correction=True,source_revision_committed_at=head['commit']['committer']['date'],source_revision_included_at_merge=pull['merged_at'],source_revision_merge_commit=merge['sha'],own_head_parent_ordinal=ordinals[0],merge_parent_count=len(merge['parents']),claim_package=claim['head_kappa_package'],source_sha256=source,checks=checks,script_sha256=hs(Path(__file__).name),scope='Preserve the historical parsed fixture value. Actual final own source is separately selected and dated at its committed revision and inclusion at merge, not retroactively at PR creation. Sixth parent of a23-parent octopus merge, not second-parent inference.')
(R/'pr1175-final-mixed-source/chronology-primary-receipt.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS1175actualfinalsource chronology',len(checks))
