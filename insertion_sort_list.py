import pdb


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + ' ' + self.next.__repr__()


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head

        prev = head
        curr = head.next
        while curr:
            curr.next, prev.next = head, curr.next
            head = curr

            tmp = head.next
            tmp_prev = head
            key = prev.next
            while tmp and head.val > tmp.val:
                if tmp == key:
                    break
                tmp, tmp_prev = tmp.next, tmp

            if tmp_prev == head:
                curr = prev.next
                continue

            if tmp is None:
                tmp.next = head
                head = head.next
                tmp.next.next = None
                return head

            # pdb.set_trace()
            tmp_head = head.next
            tmp_prev.next, head.next = head, tmp
            head = tmp_head
            curr = prev.next
        return head


def list_maker(arr):
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head


def print_list(node):
    while node:
        print(node.val, end=' ')
        node = node.next


def main():
    head = list_maker([4, 2, 1, 3])
    print_list(Solution().insertionSortList(head))


if __name__ == '__main__':
    main()
