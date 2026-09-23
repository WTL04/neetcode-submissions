# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        understand: 
            swap the children of a parent node
            need to return the root

        match:
             by using dfs, we can reach the bottom of the left subtree, swap the children nodes,
             then traverse the right of the tree, and swap the children nodes there. the recursive calls would reach the root node, 
            and swap both left and right subtrees. since we need to swap the left and right children first, maybe we need to try postorder dfs

        plan:

            if not root:
                reach null and simply return

            self.invertTree(root.left) 
            self.invertTree(root.right)

            swap left and right nodes
            temp = root.left
            root.left = root.right
            root.right = temp

            return root
        """


        if not root:
            return

        # depth search left first then right
        self.invertTree(root.left)
        self.invertTree(root.right)

        # swap child nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        return root
