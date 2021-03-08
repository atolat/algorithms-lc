# 23. Merge k Sorted Lists
# Hard

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Time Complexity: O(n log k)
# Space Complexity: O(k)
# Approach: Add the heads of all lists to a minheap. Pop out the min element and add the next element from the corresponding list to the heap. 

from heapq import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Initialize a minheap
        minheap = []
        
        # Push the heads of all lists in the heap
        for root in lists:
            if root:
                heappush(minheap, (root.val, root))
        
        # Create a sentinel head
        head = ListNode(-1,-1)
        
        # Pop out smallest element, push the next smallest from that list in the heap 
        curr = head
        while minheap:
            val, node = heappop(minheap)
            curr.next = node
            curr = node
            # Push the next smallest element 
            if node.next:
                heappush(minheap, (node.next.val, node.next))
                
        if head.next != -1:
            return head.next
        return None