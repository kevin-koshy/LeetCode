# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display_list(self):
        elems = []
        curr = self
        while curr is not None:
            elems.append(curr.val)
            curr = curr.next
        return elems



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array_list = []
        curr = head
        while curr is not None:
            array_list.append(curr.val)
            curr = curr.next
        print(array_list)
        return array_list == array_list[::-1]

result = Solution
list_array = [3, 2, 1, 3]


def convert_array_to_ll(ll_array):
    head = ListNode(ll_array[0])
    last = head

    for i in range(1, len(ll_array)):
        temp = ListNode()
        temp.val = ll_array[i]
        temp.next = None
        last.next = temp
        last = temp
    return head


node = convert_array_to_ll([9, 7, 76,7,9])
# print(node.display_list())
print(result.isPalindrome(self=result,head=node))
