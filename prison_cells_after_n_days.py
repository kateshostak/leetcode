from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        res = [-1]*len(cells)
        d = {}
        period = 0
        for i in range(N):
            n = self.bin_to_dec(cells)
            if n in d:
                period = i - d[n]
                break
            d[n] = i
            res[0] = 0
            for j in range(1, len(cells) - 1):
                res[j] = ~(cells[j - 1] ^ cells[j + 1]) + 2
            res[-1] = 0
            res, cells = cells, res

        if period:
            for i in range(1 + (N - i - 1) % period):
                res[0] = 0
                for j in range(1, len(cells) - 1):
                    res[j] = ~(cells[j - 1] ^ cells[j + 1]) + 2
                res[-1] = 0
                res, cells = cells, res
        return cells

    def bin_to_dec(self, arr):
        return (sum([arr[i]*2**(len(arr) - 1 - i) for i in range(len(arr))]))


def main():
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7
    res = Solution().prisonAfterNDays(cells, N)
    print(f'expected::[0, 0, 1, 1, 0, 0, 0, 0], got::{res}')

    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    N = 1000000000
    res = Solution().prisonAfterNDays(cells, N)
    print(f'expected::[0, 0, 1, 1, 1, 1, 1, 0], got::{res}')


if __name__ == '__main__':
    main()
