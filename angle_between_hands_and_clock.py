class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = (hour % 12) * 5 + ((5 * minutes)/60)
        diff = min(60 - abs(hour - minutes), abs(hour - minutes))
        return diff * 6

def main():
    h = 12
    m = 30
    res = Solution().angleClock(h, m)
    print(f'expected::165, got::{res}')

    h = 3
    m = 30
    res = Solution().angleClock(h, m)
    print(f'expected::75, got::{res}')

    h = 3
    m = 15
    res = Solution().angleClock(h, m)
    print(f'expected::7.5, got::{res}')

    h = 4
    m = 50
    res = Solution().angleClock(h, m)
    print(f'expected::155, got::{res}')

    h = 12
    m = 0
    res = Solution().angleClock(h, m)
    print(f'expected::0, got::{res}')

    h = 6
    m = 5
    res = Solution().angleClock(h, m)
    print(f'expected::152.5, got::{res}')

    h = 1
    m = 57
    res = Solution().angleClock(h, m)
    print(f'expected:76.5, got::{res}')


if __name__ == '__main__':
    main()
