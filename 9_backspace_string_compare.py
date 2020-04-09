from typing import List
import pdb


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        are_equal = True
        while are_equal and i >= 0 and j >= 0:
            if S[i] == '#':
                count_i = 0
                while S[i] == '#' and i >= 0:
                    count_i += 1
                    i -= 1
                i -= count_i

            if T[j] == '#':
                count_j = 0
                while T[j] == '#' and j >= 0:
                    count_j += 1
                    j -= 1
                j -= count_j

            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    are_equal = False
                i -= 1
                j -= 1

        return are_equal


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

    s = Solution()
    print(s.backspaceCompare(S, T))


if __name__ == '__main__':
    main()
