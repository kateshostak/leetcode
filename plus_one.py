from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(map(str, digits))) + 1
        return [int(elem) for elem in str(a)]


def main():
    digits = [1, 2, 3]
    res = Solution().plusOne(digits)
    print(f'expected::[1, 2, 4], got::{res}')

    digits = [9, 9, 9]
    res = Solution().plusOne(digits)
    print(f'expected::[1, 0, 0, 0], got::{res}')

    digits = [8, 9, 9, 9]
    res = Solution().plusOne(digits)
    print(f'expected::[9, 0, 0, 0], got::{res}')


if __name__ == '__main__':
    main()
