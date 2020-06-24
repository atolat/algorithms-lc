# 144. Binary Tree Preorder Traversal
# Medium

# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Try and simulate the call stack and program counter
        # during recursive execution

        # Edge
        if root is None:
            return []
        result = []
        stack = [(root, None)]

        while len(stack) != 0:
            (node, zone) = stack[-1]

            if zone is None:
                stack[-1] = (node, "ARRIVAL")
                result.append(node.val)
                if node.left is not None:
                    stack.append((node.left, None))
            elif zone == "ARRIVAL":
                stack[-1] = (node, "INTERIM")
                if node.right is not None:
                    stack.append((node.right, None))
            elif zone == "INTERIM":
                stack[-1] = (node, "DEPARTURE")
                stack.pop()
        return result
