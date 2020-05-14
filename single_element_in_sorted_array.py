from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def traverse(start, end):
            if end - start <= 2:
                print(f'st::{start}, end::{end}')
                res = nums[start]
                for i in range(start + 1, end + 1):
                    res ^= nums[i]
                return res
            mid = (start + end)//2
            print(f'st::{start}, mid::{mid}, end::{end}')
            print(nums[mid], nums[mid + 1])
            if nums[mid] == nums[mid + 1]:
                res = traverse(mid, end)
            else:
                res = traverse(start, mid)
            return res
        return traverse(0, len(nums))


def main():
    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::2, got::{res}')
    print()
    arr = [3, 3, 7, 7, 10, 11, 11]
    res = Solution().singleNonDuplicate(arr)
    print(f'expected::10, got::{res}')


if __name__ == '__main__':
    main()
