# 1161. Maximum Level Sum of a Binary Tree
# Medium

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
# Example 1:
# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxsum = float('-inf')
        minlevel = 0
        level = 0

        if not root:
            return 0

        q = deque([root])

        while q:
            numnodes = len(q)
            level += 1
            levelSum = 0
            for _ in range(numnodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                levelSum += node.val
            if levelSum > maxsum:
                maxsum = levelSum
                minlevel = level

        return minlevel
