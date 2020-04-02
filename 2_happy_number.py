from functools import reduce


class Solution:
    def isHappy(self, n: int) -> bool: # noqa
        nums = [n]
        while n!= 1:
            n = sum(map(lambda x: x**2, self.get_digits(n)))
            if n in nums:
                return False
            nums.append(n)
        return True

    def get_digits(self, n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return digits


def main():
    s = Solution()
    print(s.isHappy(82))

if __name__ == '__main__':
    main()
