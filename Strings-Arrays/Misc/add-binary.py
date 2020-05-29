# 67. Add Binary
# Easy

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            # carry can be 0, 1, 2
            # append 1 to answer when carry is 1 
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            # If carry was 2 -> 1
            # If carry was 0, 1 -> 0
            carry = carry // 2
            
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)

# Time complexity: O(max(N,M)), where N and M are lengths of the input strings a and b.

# Space complexity: O(max(N,M)) to keep the answer.