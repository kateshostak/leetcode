import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1
        for i, j, k, q in itertools.permutations(A):
            hours = i * 10 + j
            minutes = k * 10 + q
            if hours < 24 and minutes < 60:
                max_time = max(hours * 60 + minutes, max_time)

        if max_time == -1:
            return ''
        hours = max_time // 60
        minutes = max_time % 60
        return f'{hours:02d}:{minutes:02d}'


def main():
    A = [0, 6, 2, 6]
    res = Solution().largestTimeFromDigits(A)
    print(f'expected::06:26, got::{res}')

    A = [5, 5, 5, 5]
    res = Solution().largestTimeFromDigits(A)
    print(f'expected::, got::{res}')

    A = [0, 0, 0, 0]
    res = Solution().largestTimeFromDigits(A)
    print(f'expected::00:00, got::{res}')


if __name__ == '__main__':
    main()
