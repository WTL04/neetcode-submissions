# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        understand: 
            we only want the value of nodes visable from the right side, in order of top to bottom

        match:
            this sounds like a problem we can use bfs since we need the order to be top to bottom aka level by level.

        plan:
            the plan is to implement bfs but instead of tracking all nodes in a level, only return the last node in that level 

            q = queue
            add root to queue
            results = []

            while queue:
                qLen = len(queue)
                level subarray

                for i in range(qLen):
                    pop left queue
                    append node to level subarray

                if node has left child:
                    append node to queue

                if node has right child:
                    append node to queue

                append last element of level to result

            return result
        """
        # edge case
        if not root:
            return []

        from collections import deque

        q = deque()
        q.append(root)
        result = []

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                level.append(node)

                # add next level nodes to queue
                if node.left:
                    q.append(node.left)
    
                if node.right:
                    q.append(node.right)

            # append last element of level
            result.append(level[-1].val)



        return result

