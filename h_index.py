from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not len(citations):
            return 0
        citations.sort()
        start = 0
        end = len(citations)
        h = 0
        while start < end:
            mid = (start + end)//2
            if citations[mid] > len(citations) - mid:
                end = mid
                h = max(len(citations) - mid, h)
            else:
                h = max(h, citations[mid])
                start = mid + 1
        return h


def main():
    citations = [3, 0, 6, 1, 5]
    res = Solution().hIndex(citations)
    print(f'expected::{3}, got::{res}')

    citations = [100]
    res = Solution().hIndex(citations)
    print(f'expected::{1}, got::{res}')

    citations = [1, 1]
    res = Solution().hIndex(citations)
    print(f'expected::{1}, got::{res}')

    citations = [3, 3, 3, 3, 3, 3]
    res = Solution().hIndex(citations)
    print(f'expected::{3}, got::{res}')

    citations = [1, 2]
    res = Solution().hIndex(citations)
    print(f'expected::{1}, got::{res}')

    citations = [5, 5, 5]
    res = Solution().hIndex(citations)
    print(f'expected::{3}, got::{res}')


if __name__ == '__main__':
    main()
