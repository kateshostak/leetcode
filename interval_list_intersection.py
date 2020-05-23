from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [-1]*(max(A[-1][1], B[-1][1]) + 1)
        intrvl = []
        for start, end in A:
            for i in range(start, end + 1):
                res[i] = end

        for start, end in B:
            for i in range(start, end + 1):
                if res[i] != -1:
                    start_n = max(i, start)
                    end_n = min(end, res[i])
                    intrvl.append((start_n, end_n))
                    break

            for i in range(start, end + 1):
                res[i] = max(end, res[i])

        return intrvl


def main():
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = Solution().intervalIntersection(A, B)
    print(f'expected::[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], got::{res}')


if __name__ == '__main__':
    main()
