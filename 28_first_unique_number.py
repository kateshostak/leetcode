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
        return prev + ' ' + str(self.x) + ' ' + next_


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
        return self.first_unique.x

    def add(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
            self.nums_to_nodes[x] = self.head
            self.first_unique = self.head
        else:
            if x in self.nums_to_nodes:
                tmp = self.nums_to_nodes[x]
                if x == self.first_unique.x:
                    tmp = self.first_unique.next
                    if tmp:
                        self.first_unique = tmp
                    else:
                        self.first_unique = Node(-1)
                if tmp:
                    prev = tmp.prev
                    next_ = tmp.next
                    if prev:
                        prev.next = tmp.next
                        if next_:
                            next_.prev = prev
                    else:
                        self.head = next_
                    self.nums_to_nodes[x] = None

            else:
                tmp = Node(x)
                if self.first_unique.x == -1:
                    self.first_unique = tmp
                self.tail.next = tmp
                tmp.prev = self.tail
                self.tail = tmp
                self.nums_to_nodes[x] = tmp


def main():
    comms = ["showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
    args = [[], [5], [], [2], [], [3], []]
    res = []
    f = FirstUnique([2, 3, 5])
    # out = [2,null,2,null,3,null,-1]
    tmp = []
    for com, arg in zip(comms, args):
        tmp.append(getattr(f, com)(*arg))
    res.append(tmp)

    comms = ["showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
    args = [[], [7], [3], [3], [7], [17], []]
    f = FirstUnique([7, 7, 7, 7, 7, 7])
    # out = [null,-1,null,null,null,null,null,17]
    tmp = []
    for com, arg in zip(comms, args):
        tmp.append(getattr(f, com)(*arg))
    res.append(tmp)

    comms = ["showFirstUnique", "add", "showFirstUnique"]
    args = [[], [809], []]
    f = FirstUnique([809])
    # out = [809,null,-1]
    tmp = []
    for com, arg in zip(comms, args):
        tmp.append(getattr(f, com)(*arg))
    res.append(tmp)
    print(res)


if __name__ == '__main__':
    main()
