# 941. Valid Mountain Array
# Easy

# Given an array A of integers, return true if and only if it is a valid mountain array.

# Recall that A is a mountain array if and only if:
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

# Example 1:

# Input: [2,1]
# Output: false
# Example 2:

# Input: [3,5,5]
# Output: false
# Example 3:

# Input: [0,3,2,1]
# Output: true

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2: return False
        
        for i in range(len(A)-1):
            if A[i] >= A[i+1]:
                break
            
        for j in range(len(A)-1,0,-1):
            if A[j-1] <= A[j]:
                break
            
        if i == j:
            return True
        else:
            return False