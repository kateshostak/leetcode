import random
import bisect
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        sum_ = 0
        self.part_sums = []
        for elem in self.w:
            sum_ += elem
            self.part_sums.append(sum_)
        self.sum = sum(w)

    def pickIndex(self) -> int:
        j = random.randint(1, self.sum)
        return bisect.bisect_left(self.part_sums, j)

def main():
    w = [1, 3]
    print(Solution(w).pickIndex())


if __name__ == '__main__':
    main()
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
