class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_ = 1
        tmp = 1
        curr = s[0]
        for i in range(1, len(s)):
            if s[i] == curr:
                tmp += 1
            else:
                tmp = 1
                curr = s[i]
            max_ = max(max_, tmp)

        return max_
