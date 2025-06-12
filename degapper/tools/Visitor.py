import ast

from ..tools.utils import changeNameNode


class Visitor():
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(self.code)

    def visit(self, node=None, nodes=None, route=None,
              isFirst=False, isFuncNode=False, isOrElse=False,
              changeNameFunc=changeNameNode):

        if node is None:
            node = self.tree
        if nodes is None:
            nodes = []
        if route is None:
            route = ""

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
            # print(ast.dump(node, indent=4))
        else:
            r = f"{route}/{name}"

        nodes.append(r)
        res = nodes
        self.generic_visit(node=node, nodes=nodes, route=r, isFirst=False)

        return res

    def generic_visit(self, node, nodes, route, isFirst):
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        # print(ast.dump(node, indent=4))
                        # print(field)
                        # print("-" * 10)
                        if field == "orelse":
                            self.visit(node=item, nodes=nodes, route=route,
                                       isFirst=isFirst, isOrElse=True)
                        else:
                            self.visit(node=item, nodes=nodes, route=route,
                                       isFirst=isFirst)
            elif isinstance(value, ast.AST):
                # print(ast.dump(node, indent=4))
                # print(field)
                # print("-" * 10)
                if field == "func":
                    self.visit(node=value, nodes=nodes, route=route,
                               isFirst=isFirst, isFuncNode=True)
                else:
                    self.visit(node=value, nodes=nodes, route=route,
                               isFirst=isFirst, isFuncNode=False)

if __name__ == "__main__":
    code = """
x = 10
if x == 0:
    print("ok")
elif x == 1:
    print("ok")
elif x == 2:
    if x == 3:
        print("v")
else:
    print("a")
    """

    # tree = ast.parse(code)
    # print(ast.dump(tree, indent=2))

    res = Visitor(code).visit(isFirst=True, isFuncNode=False)
    print(res)
