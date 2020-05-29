# 125. Valid Palindrome
# Easy

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 1:
            return True
        # Sanitize string
        s = ''.join(e for e in s if e.isalnum()).lower()
        
        if len(s) == 2:
            return s[0] == s[1]
        
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
            
        return True
        
# Complexity Analysis

# Time complexity : O(n), in length n of the string.
# Space complexity : O(1)