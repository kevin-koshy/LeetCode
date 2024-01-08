# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy_head = ListNode(0)
        curr = head
        after = curr.next
        prev = dummy_head
        prev.next = curr

        while after:
            if curr.val == after.val:
                while after and curr.val == after.val:
                    curr = curr.next
                    after = curr.next
                prev.next = curr.next
                curr = curr.next
                after = curr.next if curr else None
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
                after = after.next
        return dummy_head.next

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


result = Solution()
# head1 = [1,1,1,2,3]
# head1 = [1,2,3,3,4,4,5]
head1 = [1,1]
head2 = convert_arr_to_nodes(head1)
t1 = result.deleteDuplicates(head2)
print_linked_list(t1)
