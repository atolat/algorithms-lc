from tree_node import TreeNode, insert

def pre_order(root: TreeNode):
    curr = root
    print(curr)

    if curr.left is not None:
        pre_order(curr.left)

    if curr.right is not None:
        pre_order(curr.right)


def in_order(root: TreeNode):
    curr = root

    if curr.left is not None:
        in_order(curr.left)
    print(curr)
    if curr.right is not None:
        in_order(curr.right)
    

def post_order(root: TreeNode):
    curr = root
    if curr.left is not None:
        pre_order(curr.left)
    
    if curr.right is not None:
        pre_order(curr.right)  
    print(curr)
     

rootNode = TreeNode(5)
insert(rootNode, 2)
insert(rootNode, 3)
insert(rootNode, 1)
insert(rootNode, 4)
insert(rootNode, 6)
insert(rootNode, 8)

