from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = 0
        tmp = 0
        sums = {}
        print(nums)
        for elem in nums:
            tmp += elem
            if tmp == k:
                n += 1
            if tmp in sums:
                sums[tmp] += 1
            else:
                sums[tmp] = 1

        print(n)
        print(sums)
        tmp = nums[0]
        for elem in nums[1:]:
            tmp += elem
            for key, value in sums.items():
                if key - tmp == k:
                    n += value
                    break
        return n


def main():
    nums = [1, 1, 1]
    k = 2

    # nums = [-1, -1, 1]
    # k = 0

    nums = [100,1,2,3,4]
    k = 6
    print(Solution().subarraySum(nums, k))


if __name__ == '__main__':
    main()
