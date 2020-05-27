from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        N += 1
        self.gr_A = [-1]*N
        self.gr_B = [-1]*N

        def traverse(a, b, i):
            if self.gr_A[a] == -1 and self.gr_A[b] == -1:
                self.gr_A[a] = 1
                self.gr_A[b] = 0
                self.gr_B[b] = 1
                self.gr_B[a] = 0
            elif self.gr_A[a] == -1:
                if self.gr_A[b] == 0:
                    self.gr_A[a] = 1
                    self.gr_B[a] = 0
                else:
                    self.gr_A[a] = 0
                    self.gr_B[a] = 1
            elif self.gr_A[b] == -1:
                if self.gr_A[a] == 0:
                    self.gr_A[b] = 1
                    self.gr_B[b] = 0
                else:
                    self.gr_A[b] = 0
                    self.gr_B[b] = 1
            else:
                if not self.gr_A[a] ^ self.gr_A[b]:
                    return False

            if i < len(dislikes) - 1:
                print(i)
                if not traverse(dislikes[i + 1][0], dislikes[i + 1][1], i + 1):
                    return traverse(dislikes[i + 1][1], dislikes[i + 1][0], i + 1)
            return True

        return traverse(dislikes[0][0], dislikes[0][1], 0) or traverse(dislikes[0][1], dislikes[0][0], 0)


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

    N = 10
    dislikes = [[4, 7], [4, 8], [2, 8], [8, 9], [1, 6], [5, 8], [1, 2], [6, 7], [3, 10], [8, 10], [1, 5], [7, 10], [1, 10], [3, 5], [3, 6], [1, 4], [3, 9], [2, 3], [1, 9], [7, 9], [2, 7], [6, 8], [5, 7], [3, 4]] # noqa
    res = Solution().possibleBipartition(N, dislikes)
    print(f'expected::True, got::{res}')


if __name__ == '__main__':
    main()
