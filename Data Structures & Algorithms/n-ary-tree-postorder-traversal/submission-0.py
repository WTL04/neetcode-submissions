"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        understanding:
            post order = left -> right -> parent
                in other words, search through all children before adding the parents

            each node has n amount of children, there are no left or rights

            the children are stored in as a 'list of nodes', while the function only takes a single node as a parameter

            return an array of the search results in postorder
        
        match: 
            we can traverse post order using recursive DFS


        plan:

            base case: 
            if not root:
                return []

            return self.postorder(root.children[:1]) + self.postorder(root.children[1:]) + [root.val]


        """

        if not root:
            return []

        result = []

        for child in root.children:
            result.extend(self.postorder(child))

        return result + [root.val]

        
