# 199. Binary Tree Right Side View
# Medium

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Initialize Empty Results array
        results = []
        
        # Initialize empty queue
        q = Queue()
        
        # Edge Case
        if root is None:
            return []
        
        # Push root onto queue
        q.put(root)
        temp = []
        while q.empty() is not True:
            numnodes = q.qsize()

            for _ in xrange(numnodes):
                node = q.get()
                temp.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            results.append(temp[-1])
        
        return results