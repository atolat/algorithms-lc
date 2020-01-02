# Template for DFS based problems
from tree_node import TreeNode, insert

def dfs(node: TreeNode):
    # Base Case : Leaf Node
    if node.left is None and node.right is None:
        # Process the leaf node, check for some conditions, etc...
        return

    # Recursive Case : Internal Node
    if node.left is not None:
        dfs(node.left)

    if node.right is not None:
        dfs(node.right)