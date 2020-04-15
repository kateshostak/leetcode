from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        for letter in S:
            if letter == '#':
                if len(s_stack):
                    s_stack.pop()
            else:
                s_stack.append(letter)

        for letter in T:
            if letter == '#':
                if len(t_stack):
                    t_stack.pop()
            else:
                t_stack.append(letter)

        return s_stack == t_stack


def main():
    # Input: S = "ab#c", T = "ad#c"
    # Output: true

    # Input: S = "ab##", T = "c#d#"
    # Output: true

    # Input: S = "a##c", T = "#a#c"
    # Output: true

    # Input: S = "a#c", T = "b"
    # Output: false
    S = "ab#c"
    T = "ad#c"
    print(Solution().backspaceCompare(S, T))


if __name__ == '__main__':
    main()
