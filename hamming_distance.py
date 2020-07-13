class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        i = 0
        while z != 0:
            if z & 1:
                i += 1
            z >>= 1
        return i


def main():
    x = 1
    y = 4
    res = Solution().hammingDistance(x, y)
    print(f'expected::2, got::{res}')


if __name__ == '__main__':
    main()
