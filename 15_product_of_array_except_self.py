from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        preff = 1
        suff = 1

        for elem in reversed(nums):
            output.append(suff)
            suff *= elem
        output = list(reversed(output))

        for i in range(len(output)):
            output[i] *= preff
            preff*= nums[i]

        return output

def main():
    # Input:  [1,2,3,4]
    # Output: [24,12,8,6]
    arr = [1, 2, 3, 4]
    print(Solution().productExceptSelf(arr))


if __name__ == '__main__':
    main()
