# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        curr = dummy_head

        while curr.next:
            prev = curr
            if curr.next.val == 0:
                curr = curr.next
            if curr.next:
                curr.val += curr.next.val
                curr.next = curr.next.next
        prev.next = None
        return head


result = Solution()
listnode_array = [0, 3, 1, 0, 4, 5, 2, 0]


def convert_array_to_linked_list(arr):
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head


def print_linked_list(head):
    elems = []
    curr = head
    while curr:
        elems.append(curr.val)
        curr = curr.next
    print(elems)


l_node = convert_array_to_linked_list(listnode_array)
# print_linked_list(l_node)
print_linked_list(result.mergeNodes(l_node))
