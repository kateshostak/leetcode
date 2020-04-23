import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        res = []
        len_ = math.floor(math.log2(n)) + 1
        mid = 2**len_ - 1
        while len_ > 1:
            if m > mid//2 and n > mid//2:
                res.append(1)
            else:
                res.append(0)
            len_ -= 1
            m %= 2**len_
            n %= 2**len_
            tmp = 2**len_ - 1
        res.append(0)
        return res


def main():
    m = 5
    n = 7
    print(Solution().rangeBitwiseAnd(m, n))


if __name__ == '__main__':
    main()
