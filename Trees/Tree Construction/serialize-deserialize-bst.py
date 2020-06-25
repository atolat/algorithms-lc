# 449. Serialize and Deserialize BST
# Medium

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.stack = []

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        result = []
        self.stack.append(root)

        while len(self.stack) > 0:
            h = self.stack.pop()
            if h:
                result.append(str(h.val)+',')
                self.stack.append(h.right)
                self.stack.append(h.left)
            else:
                result.append('#,')
        return ''.join(result)[0:-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(arr, t):
            if arr[t[0]] == '#':
                return None
            root = TreeNode(int(arr[t[0]]))
            t[0] += 1
            root.left = helper(arr, t)
            t[0] += 1
            root.right = helper(arr, t)
            return root

        arr = data.split(',')
        t = [0]
        return helper(arr, t)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
