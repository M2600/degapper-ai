import sys, os
import lizard


def calcCC(code):
    code = code.split("\n")
    while code[-1] == "":
        code = code[:-1]
    _code = []
    for c in code:
        c = c.replace("\t", "    ")
        c = "    " + c
        _code.append(c)

    code = "\n".join(_code)
    code = "def main():\n" + code
    # print(code)

    res = lizard.analyze_file.analyze_source_code("prog.py", code)
    res = res.function_list
    cc = 0
    for r in res:
        cc += r.__dict__["cyclomatic_complexity"]

    return cc


if __name__ == "__main__":
    print(calcCC("test2.py"))
