# 852. Peak Index in a Mountain Array
# Easy

# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Use Binary Search Template
        start = 1
        end = len(A)-2
        
        while start <= end:
            mid = (start+end)//2
            
            # Zones
            # ***ASCENDING ZONE***PEAK***DESCENDING ZONE***
            
            if A[mid - 1] < A[mid] and A[mid + 1] < A[mid]: # Peak
                return mid
            elif A[mid] < A[mid+1]: # Ascending Zone
                start = mid + 1
            else: # Descending Zone
                end = mid - 1
                
        return -1