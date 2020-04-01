from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int: # noqa
        s = reduce(lambda x, y:x^y , nums)
        return s


def main():
    nums = [1, 2, 3, 4, 3, 2, 1]
    nums = [2, 2, 1]
    s = Solution()
    print(s.singleNumber(nums))


if __name__ == '__main__':
    main()
