from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        paths = {}
        for i, elem in enumerate(nums[:-1]):
            paths[i] = [i + j + 1 for j in range(elem)]

        paths_rev = {}
        for elem, vals in paths.items():
            for v in vals:
                if v not in paths_rev:
                    paths_rev[v] = [elem]
                else:
                    paths_rev[v].append(elem)

        start = len(nums) - 1
        end = 0
        nodes = []
        def traverse(start, end, nodes):
            nodes.append(start)
            if start not in paths_rev:
                return None
            if start == end:
                return nodes

            for node in paths_rev[start]:
                if node not in nodes:
                    new_path = traverse(node, end, nodes)
                    if new_path:
                        return new_path
            return None
        traverse(start, end, nodes)
        if end in nodes and start in nodes:
            return True
        else:
            return False

def main():
    arr = [2, 3, 1, 1, 4]
    # arr = [3, 2, 1, 0, 4]
    # arr = [0, 2, 3]
    print(Solution().canJump(arr))


if __name__ == '__main__':
    main()
