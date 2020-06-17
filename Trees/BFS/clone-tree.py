# Clone a Binary Tree
# Given a binary tree (represented by its root node, as usual), clone it. Return the root node of the cloned tree.

from collections import deque
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: root of the cloned tree

def cloneTree(root):
    if not root:
        return None
    cloneRoot = TreeNode(root.val)
    q = deque([(root, cloneRoot)])
    
    while q:
        node, clone = q.popleft()
        if node.left_ptr:
            clone.left_ptr = TreeNode(node.left_ptr.val)
            q.append((node.left_ptr, clone.left_ptr))
        if node.right_ptr:
            clone.right_ptr = TreeNode(node.right_ptr.val)
            q.append((node.right_ptr, clone.right_ptr))
    return cloneRoot