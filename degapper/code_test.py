import os
from glob import glob


files = glob("tb/*/*.py")
for file in files:
    dir = os.path.dirname(file)
    name = os.path.basename(file)
    name, ext = name.split(".")

    name = f"0{name}p.{ext}"

    npath = f"{dir}/{name}"

    os.rename(file, npath)
