from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        i = 0
        head = 0
        print(nums)
        for _ in range(len(nums) - 1):
            shift = (len(nums) - k + i) % len(nums)
            if shift == head:
                i = shift + 1
                head = i
                continue
            nums[i], nums[shift] = nums[shift], nums[i]
            i = shift

        return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = Solution().rotate(nums, k)
    print(res)

    nums = [-1, -100, 3, 99]
    k = 2
    res = Solution().rotate(nums, k)
    print(res)

    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    res = Solution().rotate(nums, k)
    print(res)


if __name__ == '__main__':
    main()
