import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n or n == 0:
            return m
        res = []
        len_ = math.floor(math.log2(n)) + 1
        mid = (2**len_ - 1)//2
        while len_ > 1:
            if m > mid and n > mid:
                res.append(1)
            else:
                res.append(0)
            len_ -= 1
            mid += (2**len_)//2
        res.append(0)
        print(res)
        return self.dec(res)

    def dec(self, arr):
        res = 0
        j = 0
        for i in range(len(arr) - 1, -1, -1):
            res += arr[j]*2**i
            j += 1
        return res


def main():
    m = 6
    n = 7
    # out = 6

    #m = 2
    #n = 6
    # out = 0
    # m = 5
    # n = 7
    # m = 0
    # n = 0
    m = 10
    n = 11
    print(Solution().rangeBitwiseAnd(m, n))


if __name__ == '__main__':
    main()
