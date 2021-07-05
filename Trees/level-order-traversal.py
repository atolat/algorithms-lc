# 102. Binary Tree Level Order Traversal
# Medium

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Initialize empty results list
        results = []

        # Null Check
        if root is None:
            return results

        # Initialize empty Queue
        q = Queue()

        # Push root node in queue
        q.put(root)

        while q.empty() is not True:
            # Count the number of nodes at each level --> length of the queue
            numnodes = q.qsize()
            temp = []
            # Repeat this numnodes number of times
            for _ in range(numnodes):
                node = q.get()
                temp.append(node.val)

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)
            results.append(temp)
        return results

# DFS approach


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        # DFS

        def dfs(node, level):
            # Level is the index of the array in result
            if level > len(result):
                result.append([])
            result[level-1].append(node.val)
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
        if not root:
            return []
        dfs(root, 1)
        return result