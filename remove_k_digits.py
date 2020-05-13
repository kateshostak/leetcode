class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k or len(num) == 1:
            return 0

        if len(num) - k == 1:
            return(str(min(map(int, num))))

        new_num = ''
        start = 0
        end = len(num) - k
        counter = 0
        while counter < k:
            min_i = start
            for i in range(start + 1, end+1):
                if num[i] < num[min_i]:
                    min_i = i
            counter += 1
            if num[min_i] != 0:
                new_num += num[min_i]
            start = min_i + 1
            end += 1
        print(new_num)
        if len(new_num) < len(num) - k:
            new_num += num[start:]
        nn = int(new_num)
        return str(nn)


def main():
    num = "1432219"
    k = 3
    res = Solution().removeKdigits(num, k)
    print(f'expected::1219, got::{res}')

    num = "10200"
    k = 1
    res = Solution().removeKdigits(num, k)
    print(f'expected::200, got::{res}')

    num = "10"
    k = 2
    res = Solution().removeKdigits(num, k)
    print(f'expected::0, got::{res}')

    num = "100"
    k = 1
    res = Solution().removeKdigits(num, k)
    print(f'expected::0, got::{res}')

    num = "1000"
    k = 2
    res = Solution().removeKdigits(num, k)
    print(f'expected::0, got::{res}')

    num = "10"
    k = 1
    res = Solution().removeKdigits(num, k)
    print(f'expected::0, got::{res}')

    num = "112"
    k = 1
    res = Solution().removeKdigits(num, k)
    print(f'expected::11, got::{res}')


if __name__ == '__main__':
    main()
