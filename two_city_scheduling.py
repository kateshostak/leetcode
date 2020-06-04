from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = {i: elem[0] - elem[1] for i, elem in enumerate(costs)}
        i = 0
        sum_ = 0
        for key in sorted(diff, key=lambda x: diff[x]):
            if i < n//2:
                sum_ += costs[key][0]
            else:
                sum_ += costs[key][1]
            i += 1
        return sum_


def main():
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    res = Solution().twoCitySchedCost(costs)
    print(f'expected::110, got::{res}')

    costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    res = Solution().twoCitySchedCost(costs)
    print(f'expected::1859, got::{res}')


if __name__ == '__main__':
    main()
