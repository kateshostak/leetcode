class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        if s[-1]*len(s) == s:
            return True
        start = 1
        end = len(s) - 1
        while start < len(s):
            i = s[start:].find(s[-1]) + start
            j = end
            if i == j:
                return False
            start = i + 1
            if self.check_subs(s, start):
                return True
        return False

    def check_subs(self, s, start):
        subs = s[:start]
        i = start
        j = 0
        while i < len(s):
            j %= len(subs)
            if subs[j] != s[i]:
                return False
            i += 1
            j += 1

        return j == len(subs)


def main():
    s = 'abcabcabcabc'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::True, got::{res}')

    s = 'ab'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::False, got::{res}')

    s = 'aba'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::False, got::{res}')

    s = 'abaababaab'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::True, got::{res}')

    s = 'babbabbabbabbab'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::True, got::{res}')

    s = 'abbabbabbabbabb'
    # pdb.set_trace()
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::True, got::{res}')

    s = 'abaabaa'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
