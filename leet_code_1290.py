# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        ans =""
        while curr:
            ans = ans+str(curr.val)
            curr = curr.next
        return int(ans,2)

def convert_array_to_linked_list(arr):
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head

head = [1,0,1]

head_list = convert_array_to_linked_list(head)

result = Solution()

print(result.getDecimalValue(head_list))
