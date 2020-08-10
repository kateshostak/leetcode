from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        tmp = 2**(len(nums) + 1)
        print(format(tmp, 'b'))
        for elem in nums:
            tmp |= 2**elem
            print(elem, format(tmp, 'b'))

        for elem in nums:
            tmp ^= 2**elem
            print(elem, format(tmp, 'b'))

        res = []
        for elem in nums:
            if tmp & 2**elem != 0:
                tmp ^= 2**elem
                res.append(elem)
            print(elem, format(tmp, 'b'))

        return res

def main():
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(nums))


main()

