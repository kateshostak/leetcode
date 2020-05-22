from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        swapped = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                swapped = True
                break

        if not swapped:
            nums.reverse()


def main():
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    print(f'expected::[1, 3, 2], got::{nums}')

    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print(f'expected::[1, 2, 3], got::{nums}')

    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    print(f'expected::[1, 5, 1], got::{nums}')


if __name__ == '__main__':
    main()
