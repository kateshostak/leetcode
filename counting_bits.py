from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        return [sum(map(int, format(elem, 'b'))) for elem in range(num + 1)]


def main():
    n = 2
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1], got::{res}')

    n = 5
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1, 2, 1, 2], got::{res}')

    print(Solution().countBits(32))

if __name__ == '__main__':
    main()
