"""Portable actual-native census; optional import from completed research jobs.

Default reproduction reads recovered finite bytes already committed by each
own SPEC's semantic hashes. It replays scalar identities/costs, not discovery,
constructor controls or full Clifford phase synthesis.
"""
from pathlib import Path
from collections import Counter
import argparse,gzip,hashlib,importlib.util,json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'early-mixed-native-outputs';C=R/'early-mixed-provider-source'
def read(p):return json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_bytes())
def hs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def ident(o):return hashlib.sha256(canon(o)).hexdigest()
def portable(o):
    b=bytearray(gzip.compress(canon(o),mtime=0));b[9]=255;return bytes(b)
ap=argparse.ArgumentParser();ap.add_argument('--import-workbenches',action='store_true');args=ap.parse_args()
checks={}
def ck(n,v):assert v,n;checks[n]=True
own=read(C/'own-packages-manifest.json')
if args.import_workbenches:
    a=read(R/'early-mixed-provider-reconstruction-workbench.json');b=read(R/'early-mixed-later-layer-workbench.json')
    assert a['status']=='own_selected_native_components_only'and all(a['checks'].values())and a['script_sha256']==hs(R/'early_mixed_provider_reconstruction.py')
    assert b['status']=='own_selected_native_components_only'and all(b['checks'].values())and b['script_sha256']==hs(R/'early_mixed_later_layers.py')
    rows={588:a['providers'],**{int(k):v['providers']for k,v in b['rows'].items()}}
    imported=[]
    for pr,providers in rows.items():
        ownspec=next(x for x in own if x['pr']==pr and x['logical_path']=='data/SPEC.json')
        for pid,w in providers.items():
            loc=Path(w['local_dir']);dest=D/str(pr)/pid;dest.mkdir(parents=True,exist_ok=True)
            files={}
            for name in['CANONICAL-WORD.json.gz','LOCAL-PROGRAMS.json.gz']:
                obj=read(loc/name);p=dest/name;p.write_bytes(portable(obj));files[name]=dict(file=p.relative_to(R).as_posix(),sha256=hs(p),semantic_sha256=ident(obj))
            imported.append(dict(pr=pr,own_head=ownspec['head'],provider=pid,own_SPEC_file='early-mixed-provider-source/'+ownspec['file'],own_SPEC_sha256=ownspec['sha256'],files=files,origin='Recovered by deterministic own-SPEC pinned construction and local pipelines; derived bytes, not a Git primary artifact.',construction_component_script_sha256=hs(R/('early_mixed_provider_reconstruction.py'if pr==588 else'early_mixed_later_layers.py'))))
    D.mkdir(exist_ok=True);(D/'manifest.json').write_text(json.dumps(imported,indent=2)+'\n')

rows=read(D/'manifest.json')
s=importlib.util.spec_from_file_location('actual_program_component',R/'finite_selected_program_census.py');mod=importlib.util.module_from_spec(s);s.loader.exec_module(mod)
outputs=[];sourcepins={};derivedpins={}
for row in rows:
    pr=row['pr'];pid=row['provider'];tag=str(pr)+'_'+pid+'_'
    ck(tag+'own_SPEC_primary_sha',hs(R/row['own_SPEC_file'])==row['own_SPEC_sha256'])
    sourcepins[row['own_SPEC_file']]=row['own_SPEC_sha256'];spec=read(R/row['own_SPEC_file']);provider=spec['providers'][pid]
    for name,f in row['files'].items():
        ck(tag+'derived_file_'+name,hs(R/f['file'])==f['sha256'])
        ck(tag+'own_selected_semantic_'+name,ident(read(R/f['file']))==f['semantic_sha256']==provider['artifact_semantic_sha256'][name])
        derivedpins[f['file']]=f['sha256']
    programs=read(R/row['files']['LOCAL-PROGRAMS.json.gz']['file']);word=read(R/row['files']['CANONICAL-WORD.json.gz']['file'])
    census=mod.census(programs,canonical=word);contract=provider['complete_contract']
    ck(tag+'own_two_orientation_pins',all(census[o]['sha256']==provider['program_hashes'][o]for o in programs))
    ck(tag+'own_actual_columns',all(census[o]['columns']==2*word['v']+word['R']==contract['n']for o in programs))
    for orientation,c in census.items():
        expected=contract['local'][orientation]
        ck(tag+orientation+'_actual_cost_and_prefix',c['events']==expected['events']and c['scalar_macros']==expected['macros']and c['real_component_primitives']==expected['real_component_primitives']and c['coefficient_work_primitives']==expected['coefficient_work_primitive_count']and c['prefix_l1']==expected['prefix_l1'])
        ck(tag+orientation+'_actual_widths_profile_and_wrappers',c['widths']==contract['widths']and c['paid_profile']=={int(k):v for k,v in provider['expected_profile'].items()}and c['pre_wrappers']==expected['pre_wrappers']and c['post_wrappers']==expected['post_wrappers'])
    ck(tag+'source_inventory',Counter(census['forward']['widths'])=={int(k):v for k,v in provider['inventory'].items()})
    outputs.append(dict(pr=pr,own_head=row['own_head'],provider=pid,own_SPEC_file=row['own_SPEC_file'],own_SPEC_sha256=row['own_SPEC_sha256'],canonical_file=row['files']['CANONICAL-WORD.json.gz']['file'],program_file=row['files']['LOCAL-PROGRAMS.json.gz']['file'],canonical_semantic_sha256=ident(word),program_semantic_sha256=ident(programs),selected_local_census=census,ports=word['ports'],centre_frames=[word['frames'][f]for f in word['center_frames']],frame_dimension=word['h'],native_coordinate_rank=73,full_phase_engine_replayed_now=False,scope='Exact earlier own-selected native bytes and fresh scalar identities, dimensions, widths, primitives/prefixes. Constructor/native-frame replay is archived research evidence; phase/normalized-wrapper semantics and whole hosting remain separate hypotheses.'))
deps=['finite_selected_program_census.py','early-mixed-native-outputs/manifest.json']
out=dict(schema='own-mixed-selected-native-components/1',status='actual_selected_native_scalar_components_verified_no_whole_bound',rows=outputs,checks_passed=len(checks),checks=checks,source_sha256=sourcepins,derived_selected_bytes_sha256=derivedpins,dependency_hashes={p:hs(R/p)for p in deps},script_sha256=hs(Path(__file__)),whole_integer_upper=None,meaningful_lower=None,constructor_replay_in_default_job=False,full_phase_engine_replay_in_default_job=False)
(R/'early-mixed-native-components.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'native_components':len(outputs),'prs':sorted({x['pr']for x in outputs})},indent=2))
