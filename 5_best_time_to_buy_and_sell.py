from typing import List
import pdb


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0


        for i in range(len(prices) - 1):
            tmp_sum = 0
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                print(f'i::{i}, j::{j}, diff::{diff}')
                if diff > 0:
                    tmp_sum += diff
                    i = j + 1
                    continue
            max_sum = max(tmp_sum, max_sum)
        return max_sum

def main():
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    res = s.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
