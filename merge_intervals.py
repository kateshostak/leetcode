from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for tmp_start, tmp_end in intervals:
            if end < tmp_start:
                res.append([start, end])
                start, end = tmp_start, tmp_end
                continue

            if end < tmp_end:
                end = tmp_end

        if len(res) == 0 or res[-1] != [start, end]:
            res.append([start, end])
        return res


def main():
    intervals = [[1, 4], [0, 4]]
    res = Solution().merge(intervals)
    print(f'expected::[[0, 4]], got::{res}')


if __name__ == '__main__':
    main()
