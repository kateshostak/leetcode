from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        len_ = len(A)
        A += A[:-1]

        print(A)
        max_here = max_ = A[0]
        for i in range(1, len(A)):
            if A[i] >= max_here + A[i]
            max_here = max(elem, max_here + elem)
            max_ = max(max_here, max_)
        return max_


def main():
    arr = [1, -2, 3, -2]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::3, got::{res}')

    arr = [5, -3, 5]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::10, got::{res}')

    arr = [3, -1, 2, -1]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::4, got::{res}')

    arr = [-2, -3, -1]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::-1, got::{res}')

    arr = [3, -2, 2, -3]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::3, got::{res}')


if __name__ == '__main__':
    main()
