# 234. Palindrome Linked List
# Easy

# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        first_half_end = self.find_mid(head)
        second_half_start = self.reverse(first_half_end)
        start = head

        while start and second_half_start:
            if start.val != second_half_start.val:
                return False
            start = start.next
            second_half_start = second_half_start.next
        return True

    # Find middle
    def find_mid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    # Reverse
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
