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

        """
        
        def dfs(node, curSum):
            if not node:
                return False
            
            # record current path sum
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

        """
        eval:
            time: O(n), where n is the number of nodes in the tree
            space: O(h), where h is the height of the tree
        """

            