# 257. Binary Tree Paths
# Easy

# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Top Down DFS Approach
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        # top down dfs

        def printPaths(node, slate):
            if node.right is None and node.left is None:
                slate.append(str(node.val))
                paths.append(''.join(slate[:]))
                slate.pop()
                return

            slate.append(str(node.val)+'->')
            if node.left is not None:
                printPaths(node.left, slate)
            if node.right is not None:
                printPaths(node.right, slate)
            slate.pop()

        if not root:
            return []

        printPaths(root, [])
        return paths

# BFS Approach
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        q = deque([(root, [])])

        while q:
            node, slate = q.popleft()
            if node.left:
                q.append((node.left, slate + [str(node.val)+'->']))
            if node.right:
                q.append((node.right, slate + [str(node.val)+'->']))
            if not node.right and not node.left:
                slate = slate + [str(node.val)]
                result.append(''.join(slate))
        return result
