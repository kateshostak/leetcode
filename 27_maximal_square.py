from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            if sum(matrix[i]) >= 2:
                for j in range(i + 1, len(matrix)):
                    for k in range(len(matrix[i])):
                        matrix[i][k] &= matrix[j][k]

        for row in matrix:
            print(row)


def main():
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        ]
    print(Solution().maximalSquare(matrix))


if __name__ == '__main__':
    main()
