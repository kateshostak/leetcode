from typing import List
import pdb


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        for l in S:
            if l == '#':
                if len(s_stack):
                    s_stack.pop()
            else:
                s_stack.append(l)

        for l in T:
            if l == '#':
                if len(t_stack):
                    t_stack.pop()
            else:
                t_stack.append(l)

        return s_stack == t_stack


def main():
    # S = "ab#c"
    # T = "ad#c"

    #S = "ab##"
    #T = "c#d#"

    # S = "a##c"
    # T = "#a#c"

    # S = "a#c"
    # T = "b"

    S = "bxj##tw"
    T = "bxo#j##tw"

    S = "ab##"
    T = "c#b#"

    S = "y#fo##f"
    T = "y#f#o##f"
    s = Solution()
    print(s.backspaceCompare(S, T))


if __name__ == '__main__':
    main()
