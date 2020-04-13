from typing import List
import pdb


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sentiel = nums[0]
        arr = []
        i = 1
        for elem in nums[1:]:
            if elem != sentiel:
                arr.append(i)
                sentiel = elem
                i = 1
            else:
                i += 1
        arr.append(i)
        max_arr = 0
        for j in range(len(arr) - 1):
            tmp_max = min(arr[j], arr[j + 1])
            max_arr = max(tmp_max, max_arr)

        return max_arr*2


def main():
    arr = [0, 1]
    arr = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
    arr = [0, 1, 1]
    arr = [0, 1, 0, 1]
    s = Solution()
    print(s.findMaxLength(arr))


if __name__ == '__main__':
    main()


