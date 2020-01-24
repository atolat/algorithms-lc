# 138. Copy List with Random Pointer
# Medium
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# Example 4:

# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cloneMap = {}
        
        curr = head
        
        # 1st pass -> construct cloneMap
        while curr != None:
            cloneMap[curr] = Node(curr.val)
            curr = curr.next
            
        # 2nd pass -> build new list from cloneMap 
        curr = head
        while curr != None:
            cloneMap[curr].next = cloneMap.get(curr.next)
            cloneMap[curr].random = cloneMap.get(curr.random)
            curr = curr.next
            
        return cloneMap.get(head)
    
# Time Complexity : O(N)O(N) because we make one pass over the original linked list.
# Space Complexity : O(N)O(N) as we have a dictionary containing mapping from old list nodes to new list nodes. Since there are NN nodes, we have O(N)O(N) space complexity.