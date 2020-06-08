from typing import List


class Node:
    def __init__(self, arr):
        self.arr = arr
        self.prev = None
        self.next_ = None


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = {(key, elem): elem for key, elem in people}
        print(d)
        l = sorted(d, key=lambda x: d[x])
        head = None
        for person in d:
            print(person[0])
            tmp = []
            i = 0
            node = head
            while node:
                if node.arr[0] >= person[0]:
                    i += 1
                    if i > person[1]:
                        break
                node = node.next

            if node:
                tmp = node.next_
                node.next_ = Node(list(person))
                node.next_.prev = node
                if tmp:
                    tmp.prev = node.next_
            else:
                node = Node(list(person))
                if not head:
                    head = node
                else:
                    node.next_ = head
                    head.prev = node
                    head = node

            res = []
            node = head
            while node:
                res.append(node.arr)
                node = node.next_

            for elem in res:
                print(elem)
            return res


def main():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    res = Solution().reconstructQueue(people)
    print(f'expected::[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]], got::{res}')


if __name__ == '__main__':
    main()
