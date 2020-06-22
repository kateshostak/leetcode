import pdb


class Solution():
    def checkValidString(self, s):
        ast = 0
        stack = []
        for elem in s:
            if elem == '(':
                stack.append(elem)
            else:
                if elem == ')' and stack:
                    stack.pop()
                elif elem == ')' and ast != 0:
                    ast -= 1
                elif elem == ')':
                    return False

                else:
                    ast += 1
                    if stack:
                        stack.pop()
                        ast += 1
        return not stack


def main():
    # Input: "()"
    # Output: True

    # Input: "(*)"
    # Output: True

    # Input: "(*))"
    # Output: True
    s = '()'
    res = Solution().checkValidString(s)
    print(f'expected::True, got::{res}')

    s = '(*)'
    res = Solution().checkValidString(s)
    print(f'expected::True, got::{res}')

    s = '(*))'
    res = Solution().checkValidString(s)
    print(f'expected::True, got::{res}')

    s = '(*()'
    res = Solution().checkValidString(s)
    print(f'expected::True, got::{res}')


if __name__ == '__main__':
    main()
