class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


arr_nodes = [10, 5, 15, 3, 7, None, 18]


def create_binary_tree(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    for index in range(1, len(arr)):
        if not isinstance(arr[index], int):
            break
        temp = root
        new_node = TreeNode(arr[index])
        while True:
            if new_node and new_node.val == temp.val:
                break
            if new_node.val < temp.val:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
    return root


bst1 = create_binary_tree(arr_nodes)
print(bst1.val)
print(bst1.left.val)
print(bst1.right.val)
