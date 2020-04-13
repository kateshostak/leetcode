from typing import List
import pdb


class Solution:
    def findMaxLength(self, nums: List[int]) -> int: # noqa
        max_ = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                sum_ = -1
            else:
                sum_ = 1
            for j in range(i + 1, len(nums)):
                if nums[j] == 0:
                    sum_ -= 1
                else:
                    sum_ += 1
                if sum_ == 0:
                    tmp_max = j - i + 1
                    max_ = max(tmp_max, max_)
        return max_

def main():
    arr = [0, 1]
    # arr = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
    # arr = [0, 1, 1]
    # arr = [0, 1, 0, 1]
    s = Solution()
    print(s.findMaxLength(arr))


if __name__ == '__main__':
    main()
