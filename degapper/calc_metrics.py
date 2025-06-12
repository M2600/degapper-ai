# CCHVとかネスト数とか、その辺を計算する
import math
import argparse
import re

from glob import glob

from tools.calcCC import calcCC
from tools.calcHV import CalcHV


parser = argparse.ArgumentParser()
parser.add_argument("dir")
parser.add_argument("-dpd", "--decimal-point-digit", default=-1)
args = parser.parse_args()

# ファイル検索パターンを修正
files = glob(f"{args.dir}/*.py")
regex = re.compile(r".*[0-9]{4}[pq].py$")

print("file,loc,cc,hv,mi")
if args.decimal_point_digit == -1:
    template = "{file},{loc},{cc},{hv},{mi}"
else:
    dpd = str(args.decimal_point_digit)
    template = "{file},{loc},{cc},{hv:." + dpd + "f},{mi:." + dpd + "f}"

for file in files:
    if not regex.match(file):
        continue

    with open(file, "r", encoding="utf-8") as f:
        code = f.read()

    cc = calcCC(code)
    hv = CalcHV(code).calc()
    loc = len(list(filter(lambda x: x != "", code.split("\n"))))
    if hv == 0:
        mi = (171 - 0 - 0.23 * cc - 16.2 * math.log(loc)) * 100 / 171
    else:
        mi = (171 - 5.2 * math.log(hv) - 0.23 * cc - 16.2 * math.log(loc)) * 100 / 171

    print(template.format(file=file, loc=loc, cc=cc, hv=hv, mi=mi))
