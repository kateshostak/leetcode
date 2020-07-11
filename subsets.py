from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1 + 2**len(nums) - 1):
            tmp = []
            for j, elem in enumerate(reversed(format(i, 'b'))):
                if elem == '1':
                    tmp.append(nums[j])
            res.append(tmp)
        return res


def main():
    nums = [1, 2, 3]
    print(Solution().subsets(nums))


if __name__ == '__main__':
    main()
