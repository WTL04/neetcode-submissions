# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative solution:
        By using a stack, we can remember the return path of our search. We first decend the left 
        subtree, pushing every node we pass onto the stack. When we can no longer go left, we pop
        the top of the stack (deepest unvisted node) and record it's value. Then we move to the 
        right subtree and do the same. 
        """
        result = []
        stack = []
        curr = root

        while curr or stack:

            # traverse left subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # reach null from left subtree
            curr = stack.pop()
            result.append(curr.val)

            # traverse right subtree
            curr = curr.right

        return result