from .tools.Visitor import Visitor

class ParseTree:
    def __init__(self):
        pass

    def extract_routes(self, file):
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        name = file.replace(".py", "")
        routes = Visitor(code).visit(isFirst=True)
        # 重複を削除しながら順序を保持
        seen = set()
        unique_routes = []
        for route in routes:
            if route not in seen:
                unique_routes.append(route)
                seen.add(route)
        return name, unique_routes

    def process_files(self, files):
        results = []
        for file in files:
            name, routes = self.extract_routes(file)
            for i, route in enumerate(routes, start=1):
                results.append((f"{name}-{i:03d}", route))
        return results