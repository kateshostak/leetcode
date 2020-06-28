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

        res = []
        start = sorted(d)[0]
        while start in d:
            res.append(start)
            start = d[start]
        res.append(start)
        return res


def main():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = Solution().findItinerary(tickets)
    print(f'expected::["JFK", "MUC", "LHR", "SFO", "SJC"], got::{res}')


if __name__ == '__main__':
    main()
