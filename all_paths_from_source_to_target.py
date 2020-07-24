from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.tmp = ''
        paths = []

        def traverse(node):
            if node == len(graph) - 1:
                return True
            for n in graph[node]:
                self.tmp += str(n)
                if traverse(n):
                    paths.append(self.tmp)
                self.tmp = self.tmp[:-1]
        traverse(0)
        return [[0] + list(map(int, elem)) for elem in paths]


def main():
    graph = [[1, 2], [3], [3], []]
    res = Solution().allPathsSourceTarget(graph)
    print(f'expected::[[0, 1, 3], [0, 2, 3], got::{res}')

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    res = Solution().allPathsSourceTarget(graph)
    print(f'expected::[[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]], got::{res}')


if __name__ == '__main__':
    main()
