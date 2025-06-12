import re


def Input():
    res = []
    while True:
        try:
            res.append(input())
        except:
            break
    return res


def changeNameNode(**kargs):
    node = kargs["node"]
    nodes = kargs["nodes"]
    isFuncNode = kargs["isFuncNode"]
    isOreElse = kargs["isOrElse"]

    name = str(type(node).__name__)

    if len(nodes) > 1 and name == "Name":
        if isFuncNode:
            name = "Name(func)"
        else:
            name = "Name(var)"
    elif name == "If" and isOreElse:
        name = "Elif"
    return name


def saveResult(outputPath, gaps, args, dontShow=False):
    folderName = re.split(r"[\/]", outputPath)[-2]
    with open(outputPath, "w", encoding="utf-8") as f:
        if args.csv_style and not dontShow:
            print("fileName,major,minor")
            f.write("fileName,major,minor\n")
        if args.check_times: print(f"=== {folderName} ===")

        major = 0
        minor = 0
        file = ""
        for k, v in gaps.items():
            if v is not None:
                if v[1] == "":
                    major += 1
                else:
                    minor += 1

            _file = k.split("-")[0]
            if file != _file:
                if file != "":
                    if args.csv_style:
                        output = f"{file},{major},{minor}"
                        f.write(output + "\n")
                        if not dontShow: print(output)
                    else:
                        output = f"[{file}] major={major}, minor={minor}"
                        f.write(output + "\n")
                        if not dontShow: print(output)
                file = _file
                major = 0
                minor = 0
                # print("::", file, major, minor)

            if not args.csv_style and args.detail_result:
                if v is None:
                    if not dontShow: print(f"{k}: no gaps")
                else:
                    output = f"{k}: {v[0]}" + ("" if v[1] == "" else f" ({v[1]})")
                    f.write(output + "\n")
                    if not dontShow: print(output)

        # ループ内では最後のファイルが出力されないので、追加で処理する
        if args.csv_style:
            output = f"{file},{major},{minor}"
            f.write(output + "\n")
            if not dontShow: print(output)
        else:
            output = f"[{file}] major={major}, minor={minor}"
            f.write(output + "\n")
            if not dontShow: print(output)
