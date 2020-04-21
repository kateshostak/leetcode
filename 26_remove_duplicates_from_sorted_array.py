from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        tmp_elem = nums[len(nums) - 1]
        for elem in reversed(nums[:len(nums) - 1]):
            if elem == tmp_elem:
                nums.remove(elem)
            else:
                tmp_elem = elem


def main():
    # Input: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # Output: [0, 1, 2, 3, 4]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Solution().removeDuplicates(nums)
    print(nums)


if __name__ == '__main__':
    main()
