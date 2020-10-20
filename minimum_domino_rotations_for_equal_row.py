from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) <= 1:
            return -1
        r = 0
        prev1 = A[0]
        prev2 = B[0]
        print(*list(range(len(A))))
        print(*A)
        print(*B)
        for i in range(1, len(A)):
            if A[i] == prev1:
                continue
            if B[i] == prev2:
                continue
            if A[i] == prev2:
                print(i)
                prev2 = A[i]
                r += 1
                continue
            if B[i] == prev1:
                print(i)
                prev1 = B[i]
                r += 1
                continue
            return -1
        return r


def main():
    A = [2, 1, 1, 3, 2, 1, 2, 2, 1]
    B = [3, 2, 3, 1, 3, 2, 3, 3, 2]
    res = Solution().minDominoRotations(A, B)
    print(f'expected:: -1, got:: {res}')


if __name__ == '__main__':
    main()
