import sys
from pathlib import Path
from numpy import fromfile, uint8   # pip install numpy

ROOT = Path(sys.argv[0]).resolve().parent  # 脚本文件的父文件夹的绝对路径

for f in ROOT.rglob("**/*.mp4"):
    read = fromfile(f, dtype=uint8)
    if all(read[0:3] == [255, 255, 255]):
        outfile = f"{str(f.name).split('_')[1]}.mp4"
        read[3:].tofile(ROOT / outfile)
        print(outfile)

input()
