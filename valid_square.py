from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        d = dict()
        points = [p1, p2, p3, p4]
        for elem in points:
            if elem[0] not in d:
                d[elem[0]] = []
            d[elem[0]].append(elem)

        if len(d) > 2:
            return False

        d2 = dict()
        for elem in points:
            if elem[1] not in d2:
                d2[elem[1]] = []
            d2[elem[1]].append(elem)

        if len(d2) > 2:
            return False

        for key, p in d.items():
            if p[0][1] == p[1][1]:
                return False

        return True
