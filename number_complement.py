import math


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        elif num == 1:
            return 0

        n = math.ceil(math.log2(num))
        max_ = 2**(n+1) - 1
        return (max_ - num)%2**n


def main():
    num = 5
    res = Solution().findComplement(num)
    print(f'expected::2, got::{res}')


    num = 1
    res = Solution().findComplement(num)
    print(f'expected::0, got::{res}')

    num = 2
    res = Solution().findComplement(num)
    print(f'expected::1, got::{res}')


if __name__ == '__main__':
    main()
