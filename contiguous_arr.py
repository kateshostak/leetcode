from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [-2]*(2*len(nums) + 1)
        arr[len(nums)] = -1
        count = tmp = max_ = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if arr[count + len(nums)] >= -1:
                tmp = i - arr[count + len(nums)]
                max_ = max(max_, tmp)
            else:
                arr[count + len(nums)] = i

        return max_


def main():
    nums = [0, 0, 0, 0, 0, 1, 1, 1]
    res = Solution().findMaxLength(nums)
    print(f'expected::6, got::{res}')


if __name__ == '__main__':
    main()
