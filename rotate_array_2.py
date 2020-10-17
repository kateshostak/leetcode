from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if len(nums) % 2 == 0 and k == len(nums)//2:
            for i in range(len(nums)//2):
                nums[i], nums[i + k] = nums[i + k], nums[i]
            return nums

        i = 0
        not_cycle = True
        for i in range(len(nums) - 1):
            shift = (len(nums) - k + i) % len(nums)
            nums[i], nums[shift] = nums[shift], nums[i]
            print(i, shift)
            i = shift
            if shift == 0:
                i = shift + 1
            print(nums)
        return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = Solution().rotate(nums, k)
    print(res)

    nums = [-1, -100, 3, 99]
    k = 2
    res = Solution().rotate(nums, k)
    print(res)

    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    res = Solution().rotate(nums, k)
    print(res)

if __name__ == '__main__':
    main()
