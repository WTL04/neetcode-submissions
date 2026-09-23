# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        understanding:
            a 'good' node contains a path from root, values that increase 

            root will always be a 'good' node

            we need to return the count of good nodes (int)

        match:
            sounds like a dfs problem where we need to check the path for each node,
            and see if the current node's value is greater than the previous.
            i think the iterative approach to dfs would work better since we are storing
            and checking if a node is 'good' based on its existing path.
            we can check if the child val is greater than the current node,
            mark it as 'good' then keep searching. 

        plan:
            had to look at solution.


        """

        def dfs(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                count = 1
            else:
                count  = 0

            # calculate new maximum
            maxVal = max(maxVal, node.val)
            count += dfs(node.left, maxVal) # search left subtree
            count += dfs(node.right, maxVal) # search right subtree
            return count

        return dfs(root, root.val)
        """
        eval:
            time: o(n), where n is the number of nodes
            space: o(h), where h is the height of the tree
        """
