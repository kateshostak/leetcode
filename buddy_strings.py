import collections


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not A or not B:
            return False
        if len(A) != len(B):
            return False
        if A == B:
            c = collections.Counter(A)
            return any(val >= 2 for _, val in c.items())

        ind = []
        for i in range(len(A)):
            if A[i] != B[i]:
                ind.append(i)
        if len(ind) != 2:
            return False
        i, j = ind
        return A[i] == B[j] and A[j] == B[i]


def main():
    A = 'aa'
    B = 'aa'
    res = Solution().buddyStrings(A, B)
    print(f'expected::True, got::{res}')

    A = 'abcd'
    B = 'badc'
    res = Solution().buddyStrings(A, B)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
