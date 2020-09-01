from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        res = []
        first_h = [2, 1, 0]
        second_h = [3, 2, 1, 0]
        first_m = [5, 4, 3, 2, 1, 0]
        second_m = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        for digit in first_h:
            if digit in A:
                res.append(digit)
                A.remove(digit)
                break
        if not res:
            return ""
        print(res)
        if res[0] == 2:
            for digit in second_h:
                if digit in A:
                    res.append(digit)
                    A.remove(digit)
                    break

            res.append(':')

            for digit in first_m:
                if digit in A:
                    res.append(digit)
                    A.remove(digit)
                    break
            for digit in second_m:
                if digit in A:
                    res.append(digit)
                    A.remove(digit)
                    break
        else:
            print(res)
            for digit in second_m:
                if digit in A:
                    res.append(digit)
                    A.remove(digit)
                    break

            res.append(':')

            for digit in first_m:
                if digit in A:
                    res.append(digit)
                    A.remove(digit)
                    break
            for digit in second_m:
                if digit in A:
                    res.append(digit)
                    A.remove(digit)
                    break
        if len(res) < 5:
            return ""

        return ''.join(map(str, res))


def main():
    A = [2, 0, 6, 6]
    res = Solution().largestTimeFromDigits(A)
    print(f'expected::"06:26", got::{res}')


if __name__ == '__main__':
    main()
