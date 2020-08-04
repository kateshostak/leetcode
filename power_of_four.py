import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        p = math.log2(num)
        if p > 1 and p % 2 == 0:
            return True
        return False


def main():
    num = 16
    res = Solution().isPowerOfFour(num)
    print(f'expected::True, got::{res}')

    num = 5
    res = Solution().isPowerOfFour(num)
    print(f'expected::False, got::{res}')

    num = 2
    res = Solution().isPowerOfFour(num)
    print(f'expected::False, got::{res}')

    num = 8
    res = Solution().isPowerOfFour(num)
    print(f'expected::False, got::{res}')

if __name__ == '__main__':
    main()
