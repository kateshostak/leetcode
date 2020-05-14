from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def traverse(start, end):
            mid = (start + end)//2
            print(f'st::{start}, mid::{mid}, end::{end}')
            print(nums[mid], nums[mid + 1])
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    res = traverse(mid, end)
                elif nums[mid] == nums[mid - 1]:
                    res = traverse(start, mid)
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    res = traverse(start, mid)
                elif nums[mid] == nums[mid - 1]:
                    res = traverse(mid, end)
                else:
                    return nums[mid]
            return res
        return traverse(0, len(nums) - 1)


def main():
    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::2, got::{res}')
    print()
    arr = [3, 3, 7, 7, 10, 11, 11]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::10, got::{res}')
    print()
    arr = [0, 1, 1, 2, 2, 5, 5]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::0, got::{res}')
    print()
    arr = [7, 7, 10, 11, 11, 12, 12]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::10, got::{res}')
    print()
    arr = [0, 1, 1, 2, 2, 12, 12]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::0, got::{res}')
    print()
    arr = [1]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::1, got::{res}')


if __name__ == '__main__':
    main()
