class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([elem in J for elem in S])


def main():
    S = "aAAbbbb"
    J = "aA"
    res = Solution().numJewelsInStones(J, S)
    print(f'expected::{3}, got::{res}')

    S = "ZZ"
    J = "z"
    res = Solution().numJewelsInStones(J, S)
    print(f'expected::{0}, got::{res}')


if __name__ == '__main__':
    main()
