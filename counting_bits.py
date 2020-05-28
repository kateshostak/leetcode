from typing import List
import math


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        elif num == 2:
            return [0, 1, 1]
        elif num == 3:
            return [0, 1, 1, 2]

        res = [0, 1, 1, 2]
        start = 2
        end = 3
        n = math.floor(math.log2(num)) + 1

        while end <= n + 1:
            while start < end:
                for i in range(start, end):
                    print(start)
                    res.append(res[i])
                    start = (start + end)//2 + 1
            res.append(res[end])
            res.append(res[-1] + 1)
            start += 1
            end += 1
        return res


def main():
    n = 2
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1], got::{res}')

    n = 5
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1, 2, 1, 2], got::{res}')

    print(Solution().countBits(32))


if __name__ == '__main__':
    main()
