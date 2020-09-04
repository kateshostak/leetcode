class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s * 2)[1:-1]


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
