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
                    step = 1
                    is_square = True
                    while is_square and j + step < len(matrix[i]) and i + step < len(matrix):
                        if int(matrix[i + step][j + step]):

                            size += 1
                            for delta in range(step + 1):
                                if not int(matrix[i + delta][j + step]):
                                    is_square = False
                                    size -= 1
                                    break

                            if not is_square:
                                break

                            for delta in range(step + 1):
                                if not int(matrix[i + step][j + delta]):
                                    is_square = False
                                    size -= 1
                        step += 1
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

    matrix = [[1, 1], [1, 1]]
    print(Solution().maximalSquare(matrix))


if __name__ == '__main__':
    main()
