class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 2
        if n == 1:
            return f1
        if n == 2:
            return f2

        for i in range(n - 2):
            f2, f1 = f1 + f2, f2
        return f2


def main():
    n = 3
    print(Solution().climbStairs(n))

    n = 4
    print(Solution().climbStairs(n))

    n = 5
    print(Solution().climbStairs(n))


main()
