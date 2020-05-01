# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.isBadVersion = lambda x: x >= 4

        if self.isBadVersion(0):
            return 1

        i = 1
        while i < n and not self.isBadVersion(i):
            i *= 2

        start = i//2
        end = min(i, n - 1)
        while end - start > 1:
            mid = (start + end)//2
            print(f'start {start}::end {end}::mid {mid}')
            if not self.isBadVersion(mid):
                start = mid
            else:
                end = mid
        if self.isBadVersion(start):
            return start
        return end


def main():
    n = 5
    print(Solution().firstBadVersion(n))


if __name__ == '__main__':
    main()
