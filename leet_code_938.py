from typing import Optional

from BinarySearchTree import TreeNode, create_binary_tree, print_tree


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total = []

        def print_in_order(root):
            ans = 0
            if root:
                print_in_order(root.left)
                if low <= root.val <= high:
                    ans += root.val
                print_in_order(root.right)
            return ans
        total.append(print_in_order(root))
        return sum(total)


result = Solution()
root = [10, 5, 15, 3, 7, None, 18]
bst1 = create_binary_tree(root)
# print_tree(bst1)
low = 7
high = 15
print(result.rangeSumBST(bst1, low, high))
