from typing import List


class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        x1, y1 = coor[0]
        x2, y2 = coor[1]
        delta_y = y2 - y1
        delta_x = x2 - x1
        for i in range(2, len(coor)):
            x, y = coor[i]
            if delta_y*(x - x1) != delta_x*(y - y1):
                return False
        return True


def main():
    coor = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    res = Solution().checkStraightLine(coor)
    print(f'expected::True, got::{res}')

    coor = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    res = Solution().checkStraightLine(coor)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
