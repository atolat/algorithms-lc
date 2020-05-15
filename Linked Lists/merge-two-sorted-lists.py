# 21. Merge Two Sorted Lists
# Easy

# Add to List

# Share
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(-1)
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
                
            elif l2.val <= l1.val:
                dummy.next = l2
                l2 = l2.next
                
            dummy = dummy.next
            
        while l1 != None:
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next
            
        while l2 != None:
            dummy.next = l2
            l2 = l2.next
            dummy = dummy.next
        
        return curr.next
    
    
# Complexity Analysis

# Time complexity : O(n + m)O(n+m)

# Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

# Space complexity : O(1)O(1)

# The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.