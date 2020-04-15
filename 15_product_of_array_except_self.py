from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_arr = []
        suff_arr = []
        preff = 1
        suff = 1

        for elem in nums:
            pref_arr.append(preff)
            preff *= elem

        for elem in reversed(nums):
            suff_arr.append(suff)
            suff *= elem
        suff_arr = list(reversed(suff_arr))

        output = []
        for preff,suff in zip(pref_arr, suff_arr):
            output.append(preff*suff)

        return output

def main():
    # Input:  [1,2,3,4]
    # Output: [24,12,8,6]
    arr = [1, 2, 3, 4]
    print(Solution().productExceptSelf(arr))


if __name__ == '__main__':
    main()
