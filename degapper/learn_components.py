import re
import argparse
import os

from glob import glob
from pprint import pprint
from collections import defaultdict

from tools.Visitor import Visitor

printMatchTemplate = re.compile(r"\s*print\(")
inputMatchTemplate = re.compile(r".*\sinput\(")
loopMatchTemplate = re.compile(r".*while\sTrue:")

parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

result = defaultdict(dict)  # {folder: file: [comp, struct]}
folders = glob(f"{args.dir}/*/")
for folder in folders:
    files = glob(f"{folder}/*.py")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        # 検出した構文要素
        components = set()

        # ソースコードから判断する要素
        for line in code.split("\n"):
            if printMatchTemplate.match(line):
                components.add("表示")
            if inputMatchTemplate.match(line):
                components.add("入力")
            if loopMatchTemplate.match(line):
                components.add("loop")

        # 構文木で判断できる要素
        routes = Visitor(code).visit(isFirst=True)
        for route in routes:
            if re.match(r".*Name\(var\)", route):
                components.add("変数")
            if re.match(r".*/If", route):
                components.add("if/else")
            if re.match(r".*/For", route):
                components.add("for")
            if re.match(r".*/While", route):
                components.add("while")
            if re.match(r".*/List", route):
                components.add("配列")
            if re.match(r".*/FunctionDef", route):
                components.add("関数定義")
            if re.match(r".*/(And)|(Or)", route):
                components.add("and/or")
            if re.match(r".*/Elif", route):
                components.add("elseif")
            if re.match(r".*/Dict", route):
                components.add("辞書")

        # 入れ子構造の判定
        structure = set()
        for route in routes:
            if re.match(r".*(/If|/For|/While){2,}", route):
                components.add("入れ子構造")

        fileName = os.path.basename(file)
        result[folder][fileName] = components

# 構文要素のチェック表を表示
print("file,output,variable,input,if/else,for,while,array,nest,function,and/or,elseif,loop,dict")
target = ["表示", "変数", "入力",
          "if/else", "for", "while", "配列", "入れ子構造",
          "関数定義", "and/or", "elseif", "loop", "辞書"]
for folder, data in result.items():
    for file, components in data.items():
        s = f"{folder}{file},".replace("\\", "/")
        for t in target:
            s += "1," if t in components else "0,"
        s = s[:-1]
        print(s)
