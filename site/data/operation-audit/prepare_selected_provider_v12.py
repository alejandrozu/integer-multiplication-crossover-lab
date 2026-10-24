"""Frozen source-specific cold14 cohort after exact typed native byte reconstruction."""
from pathlib import Path
from hashlib import sha256
import copy,json,shutil
A=Path(__file__).resolve().parent;rd=lambda n:json.loads((A/n).read_bytes());hs=lambda n:sha256((A/n).read_bytes()).hexdigest()
old=rd("selected-provider-dispatch-v10-inputs.json");recovery=rd("cold14-typed-chain-native-byte-recovery.json");selection=rd("cold14-own-selection-source/manifest.json")
IDS={586,601,603,604,607,609,610,614,616,618};cohort=[copy.deepcopy(r)for r in old["cohort_rows"]if r["pr"]in IDS];assert {r["pr"]for r in cohort}==IDS
sources={a["file"]:a for a in old["actual_native_archive_sources"]}
for a in recovery["outputs"]:
 if a["artifact"]not in ["CANONICAL-WORD.json.gz","LOCAL-PROGRAMS.json.gz"]:continue
 assert hs(a["file"])==a["sha256"];sources[a["file"]]=dict(file=a["file"],sha256=a["sha256"],origin="exact_own604_typed_constructor_derived_native_bytes",primary=a)
D=A/"selected-provider-dispatch-v12-source";D.mkdir(exist_ok=True)
for row in cohort:
 pr=row["pr"];out=D/str(pr);out.mkdir(exist_ok=True)
 # Both own physical artifacts already have own selectedSPEC hash-bound receipts.
 for kind in ["PLAN","OWNERS"]:
  path=f"selected-provider-dispatch-v10-source/{pr}/{kind}.json";r=rd(path);assert r.get("status")=="authenticated_own_SPEC_declared_bytes"and hs(r["file"])==r["sha256"];shutil.copy2(A/path,out/(kind+".json"))
 # Own-head entrypoint literal default and MANIFEST resolve actual selectedSPEC,
 # independently of quoted kappa or the programme recovery archive.
 files=[a for a in selection if a["pr"]==pr and"error"not in a];M=next(a for a in files if a["path"].endswith("/MANIFEST.json"));V=next(a for a in files if a["path"].endswith("/verify.py"));manifest=rd(M["file"]);v=(A/V["file"]).read_text()
 assert all(a["own_head"]==row["own_head"]and hs(a["file"])==a["sha256"]and a["api_own_blob_verified"] for a in files)
 assert ("default=P/'data/SPEC.json'"in v or "SPECFILE=P/'data/SPEC.json';SPEC="in v) and "SPEC=json.loads(SPECFILE.read_bytes());BUILD=SPEC['build']"in v and manifest["verify.py"]==V["sha256"]
 candidates=[a for a in row["verified_components"]if a.get("path","").endswith("/data/SPEC.json")and a["sha256"]==manifest["data/SPEC.json"]];assert len(candidates)==1,(pr,candidates)
 assert hs(candidates[0]["file"])==candidates[0]["sha256"]
 (out/"actual-own-selector.json").write_text(json.dumps(dict(pr=pr,own_head=row["own_head"],SPEC_file=candidates[0]["file"],SPEC_sha256=candidates[0]["sha256"],MANIFEST=M,verifier=V,verified_primary=files),indent=2)+"\n")
out=dict(schema="selected-provider-dispatch-frozen-inputs/12",cohort_rows=cohort,claim_metadata=[a for a in old["claim_metadata"]if a["pr"]in IDS],actual_native_archive_sources=list(sources.values()),original_input_sha256={p:hs(p)for p in ["selected-provider-dispatch-v10-inputs.json","cold14-typed-chain-native-byte-recovery.json","cold14-own-selection-source/manifest.json"]},scope="Ten actual own selected finite-controller packages. Programme byteobjects are discovered through exact original typed constructor identities; no native phase or cost transfer. Own entrypoint+MANIFEST+SPEC+PLAN+OWNERS/program/physical/invoice and parameter funding are each mandatory.")
(A/"selected-provider-dispatch-v12-inputs.json").write_text(json.dumps(out,indent=2)+"\n")
s=(A/"selected_provider_dispatch.py").read_text().replace("selected-provider-dispatch-source","selected-provider-dispatch-v12-source").replace("selected-provider-dispatch-inputs","selected-provider-dispatch-v12-inputs").replace("selected-provider-dispatch.json","selected-provider-dispatch-v12.json")
s=s.replace("finite_actual_owner_census","finite_actual_owner_census_v2")
needle="            adapter=16*(max(v['scalar_macros']for v in c.values())"
insert="""            require(w is not None,'actual canonical catalogue required for helper-entry census in this cohort')
            first=2*w['v'];entry_ranks=[len(w['frames'][i])for i in w['start'][first:]]
            require(len(entry_ranks)==f['helpers']and all(type(x)is int and 0<=x<=9 for x in entry_ranks),'own actual canonical initial helper dimensions')
            final_ranks=[len(w['frames'][i])for i in w['final'][first:]]
            require(len(final_ranks)==f['helpers']and [b-a for a,b in zip(entry_ranks,final_ranks)]==f['widths'],'own helper productive width equals actual final-minus-initial rank')
            require(all(ownerc.basis(w['frames'][a]+w['frames'][b])==ownerc.basis(w['frames'][b])for a,b in zip(w['start'][first:],w['final'][first:])),'own initial helper subspace lies in final subspace')
            providers[pid].update(entering_flags=[bool(x)for x in entry_ranks],initial_helper_ranks=entry_ranks,final_helper_ranks=final_ranks)
            require(sum(providers[pid]['entering_flags'])==p['entering']and sum(entry_ranks)==p['entrance'],'own actual canonical entering-helper count/rank')
"""
assert needle in s;s=s.replace(needle,insert+needle)
s=s.replace("physical_entry_output_absolute_phase_contract_freshly_proved=False))","physical_entry_output_absolute_phase_contract_freshly_proved=False,initial_helper_ranks=providers[pid]['initial_helper_ranks'],final_helper_ranks=providers[pid]['final_helper_ranks'],entering_flags=providers[pid]['entering_flags']))")
s=s.replace(",('entering_helpers','entering_helper_roles')","")
needle="        require(role['rank_surplus']==73*ex['live']-ex['rank_mass'],'own exact live/mass surplus')"
insert="""        declared=ex.get('entering_helper_roles');actual=role['actual_nonzero_start_frame_roles'];legacy=role['width_below_9_roles']
        meter=dict(source_declared_entering_helper_roles=declared,actual_nonzero_start_frame_roles=actual,width_below_9_roles=legacy,source_declared_meter_style='actual_initial_nonzero_frames'if declared==actual else'legacy_width_below_9'if declared==legacy else'unreproduced_descriptive_metadata',source_declared_counter_matches_actual=declared==actual,used_by_new_cost_stock_or_precision=False)
"""
assert needle in s;s=s.replace(needle,insert+needle)
s=s.replace("operator_phase_proved=False,canonical_catalogue_absent_for=", "operator_phase_proved=False,descriptive_entering_counter=meter,canonical_catalogue_absent_for=")
(A/"selected_provider_dispatch_v12.py").write_text(s,encoding="utf8")
print("Preparedowncold14cohort",len(cohort),"actualnativebytefiles",len(sources))
