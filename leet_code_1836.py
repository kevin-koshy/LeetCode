# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        curr = head
        list_dict = {}
        while curr:
            list_dict[curr.val] = list_dict.get(curr.val, 0) + 1
            curr = curr.next

        # if all(value > 1 for value in list_dict.values()):
        #     return None

        dummy_head = ListNode(0)
        curr = head
        prev = dummy_head
        prev.next = curr
        after = curr.next
        while curr:
            if list_dict[curr.val] > 1:
                curr.next = None
                curr = after
                after = after.next if curr and curr.next else None
                prev.next = curr
            else:
                prev = curr
                curr = after
                after = after.next if curr and curr.next else None

        return dummy_head.next


# arr1 = [2,1,1,2]
arr1 = [3,2,2,1,3,2,4]

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

t1 = convert_arr_to_nodes(arr1)
print_linked_list(t1)
t2 = result.deleteDuplicatesUnsorted(t1)
print_linked_list(t2)
