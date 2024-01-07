# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        after = curr.next
        dummy = ListNode(0)
        dummy.next = after
        while curr.next and curr.next.next:
            after = curr.next
            curr.next = after.next
            # if after.next and after.next.next:
            after.next = after.next.next
            curr = curr.next
        curr.next = None
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = dummy.next

        return head


arr1 = [1, 2, 3, 4, 5, 6, 7, 8]


def convert_arr_to_nodes(arr):
    new_node = ListNode(arr[0])
    head = new_node
    curr = head
    for i in range(1, len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = curr.next
    return head


def print_linked_list(arr):
    arr_nodes = []
    curr = arr
    while curr:
        arr_nodes.append(curr.val)
        curr = curr.next
    print(arr_nodes)


t1 = convert_arr_to_nodes(arr1)
# print_linked_list(t1)

result = Solution()
t2 = result.oddEvenList(t1)
print_linked_list(t1)
