from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        tmp = []
        paths = []

        def traverse(node):
            tmp.append(node)
            if node == len(graph) - 1:
                paths.append(tmp.copy())

            for elem in graph[node]:
                traverse(elem)
                if tmp:
                    tmp.pop(-1)
        traverse(0)
        return paths

def main():
    graph = [[1, 2], [3], [3], []]
    res = Solution().allPathsSourceTarget(graph)
    print(f'expected::[[0, 1, 3], [0, 2, 3], got::{res}')

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    res = Solution().allPathsSourceTarget(graph)
    print(f'expected::[[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]], got::{res}')

    graph = [[4, 3, 11, 5, 7, 8, 10, 2, 1, 6], [2, 9, 3, 11, 10, 6, 7, 4, 5], [10, 7, 9, 4, 3, 6, 11, 5], [9, 4, 11, 6, 8, 10, 7, 5], [5, 7, 6, 9, 8, 11, 10], [8, 7, 11, 9, 10, 6], [10, 7, 11, 9, 8], [9, 10, 11, 8], [10, 9], [11, 10], [11], []] # noqa
    res = Solution().allPathsSourceTarget(graph)
    print(f'expected::[[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]], got::{res}')


if __name__ == '__main__':
    main()
