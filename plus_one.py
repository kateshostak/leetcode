from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i] + carry
            if tmp == 10:
                carry = 1
            else:
                carry = 0

            res.append(tmp % 10)
        if carry:
            res.append(1)
            res.reverse()
            return res


def main():
    digits = [1, 2, 3]
    res = Solution().plusOne(digits)
    print(f'expected::[1, 2, 4], got::{res}')

    digits = [9, 9, 9]
    res = Solution().plusOne(digits)
    print(f'expected::[1, 0, 0, 0], got::{res}')


if __name__ == '__main__':
    main()
