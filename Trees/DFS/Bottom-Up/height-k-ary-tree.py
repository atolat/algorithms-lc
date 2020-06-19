# Height Of K-Ary Tree
# Given a k-ary tree, find the height of that tree: number of edges in the longest path from the root to any node.
# A k-ary tree is a rooted tree in which each node has no more than k children.

'''
    For your reference:
    
    class TreeNode:
        def __init__(self):
            self.children = []

'''

# Complete the function below.
# Top Down DFS
'''
    For your reference:
    
    class TreeNode:
        def __init__(self):
            self.children = []

'''

# Complete the function below.

# Bottom - Up DFS Approach
def find_height(root):
    if not root:
        return 0
    
    def dfs(node):
        if not node.children:
            return 0
        ht = 0

        for child in node.children:
            ht = max(1 + dfs(child), ht)

        return ht
    return dfs(root)
