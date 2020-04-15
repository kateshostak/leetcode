# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def print_list(node):
    while node:
        print(node.val)
        node = node.next


def main():
    # Input: [1,2,3,4,5]
    # Output: Node 3 from this list (Serialization: [3,4,5])
    arr = [1, 2, 3, 4, 5]
    head = tmp = ListNode(1)
    for x in arr[1:]:
        tmp.next = ListNode(x)
        tmp = tmp.next

    print_list(Solution().middleNode(head))


if __name__ == '__main__':
    main()
