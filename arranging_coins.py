class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        stair = 1
        while stair <= n:
            i += 1
            n -= stair
            stair += 1
        return i


def main():
    n = 8
    res = Solution().arrangeCoins(n)
    print(f'expeced::3, return::{res}')

    n = 3
    res = Solution().arrangeCoins(n)
    print(f'expeced::2, return::{res}')

    n = 0
    res = Solution().arrangeCoins(n)
    print(f'expeced::0, return::{res}')

    n = 1
    res = Solution().arrangeCoins(n)
    print(f'expeced::1, return::{res}')


if __name__ == '__main__':
    main()
