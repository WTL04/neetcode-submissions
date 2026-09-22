# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case: return empty array
        if not root:
            return []

        # recursive step
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)