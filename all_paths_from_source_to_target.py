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


if __name__ == '__main__':
    main()
