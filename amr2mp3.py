#-*- coding:utf-8 -*-
import os
import subprocess
import sys
 
def amr2mp3(amr_path,mp3_path=None):
    path, name = os.path.split(amr_path)
    if name.split('.')[-1]!='amr':
        print('not a amr file')
        return 0
    if mp3_path is None or mp3_path.split('.')[-1]!='mp3':
        mp3_path = os.path.join(path, name.split('.')[0] +'.mp3')
    error = subprocess.call(['ffmpeg','-loglevel','error','-y','-i',amr_path,mp3_path])
    if error:
        return 0
    print('amr2mp3 success :' , mp3_path)
    return mp3_path
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('没有要转换的amr文件路径')
        sys.exit()
    if len(sys.argv) == 2:
        scrpit,amr_path = sys.argv
        mp3_path=None
    else:
        scrpit,amr_path,mp3_path = sys.argv
    amr2mp3(amr_path,mp3_path)
