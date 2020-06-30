# 66. Plus One
# Easy

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []

        digits[-1] += 1

        for i in reversed(xrange(1, len(digits))):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1

        else:
            if digits[0] == 10:
                digits[0] = 1
                digits.append(0)

        return digits
