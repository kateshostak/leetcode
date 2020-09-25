class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

def main():
    N = 3
    res = Solution().divisorGame(N)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
