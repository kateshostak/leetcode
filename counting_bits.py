from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        elif num == 2:
            return [0, 1, 1]
        elif num == 3:
            return [0, 1, 1, 2]

        res = [0, 1, 1, 2]
        i = 1
        j = 2

        while len(res) <= num + 1:
            start = 2**i
            end = 2**j - 1
            while start < end:
                for k in range(start, end + 1):
                    res.append(res[k])
                start = (start + end)//2 + 1
            res.append(res[end])
            res.append(res[-1] + 1)
            i += 1
            j += 1
        return res[:num + 1]


def main():
    n = 2
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1], got::{res}')

    n = 5
    res = Solution().countBits(n)
    print(f'expected::[0, 1, 1, 2, 1, 2], got::{res}')


if __name__ == '__main__':
    main()
