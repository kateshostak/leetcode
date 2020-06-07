import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.start_to_index = {}
        self.start_to_end = {}
        start = 0
        self.len_ = 0
        for i, elem in enumerate(w):
            self.start_to_index[start] = i
            self.start_to_end[start] = start + elem
            start += elem
            self.len_ = start

    def pickIndex(self) -> int:
        j = random.randint(0, self.len_ - 1)
        for start, end in self.start_to_end.items():
            if j >= start and j < end:
                return self.start_to_index[start]


def main():
    w = [1, 3]
    print(Solution(w).pickIndex())


if __name__ == '__main__':
    main()
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
