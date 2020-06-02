import pdb


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val, node.next = node.next.val, node.next.next

    def as_arr(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res


def main():
    arr = [4, 5, 1, 9]
    n = 5
    tmp = head = ListNode(4)
    for elem in arr[1:]:
        tmp.next = ListNode(elem)
        tmp = tmp.next
    node = head.next

    Solution().deleteNode(node)
    res = Solution().as_arr(head)
    print(f'expected::[4, 1, 9], got::{res}')

    arr = [4, 5, 1, 9]
    n = 1
    tmp = head = ListNode(4)
    for elem in arr[1:]:
        tmp.next = ListNode(elem)
        tmp = tmp.next
    node = head.next.next

    Solution().deleteNode(node)
    res = Solution().as_arr(head)
    print(f'expected::[4, 5, 9], got::{res}')

    arr = [2, 0, 1, 3]
    n = 2
    tmp = head = ListNode(2)
    for elem in arr[1:]:
        tmp.next = ListNode(elem)
        tmp = tmp.next
    node = head

    Solution().deleteNode(node)
    res = Solution().as_arr(head)
    print(f'expected::[0, 1, 3], got::{res}')


if __name__ == '__main__':
    main()
