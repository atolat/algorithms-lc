# 662. Maximum Width of Binary Tree
# Medium

# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input:

#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input:

#           1
#          /
#         3
#        / \
#       5   3

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input:

#           1
#          / \
#         3   2
#        /
#       5

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input:

#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxwidth = float('-inf')
        q = deque([(root, 1)])

        while q:
            numnodes = len(q)
            first, last = None, None
            for _ in range(numnodes):
                node, id = q.popleft()
                if node.left:
                    q.append((node.left, id*2))
                if node.right:
                    q.append((node.right, id*2+1))

                last = id
                if first is None:
                    first = id
            maxwidth = max(maxwidth, (last-first+1))

        return maxwidth
