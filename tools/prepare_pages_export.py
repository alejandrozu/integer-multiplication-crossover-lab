"""Copy an explicitly approved static export, preserving every published byte.

Large reproduction ZIPs stay in the public GitHub release. This tool never
copies a workspace, Git checkout metadata or Site credentials.
"""
from pathlib import Path
from hashlib import sha256
import argparse,json,re,shutil

ROOT=Path(__file__).resolve().parents[1]
RELEASE=re.compile(r'https://github\.com/alejandrozu/integer-multiplication-crossover-lab/releases/download/audit-[0-9][0-9a-z-]*/')
FORBIDDEN_DIRS={'.git','.openai','node_modules','__pycache__','.cache'}
FORBIDDEN_FILES={'.env','.env.local','.env.production','id_rsa','id_ed25519'}

def digest(p):
    h=sha256()
    with p.open('rb')as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True,help='The final static dist snapshot explicitly approved for publication')
    args=ap.parse_args();source=args.source.resolve();dest=ROOT/'site'
    assert(source/'index.html').is_file(),'Expected a static dist containing index.html'
    assert source!=ROOT and source!=ROOT.parent and source!=dest
    descriptor=json.loads((source/'data/reproduction-package.json').read_bytes())
    assert descriptor['schema']=='content-addressed-reproduction/1'
    for a in descriptor['archives']:
        assert RELEASE.fullmatch(a['download_url'].removesuffix(a['file'])) and a['download_url'].endswith('/'+a['file']),('Archive still requires a different/private hosting service',a['file'])
    approved={};omitted=[]
    for p in sorted(source.rglob('*')):
        rel=p.relative_to(source)
        assert not p.is_symlink(),('Symbolic link in export',rel.as_posix())
        assert not(FORBIDDEN_DIRS&set(rel.parts)),('Workspace/credential directory in export',rel.as_posix())
        if not p.is_file():continue
        assert p.name not in FORBIDDEN_FILES and not p.name.startswith('.env.'),('Credential filename in export',rel.as_posix())
        if p.suffix.lower()in{'.zip','.tar'}or p.name.endswith('.tar.gz'):
            omitted.append(rel.as_posix());continue
        approved[rel.as_posix()]=p
    assert approved and 'index.html'in approved and 'data/reproduction-package.json'in approved
    existing={p.relative_to(dest).as_posix()for p in dest.rglob('*')if p.is_file()}
    assert not(existing-set(approved)-{'.nojekyll'}),('Stale export paths require review',sorted(existing-set(approved)-{'.nojekyll'}))
    hashes={}
    for rel,p in approved.items():
        out=dest/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,out)
        before=digest(p);assert digest(out)==before,rel;hashes['site/'+rel]=before
    (dest/'.nojekyll').write_bytes(b'')
    report=dict(schema='public-static-export-byte-verification/1',public_repository='https://github.com/alejandrozu/integer-multiplication-crossover-lab',public_site='https://alejandrozu.github.io/integer-multiplication-crossover-lab/',files_copied=len(hashes),export_bytes=sum(p.stat().st_size for p in approved.values()),source_reproduction_descriptor_sha256=digest(source/'data/reproduction-package.json'),omitted_release_archives=omitted,files_sha256=hashes,scope='Explicitly approved final dist only. Every copied file is byte-identical; ZIP archives are public release assets. No workspace, .git, .openai, credentials or symbolic links are copied.')
    (ROOT/'public-export-verification.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(dict(passed=True,files=len(hashes),bytes=report['export_bytes'],omitted_archives=len(omitted)),indent=2))

if __name__=='__main__':main()
