from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_c = Counter(p)
        s_c = Counter(s[:len(p)])
        res = []
        start = 0
        for i in range(len(p), len(s)):
            if p_c == s_c:
                res.append(start)
            s_c[s[start]] -= 1
            if s_c[s[start]] <= 0:
                s_c.pop(s[start])
            s_c[s[i]] += 1
            start += 1
        if s_c == p_c and start not in res:
            res.append(start)
        return res


def main():
    s = "cbaebabacd"
    p = "abc"
    res = Solution().findAnagrams(s, p)
    print(f'expected::[0, 6], got::{res}')

    s = "abab"
    p = "ab"
    res = Solution().findAnagrams(s, p)
    print(f'expected::[0, 1, 2], got::{res}')


if __name__ == '__main__':
    main()
