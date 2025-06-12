import re
import argparse
import os
import json

from glob import glob
from pprint import pprint
from collections import defaultdict

from tools.Visitor import Visitor

parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

result = defaultdict(dict)  # {folder: file: [max_nest, structures]}
folders = glob(f"{args.dir}/*/")
for folder in folders:
    files = glob(f"{folder}/*.py")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        # 構文木で判断できる要素
        routes = Visitor(code).visit(isFirst=True)

        structures = set()
        # 最も深いネスト構造の深さを記録する
        maxNest = 0
        for route in routes:
            nest = re.search(r"((/If|/For|/While){2,})", route)
            if nest:
                nest = nest.group()[1:]  # 最初の/を消す
                structures.add(nest)
                nest = nest.split("/")
                maxNest = max(maxNest, len(nest))
        fileName = os.path.basename(file)
        folder = folder.replace("\\", "/")
        result[folder][fileName] = [maxNest, list(structures)]

# 検出したネスト構造を出力(json形式)
print(json.dumps(result, indent=4))

# 最大深さをcsv形式で出力
# print("file,max_nest")
# for folder, data in result.items():
#     for file, maxNest in data.items():
#         print(f"{folder}{file},{maxNest}")
