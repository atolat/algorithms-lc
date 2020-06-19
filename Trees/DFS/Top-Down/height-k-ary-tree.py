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
def find_height(root):
    if not root:
        return 0
    global_max = [0]
        
    def dfs(node, edges_upto_parent):
        edges_upto_me = 1 + edges_upto_parent
        global_max[0] = max(global_max[0], edges_upto_me)
        
        for child in node.children:
            dfs(child, edges_upto_me)
    
    dfs(root, -1)
    return global_max[0]