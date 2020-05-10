from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1
        d1 = defaultdict(list)
        d2 = defaultdict(list)
        for elem in trust:
            d1[elem[0]].append(elem[1])
            d2[elem[1]].append(elem[0])

        for key, arr in d2.items():
            if len(arr) == N - 1 and key not in d1:
                return key
        return -1


def main():
    N = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    res = Solution().findJudge(N, trust)
    print(f'expected::3, got::{res}')

    N = 2
    trust = [[1, 2]]
    res = Solution().findJudge(N, trust)
    print(f'expected::2, got::{res}')

    N = 3
    trust = [[1, 3], [2, 3]]
    res = Solution().findJudge(N, trust)
    print(f'expected::3, got::{res}')

    N = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    res = Solution().findJudge(N, trust)
    print(f'expected::-1, got::{res}')

    N = 3
    trust = [[1, 2], [2, 3]]
    res = Solution().findJudge(N, trust)
    print(f'expected::-1, got::{res}')


if __name__ == '__main__':
    main()
