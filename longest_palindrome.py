class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for elem in s:
            if elem not in d:
                d[elem] = 0
            d[elem] += 1

        length = 0
        has_odd_freq = False
        for _, freq in d.items():
            if freq % 2 == 0:
                length += freq
            elif freq % 2 == 1 and freq > 1:
                length += freq - 1
                has_odd_freq = True
            else:
                has_odd_freq = True

        if has_odd_freq:
            return length + 1
        return length


def main():
    s = "abccccdd"
    res = Solution().longestPalindrome(s)
    print(f'expected::7, got::{res}')

    s = 'bananas'
    res = Solution().longestPalindrome(s)
    print(f'expected::5, got::{res}')

    s = 'ccc'
    res = Solution().longestPalindrome(s)
    print(f'expected::3, got::{res}')

    s = input()
    res = Solution().longestPalindrome(s)
    print(f'expected::983, got::{res}')


if __name__ == '__main__':
    main()
