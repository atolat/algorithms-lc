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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap = []
        
        for head in lists:
            while head is not None:
                heapq.heappush(minHeap, head.val)
                head = head.next                
        
        sentinel = ListNode(-1)
        head = sentinel
        
        while minHeap:
            val = heapq.heappop(minHeap)
            node = ListNode(val)
            head.next = node
            head = head.next
            
        return sentinel.next