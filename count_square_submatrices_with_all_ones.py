from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and i >= 1 and j >= 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                res += matrix[i][j]
        return res


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
