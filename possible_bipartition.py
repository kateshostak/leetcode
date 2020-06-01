from typing import List
import collections


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True

        graph = collections.defaultdict(list)
        colors = [-1]*(N + 1)
        for node, nei in dislikes:
            graph[node].append(nei)
            graph[nei].append(node)

        def traverse(node, color):
            if colors[node] != -1:
                return colors[node] == color
            colors[node] = color
            return all(traverse(nei, color ^ 1) for nei in graph[node])

        return all(traverse(node, 0) for node in range(1, N + 1) if colors[node] == -1)


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
