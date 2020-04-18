from typing import List
import pdb


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        self.sum_ = 0
        sums = []
        sum_ = 0
        def traverse(i, j, sum_):
            if i == m and j == n:
                sum_ += grid[i][j]
                sums.append(sum_)
                return
            sum_ += grid[i][j]
            if j + 1 <= n:
                traverse(i, j+1, sum_)
            if i + 1 <= m:
                traverse(i+1, j, sum_)
        traverse(0, 0, sum_)
        return min(sums)

def main():
    # Input:
    # [
    # [1,3,1],
    # [1,5,1],
    # [4,2,1]
    # ]
    # Output: 7
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(grid))


if __name__ == '__main__':
    main()
