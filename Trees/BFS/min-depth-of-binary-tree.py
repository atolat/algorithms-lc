# 111. Minimum Depth of Binary Tree
# Easy

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        if not root: return 0
        
        q = deque([root])
        
        while q:
            numnodes = len(q)
            level += 1
            for _ in range(numnodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # First leaf encountered - return level
                if node.left is None and node.right is None:
                    return level
