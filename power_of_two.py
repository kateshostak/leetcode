class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not(n & (n - 1))


def main():
    n = 1
    res = Solution().isPowerOfTwo(n)
    print(f'expected::True, got::{res}')

    n = 16
    res = Solution().isPowerOfTwo(n)
    print(f'expected::True, got::{res}')

    n = 218
    res = Solution().isPowerOfTwo(n)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
