# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_array_to_linked_list(arr):
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        temp = ListNode(arr[i])
        curr.next = temp
        curr = temp
    return head


def display_linked_list(head: ListNode):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = head
        p = head
        while curr:
            loop_m, loop_n = 0, 0
            while loop_m < m and curr:
                p = curr
                curr = curr.next
                loop_m += 1
            while loop_n < n and curr:
                curr = curr.next
                loop_n += 1

            p.next = curr
        return head


head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
m = 2
n = 3

head_node = convert_array_to_linked_list(head)
# display_linked_list(head_node)

result = Solution()
head_node2 = result.deleteNodes(head_node, m, n)
display_linked_list(head_node2)
