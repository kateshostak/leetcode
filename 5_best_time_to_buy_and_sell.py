from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                max_sum += diff
        return max_sum


def main():
    # Input: [7,1,5,3,6,4]
    # Output: 7

    # Input: [1,2,3,4,5]
    # Output: 4
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))


if __name__ == '__main__':
    main()
