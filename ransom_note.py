class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = self.counter(ransomNote)
        d2 = self.counter(magazine)
        canConstruct = True
        for key, val in d1.items():
            if key in d2:
                if d2[key] < val:
                    canConstruct = False
            else:
                canConstruct = False
        return canConstruct

    def counter(self, s):
        tmp = {}
        for elem in s:
            if elem in tmp:
                tmp[elem] += 1
            else:
                tmp[elem] = 1
        return tmp


def main():
    s1 = 'a'
    s2 = 'b'
    res = Solution().canConstruct(s1, s2)
    print(f'expected::False, got::{res}')

    s1 = 'ab'
    s2 = 'aab'
    res = Solution().canConstruct(s1, s2)
    print(f'expected::True, got::{res}')

if __name__ == '__main__':
    main()
