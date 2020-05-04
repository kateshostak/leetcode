from typing import List
import pdb


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_ = 0
        matrix2 = []
        matrix3 = []
        for i in range(len(matrix)):
            tmp = []
            tmp2 = []
            sum_ = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    sum_ += 1
                else:
                    sum_ = 0
                tmp.append(sum_)
                tmp2.append(sum_)
            matrix2.append(tmp)
            matrix3.append(tmp2)

        for j in range(len(matrix[0])):
            sum_ = 0
            tmp = []
            for i in range(len(matrix)):
                if matrix[i][j] == 1:
                    sum_ += 1
                else:
                    sum_ = 0
                matrix3[i][j] = sum_

                if matrix3[i][j] >= matrix2[i][j]:
                    is_square = True
                    size = 1
                    step = 1
                    while is_square and i - step == 0 and j - step >= 0:
                        if matrix3[i - step][j - step] != matrix2[i - step][j- step]:
                            is_square = False
                        else:
                            size += 1
                        step += 1
                    max_ = max(max_, size)
        for row in matrix:
            print(row)

        print()

        for row in matrix2:
            print(row)

        print()

        for row in matrix3:
            print(row)

        return max_*max_



def main():
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        ]
    # out = 4

    matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
            ]
    # out = 4

    matrix = [[1, 1], [1, 1]]
    # out = 4

    matrix = [
            [1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1]
            ]
    # out = 4

    print(Solution().maximalSquare(matrix))


if __name__ == '__main__':
    main()
