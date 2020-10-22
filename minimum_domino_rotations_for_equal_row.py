from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) <= 1:
            return -1

        def find_min(prev1, prev2):
            r1 = 0
            r2 = 0
            for i in range(1, len(A)):
                if A[i] != prev1:
                    if B[i] != prev1:
                        r1 = None
                        break
                    r1 += 1

            for i in range(1, len(B)):
                if B[i] != prev2:
                    if A[i] != prev2:
                        r2 = None
                        break
                    r2 += 1

            print(r1, r2)
            if r1 is None and r2 is None:
                return -1
            if r1 is None:
                return r2
            if r2 is None:
                return r1
            return min(r1, r2)
        return min(find_min(A[0], B[0]), find_min(B[0], A[0]))


def main():
    A = [2, 1, 1, 3, 2, 1, 2, 2, 1]
    B = [3, 2, 3, 1, 3, 2, 3, 3, 2]
    res = Solution().minDominoRotations(A, B)
    print(f'expected:: -1, got:: {res}')

    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    res = Solution().minDominoRotations(A, B)
    print(f'expected:: 2, got:: {res}')

    A = [1, 1, 2, 1, 1, 1, 2, 1, 2]
    B = [2, 2, 1, 2, 2, 2, 1, 1, 1]
    res = Solution().minDominoRotations(A, B)
    print(f'expected:: 3, got:: {res}')


if __name__ == '__main__':
    main()
