"""Restore the archived local paths from exact-byte release objects."""
from pathlib import Path
import argparse,json,hashlib,zipfile,shutil
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--assets',type=Path,required=True)
 parser.add_argument('--output',type=Path,required=True)
 parser.add_argument('--round',type=int,choices=range(12))
 parser.add_argument('--verify-only',action='store_true')
 args=parser.parse_args();base=Path(__file__).resolve().parents[1]
 source=json.loads((base/'archive/SOURCE_MAP.json').read_text(encoding='utf8'))
 objects={o['sha256']:o for o in json.loads((base/'archive/OBJECT_INDEX.json').read_text(encoding='utf8'))['objects']}
 prefix=None
 if args.round is not None:
  prefix=next(r['legacy_path_prefix'] for r in json.loads((base/'archive/ROUNDS.json').read_text(encoding='utf8')) if r['round']==args.round)
 entries=[e for e in source['entries'] if prefix is None or e['path']==prefix or e['path'].startswith(prefix+'/')]
 required={objects[e['sha256']]['pack'] for e in entries}
 assets={r['name']:r for r in json.loads((base/'archive/ASSETS.json').read_text(encoding='utf8'))}
 for name in sorted(required):
  p=args.assets/name
  if p.stat().st_size!=assets[name]['bytes'] or digest(p)!=assets[name]['sha256']:raise ValueError('Part checksum mismatch: '+name)
 print('Part checksums verified.',flush=True)
 target=args.output.resolve();target.mkdir(parents=True,exist_ok=True)
 if not args.verify_only:
  for name in source.get('directories',[]):
   if prefix is not None and not (name==prefix or name.startswith(prefix+'/')):continue
   p=(target/name).resolve()
   if not p.is_relative_to(target):raise ValueError('Unsafe directory path')
   p.mkdir(parents=True,exist_ok=True)
 packs={};count=0
 try:
  for e in entries:
   p=(target/e['path']).resolve()
   if not p.is_relative_to(target):raise ValueError('Unsafe source path')
   if args.verify_only or p.exists():
    if not p.is_file() or p.stat().st_size!=e['bytes'] or digest(p)!=e['sha256']:raise ValueError('Restored file mismatch: '+e['path'])
   else:
    obj=objects[e['sha256']];name=obj['pack']
    if name not in packs:packs[name]=zipfile.ZipFile(args.assets/name)
    p.parent.mkdir(parents=True,exist_ok=True);h=hashlib.sha256();written=0
    with packs[name].open(obj['member']) as f,p.open('xb') as g:
     for b in iter(lambda:f.read(8*1024*1024),b''):g.write(b);h.update(b);written+=len(b)
    if written!=e['bytes'] or h.hexdigest()!=e['sha256']:raise ValueError('Object mismatch: '+e['path'])
   count+=1
   if count%2000==0:print('Verified/restored',count,'of',len(entries),flush=True)
 finally:
  for z in packs.values():z.close()
 print('PASS:',count,'files. No archived code was executed.')
if __name__=='__main__':main()
