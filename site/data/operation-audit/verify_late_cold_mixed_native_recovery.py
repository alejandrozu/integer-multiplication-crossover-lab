"""Fast offline byte/selection verification; does not rerun the native engines."""
from pathlib import Path
from hashlib import sha256
import gzip,json,sys

sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
checks={}

def ck(name,value):
    if not value:raise AssertionError(name)
    checks[name]=True

def hs(file):return sha256((R/file).read_bytes()).hexdigest()

def rd(file):
    b=(R/file).read_bytes()
    return json.loads(gzip.decompress(b)if str(file).endswith('.gz')else b)

def ident(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

names=['late-cold-mixed-native-byte-recovery-638.json','late-cold-mixed-native-variant-recovery.json']
receipts=[rd(f)for f in names]
scripts=['recover_late_cold_mixed_native_bytes.py','recover_late_cold_variants_native_bytes.py']
for name,script,doc in zip(names,scripts,receipts):
    ck(name+' script',hs(script)==doc['script_sha256'])
    ck(name+' checks',len(doc['checks'])==doc['checks_passed']and all(v is True for v in doc['checks'].values()))
    ck(name+' stages',bool(doc['steps'])and all(a['exit_code']==0 for a in doc['steps']))
    ck(name+' phase scope',doc['full_phase_or_operator_engine_replayed']is False)
    for field in ['source_sha256','retained_base_sha256','dependency_hashes']:
        for f,h in doc.get(field,{}).items():ck(name+' '+field+' '+f,hs(f)==h)

base,variants=receipts
ck('base limited replay scope',base['original_complete_source_package_replay_claimed']is False and base['whole_owner_or_cost_proved']is False)
ck('variant limited replay scope',variants['complete_global_or_cost_proved']is False)
closure=rd('late-cold-mixed-source/native-source-closure-638.json')
manifest=rd('late-cold-mixed-source/variant-own-source-manifest.json')
for a in closure['objects']:ck('closure '+a['file'],hs(a['file'])==a['sha256'])
for row in manifest['rows']:
    M=rd(row['own_MANIFEST_file'])
    for a in row['source_files']:
        ck(str(row['pr'])+' own source '+a['relative'],hs(a['file'])==a['sha256'])
        if a['relative']!='MANIFEST.json':ck(str(row['pr'])+' own M '+a['relative'],M[a['relative']]==a['sha256'])

raws=base['raw_intermediates']+variants['new_raw_intermediates']
for a in raws:
    ck('raw container '+a['file'],hs(a['file'])==a['sha256'])
    ck('raw complete bytes '+a['decompressed_sha256'],sha256(gzip.decompress((R/a['file']).read_bytes())).hexdigest()==a['decompressed_sha256'])

outputs=variants['outputs'];objects={}
for a in outputs:
    ck('selected container '+a['file'],hs(a['file'])==a['sha256'])
    obj=rd(a['file']);ck('selected whole object '+a['file'],ident(obj)==a['semantic_sha256'])
    if a['artifact']=='LOCAL-PROGRAMS.json.gz':ck('selected both orientations '+a['file'],{k:ident(v)for k,v in obj.items()}==a['orientation_sha256'])
    objects.setdefault(a['raw_content_sha256'],{})[a['artifact']]=a

rows=[dict(pr=638,own_head=base['own_head'],SPEC_file=closure['SPEC_file'],SPEC_sha256=closure['SPEC_sha256']),*manifest['rows']]
ck('six independently bound source heads',{r['pr']for r in rows}=={636,638,639,640,642,644}and len(rows)==6)
selected=[]
for row in rows:
    pr=row['pr'];spec=rd(row['SPEC_file']);ck(str(pr)+' own SPEC bytes',hs(row['SPEC_file'])==row['SPEC_sha256'])
    for pid,p in spec['providers'].items():
        matches=[]
        for raw,objs in objects.items():
            can=objs['CANONICAL-WORD.json.gz'];prog=objs['LOCAL-PROGRAMS.json.gz']
            if can['semantic_sha256']==p['artifact_semantic_sha256']['CANONICAL-WORD.json.gz']and prog['semantic_sha256']==p['artifact_semantic_sha256']['LOCAL-PROGRAMS.json.gz']and prog['orientation_sha256']==p['program_hashes']:matches.append(raw)
        ck(str(pr)+' complete own provider '+pid,len(matches)==1)
        stored=[a for a in variants['exact_own_selected_provider_matches']if a['pr']==pr and a['provider']==pid]
        ck(str(pr)+' receipt own provider '+pid,len(stored)==1 and stored[0]['own_head']==row['own_head']and stored[0]['SPEC_sha256']==row['SPEC_sha256']and stored[0]['raw_content_sha256']==matches[0])
        selected.append(dict(pr=pr,provider=pid,raw_content_sha256=matches[0]))

out=dict(schema='own-K492-native-fast-offline-byte-verification/1',status='passed',checks_passed=len(checks),checks=checks,source_recovery_receipts={f:hs(f)for f in names},selected_own_providers=selected,script_sha256=hs(Path(__file__).name),scope='Checks every retained source, RAW byte string, complete selected canonical/program object and both orientation commitments in the executed native-recovery receipts. It authenticates the saved successful stage receipts but does not rerun their constructors/engines, prove universal native operator/absolute-phase contracts, or create a physical invoice or crossover bound.')
(R/'late-cold-mixed-native-fast-offline-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('PASS',len(checks),'offline native byte/own selection checks;',len(selected),'own selected providers')
