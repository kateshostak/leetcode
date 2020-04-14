from typing import List
import pdb


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
    # arr = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
    # arr = [0, 1, 1]
    # arr = [0, 1, 0, 1]
    s = Solution()
    print(s.findMaxLength(arr))


if __name__ == '__main__':
    main()
