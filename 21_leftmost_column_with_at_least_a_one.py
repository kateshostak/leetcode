class BinaryMatrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self):
        if self.matrix:
            return [len(self.matrix), len(self.matrix[0])]
        return [0, 0]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, columns = binaryMatrix.dimensions()
        min_col = -1
        for i in range(rows):
            if min_col > -1:
                if binaryMatrix.get(i, min_col) == 1:
                    tmp_min = self.find_one(binaryMatrix, i, columns)
                    if tmp_min < min_col:
                        min_col = tmp_min
            else:
                min_col = self.find_one(binaryMatrix, i, columns)
        return min_col

    def find_one(self, matrix, row, columns):
        i = 0
        j = matrix.dimensions()[1] - 1
        while i < j:
            mid = (i + j)//2
            if matrix.get(row, mid) == 0:
                i = mid + 1
            else:
                j = mid

        if i < columns:
            if matrix.get(row, i) == 1:
                return i
        return -1


def main():
    # Input: mat = [[0,0],[1,1]]
    # Output: 0

    # Input: mat = [[0,0],[0,1]]
    # Output: 1

    # Input: mat = [[0,0],[0,0]]
    # Output: -1

    # Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    # Output: 1
    mat = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
    print(Solution().leftMostColumnWithOne(BinaryMatrix(mat)))


if __name__ == '__main__':
    main()
