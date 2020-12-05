# USING AN ARRAY OF LISTNODES #
# // Time Complexity :
# put - O(1) - Assuming int keys
# get - O(1) Asymptomatic - Assuming int keys and low probability of collisions 
# get - O(n) in the worst case, if there are many collisions, the performance degrades to a linked list lookup
# remove - O(1) asymptomatic, O(n) worst case

# // Space Complexity : O(n)

# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach

# USING ARRAY OF LISTNODES #
class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.arr = [None]*self.size
        
    def get_index(self, key):
        return key%self.size
    
    # Returns the previous node for a node referenced by key
    def get_prev(self, head, key):
        curr = head
        prev = None
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev        
    
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.get_index(key)
        # If the index does not exist, create a new sentinel head 
        if self.arr[index] is None: 
            self.arr[index] = ListNode(-1,-1)
        # Get prev node
        prev = self.get_prev(self.arr[index],key)
        if prev.next is None: # Key does not exist, create a new ListNode at end of list
            prev.next = ListNode(key, value)
        else: # Key exists, update value
            prev.next.val = value
            
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.get_index(key)
        if self.arr[index] is None:
            return -1
        prev = self.get_prev(self.arr[index],key)
        if prev.next is None:
            return -1
        else:
            return prev.next.val

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = self.get_index(key)
        if self.arr[index] is None: return
        prev = self.get_prev(self.arr[index],key)
        if prev.next is None:
            return
        else:
            prev.next = prev.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)