class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < len(s):
            i = s[start:].find(s[-1])
            j = end
            if i == j or i == 0:
                return False
            start += i + 1
            while True:
                if i == -1:
                    break
                if s[i] != s[j]:
                    break
                i -= 1
                j -= 1

            if i != -1:
                return False
            if self.check_subs(s, start):
                return True
        return False

    def check_subs(self, s, start):
        subs = s[:start]
        i = start + 1
        j = 0
        while i < len(s):
            j %= len(subs)
            if subs[j] != s[i]:
                return False
            i += 1
            j += 1
        return True


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

    s = 'abab'
    res = Solution().repeatedSubstringPattern(s)
    print(f'expected::True, got::{res}')


if __name__ == '__main__':
    main()
