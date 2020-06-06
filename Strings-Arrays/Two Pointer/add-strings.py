# 415. Add Strings
# Easy

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        result = []
        carry = 0
        for i in reversed(range(max_len)):
            ans = sum(map(int, [num1[i], num2[i], carry]))
            result.append(ans%10)
            carry = ans//10
        
        if carry:
            result.append(carry)
            
        return ''.join(map(str, result))[::-1]