from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[-1] == nums[0]:
            if nums[-1] == 0:
                return [[0]*3]
            return []
        d = {}
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            elem = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j != k:
                arr = []
                tmp = nums[j] + nums[k]
                if tmp < 0:
                    j += 1
                elif tmp > abs(elem):
                    k -= 1
                else:
                    if tmp + elem == 0:
                        arr.append(elem)
                        arr.append(nums[j])
                        arr.append(nums[k])
                        d[''.join(map(str, arr))] = arr
                    j += 1
        return [item for k, item in d.items()]


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(nums)
    print(f'expected::[[-1, 0, 1], [-1, -1, 2]], got::{res}')

    nums = [0, 0, 0]
    res = Solution().threeSum(nums)
    print(f'expected::[0, 0, 0], got::{res}')


if __name__ == '__main__':
    main()
