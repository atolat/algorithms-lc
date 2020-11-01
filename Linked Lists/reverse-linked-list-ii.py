# 92. Reverse Linked List II
# Medium

# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        if m == n:
            return head

        # Go to m-th node
        # prev_node, next_node = None, None
        current_node = head
        prev_node = None
        i = 0
        while current_node and i < m - 1:
            prev_node = current_node
            current_node = current_node.next
            i += 1

        last_node_of_first_list = prev_node
        last_node_of_sub_list = current_node

        # Reverse sublist - It starts at current_node and ends at n-th node
        i = 0
        next_node, prev_node = None, None
        while current_node and i < n - m + 1:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            i += 1

        # Connect this sublist to list
        if last_node_of_first_list:
            last_node_of_first_list.next = prev_node
        else:  # m = 1
            head = prev_node
        last_node_of_sub_list.next = current_node

        return head
