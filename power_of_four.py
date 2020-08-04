class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num > 0 and (num & (num - 1)) == 0 and num & 0x55555555 != 0:
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
