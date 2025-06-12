import argparse
import json
from degapper.tools.utils import Input
from degapper.degapper import Degapper
from glob import glob
from degapper.parse_tree import ParseTree
from degapper.count_major_minor import CountMajorMinor


parser = argparse.ArgumentParser()
parser.add_argument("--check-times", action="store_true")
parser.add_argument("dir")
args = parser.parse_args()


def call_parse_tree():

    files = sorted(glob(f"{args.dir}/**/*.py", recursive=True))
    if not files:
        print("No Python files found in the specified directory.")
        return
    parse_tree = ParseTree()
    results = parse_tree.process_files(files)

    resultText = "\n".join(f"{name},{route}" for name, route in results)

    #print("name,component")
    # for name, route in results:
    #     print(f"{name},{route}")
    #print(resultText)
    
    return resultText

def call_degapper(tree):

    degapper = Degapper(check_times=args.check_times)
    result = degapper.process(tree)

    gapsText = "\n".join(f"{name},{route[0]},{route[1]}" if route else f"{name},," for name, route in result.items())

    #print("name,gap,major/minor")
    # for f, r in result.items():
    #     if r is None:
    #         print(f"{f},,")
    #     else:
    #         print(f"{f},{r[0]},{r[1]}")
    #print(gapsText)
    if not gapsText.strip():
        print("No gaps found in the provided routes.")
        return None
    return gapsText
    



def call_count_degaps(gaps):
    count_major_minor = CountMajorMinor()
    counts = count_major_minor.count(gaps)

    counts_text = "\n".join(
        f"{folder}/{file},{count['major']},{count['minor']}"
        for folder, files in counts.items()
        for file, count in files.items()
    )

    #print("folder/file,major,minor")
    # for folder, files in counts.items():
    #     for file, count in files.items():
    #         print(f"{folder}/{file},{count['major']},{count['minor']}")
    #print(counts_text)
    return counts_text

def call_draw_graph():
    pass


def main():
    tree = call_parse_tree()
    tree_lines = tree.split("\n") if tree else []
    if tree:
        gaps = call_degapper(tree_lines)
    else:
        print("No routes found in the provided files.")
        return
    if gaps:
        gaps_lines = gaps.split("\n") if gaps else []
        gap_counts = call_count_degaps(gaps_lines)
    else:
        print("No gaps found in the provided routes.")
        return
    if gap_counts:
        print(gap_counts)
    else:
        print("No gap counts available.")
        return

if __name__ == "__main__":
    main()