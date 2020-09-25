class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return set(t).difference(set(s)).pop()


def main():
    s = "abcd"
    t = "abcde"
    res = Solution().findTheDifference(s, t)
    print(f'expected::"e", got::{res}')


if __name__ == '__main__':
    main()
