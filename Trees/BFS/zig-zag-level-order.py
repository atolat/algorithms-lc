# 103. Binary Tree Zigzag Level Order Traversal
# Medium

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        result = []
        q = collections.deque()
        q.append(root)
        left_to_right = True

        while q:
            numnodes = len(q)
            temp = collections.deque()
            for _ in range(numnodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if left_to_right:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
            left_to_right = not left_to_right
            result.append(temp)
        return result
