from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations)
        n = end - 1
        max_ = 0
        while start < end:
            mid = (start + end)//2
            if citations[mid] > n - mid:
                end = mid
            else:
                max_ = max(citations[mid], max_)
                start = mid + 1
        return max_

def main():
    citations = [0, 1, 3, 5, 6]
    res = Solution().hIndex(citations)
    print(f'expected::3, got::{res}')


if __name__ == '__main__':
    main()
