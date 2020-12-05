# 155. Min Stack
# Easy

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# // Time Complexity : 
# O(1) - push, pop, getMin
# // Space Complexity : O(n) auxillary space to store min element
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# Use two stacks, one stack to push pop values and the other to keep track of the minimum element
class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # For every value pushed on the stack, keep track of the current min and push it on the minstack
        if self.size == 0:
            self.min.append(x)
        else:
            self.min.append(min(self.min[self.size - 1], x))
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        :rtype: None
        """
        # For a pop operation, delete from both stacks
        if self.size == 0:
            return
        del self.stack[self.size - 1]
        del self.min[self.size - 1]
        self.size -= 1
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.size - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[self.size - 1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()