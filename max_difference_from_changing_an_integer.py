class Solution:
    def maxDiff(self, num: int) -> int:
        n1 = self.get_nums(num)
        n2 = n1.copy()
        a = None
        b = None
        for i in range(len(n1)):
            if n1[i] != 9:
                a = n1[i]
                break

        for i in range(len(n1)):
            if n1[i] == a:
                n1[i] = 9

        if n2[0] != 1:
            b = n2[0]
            for i in range(len(n2)):
                if n2[i] == b:
                    n2[i] = 1
        else:
            for i in range(1, len(n2)):
                if n2[i] != 0 and n2[i] != 1:
                    b = n2[i]
                    break
            for i in range(1, len(n2)):
                if n2[i] == b:
                    n2[i] = 0
        return int(''.join(map(str, n1))) - int(''.join(map(str, n2)))

    def get_nums(self, num):
        res = []
        while num:
            res.append(num % 10)
            num //= 10
        return list(reversed(res))


def main():
    num = 555
    res = Solution().maxDiff(num)
    print(f'expected::888, got::{res}')

    num = 9
    res = Solution().maxDiff(num)
    print(f'expected::8, got::{res}')

    num = 123456
    res = Solution().maxDiff(num)
    print(f'expected::820000, got::{res}')

    num = 10000
    res = Solution().maxDiff(num)
    print(f'expected::80000, got::{res}')

    num = 9288
    res = Solution().maxDiff(num)
    print(f'expected::8700, got::{res}')

    num = 111
    res = Solution().maxDiff(num)
    print(f'expected::888, got::{res}')

    num = 1101057
    res = Solution().maxDiff(num)
    print(f'expected::8808050, got::{res}')


if __name__ == '__main__':
    main()
