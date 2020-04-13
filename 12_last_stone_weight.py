from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        for i in range(len(stones) - 1):
            stones.sort(reverse=True)
            stones[i+1] = abs(stones[i] - stones[i+1])
        return(stones.pop())

def main():
    stones = [2,7,4,1,8,1]
    stones = [7,6,7,6,9]
    s = Solution()
    print(s.lastStoneWeight(stones))


if __name__ == '__main__':
    main()



