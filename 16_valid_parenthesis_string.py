import pdb


class Solution():
    def checkValidString(self, s):
        low = high = 0
        for c in s:
            low += 1 if c == '(' else -1
            high += 1 if c != ')' else -1
            if high < 0:
                break
            low = max(low, 0)

        return low == 0

def main():
    # Input: "()"
    # Output: True

    # Input: "(*)"
    # Output: True

    # Input: "(*))"
    # Output: True
    s = '(*()'
    print(Solution().checkValidString(s))


if __name__ == '__main__':
    main()
