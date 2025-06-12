import sys, os
import ast
import math

from tools.utils import changeNameNode


class CalcHV():
    def __init__(self, code):
        self.code = code

    def calc(self):
        tree = ast.parse(self.code)
        self.operators = []
        self.operands = []
        self.visit(tree, [], "", isFirst=True)

        N1 = len(self.operators)
        N2 = len(self.operands)
        n1 = len(set(self.operators))
        n2 = len(set(self.operands))

        if n1 + n2 == 0:
            return 0
        vol = (N1 + N2) * math.log2(n1 + n2)

        return vol

    def visit(self, node, nodes, route,
              isFirst=False, isFuncNode=False, isOrElse=False,
              changeNameFunc=changeNameNode):

        name = changeNameFunc(node=node,
                              nodes=nodes,
                              isFuncNode=isFuncNode,
                              isOrElse=isOrElse)

        if name == "Module":
            name = "Program"
        if name in ["Store", "Load"]:
            return nodes

        if isFirst:
            r = f"{name}"
        else:
            r = f"{route}/{name}"

        if name in ["Call"]:
            tn = type(node.func).__name__
            if tn == "Attribute":
                op = node.func.attr
            else:
                op = node.func.id
            self.operators.append(op)
        elif name in ["Assign", "AugAssign"]:
            self.operators.append("=")
        elif name in ["Add", "Sub", "Mult", "Div", "FloorDiv", "Pow", "Mod"]:
            self.operators.append(name)
        elif name in ["If", "Elif", "For", "While",
                      "And", "Or", "Not",
                      "Is", "IsNot", "In", "NotIn",
                      "Eq", "NotEq", "Lt", "LtE", "Gt", "GtE"]:
            self.operators.append(name)
        elif name == "IfExp":
            self.operators.append("If")
        elif name in ["Break", "Continue", "Pass", "Delete"]:
            self.operators.append(name)
        elif name in ["List", "Dict", "Tuple", "Set"]:
            self.operators.append(name)
        elif name in ["FunctionDef", "ClassDef"]:
            op = node.name
            self.operators.append(op)
        elif name == "arguments":
            defaults = node.defaults
            for default in defaults:
                self.operators.append("=")

        if name in ["Constant"]:
            od = node.value
            self.operands.append(od)
        elif name in ["Name(var)"]:
            od = node.id
            self.operands.append(od)
        elif name == "arguments":
            args = node.args
            for arg in args:
                an = arg.arg
                self.operands.append(an)
        # elif name in ["Call"]:
        #     args = node.args
        #     for arg in args:
        #         if type(arg).__name__ == "Name":
        #             an = arg.id
        #             self.operands.append(an)


        nodes.append(r)
        self.generic_visit(node=node, nodes=nodes, route=r,
                           isFirst=False)

        # print(ast.dump(node, indent=2))
        # print("::", name)
        # print(self.operators)
        # print(self.operands)
        # print("-" * 10)

    def generic_visit(self, node, nodes, route, isFirst):
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        if field == "orelse":
                            self.visit(node=item, nodes=nodes, route=route,
                                       isFirst=isFirst, isOrElse=True)
                        else:
                            self.visit(node=item, nodes=nodes, route=route,
                                       isFirst=isFirst)
            elif isinstance(value, ast.AST):
                if field == "func":
                    self.visit(node=value, nodes=nodes, route=route,
                               isFirst=isFirst, isFuncNode=True)
                else:
                    self.visit(node=value, nodes=nodes, route=route,
                               isFirst=isFirst, isFuncNode=False)


def calcHV(code, wantOps=False):
    # with open(file, "r", encoding="utf-8") as f:
    #     code = f.read()

    operators, operands = [], []
    tree = ast.parse(code)
    operators, operands = CalcHV(code).visit(tree, [], "",
                                          isFirst=True, isFuncNode=False)

    N1 = len(operators)
    N2 = len(operands)
    n1 = len(set(operators))
    n2 = len(set(operands))

    if n1 + n2 == 0:
        if wantOps:
            return 0, operators, operands
        else:
            return 0
    vol = (N1 + N2) * math.log2(n1 + n2)

    if wantOps:
        return vol, operators, operands
    else:
        return vol


if __name__ == "__main__":
    with open("../test.py", "r", encoding="utf-8") as f:
        code = f.read()
    # print(calcHV(code, wantOps=True))

    print(CalcHV(code).calc())
