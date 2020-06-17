# 107. Binary Tree Level Order Traversal II
# Easy

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = deque()
        if not root:
            return []

        q = deque([root])

        while q:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                currentNode = q.popleft()
                temp.append(currentNode.val)
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)

            result.appendleft(temp)

        return result