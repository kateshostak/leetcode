from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int: # noqa
        arr = [-2]*(2*len(nums)+1)
        arr[len(nums)] = -1
        maxlen = count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if arr[count + len(nums)] >= -1:
                maxlen = max(maxlen, i - arr[count + len(nums)])
            else:
                arr[count + len(nums)] = i

        return maxlen

def main():
    arr = [0, 1]
    res = Solution().findMaxLength(arr)
    print(f'expected::2, got::{res}')

    arr = [0, 1, 0]
    res = Solution().findMaxLength(arr)
    print(f'expected::2, got::{res}')


if __name__ == '__main__':
    main()
