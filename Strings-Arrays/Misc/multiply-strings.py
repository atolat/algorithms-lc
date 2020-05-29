# 43. Multiply Strings
# Medium

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Elementry School Algorithm
        len1 = len(num1)
        len2 = len(num2)
        
        # Initialize array of size len1 + len2 to hold result
        res = [0] * (len(num1) + len(num2))
        
        # Convert integers to strings and reverse
        str1 = list(map(int, reversed(num1)))
        str2 = list(map(int, reversed(num2)))
        
        # Scan both numbers 
        for j in range(len2):
            for i in range(len1):
                # Memorize 3 steps
                res[i+j] = res[i+j] + str1[i]*str2[j]
                res[i+j+1] = res[i+j+1] + res[i+j] // 10
                res[i+j] = res[i+j] % 10
                
        i = len(res) - 1
        while res[i] == 0 and i > 0:
            i -= 1
        
        return "".join(map(str, res[:i+1][::-1]))
