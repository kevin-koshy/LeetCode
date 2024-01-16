# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pass


result = Solution()
head = [1, 2, 6, 3, 4, 5, 6]
val = 6
print(result.removeElements(head, val))
