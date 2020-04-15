from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int: # noqa
        s = reduce(lambda x, y: x ^ y, nums)
        return s


def main():
    # Input: [2,2,1]
    # Output: 1

    # Input: [4,1,2,1,2]
    # Output: 4

    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))


if __name__ == '__main__':
    main()
