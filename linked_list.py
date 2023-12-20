class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next is not None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            elems.append(curr.data)
        return elems


list_node = LinkedList()
list_node.append(3)
list_node.append(5)
print(list_node.display())
