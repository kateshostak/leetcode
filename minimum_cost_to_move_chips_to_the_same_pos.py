from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min((odd :=sum(p % 2 for p in position)), len(position) - odd)
