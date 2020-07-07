from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if i == 0:
                    perim += 1
                if j == 0:
                    perim += 1
                if i == len(grid) - 1:
                    perim += 1
                if j == len(grid[i]) - 1:
                    perim += 1
                if i > 0 and grid[i - 1][j] == 0:
                    perim += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 0:
                    perim += 1
                if j > 0 and grid[i][j - 1] == 0:
                    perim += 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 0:
                    perim += 1
        return perim

def main():
    arr = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
            ]
    res = Solution().islandPerimeter(arr)
    print(f'expected::16, got::{res}')


if __name__ == '__main__':
    main()
