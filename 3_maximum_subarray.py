from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_here = max_ = nums[0]
        for elem in nums[1:]:
            max_here = max(max_here + elem, elem)
            max_ = max(max_here, max_)
        return max_


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))


if __name__ == '__main__':
    main()
