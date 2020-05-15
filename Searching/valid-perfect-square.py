# 367. Valid Perfect Square
# Easy

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: num = 16
# Output: true
# Example 2:

# Input: num = 14
# Output: false

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        
        start = 0
        end = num
        
        while start <= end:
            mid = (start + end) // 2
            if num == mid*mid:
                return True
            else:
                if mid*mid < num:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False