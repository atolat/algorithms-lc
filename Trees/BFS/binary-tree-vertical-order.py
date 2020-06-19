# 314. Binary Tree Vertical Order Traversal
# Medium

# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:

# Input: [3,9,20,null,null,15,7]

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7

# Output:

# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:

# Input: [3,9,8,4,0,1,7]

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7

# Output:

# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:

# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2

# Output:

# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Using BFS Template
        # Just Keep track of the vertical levels
        # of a node before inserting in the queue
        if not root:
            return None
        q = deque([(root, 0)])

        # Initialize datastructures to hold negative and positive lists
        neg = []
        zero = [[]]
        pos = []

        while q:
            numnodes = len(q)
            for _ in range(numnodes):
                node, x = q.popleft()
                if x == 0:
                    zero[0].append(node.val)
                elif x > 0:
                    if x > len(pos):
                        pos.append([])
                    pos[x-1].append(node.val)

                else:  # Negative x coordinate
                    if abs(x) > len(neg):
                        neg.append([])
                    neg[abs(x) - 1].append(node.val)

                if node.left:
                    q.append((node.left, x - 1))
                if node.right:
                    q.append((node.right, x + 1))
        neg.reverse()
        neg.extend(zero)
        neg.extend(pos)

        return neg
