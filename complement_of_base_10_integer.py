class Solution:
    def bitwiseComplement(self, N: int) -> int:
        i = 0
        tmp = N
        while tmp > 0:
            i += 1
            tmp >>= 1
        return 2**i - 1 - N


def main():
    N = 5
    res = Solution().bitwiseComplement(N)
    print(f'expected::2, got::{res}')


if __name__ == '__main__':
    main()
