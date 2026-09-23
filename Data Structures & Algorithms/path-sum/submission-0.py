# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        understanding: 
            checking if path root-to-leaf = targetSum
            return boolean if path exists

        match: 
            dfs backtracking problem, with the condition that if the path sum > target sum, 
            backtrack and search else where

        plan:



        """
        
        # dfs to search one path
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val

            # check for leaf node
            if not node.left and not node.right:
                return curSum == targetSum

            # search left subtree
            if dfs(node.left, curSum):
                return True

            # search right subtree
            if dfs(node.right, curSum):
                return True

            return False

        return dfs(root, 0)

            