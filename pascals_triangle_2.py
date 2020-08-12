import math
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        i = 0
        n = rowIndex
        k = 0
        while i <= rowIndex:

            tmp = math.factorial(n)//(math.factorial(k)*math.factorial(n - k))
            res.append(tmp)
            k += 1
            i += 1
        return res


def main():
    rowIndex = 3
    res = Solution().getRow(rowIndex)
    print(f'expected::{[1,3,3,1]}, got::{res}')

    rowIndex = 7
    res = Solution().getRow(rowIndex)
    print(f'expected::{[1, 7, 21, 35, 35, 21, 7, 1]}, got::{res}')

    rowIndex = 0
    res = Solution().getRow(rowIndex)
    print(f'expected::{[1]}, got::{res}')
if __name__ == '__main__':
    main()
