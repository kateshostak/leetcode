class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        it = iter(t)
        return all(elem in it for elem in s)

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
