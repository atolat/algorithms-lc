# 449. Serialize and Deserialize BST
# Medium

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Use preorder serialization
        if not root:
            return []
        preorder = []
        
        def dfs(node): 
            preorder.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return preorder
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data
        inorder = sorted(data)
        ino_map = {}
        for i in range(len(inorder)):
            ino_map[inorder[i]] = i
            
        def helper(p_start, p_end, i_start, i_end):
            # Base Case
            if p_start > p_end:
                return None
            if p_start == p_end:
                return TreeNode(preorder[p_start])

            root_val = preorder[p_start]
            root_index = ino_map[root_val]
            root = TreeNode(root_val)

            # Number of elements in left subtree:
            numleft = root_index - i_start
            # Number of elements in right subtree:
            numright = i_end - root_index

            # Recursively construct left and right subtrees
            root.left = helper(p_start + 1,
                               p_start + numleft,
                               i_start,
                               i_start + numleft - 1)
            root.right = helper(p_start + numleft + 1,
                                p_end,
                                root_index + 1,
                                i_end)
            return root
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)      

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
