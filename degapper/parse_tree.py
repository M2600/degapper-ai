import os
import argparse

from glob import glob

from tools.Visitor import Visitor


parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

files = sorted(glob(f"{args.dir}/*/*.py"))
print("name,component")
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        code = f.read()

    name = file.replace(".py", "")

    # 全経路を取得
    routes = Visitor(code).visit(isFirst=True)

    # 重複を削除しながら、検出順をキープする
    _routes = []
    for route in routes:
        if route not in _routes:
            _routes.append(route)

    for i, route in enumerate(_routes, start=1):
        print(f"{name}-{i:03d},{route}")
