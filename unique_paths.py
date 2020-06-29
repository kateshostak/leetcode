import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s = (m - 1) + (n - 1)
        return math.factorial(s)//(math.factorial(n - 1)*math.factorial(s - n + 1))


def main():
    m = 7
    n = 3
    res = Solution().uniquePaths(m, n)
    print(f'expected::28, got::{res}')

    m = 4
    n = 4
    res = Solution().uniquePaths(m, n)
    print(f'expected::20, got::{res}')


if __name__ == '__main__':
    main()
