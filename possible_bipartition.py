from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        N += 1
        gr_A = [-1]*N
        gr_B = [-1]*N
        for a, b in dislikes:
            if gr_A[a] == -1 and gr_A[b] == -1:
                gr_A[a] = 1
                gr_A[b] = 0
                gr_B[b] = 1
                gr_B[a] = 0
            elif gr_A[a] == -1:
                if gr_A[b] == 0:
                    gr_A[a] = 1
                    gr_B[a] = 0
                else:
                    gr_A[a] = 0
                    gr_B[a] = 1
            elif gr_A[b] == -1:
                if gr_A[a] == 0:
                    gr_A[b] = 1
                    gr_B[b] = 0
                else:
                    gr_A[b] = 0
                    gr_B[b] = 1
            else:
                if not gr_A[a] ^ gr_A[b]:
                    return False
        return True


def main():
    N = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    res = Solution().possibleBipartition(N, dislikes)
    print(f'expected::True, got::{res}')

    N = 3
    dislikes = [[1, 2], [1, 3], [2, 3]]
    res = Solution().possibleBipartition(N, dislikes)
    print(f'expected::False, got::{res}')

    N = 5
    dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    res = Solution().possibleBipartition(N, dislikes)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
