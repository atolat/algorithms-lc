# 993. Cousins in Binary Tree
# Easy

# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return false
        q = deque([root])
        px, py = None, None

        while q:
            numnodes = len(q)
            for _ in range(numnodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if node.left.val == x:
                        px = node.val
                    if node.left.val == y:
                        py = node.val

                if node.right:
                    q.append(node.right)
                    if node.right.val == x:
                        px = node.val
                    if node.right.val == y:
                        py = node.val

            if px or py:
                return px is not None and py is not None and px != py

        return False
