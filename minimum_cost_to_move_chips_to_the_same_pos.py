from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count = 0
        even_count = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return min(odd_count, even_count)
