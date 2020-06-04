from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def traverse(start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            traverse(start + 1, end - 1)
        traverse(0, len(s) - 1)


def main():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(f'expected::["o", "l", "l", "e", "h"], got::{s}')


if __name__ == '__main__':
    main()
