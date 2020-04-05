import pdb
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = None
        end = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if start is None:
                    start = end = i
                else:
                    end = i
            else:
                if start is not None:
                    nums[start], nums[i] = nums[i], nums[start]
                    if start < end:
                        start += 1
                        end = i
                    else:
                        start = end = i

def main():
    nums = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
