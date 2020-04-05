from typing import List
import pdb


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0 :
                max_sum += diff
        return max_sum

def main():
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    res = s.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
