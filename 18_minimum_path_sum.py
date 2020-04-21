from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        self.sum_ = 0
        sums = []
        sum_ = 0
        self.min_sum = None
        def traverse(i, j, sum_):
            if i == m and j == n:
                sum_ += grid[i][j]
                if not self.min_sum:
                    self.min_sum = sum_
                else:
                    if sum_ < self.min_sum:
                        self.min_sum = sum_
                sums.append(sum_)
                return
            sum_ += grid[i][j]
            if self.min_sum:
                if sum_ > self.min_sum:
                    print('r')
                    return
            if j + 1 <= n:
                traverse(i, j+1, sum_)
            if i + 1 <= m:
                traverse(i+1, j, sum_)
        traverse(0, 0, sum_)
        print(sums)
        return self.min_sum



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
    # grid = [[1,2],
    #         [1,1]]
    # grid = [[0,7,7,8,1,2,4,3,0,0,5,9,8,3,6,5,1,0],[2,1,1,0,8,1,3,3,9,9,5,8,7,5,7,5,5,8],[9,2,3,1,2,8,1,2,3,7,9,7,9,3,0,0,3,8],[3,9,3,4,8,1,2,6,8,9,3,4,9,4,8,3,6,2],[3,7,4,7,6,5,6,5,8,6,7,3,6,2,2,9,9,3],[2,3,1,1,5,4,7,4,0,7,7,6,9,1,5,5,0,3],[0,8,8,8,4,7,1,0,2,6,1,1,1,6,4,2,7,9],[8,6,6,8,3,3,5,4,6,2,9,8,6,9,6,6,9,2],[6,2,2,8,0,6,1,1,4,5,3,1,7,3,9,3,2,2],[8,9,8,5,3,7,5,9,8,2,8,7,4,4,1,9,2,2],[7,3,3,1,0,9,4,7,2,3,2,6,7,1,7,7,8,1],[4,3,2,2,7,0,1,4,4,4,3,8,6,2,1,2,5,4],[1,9,3,5,4,6,4,3,7,1,0,7,2,4,0,7,8,0],[7,1,4,2,5,9,0,4,1,4,6,6,8,9,7,1,4,3],[9,8,6,8,2,6,5,6,2,8,3,2,8,1,5,4,5,2],[3,7,8,6,3,4,2,3,5,1,7,2,4,6,0,2,5,4],[8,2,1,2,2,6,6,0,7,3,6,4,5,9,4,4,5,7]]
    print(Solution().minPathSum(grid))


if __name__ == '__main__':
    main()
