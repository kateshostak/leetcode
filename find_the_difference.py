import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        c2.subtract(c1)
        for key, value in c2.items():
            if value > 0:
                return key


def main():
    s = "abcd"
    t = "abcde"
    res = Solution().findTheDifference(s, t)
    print(f'expected::"e", got::{res}')


if __name__ == '__main__':
    main()
