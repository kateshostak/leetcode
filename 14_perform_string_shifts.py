from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        head = 0
        for direction, step in shift:
            if direction == 0:
                head += step
            else:
                head -= step

            head %= len(s)

        return s[head:]+s[:head]


def main():
    # Input: s = "abc", shift = [[0,1],[1,2]]
    # Output: "cab"

    # Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
    # Output: "efgabcd"
    s = "abcdefg"
    shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    print(Solution().stringShift(s, shift))


if __name__ == '__main__':
    main()
