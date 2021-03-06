from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        buckets = [0]*1001
        for trip in trips:
            passengers, start, end = trip
            buckets[start] += passengers
            buckets[end] -= passengers

        used_cap = 0
        for elem in buckets:
            used_cap += elem
            if used_cap > capacity:
                return False

        return True


def main():
    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    capacity = 11
    res = Solution().carPooling(trips, capacity)
    print(f'expected::True, got::{res}')

    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3
    res = Solution().carPooling(trips, capacity)
    print(f'expected::True, got::{res}')


if __name__ == '__main__':
    main()
