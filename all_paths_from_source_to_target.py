from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def traverse(node, tmp):
            if node == len(graph) - 1:
                paths.append(tmp)

            for elem in graph[node]:
                traverse(elem, tmp + [elem])
        traverse(0, [0])
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
