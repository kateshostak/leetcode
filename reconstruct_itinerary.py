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
        while start in d:
            res.append(start)
            if d[start]:
                start = d[start].pop(0)
            else:
                break
        if res[-1] != start:
            res.append(start)
        return res


def main():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK", "MUC", "LHR", "SFO", "SJC"], got::{res}')

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK","ATL","JFK","SFO","ATL","SFO"], got::{res}')


if __name__ == '__main__':
    main()
