class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        d = {}
        for i, letter in enumerate(t):
            if letter not in d:
                d[letter] = []
            d[letter].append(i)

        curr = prev = 0
        for letter in s:
            if letter in d:
                if prev > d[letter][-1]:
                    return False
                else:
                    k = 0
                    while d[letter][k] < prev:
                        k += 1
                    curr, prev = d[letter][k], curr
            else:
                return False

        return True


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



if __name__ == '__main__':
    main()
