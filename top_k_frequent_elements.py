from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for elem in nums:
            if elem not in d:
                d[elem] = 0
            d[elem] += 1

        h = []
        for val, freq in d.items():
            heapq.heappush(h, (freq, val))

        return [elem[1] for elem in heapq.nlargest(k, h)]


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    res = Solution().topKFrequent(nums, k)
    print(f'expected::[1, 2], got::{res}')

    nums = [1]
    k = 1
    res = Solution().topKFrequent(nums, k)
    print(f'expected::[1], got::{res}')

    nums = [-1, -1]
    k = 1
    res = Solution().topKFrequent(nums, k)
    print(f'expected::[-1], got::{res}')


if __name__ == '__main__':
    main()
