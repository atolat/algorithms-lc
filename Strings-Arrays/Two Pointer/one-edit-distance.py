# 161. One Edit Distance
# Medium

# Given two strings s and t, determine if they are both one edit distance apart.

# Note: 

# There are 3 possiblities to satisify one edit distance apart:

# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:

# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns, nt = len(s), len(t)  
    
        # Ensure s is smaller than t
        if ns > nt:
            return self.isOneEditDistance(t, s)
            
        if nt - ns > 1:
            return False
            
        for i in range(ns):
            if s[i] != t[i]:
                # Case 1: Strings have equal length
                # s(i+1,n) should be equal to t(i+1,n)
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                
                # Case 2: Strings have different length
                # s(i,n) == t(i+1, n+1)
                else:
                    return s[i:] == t[i+1:]
                
        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character.
        
        return ns + 1 == nt
    
# Two Pointer approach - O(1) space
class Solution(object):
    def isOneEditDistance(self, s, t):
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        found_inequality = False
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if found_inequality: return False
                found_inequality = True
                if len(s) < len(t): i -= 1
                elif len(s) > len(t): j -= 1
            i += 1
            j += 1
        
        return True