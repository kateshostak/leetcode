from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = {}
        for start, end in tickets:
            if start not in d:
                d[start] = end
            else:
                if d[start] > end:
                    d[start] = end

        res = {}
        start = sorted(d)[0]
        while start in d and start not in res:
            res[start] = 0
            start = d[start]
        res[start] = 0
        return res.keys()


def main():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK", "MUC", "LHR", "SFO", "SJC"], got::{res}')

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK", "MUC", "LHR", "SFO", "SJC"], got::{res}')


if __name__ == '__main__':
    main()
