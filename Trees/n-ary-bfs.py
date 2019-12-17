# 429. N-ary Tree Level Order Traversal
# Medium

# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

# Constraints:

# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from Queue import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # Initialize Empty Results array
        results = []
        
        # Initialize Empty Queue
        q = Queue()
        
        # Edge Case
        if root is None:
            return results
        
        # Push root onto queue
        q.put(root)

        while q.empty() is not True:
            # Count number of nodes at that level
            numnodes = q.qsize()
            
            temp = []
            
            # Repeat numnodes number of times
            for _ in range(numnodes):
                node = q.get()
                temp.append(node.val)
                
                for child in node.children:
                    if child is not None:
                        q.put(child)
                        
            results.append(temp)
            
        return results