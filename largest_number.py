from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        tmp = []
        max_ = ''
        for elem in nums:
            print(max_)
            tmp.append(elem)
            j = -1
            for i in range(len(tmp)):
                tmp[-1 - i], tmp[j] = tmp[j], tmp[-1 - i]
                new = ''.join(map(str, tmp))
                print(f'i::{i}, new::{new}')
                if new > max_:
                    j = -1 - i
                    max_ = new
                else:
                    tmp[-1 - i], tmp[j] = tmp[j], tmp[-1 - i]
        return max_


def main():
    nums = [3, 30, 34, 5, 9]
    res = Solution().largestNumber(nums)
    print(f'expected::"9534330", got::{res}')


if __name__ == '__main__':
    main()
