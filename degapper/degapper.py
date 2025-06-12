import ast
import os
import sys
import argparse
import re

from collections import defaultdict
from pprint import pprint

from tools.utils import Input


def searchFront(route, routes):
    n = len(route.split("/"))
    for i in range(1, n):
        nodes = route.split("/")[:-i]
        if len(nodes) < 2 + i:
            continue

        r = "/".join(nodes)
        for k, v in routes.items():
            if v is None:
                continue
            if v[0] == r:
                return k, i

    return None, None


def searchBack(route, routes, i):
    r = route.split("/")[-(i + 1):]
    r = "/".join(r)
    for k, v in routes.items():
        if v is None:
            continue

        vv = v[0].split("/")[-(i + 1):]
        vv = "/".join(vv)
        if vv == r:
            return k
    return None


def checkIsMinor(route, routes):
    front, i = searchFront(route, routes)
    if front is None:
        return None, None

    back = searchBack(route, routes, i)
    if back is None:
        return None, None

    return front, back


def DeGapper(routes, previousResult):
    # 検出したギャップのカウント
    c = 0

    # 今回検出されたギャップを蓄積していく
    result = {}

    for name, r in routes.items():
        isGap = True
        for k, v in previousResult.items():
            if v is None:
                continue
            elif v[0] == r:
                isGap = False

        if isGap:
            c += 1

            # 検出したギャップがメジャーかマイナーかチェック
            front, back = checkIsMinor(r, previousResult)

            if front is not None and back is not None:
                # 前半分と後ろ半分、両方ヒットすればマイナーギャップ
                previousResult[name] = [r, "minor"]
                result[name] = [r, "minor"]
            else:
                # そうでなければメジャーギャップ
                previousResult[name] = [r, "major"]
                result[name] = [r, "major"]

    # ギャップが検出されなかったときは、Noneを入れておく
    if result == {}:
        fileName = name.split("-")[0]
        result[f"{fileName}-000"] = None
        previousResult[f"{fileName}-000"] = None

    return previousResult, result


parser = argparse.ArgumentParser()
parser.add_argument("--check-times", action="store_true")
args = parser.parse_args()

ipt = Input()[1:]

# 入力をファイルごとに分割
routes = defaultdict(dict)  # {folder: {file: [], file: [], ...}}
for x in ipt:
    name, r = x.split(",")
    folder = "/".join(re.split(r"[\\/]", name)[:-1])
    file = re.split(r"[\\/]", name)[-1].split("-")[0]
    if file not in routes[folder]:
        routes[folder][file] = {}
    routes[folder][file][name] = r

previousResult = {}
for folder, data in routes.items():
    times = {}
    for file, r in data.items():
        if args.check_times:
            p, t = DeGapper(r, times)
            times |= t
        else:
            p, t = DeGapper(r, previousResult)

        previousResult |= t

print("name,gap,major/minor")
for f, r in previousResult.items():
    if r is None:
        print(f"{f},,")
    else:
        print(f"{f},{r[0]},{r[1]}")
