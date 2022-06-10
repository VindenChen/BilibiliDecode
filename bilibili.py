from pathlib import Path
from numpy import fromfile, uint8

ROOT = Path(__file__).resolve().parent  # 脚本文件的父文件夹的绝对路径

for f in ROOT.rglob("**/*.mp4"):
    read = fromfile(f, dtype=uint8)
    if all(read[0:3] == [255, 255, 255]):
        read = read[3:]
        outfile = f"{str(f.name).split('_')[1]}.mp4"
        read.tofile(ROOT / outfile)
        print(outfile)
