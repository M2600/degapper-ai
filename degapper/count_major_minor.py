import json
import re
import argparse

from collections import defaultdict
from pprint import pprint

from tools.utils import Input


parser = argparse.ArgumentParser()
parser.add_argument("--json", action="store_true")
args = parser.parse_args()

ipt = Input()[1:]

gaps = defaultdict(dict)
for x in ipt:
    name, route, type_ = x.split(",")
    folder = "/".join(re.split(r"[\\/]", name)[:-1])
    gaps[folder][name] = [route, type_]

counts = defaultdict(dict)
for fn, fl in gaps.items():
    for name, gap in fl.items():
        fileName = name.split("/")[-1].split("-")[0]
        if fileName not in counts[fn]:
            counts[fn][fileName] = {"major": 0, "minor": 0}
        if gap[0] != "":
            counts[fn][fileName][gap[1]] += 1

if args.json:
    print(json.dumps(counts, indent=4))
else:
    print("file,major,minor")
    for k in counts:
        for name in counts[k]:
            print(f"{name},{counts[k][name]["major"]},{counts[k][name]["minor"]}")
