from itertools import zip_longest


class Solution:
    def addBinary(self, a, b):
        c = '0'
        res = ''
        a = reversed(a)
        b = reversed(b)
        for elem1, elem2 in zip_longest(a, b, fillvalue='0'):
            if elem1 == '1' and elem2 == '1':
                if c == '1':
                    res += '1'
                else:
                    c = '1'
                    res += '0'

            elif elem1 == '0' and elem2 == '0':
                if c == '1':
                    res += '1'
                    c = '0'
                else:
                    res += '0'
            else:
                if c == '1':
                    res += '0'
                else:
                    res += '1'
        if c == '1':
            res += '1'
        return res[::-1]


def main():
    a = '11'
    b = '1'
    res = Solution().addBinary(a, b)
    print(f'expected::100, got::{res}')

    a = "1010"
    b = "1011"
    res = Solution().addBinary(a, b)
    print(f'expected::10101 got::{res}')

    a = "100"
    b = "110010"
    res = Solution().addBinary(a, b)
    print(f'expected::110110, got::{res}')


if __name__ == '__main__':
    main()
