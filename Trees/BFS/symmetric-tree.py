# 101. Symmetric Tree
# Easy

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        q = deque([(root, root)])

        while q:
            nodeL, nodeR = q.popleft()
            if nodeL.val != nodeR.val:
                return False

            if nodeL.left is not None and nodeR.right is not None:
                q.append((nodeL.left, nodeR.right))
            elif nodeL.left is not None or nodeR.right is not None:
                return False

            if nodeL.right is not None and nodeR.left is not None:
                q.append((nodeL.right, nodeR.left))
            elif nodeL.right is not None or nodeR.left is not None:
                return False

        return True
