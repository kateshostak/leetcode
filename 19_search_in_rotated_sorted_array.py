from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_elem = min(nums)
        min_elem_index = nums.index(min_elem)

        def bin_search(i, j):
            if j == j:
                if nums[i] == target:
                    return i
                else:
                    return -1
            mid = (i + j)//2
            if target < nums[mid]:
                bin_search(i, mid-1)
            else:
                bin_search(mid, j)

        if target > nums[len(nums)-1]:
            ind = bin_search(0, min_elem_index)
        else:
            ind = bin_search(min_elem_index, len(nums))
        return ind


def main():
    # Input: nums = [4,5,6,7,0,1,2], target = 0
    # Output: 4

    # Input: nums = [4,5,6,7,0,1,2], target = 3
    # Output: -1
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(Solution().search(nums, target))


if __name__ == '__main__':
    main()
