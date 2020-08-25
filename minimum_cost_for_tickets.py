from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        start = days[0]
        end = days[-1]
        nodes = {}
        curr = 0
        for i in range(len(days)):
            if curr not in nodes:
                nodes[curr] = []

            if curr + 1 in days:
                nodes[curr].append(curr + 1)

            if curr + 6 in days:
                nodes[curr].append(curr + 6)

            if curr + 29 in days:
                nodes[curr].append(curr + 29)
            curr = days[i]

        print(nodes)


def main():
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    res = Solution().mincostTickets(days, costs)


if __name__ == '__main__':
    main()
