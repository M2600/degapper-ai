import json
import re

from pprint import pprint
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
import matplotlib_fontja

from tools.utils import Input


def reg1dim(x, y):
    n = len(x)
    a = ((np.dot(x, y) - y.sum() * x.sum() / n) / ((x ** 2).sum() - x.sum() ** 2 / n))
    b = (y.sum() - a * x.sum()) / n
    return a, b


ipt = Input()

try:
    gaps = json.loads("\n".join(ipt))
except:
    # file,major,minor
    gaps = defaultdict(dict)
    for row in ipt[1:]:
        file, major, minor = row.split(",")
        folder = "/".join(re.split(r"[\\/]", file)[:-1])
        fileName = re.split(r"[\\/]", file)[-1]
        gaps[folder][file] = {"major": int(major), "minor": int(minor)}

# グラフにしやすいように整形
data = defaultdict(list)
for folder in gaps:
    names = []
    majors = []
    minors = []
    for file, res in gaps[folder].items():
        names.append(re.split(r"[\\/]", file)[-1])
        majors.append(res["major"])
        minors.append(res["minor"])
    data[folder] = [names, majors, minors]

# グラフ描画(個別)
for folder in data:
    timeName = re.split(r"[\\/]", folder)[-1]
    names = data[folder][0]
    x = np.arange(len(names))
    majorCS = np.cumsum(data[folder][1])
    minorCS = np.cumsum(data[folder][2])

    majorA, majorB = reg1dim(x, majorCS)
    minorA, minorB = reg1dim(x, minorCS)

    plt.figure(figsize=(12, 8))  # 横×縦
    plt.plot(names, majorCS, label=f"メジャー累積(回帰係数={majorA:.2f})", marker=".")
    plt.plot(names, minorCS, label=f"マイナー累積(回帰係数={minorA:.2f})", marker=".")
    plt.title(f"メジャー/マイナー累積({folder})")
    plt.legend()
    plt.ylabel("ギャップの累積数")
    plt.xlabel("ファイル名")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f"./{folder}/{timeName}_gaps.png")

# グラフ描画(全体)
className = list(data.keys())[0].split("/")[0]
totalMajors = []
totalMinors = []
totalNames = []
for folder, counts in data.items():
    name = folder.split("/")[1]
    totalNames += [f"{name}/{file}" for file in counts[0]]
    totalMajors += counts[1]
    totalMinors += counts[2]

plt.figure(figsize=(12, 8))
x = np.arange(len(totalNames))
totalMajorCS = np.cumsum(totalMajors)
totalMinorCS = np.cumsum(totalMinors)
totalMajorA, totalMajorB = reg1dim(x, totalMajorCS)
totalMinorA, totalMinorB = reg1dim(x, totalMinorCS)
plt.plot(totalNames, totalMajorCS, label=f"メジャー累積(回帰係数={totalMajorA:.2f})", marker=".")
plt.plot(totalNames, totalMinorCS, label=f"マイナー累積(回帰係数={totalMinorA:.2f})", marker=".")
plt.title(f"メジャー/マイナー累積({className})")
plt.legend()
plt.ylabel("ギャップの累積数")
plt.xlabel("ファイル名")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(f"{className}/total_gaps.png")
