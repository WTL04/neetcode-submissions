# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case: null node
        if not root:
            return []

        # recursive step
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)