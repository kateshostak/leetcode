from typing import List
import pdb


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = 0
        tmp = 0
        sums = []
        for elem in nums:
            tmp += elem
            if tmp == k:
                n += 1
            sums.append(tmp)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sums[j] -= nums[i]
                if sums[j] == k:
                    n += 1
        return n

def main():
    nums = [1, 1, 1]
    k = 2

    # nums = [-1, -1, 1]
    # k = 0

    # nums = [100,1,2,3,4]
    # k = 6
    print(Solution().subarraySum(nums, k))


if __name__ == '__main__':
    main()
