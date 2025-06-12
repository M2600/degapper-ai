import re
from collections import defaultdict

class CountMajorMinor:
    def __init__(self):
        pass

    def parse_input(self, ipt):
        gaps = defaultdict(dict)
        for x in ipt:
            name, route, type_ = x.split(",")
            folder = "/".join(re.split(r"[\\/]", name)[:-1])
            gaps[folder][name] = [route, type_]
        return gaps

    def count(self, ipt):
        gaps = self.parse_input(ipt)
        counts = defaultdict(dict)
        for fn, fl in gaps.items():
            for name, gap in fl.items():
                fileName = name.split("/")[-1].split("-")[0]
                if fileName not in counts[fn]:
                    counts[fn][fileName] = {"major": 0, "minor": 0}
                if gap[0] != "":
                    counts[fn][fileName][gap[1]] += 1
        return counts