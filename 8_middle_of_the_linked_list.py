# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        len_ = 0
        tmp = head
        while tmp:
            len_ += 1
            tmp = tmp.next

        mid = len_//2
        i = 0
        mid_node = head
        while i != mid:
            mid_node = mid_node.next
            i += 1
        return mid_node
