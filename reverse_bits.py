class Solution:
    def reverseBits(self, n: int) -> int:
        a = [
            0b0000,
            0b1000,
            0b0100,
            0b1100,
            0b0010,
            0b1010,
            0b0110,
            0b1110,
            0b0001,
            0b1001,
            0b0101,
            0b1101,
            0b0011,
            0b1011,
            0b0111,
            0b1111,
        ]
        res = 0
        for i in range(8):
            res |= a[n & 0xF] << (28 - (i << 2))
            n >>= 4
        return res


def main():
    n = 43261596
    res = Solution().reverseBits(n)
    print(f'expected::964176192, got::{res}')


if __name__ == '__main__':
    main()
