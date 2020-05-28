from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        pow_ = 0
        for i in range(num + 1):
            if not(i & (i - 1)):
                pow_ = i

            if not res:
                res.append(0)
            else:
                res.append(1 + res[i - pow_])
        return res


def main():
    n = 2
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1], got::{res}')

    n = 5
    res = Solution().countBits(n)


if __name__ == '__main__':
    main()
