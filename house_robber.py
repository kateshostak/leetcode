class Solution:
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        rolling_sum = []
        rolling_sum.append(nums[0])
        rolling_sum.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            curr_max = max(rolling_sum[i - 1], rolling_sum[i - 2] + nums[i])
            rolling_sum.append(curr_max)

        return rolling_sum[-1]


def main():
    nums = [1, 2, 3, 1]
    res = Solution().rob(nums)
    print(f'expected::4, got::{res}')


if __name__ == '__main__':
    main()
