from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        arr2 = [0]*1001
        for n in arr:
            arr2[n] = 1

        for n in arr:
            if arr2[n+1]:
                count += 1
        return count


def main():
    arr = [1,2,3]
    arr = [1,3,2,3,5,0]
    arr = [1,1,3,3,5,5,7,7]
    arr = [1,1,2,2]
    print(Solution().countElements(arr))



if __name__ == '__main__':
    main()
