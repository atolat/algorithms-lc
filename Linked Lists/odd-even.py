# 328. Odd Even Linked List
# Medium

# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Construct a list for odds and evens
        odd_head = ListNode('odd')
        even_head = ListNode('even')
        odd = True
        curr = head
        odds = odd_head
        evens = even_head

        while curr:
            if odd:
                odds.next = curr
                odds = odds.next
            else:
                evens.next = curr
                evens = evens.next
            curr = curr.next
            odd = not odd

        evens.next = None
        odds.next = even_head.next
        return odd_head.next
