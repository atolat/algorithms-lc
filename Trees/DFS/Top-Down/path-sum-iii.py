# 437. Path Sum III
# Easy

# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        numpaths = [0]

        def dfs(node, slate):
            slate.append(node.val)
            slate_sum = 0
            # Compute suffix sums of slate
            for i in range(len(slate) - 1, -1, -1):
                slate_sum += slate[i]
                if slate_sum == sum1:
                    numpaths[0] += 1

            if node.left:
                dfs(node.left, slate)
            if node.right:
                dfs(node.right, slate)
            slate.pop()

        dfs(root, [])
        return numpaths[0]
