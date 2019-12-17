# template for BFS using Queue
from tree_node import TreeNode, insert
from queue import Queue

def bfs(root: TreeNode):
    q = Queue()

    # Push Root on queue
    q.put(root)

    while q.empty() is False:
        # Pop node and print
        node = q.get()
        print(node)

        # Everytime a node is popped and printed, push its children on the queue
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)


rootNode = TreeNode(5)
insert(rootNode, 2)
insert(rootNode, 3)
insert(rootNode, 1)
insert(rootNode, 4)
insert(rootNode, 6)
insert(rootNode, 8)

bfs(rootNode)