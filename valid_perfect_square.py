class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        reminders = [0, 4, 9, 6, 5, 1]
        if num % 10 not in reminders:
            return False
        if num == 1:
            return True
        start = None
        if num % 2 == 0:
            start = 2
        else:
            start = 1

        for i in range(start, num//2 + 1, 2):
            if i*i == num:
                return True

        return False


def main():
    num = 2147483647
    num = 900
    res = Solution().isPerfectSquare(num)
    print(f'expected::false, got::{res}')


if __name__ == '__main__':
    main()
