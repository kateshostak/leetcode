import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {letter: i + 1 for i, letter in enumerate(string.ascii_uppercase)}
        res = 0
        for i, elem in enumerate(s):
            res += 26**(len(s) - i - 1)*d[elem]
        return res


def main():
    s = "ZY"
    res = Solution().titleToNumber(s)
    print(f'expected::701, got::{res}')

    s = "AZY"
    res = Solution().titleToNumber(s)
    print(f'expected::701, got::{res}')


if __name__ == '__main__':
    main()
