class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = j = 0
        while i < len(t) and j < len(t):
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == len(s)


def main():
    s = "abc"
    t = "ahbgdc"
    res = Solution().isSubsequence(s, t)
    print(f'expected::True, got::{res}')

    s = "axc"
    t = "ahbgdc"
    res = Solution().isSubsequence(s, t)
    print(f'expected::False, got::{res}')

    s = "acb"
    t = "ahbgdc"
    res = Solution().isSubsequence(s, t)
    print(f'expected::False, got::{res}')

    s = "aaaaaa"
    t = "bbaaaa"
    res = Solution().isSubsequence(s, t)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
