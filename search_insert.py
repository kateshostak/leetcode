from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end)//2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] >= target:
                end = mid
            else:
                return mid
        return end


def main():
    nums = [1, 3, 5, 6]
    target = 5
    res = Solution().searchInsert(nums, target)
    print(f'expected::2, got::{res}')

    nums = [1, 3, 5, 6]
    target = 2
    res = Solution().searchInsert(nums, target)
    print(f'expected::1, got::{res}')

    nums = [1, 3, 5, 6]
    target = 7
    res = Solution().searchInsert(nums, target)
    print(f'expected::4, got::{res}')

    nums = [1, 3, 5, 6]
    target = 0
    res = Solution().searchInsert(nums, target)
    print(f'expected::0, got::{res}')


if __name__ == '__main__':
    main()
