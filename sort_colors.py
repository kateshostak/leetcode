from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        for k in range(len(nums)):
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
            elif nums[k] == 2 and k < j:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1


def main():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(f'expected::[0, 0, 1, 1, 2, 2], got::{nums}')


if __name__ == '__main__':
    main()
