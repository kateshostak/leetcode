from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        n = 0
        tmp_sum = 0
        for i in range(len(nums)):
            if nums[i] > k:
                start = i + 1
                tmp_sum = 0
                continue

            tmp_sum += nums[i]
            if tmp_sum == k:
                n += 1
            elif tmp_sum > k:
                while tmp_sum > k and start <= i:
                    tmp_sum -= nums[start]
                    start += 1
                if tmp_sum == k:
                    n += 1
        return n

def main():
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))


if __name__ == '__main__':
    main()
