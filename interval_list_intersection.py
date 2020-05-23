from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        a_ind = 0
        b_ind = 0
        res = []
        while b_ind < len(B):
            start_a, end_a = A[a_ind]
            start_b, end_b = B[b_ind]
            start = max(start_a, start_b)
            end = min(end_a, end_b)
            if end >= start:
                res.append([start, end])

            if a_ind < len(A) - 1:
                a_ind += 1
            else:
                b_ind += 1
        return res


def main():
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = Solution().intervalIntersection(A, B)
    print(f'expected::[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], got::{res}')

    A = [[3, 5], [9, 20]]
    B = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    res = Solution().intervalIntersection(A, B)
    print(f'expected::[[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]], got::{res}')

    A = []
    B = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    res = Solution().intervalIntersection(A, B)
    print(f'expected::[], got::{res}')

    A = [[4, 6], [7, 8], [10, 17]]
    B = [[5, 10]]
    res = Solution().intervalIntersection(A, B)
    print(f'expected::[[5, 6], [7, 8], [10, 10]], got::{res}')


if __name__ == '__main__':
    main()
