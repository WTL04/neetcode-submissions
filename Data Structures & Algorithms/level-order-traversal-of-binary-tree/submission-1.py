# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        understanding:
            we are to search the node level by level, returning a nested list, where each sublist is contains the values
            of each level

            each level corresponds with its number of nodes (e.g. level 1 has 1 node, level 2 has 2 nodes, etc)

        match: 
            this is asking for the implementation of bfs

        plan:

            initialize queue
            initialise result array

            add root to queue

            while queue exists:
                track queue length
                initialize level subarray

                for i in range(queue length):
                    remove node from queue (left)
                    add to level subarray

                    if children exists:
                        add node left child to queue
                        add node right child to queue

                add level to result

            return result

        review:
            edge case:
            1. return [] when no root
        """
        from collections import deque

        # edge case: no nodes
        if not root:
            return []

        queue = deque()
        result = []
        queue.append(root)

        while queue:
            # length of queue = number of nodes in a level
            qLen = len(queue)
            level = []
            for i in range(qLen):
                # remove node from queue, add to level
                node = queue.popleft()
                level.append(node.val)

                # append children to queue
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

        """
        eval:
            time: O(n), where n is the number of nodes
            space: O(n), where n is the number of nodes
        """
                    


