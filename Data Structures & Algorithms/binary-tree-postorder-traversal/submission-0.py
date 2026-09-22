# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        last_visited = None

        while curr or stack:
            # traverse left subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # view top of stack
            peek = stack[-1]

            # traverse right subtree if it exists and hasn't been visited yet
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                last_visited = stack.pop()
                result.append(last_visited.val)

        return result