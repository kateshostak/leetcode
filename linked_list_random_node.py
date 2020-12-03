import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head
        i = 0
        res = None
        while curr:
            curr = curr.next
            if random.randint(0, i) == 0:
                res = curr.val
            i += 1

        return res
