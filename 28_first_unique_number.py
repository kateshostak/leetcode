from typing import List
import pdb


class Node():
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None

    def __repr__(self):
        prev = 'None'
        next_ = 'None'
        if self.prev:
            prev = str(prev)
        if self.next:
            next_ = str(prev)
        return prev + ' ' +  str(self.x) + ' ' + next_

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums_to_nodes = {}
        self.head = None
        self.tail = None
        self.first_unique = -1
        for n in nums:
            self.add(n)

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.x)
            tmp = tmp.next

    def showFirstUnique(self) -> int:
        return self.first_unique

    def add(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
            self.nums_to_nodes[x] = self.head
            self.first_unique = x
        else:
            if x == self.first_unique:
                tmp = self.nums_to_nodes[x].next
                if tmp:
                    self.first_unique = tmp.x
                else:
                    self.first_unique = -1
            else:
                if x in self.nums_to_nodes:
                    tmp = self.nums_to_nodes[x]
                    if tmp:
                        tmp.prev.next = tmp.next
                        self.nums_to_nodes[x] = None
                else:
                    tmp = Node(x)
                    self.tail.next = tmp
                    tmp.prev = self.tail
                    self.tail = self.tail.next
                    self.nums_to_nodes[x] = self.tail
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


def main():
    comms = ["showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
    args = [[], [5], [], [2], [], [3], []]
    res = []
    f = FirstUnique([2, 3, 5])
    # out = [2,null,2,null,3,null,-1]
    for com, arg in zip(comms, args):
        res.append(getattr(f, com)(*arg))
    print(res)


if __name__ == '__main__':
    main()
