from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        j = start
        if target >= nums[j] and target <= nums[-1]:
            start = j
            end = len(nums) - 1
        else:
            end = j
            start = 0

        while start <= end:
            mid = (start + end)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    res = Solution().search(nums, target)
    print(f'expected::4, got::{res}')

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    res = Solution().search(nums, target)
    print(f'expected::-1, got::{res}')

    nums = [1]
    target = 1
    res = Solution().search(nums, target)
    print(f'expected::0, got::{res}')


if __name__ == '__main__':
    main()
