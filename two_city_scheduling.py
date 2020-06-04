from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = []
        for a, b in costs:
            diff.append(a - b)

        i = 0
        sum_ = 0
        for elem in sorted(diff):
            while i < n:
                if i < n//2:
                    sum_ += costs[i][0]
                else:
                    sum_ += costs[i][1]
                i += 1
        return sum_



def main():
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    res = Solution().twoCitySchedCost(costs)
    print(f'expected::110, got::{res}')


if __name__ == '__main__':
    main()
