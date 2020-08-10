class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, columns = len(grid), len(grid[0])
        oranges = 0
        rotten = 0
        rotten_ind = []
        def go_rotten(i, j):
            grid[i][j] = 3
            if i + 1 < rows and grid[i + 1][j] =! 0 and grid[i + 1][j] != 3:
                rotten += 1
                grid[i + 1][j] = 3

            if i - 1 > 0 and grid[i - 1][j] != 0 and grid[i - 1][j] != 3:
                rotten += 1
                grid[i - 1][j] = 3

            if j + 1 < columns and grid[i][j + 1] != 0 and grid[i][j + 1] !+ 3:
                rotten += 1
                gird[i][j + 1] = 3

            if j - 1 > 0 and grid[i][j - 1] != 0 and grid[i][j - 1] != 3:
                rotten += 1
                grid[i][j - 1] = 3

        for i in rows:
            for j in columns:
                if grid[i][j] != 0:
                    oranges += 1
                    if grid[i][j] == 2:
                        go_rotten(i, j)


