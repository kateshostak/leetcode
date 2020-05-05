class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        d = {}
        for i, elem in enumerate(s):
            if elem in d:
                d[elem] = len(s)
            else:
                d[elem] = i


        j = min(d, key=lambda x: d[x])
        if d[j] < len(s):
            return d[j]
        else:
            return -1


def main():
    s = "leetcode"
    res = Solution().firstUniqChar(s)
    print(f'expected::0, got::{res}')

    s = "loveleetcode"
    res = Solution().firstUniqChar(s)
    print(f'expected::2, got::{res}')

    s = 'cc'
    res = Solution().firstUniqChar(s)
    print(f'expected::-1, got::{res}')


if __name__ == '__main__':
    main()
