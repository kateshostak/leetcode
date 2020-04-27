from typing import List
import pdb


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_ = 0
        min_ = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if int(matrix[i][j]):
                    size = 1
                    min_ = 1
                    i2 = i + 1
                    j2 = j - 1
                    step = 1
                    is_square = True
                    while is_square and j2 >= 0 and i2 < len(matrix):
                        size += 1

                        if int(matrix[i2][j2]):
                            for i3 in range(i2 - i):
                                if not int(matrix[i + i3][j2]):
                                    is_square = False
                                    size -= 1

                            for j3 in range(j2 - j):
                                if not int(matrix[i2][j + j3]):
                                    is_square = False
                                    size -= 1
                        i2 += 1
                        j2 -= 1
                    max_ = max(size, max_)

        return max(max_*max_, min_)

def main():
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        ]
    # out = 2*2

    matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
            ]
    # out = 4

    matrix = [
            [1, 1],
            [1, 1]
            ]
    print(Solution().maximalSquare(matrix))


if __name__ == '__main__':
    main()
