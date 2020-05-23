from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a_ind = 0
        b_ind = 0
        res = []
        while a_ind < len(A) and b_ind < len(B):
            start_a, end_a = A[a_ind]
            start_b, end_b = B[b_ind]
            start = max(start_a, start_b)
            end = min(end_a, end_b)
            if end < start:
                if start_a < start_b:
                    a_ind += 1
                else:
                    b_ind += 1
            else:
                res.append([start, end])
                if start_a < start_b:
                    a_ind += 1
                else:
                    b_ind += 1
        return res


def main():
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = Solution().intervalIntersection(A, B)
    print(f'expected::[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], got::{res}')


if __name__ == '__main__':
    main()
