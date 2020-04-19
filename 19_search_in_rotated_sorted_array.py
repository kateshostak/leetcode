from typing import List
import pdb


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        min_elem = min(nums)
        min_elem_index = nums.index(min_elem)
        ind = -1

        def bin_search(i, j):
            if j - i <= 1:
                if nums[i] == target:
                    return i
                elif nums[j] == target:
                    return j
                else:
                    return -1
            mid = (i + j)//2
            if target < nums[mid]:
                ind = bin_search(i, mid-1)
            else:
                ind = bin_search(mid, j)
            return ind

        if target > nums[len(nums)-1]:
            ind = bin_search(0, min_elem_index-1)
        else:
            ind = bin_search(min_elem_index, len(nums)-1)
        return ind


def main():
    # Input: nums = [4,5,6,7,0,1,2], target = 0
    # Output: 4

    # Input: nums = [4,5,6,7,0,1,2], target = 3
    # Output: -1
    #nums = [4, 5, 6, 7, 0, 1, 2]
    #target = 5

    # nums = [4,5,6,7,0,1,2]
    # nums = []
    # nums = [1, 3]

    nums = [3, 5, 1]
    target = 5

    nums = [4,5,6,7,0,1,2]
    target = 2
    nums = [1, 3]
    target = 3
    print(Solution().search(nums, target))


if __name__ == '__main__':
    main()
