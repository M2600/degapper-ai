import re
from collections import defaultdict

class Degapper:
    def __init__(self, check_times=False):
        self.check_times = check_times
        self.previous_result = {}

    @staticmethod
    def _search_front(route, routes):
        n = len(route.split("/"))
        for i in range(1, n):
            nodes = route.split("/")[:-i]
            if len(nodes) < 2 + i:
                continue
            r = "/".join(nodes)
            for k, v in routes.items():
                if v is None:
                    continue
                if v[0] == r:
                    return k, i
        return None, None

    @staticmethod
    def _search_back(route, routes, i):
        r = route.split("/")[-(i + 1):]
        r = "/".join(r)
        for k, v in routes.items():
            if v is None:
                continue
            vv = v[0].split("/")[-(i + 1):]
            vv = "/".join(vv)
            if vv == r:
                return k
        return None

    @classmethod
    def _check_is_minor(cls, route, routes):
        front, i = cls._search_front(route, routes)
        if front is None:
            return None, None
        back = cls._search_back(route, routes, i)
        if back is None:
            return None, None
        return front, back

    def degap(self, routes, previous_result=None):
        if previous_result is None:
            previous_result = self.previous_result
        c = 0
        result = {}
        for name, r in routes.items():
            is_gap = True
            for k, v in previous_result.items():
                if v is None:
                    continue
                elif v[0] == r:
                    is_gap = False
            if is_gap:
                c += 1
                front, back = self._check_is_minor(r, previous_result)
                if front is not None and back is not None:
                    previous_result[name] = [r, "minor"]
                    result[name] = [r, "minor"]
                else:
                    previous_result[name] = [r, "major"]
                    result[name] = [r, "major"]
        if result == {}:
            fileName = name.split("-")[0]
            result[f"{fileName}-000"] = None
            previous_result[f"{fileName}-000"] = None
        return previous_result, result

    @staticmethod
    def split_input(ipt):
        routes = defaultdict(dict)
        for x in ipt:
            name, r = x.split(",")
            folder = "/".join(re.split(r"[\\/]", name)[:-1])
            file = re.split(r"[\\/]", name)[-1].split("-")[0]
            if file not in routes[folder]:
                routes[folder][file] = {}
            routes[folder][file][name] = r
        return routes

    def process(self, ipt):
        routes = self.split_input(ipt)
        previous_result = {}
        for folder, data in routes.items():
            times = {}
            for file, r in data.items():
                if self.check_times:
                    p, t = self.degap(r, times)
                    times |= t
                else:
                    p, t = self.degap(r, previous_result)
                previous_result |= t
        return previous_result