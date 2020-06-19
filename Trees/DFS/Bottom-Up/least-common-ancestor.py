# 236. Lowest Common Ancestor of a Binary Tree
# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Bottom Up DFS
        # Initialize LCA to None
        LCA = [None]

        def dfs(node, p, q):
            pfound, qfound = False, False
            # Common
            if node is p:
                pfound = True
            if node is q:
                qfound = True

            # Recursive Case
            if node.left is not None:
                (pf, qf) = dfs(node.left, p, q)
                pfound = pf or pfound
                qfound = qf or qfound

            if node.right is not None:
                (pf, qf) = dfs(node.right, p, q)
                pfound = pf or pfound
                qfound = qf or qfound

            if pfound and qfound and LCA[0] is None:
                LCA[0] = node
            return (pfound, qfound)

        dfs(root, p, q)
        return LCA[0]
