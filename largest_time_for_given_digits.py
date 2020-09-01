import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = 0
        for i, j, k, q in itertools.permutations(A):
            hours = i * 10 + j
            minutes = k * 10 + q
            if hours < 24 and minutes < 60:
                max_time = max(hours * 100 + minutes, max_time)

        return str(max_time % 100) * ':' + str(max_time // 100)


def main():
    A = [0, 6, 2, 6]
    res = Solution().largestTimeFromDigits(A)
    print(f'expected::"06:26", got::{res}')


if __name__ == '__main__':
    main()
