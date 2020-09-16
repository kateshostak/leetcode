class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if words:
            return len(words[-1])
        return 0


def main():
    s = "Hello World"
    res = Solution().lengthOfLastWord(s)
    print(f'expected::5, got::{res}')


if __name__ == '__main__':
    main()
