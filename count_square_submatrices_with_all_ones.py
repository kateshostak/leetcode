from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r_m = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        c_m = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        res = []
        for i in range(len(matrix)):
            k = 0
            for j in range(len(matrix[i])):
                elem = matrix[i][j]
                if elem == 0:
                    k = 0
                k += elem
                r_m[i][j] = k

        for j in range(len(matrix[0])):
            k = 0
            for i in range(len(matrix)):
                elem = matrix[i][j]
                if elem == 0:
                    k = 0
                k += elem
                c_m[i][j] = k

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    k = 0
                    n = 0
                    i_1 = i
                    j_1 = j
                    while k == n and i_1 < len(matrix) and j_1 < len(matrix[0]):
                        k += 1
                        n = min(r_m[i_1][j_1], c_m[i_1][j_1])
                        n = min(k, n)
                        i_1 += 1
                        j_1 += 1
                    if k == n:
                        res.append(k)
                    else:
                        res.append(k - 1)
        return sum(res)


def main():
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    res = Solution().countSquares(matrix)
    print(f'expected::15, got::{res}')

    matrix = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    res = Solution().countSquares(matrix)
    print(f'expected::7, got::{res}')

if __name__ == '__main__':
    main()
