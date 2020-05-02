from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        else:
            tmp = nums[len(nums) - k:] + nums[:len(nums) - k]
            for i in range(len(nums)):
                nums[i] = tmp[i]

def main():
    # Input: [1, 2, 3, 4, 5, 6, 7] and k = 3
    # Output: [5, 6, 7, 1, 2, 3, 4]
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)


if __name__ == '__main__':
    main()
