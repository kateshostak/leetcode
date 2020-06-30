from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = {}
        for start, end in tickets:
            if start not in d:
                d[start] = []
            d[start].append(end)
            d[start].sort()

        res = []
        start = 'JFK'
        last_ = None
        while True:
            changed = False
            res.append(start)
            for i, elem in enumerate(d[start]):
                if elem in d:
                    changed = True
                    tmp = elem
                    d[start][i] = None
                    start = tmp
                    break
                else:
                    if elem != None:
                        last_ = elem
            if not changed:
                break
        if last_:
            res.append(last_)
        return res


def main():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK", "MUC", "LHR", "SFO", "SJC"], got::{res}')

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK","ATL","JFK","SFO","ATL","SFO"], got::{res}')

    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::,["JFK","NRT","JFK","KUL"] got::{res}')


if __name__ == '__main__':
    main()
