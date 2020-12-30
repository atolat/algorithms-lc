# 1137. N-th Tribonacci Number
# Easy
# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [None] * (n+1)
        
        if n == 0: return 0
        if n == 1 or n == 2 : return 1
        table[0] = 0
        table[1] = 1
        table[2] = 1
        
        for i in range(3, n+1):
            table[i] = table[i-1] + table[i-2] + table[i-3]
            
        return table[n] 