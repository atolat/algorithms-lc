# 142. Linked List Cycle II
# Medium

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.


# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Follow-up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow = head
        fast = head
        cycle_length = 0
        current = None

        # Use Floyd's Algorithm to detect a cycle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                current = slow
                # Cycle Exists, calculate length
                break
        if current == None:
            return None  # No Cycle

        # Now, to find the cycle length -
        # Anchor the node where fast and slow meet - This would be a node in the cycle
        # Advance the pointer one step at a time and increment cycle length
        # When the meet again, break
        while True:
            current = current.next
            cycle_length += 1
            if current == fast:
                break

        # Find Start
        pointer1 = head
        pointer2 = head

        # Move pointer2 by cycle_length
        for _ in range(cycle_length):
            pointer2 = pointer2.next

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer2
