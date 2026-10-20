# SPDX-License-Identifier: GPL-2.0-or-later
"""Build the standalone ARM64 FFmpeg component with corresponding source.

Requires macOS Command Line Tools. Never installs into the system or Homebrew.
Source archives are supplied beside SOURCES.json; all hashes are checked first.
"""
import argparse,hashlib,json,os,shutil,subprocess,tarfile
from pathlib import Path
PINS={
 'ffmpeg-7.1.tar.xz':'40973d44970dbc83ef302b0609f2e74982be2d85916dd2ee7472d30678a7abe6',
 'x264-31e19f92.tar.gz':'d053c9d86988d6bc78237ca5205865c5ddf99c98ef4cd9927eec8f6d388f6dd9',
 'lame-3.100.tar.gz':'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e',
 'pkg-config-0.29.2.tar.gz':'6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591'}
def build(sources,work,jobs):
 sources=Path(sources).resolve();work=Path(work).resolve();work.mkdir(parents=True,exist_ok=True)
 prefix=work/'prefix';prefix.mkdir(exist_ok=True);extracted={}
 for name,sha in PINS.items():
  path=sources/name
  if hashlib.sha256(path.read_bytes()).hexdigest()!=sha:raise ValueError('Source hash mismatch: '+name)
  with tarfile.open(path) as archive:
   entries=archive.getmembers()
   for entry in entries:
    target=(work/entry.name).resolve()
    if not target.is_relative_to(work) or not (entry.isfile() or entry.isdir()):raise ValueError('Unsafe source archive')
   folder=work/entries[0].name.split('/')[0]
   if not folder.exists():archive.extractall(work)
  extracted[name]=folder
 env=os.environ.copy();env.update(MACOSX_DEPLOYMENT_TARGET='14.2',CC='clang',CXX='clang++',
     CFLAGS='-O2 -mmacosx-version-min=14.2 -Wno-int-conversion -Wno-incompatible-function-pointer-types',
     PATH=str(prefix/'bin')+os.pathsep+env.get('PATH',''),PKG_CONFIG_PATH=str(prefix/'lib/pkgconfig'))
 log=work/'build.log';commands=[]
 with log.open('a') as stream:
  def run(folder,args):
   commands.append({'directory':str(folder.relative_to(work)),'argv':args})
   result=subprocess.run(args,cwd=folder,env=env,stdout=stream,stderr=subprocess.STDOUT)
   if result.returncode:raise RuntimeError('Build failed; inspect '+str(log))
  for name,args in [
    ('pkg-config-0.29.2.tar.gz',['--with-internal-glib','--disable-shared','--enable-static']),
    ('x264-31e19f92.tar.gz',['--enable-static','--disable-cli','--disable-opencl','--host=aarch64-apple-darwin']),
    ('lame-3.100.tar.gz',['--enable-static','--disable-shared','--disable-frontend','--with-pic'])]:
   folder=extracted[name]
   print('Building',name,flush=True)
   run(folder,['./configure','--prefix='+str(prefix),*args]);run(folder,['make','-j'+str(jobs)]);run(folder,['make','install'])
  folder=extracted['ffmpeg-7.1.tar.xz'];print('Building FFmpeg 7.1',flush=True)
  args=['./configure','--prefix='+str(prefix),'--arch=arm64','--cc=clang','--disable-autodetect','--disable-doc','--disable-debug','--disable-ffplay','--disable-ffprobe','--enable-zlib','--enable-gpl','--enable-libx264','--enable-libmp3lame','--enable-static','--disable-shared','--pkg-config-flags=--static','--extra-cflags=-I'+str(prefix/'include')+' -mmacosx-version-min=14.2','--extra-ldflags=-L'+str(prefix/'lib')+' -mmacosx-version-min=14.2','--disable-encoders','--enable-encoder=libx264,aac,libmp3lame,pcm_s16le,pcm_s24le,pcm_f32le,mjpeg,png,wrapped_avframe']
  run(folder,args);run(folder,['make','-j'+str(jobs)]);run(folder,['make','install'])
 (work/'build-commands.json').write_text(json.dumps(commands,indent=2))
 subprocess.run(['codesign','--force','--sign','-',str(prefix/'bin/ffmpeg')],check=True)
 subprocess.run(['codesign','--verify','--strict',str(prefix/'bin/ffmpeg')],check=True)
 print('Built',prefix/'bin/ffmpeg',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--sources',required=True);p.add_argument('--work',required=True);p.add_argument('--jobs',type=int,default=4);a=p.parse_args();build(a.sources,a.work,a.jobs)
