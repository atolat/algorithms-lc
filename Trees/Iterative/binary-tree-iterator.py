# 173. Binary Search Tree Iterator
# Medium

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Example:
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false

# Note:
# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            self.stack = []
        else:
            self.stack = [(root, None)]
            self.advance()

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        (node, zone) = self.stack[-1]
        if node.right is not None:
            self.stack.append((node.right, None))
        self.advance()
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0

    def advance(self):
        while len(self.stack) != 0:
            (node, zone) = self.stack[-1]
            if zone is None:
                self.stack[-1] = (node, "ARRIVAL")
                if node.left is not None:
                    self.stack.append((node.left, None))
            elif zone == "ARRIVAL":
                self.stack[-1] = (node, "INTERIM")
                return
                # if node.right is not None:
                #     stack.append((node.right, None))
            elif zone == "INTERIM":
                self.stack[-1] = (node, "DEPARTURE")
                self.stack.pop()


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
