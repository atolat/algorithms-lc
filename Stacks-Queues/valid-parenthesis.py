# 20. Valid Parentheses
# Easy

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hmap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
                
        stack = []
        
        for c in s:
            # If it is a closing parenthesis - 
            # the corresponding opening paren is in the map!:
            # Pop element and save to top
            # If stack is empty, top = '#'
            if c in hmap:
                top = stack.pop() if stack else '#'
                # If the top element is not a corresponding open parenthesis
                # return False
                if hmap[c] != top:
                    return False
            else: # Push only the opening parenthesis on the stack
                stack.append(c)
        # If the stack is empty, return True
        return not stack