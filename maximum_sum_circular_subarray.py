from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        len_ = len(A)
        start, end, max_ = self.max_sum(A)

        A += A[:-1]
        max_here = max_
        if end == len_ - 1:
            print('hi')
            for i in range(len_, len(A)):
                tmp = max_here - A[start]
                print(f'start::{start}, max_::{max_}, tmp::{tmp}')
                if tmp > max_:
                    max_here -= A[start]
                    max_ = max_here
                start += 1

        print(A[:len_])
        print(start, end)
        return max_

    def max_sum(self, A):
        max_ = max_here = A[0]
        start = end = 0
        for i in range(1, len(A)):
            if A[i] >= max_here + A[i]:
                start = i
                end = i
                max_here = A[i]
            else:
                max_here += A[i]
            if max_here > max_:
                end = i
                max_ = max_here
        return start, end, max_


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

    arr = [9, -4, -7, 9]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::18, got::{res}')


if __name__ == '__main__':
    main()
