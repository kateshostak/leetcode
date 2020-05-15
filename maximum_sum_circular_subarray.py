from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        len_ = len(A)
        start, end, max_ = self.max_sum(A)
        max_here = max_

        print(start, end, max_)
        if start == 0 and end == len_ - 1:
            i = start
            while i < end:
                tmp = max_here - A[i]
                max_here = max(tmp, max_here)
                max_ = max(max_here, max_)
                i += 1
        elif start == 0:
            i = len_ - 1
            tmp = None
            max_tmp = None
            while i > end:
                if not tmp:
                    tmp = A[i]
                    max_tmp = tmp
                else:
                    tmp += A[i]
                max_tmp = max(max_tmp, tmp)
                i -= 1
            max_ = max(max_ + max_tmp, max_)
        elif end == len_ - 1:
            i = 0
            tmp = None
            max_tmp = None
            while i < start:
                if not tmp:
                    tmp = A[i]
                    max_tmp = tmp
                else:
                    tmp += A[i]
                max_tmp = max(max_tmp, tmp)
                i += 1
            max_ = max(max_ + max_tmp, max_)
        return max_

    def max_sum(self, A):
        max_ = max_here = A[0]
        start = end = tmp_start = tmp_end = 0
        for i in range(1, len(A)):
            if A[i] > max_here + A[i]:
                tmp_start = i
                tmp_end = i
                max_here = A[i]
            else:
                tmp_end = i
                max_here += A[i]
            if max_here >= max_:
                start = tmp_start
                end = tmp_end
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

    arr = [-5, 3, 5]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::8, got::{res}')

    arr = [2, -2, 2, 7, 8, 0]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::19, got::{res}')

    arr = [8, -1, -3, 8, -6, -9, 2, 4]
    res = Solution().maxSubarraySumCircular(arr)
    print(f'expected::18, got::{res}')

if __name__ == '__main__':
    main()
