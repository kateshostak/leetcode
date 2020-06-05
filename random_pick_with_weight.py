import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.box = []
        for i, elem in enumerate(w):
            self.box += [i]*elem

    def pickIndex(self) -> int:
        j = random.randint(0, len(self.box) - 1)
        return(self.box[j])


def main():
    w = [1, 3]
    print(Solution(w).pickIndex())


if __name__ == '__main__':
    main()
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
