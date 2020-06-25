# 94. Binary Tree Inorder Traversal
# Medium

# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
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
                if node.left is not None:
                    stack.append((node.left, None))
            elif zone == "ARRIVAL":
                stack[-1] = (node, "INTERIM")
                result.append(node.val)
                if node.right is not None:
                    stack.append((node.right, None))
            elif zone == "INTERIM":
                stack[-1] = (node, "DEPARTURE")
                stack.pop()
        return result
