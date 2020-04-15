from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        for i in range(len(stones) - 1):
            stones.sort(reverse=True)
            stones[i+1] = abs(stones[i] - stones[i+1])
        return(stones.pop())


def main():
    # Input: [2,7,4,1,8,1]
    # Output: 1
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))


if __name__ == '__main__':
    main()
