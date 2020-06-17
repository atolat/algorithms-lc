# 958. Check Completeness of a Binary Tree
# Medium

# Given a binary tree, determine if it is a complete binary tree.

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = deque([(root, 1)])
        prevId = None
        while q:
            node, id = q.popleft()
            if prevId and id - prevId > 1:
                return False

            if node.left:
                q.append((node.left, id*2))

            if node.right:
                q.append((node.right, id*2+1))

            prevId = id
        return True
