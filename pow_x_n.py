class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n % 2 == 1:
            if n < 0:
                res /= x
            else:
                res *= x

        b = format(n, 'b')
        for i in range(len(b) - 2, -1, -1):
            x *= x
            if b[i] == '1':
                if n < 0:
                    res /= x
                else:
                    res *= x
        return res


def main():
    x = 3
    n = 5
    res = Solution().myPow(x, n)
    print(f'expected::{x**n}, got::{res}')

    x = 2
    n = -2
    res = Solution().myPow(x, n)
    print(f'expected::{x**n}, got::{res}')


if __name__ == '__main__':
    main()
