# 82. Remove Duplicates from Sorted List II
# Medium

# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Return the linked list sorted as well.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize a sentinel node
        sentinel = ListNode(0)
        sentinel.next = head
        previous = sentinel
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                while current and current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                previous.next = current
            else:
                current = current.next
                previous = previous.next
        return sentinel.next