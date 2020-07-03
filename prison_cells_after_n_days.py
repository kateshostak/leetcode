from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        res = [-1]*len(cells)
        print(len(cells))
        for i in range(N):
            res[0] = 0
            for j in range(1, len(cells) - 1):
                res[j] = ~(cells[j - 1] ^ cells[j + 1]) + 2
            res[-1] = 0
            res, cells = cells, res
        return cells


def main():
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7
    res = Solution().prisonAfterNDays(cells, N)
    print(f'expected::[0, 0, 1, 1, 0, 0, 0, 0], got::{res}')


if __name__ == '__main__':
    main()
