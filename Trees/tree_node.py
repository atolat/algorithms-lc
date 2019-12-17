class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def findMin(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr

    def findMax(self):
        curr = self
        while curr.right is not None:
            curr = curr.right
        return curr


def search(root: TreeNode, val: int):
    if root is None:
        return None

    curr = root
    while curr is not None:
        if curr.val == val:
            return curr.val
        elif val > curr.val:
            curr = curr.right
        else:
            curr = curr.left
    return None


def insert(root: TreeNode, val: int):
    newNode = TreeNode(val)

    curr = root
    prev = None

    while curr is not None:
        if val == curr.val:
            raise Exception("Value exists in tree")

        elif val < curr.val:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right

    if newNode.val > prev.val:
        prev.right = newNode
    else:
        prev.left = newNode
    return root

# # Delete Impl
# # Find Successor
# # Find Predecessor

# node1 = TreeNode(1)
# # node2 = TreeNode(2)
# # node3 = TreeNode(8)
# print(insert(node1, 2))
# print(insert(node1, 2))

# # print(node1.findMax())
