from typing import List


class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = {}
        color = {}
        for u, v in prerequisites:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            color[u] = 'w'
            color[v] = 'w'

        def dfs(node):
            if color[node] == 'g':
                return True
            color[node] = 'g'
            if node in graph:
                for elem in graph[node]:
                    if color[elem] != 'b':
                        if dfs(elem):
                            return True
            color[node] = 'b'
            return False

        return not any(dfs(node) for node in graph if color[node] != 'b')


def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::True, got::{res}')

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::False, got::{res}')

    numCourses = 3
    prerequisites = [[1, 0], [2, 1]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::True, got::{res}')

    numCourses = 3
    prerequisites = [[0, 1], [0, 2], [1, 2]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::True, got::{res}')

    numCourses = 4
    prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    res = Solution().canFinish(numCourses, prerequisites)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()
