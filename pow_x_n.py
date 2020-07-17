class Solution:
    def myPow(self, x: float, n: int) -> float:
        def traverse(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1 / traverse(x, -n)

            if n == 1:
                return x
            if n % 2 == 1:
                return x * traverse(x, n - 1)
            return traverse(x, n // 2)**2
        return traverse(x, n)


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
