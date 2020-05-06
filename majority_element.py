from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
               d[n] = 1

        return max(d, key=lambda x: d[x])


def main():
    arr = [3, 2, 3]
    res = Solution().majorityElement(arr)
    print(f'expected::3, got::{res}')

    arr = [2, 2, 1, 1, 1, 2, 2]
    res = Solution().majorityElement(arr)
    print(f'expected:2, got::{res}')


if __name__ == '__main__':
    main()
