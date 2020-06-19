from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations)
        n = end
        max_ = 0
        while start < end:
            mid = (start + end)//2
            print(max_)
            if citations[mid] < n - mid:
                max_ = max(max_, citations[mid])
                start = mid + 1
            elif citations[mid] > n - mid:
                end = mid
            else:
                max_ = max(max_, citations[mid])
                break
        return max_

def main():
    citations = [0, 1, 3, 5, 6]
    res = Solution().hIndex(citations)
    print(f'expected::3, got::{res}')

    citations = [11, 15]
    res = Solution().hIndex(citations)
    print(f'expected::2, got::{res}')

if __name__ == '__main__':
    main()
