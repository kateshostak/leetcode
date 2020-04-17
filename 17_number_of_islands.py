from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = {}
        island_n = 0
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == '1':
                    a = i, j
                    a1 = i - 1, j
                    a2 = i + 1, j
                    a3 = i, j - 1
                    a4 = i, j + 1

                    if a1 in islands:
                        islands[a] = islands[a1]
                    elif a2 in islands:
                        islands[a] = islands[a2]
                    elif a3 in islands:
                        islands[a] = islands[a3]
                    elif a4 in islands:
                        islands[a] = islands[a4]
                    else:
                        island_n += 1
                        islands[a] = island_n

        grouped_islands = {}
        for key, elem in islands.items():
            if elem in grouped_islands:
                grouped_islands[elem].append(key)
            else:
                grouped_islands[elem] = [key]

        print(grouped_islands)
        return len(set(islands.values()))


def main():
    # Input:
    # 11110
    # 11010
    # 11000
    # 00000
    # Output: 1

    # Input:
    # 11000
    # 11000
    # 00100
    # 00011
    # Output: 3
    grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
    ]
    grid = [
            ["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]
    ]
    print(Solution().numIslands(grid))


if __name__ == '__main__':
    main()
