"""Restore and verify the complete source/proof tree from deduplicated ZIP parts."""
from pathlib import Path,PurePosixPath,PureWindowsPath
from hashlib import sha256
from collections import defaultdict
import argparse,json,os,re,zipfile

def digest(path):
    h=sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def long(path):
    # Callers pass absolute, lexically checked paths inside a freshly created
    # output tree. Re-resolving every path repeatedly traverses Windows parents.
    path=Path(path).absolute();text=str(path)
    return Path('\\\\?\\'+text) if os.name=='nt' and not text.startswith('\\\\?\\') else path

def restore(package_dir,output,progress=None):
    package_dir=Path(package_dir).resolve();output=Path(output).resolve()
    descriptor=json.loads((package_dir/'reproduction-package.json').read_text(encoding='utf8'))
    assert descriptor['schema']=='content-addressed-reproduction/1'
    assert digest(Path(__file__).resolve())==descriptor['restore_script_sha256'],'Restore tool differs from the package manifest'
    parts=descriptor['archives'];assert parts
    for part in parts:
        assert re.fullmatch(r'operation-audit-objects-\d+\.zip',part['file'])
        p=package_dir/part['file']
        assert p.stat().st_size==part['bytes'] and digest(p)==part['sha256'],part['file']
    with zipfile.ZipFile(package_dir/descriptor['manifest_archive']) as z:
        manifest=json.loads(z.read('REPRODUCTION-MANIFEST.json'))
    assert manifest['required_archives']==[p['file']for p in parts]
    members=manifest['members_sha256']
    assert sha256(json.dumps(members,sort_keys=True).encode()).hexdigest()==descriptor['full_payload_hash_map_sha256']
    assert not output.exists(),'Choose a new output directory'
    byhash=defaultdict(list);names=set();file_names=set()
    for name,h in members.items():
        rel=PurePosixPath(name)
        assert rel.parts and name==rel.as_posix() and not rel.is_absolute() and '..' not in rel.parts and '\\' not in name and ':' not in name
        assert not any(c<' ' for c in name)
        assert all(not p.endswith(('.', ' ')) and not PureWindowsPath(p).is_reserved() for p in rel.parts)
        assert re.fullmatch('[a-f0-9]{64}',h)
        key=name.casefold();assert key not in names,('Case-colliding output paths',name)
        names.add(key);file_names.add(tuple(p.casefold() for p in rel.parts))
        target=output/Path(*rel.parts);assert target.is_relative_to(output)
        byhash[h].append(target)
    assert all(parts[:i] not in file_names for parts in file_names for i in range(1,len(parts))),'File/directory output collision'
    assert len(members)==descriptor['full_payload_members']
    assert len(byhash)==descriptor['unique_objects']==manifest['unique_objects']
    long(output).mkdir(parents=True)
    written=0;size=0;seen=set();all_seen=set();created_directories={output}
    for part in parts:
        with zipfile.ZipFile(package_dir/part['file']) as z:
            for item in z.infolist():
                if not item.filename.startswith('objects/'):continue
                h=item.filename.removeprefix('objects/')
                assert re.fullmatch('[a-f0-9]{64}',h)and h not in all_seen,('Invalid or repeated object',h)
                all_seen.add(h)
                if h not in byhash:continue
                raw=z.read(item);assert sha256(raw).hexdigest()==h,('Corrupt object',h)
                for target in byhash[h]:
                    if target.parent not in created_directories:
                        long(target.parent).mkdir(parents=True,exist_ok=True)
                        created_directories.add(target.parent)
                    assert long(target).write_bytes(raw)==len(raw)
                    written+=1;size+=len(raw)
                    if progress and written%2000==0:progress(dict(files=written,total=len(members)))
                seen.add(h)
    assert seen==set(byhash) and written==len(members)
    if progress:progress(dict(files=written,total=len(members),complete=True))
    return dict(passed=True,files=written,unique_objects=len(seen),restored_bytes=size,
        full_payload_hash_map_sha256=descriptor['full_payload_hash_map_sha256'],
        output=str(output),scope='Exact source/proof reconstruction. Mathematical claims retain their individual assumptions.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(restore(args.package_dir,args.output),indent=2))
