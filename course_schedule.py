import collections
from typing import List


class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        color = {}

        def dfs(node):
            if node in color:
                return True
            color[node] = 'g'
            for elem in graph[node]:
                if elem in color and color[elem] != 'b':
                    dfs(elem)
                color[node] = 'b'
            return False

        return all(dfs(node)
                   for node in range(numCourses)
                   if node not in color)


def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::True, got::{res}')

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
