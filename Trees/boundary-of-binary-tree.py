# 545. Boundary of Binary Tree
# Medium

# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

# Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

# The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

# The right-most node is also defined by the same way with left and right exchanged.

# Example 1

# Input:
#   1
#    \
#     2
#    / \
#   3   4

# Ouput:
# [1, 3, 4, 2]

# Explanation:
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].


# Example 2

# Input:
#     ____1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10

# Ouput:
# [1,2,4,7,8,9,10,6,3]

# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to definition)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Edge cases
        if not root:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        # 3 walks
        # Boundary = leftview + leaves + rightview
        leftboundary = [root.val]
        if root.left:
            curr = root.left
            while curr:
                leftboundary.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
            leftboundary.pop()  # Last node is a leaf

        rightboundary = collections.deque()
        if root.right:
            curr = root.right
            while curr:
                rightboundary.appendleft(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left

            rightboundary.popleft()  # last node is a leaf
        # rightboundary.reverse()

        leaves = []

        def dfs(node):
            if node.left is None and node.right is None:
                leaves.append(node.val)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)

        return leftboundary + leaves + list(rightboundary)
