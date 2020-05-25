# 977. Squares of a Sorted Array
# Easy

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Note:

# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return [A[0]**2]
        start = 0
        end = len(A) - 1
        out = []
         
        while start <= end:
            mid = (start + end) // 2
            if A[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
        
        # End is the pointer that marks start of negative numbers
        # Start marks start of positive numbers
        p1 = end
        p2 = start
        
        while p1 >= 0 and p2 < len(A):
            if A[p1]**2 <= A[p2]**2:
                out.append(A[p1]**2)
                p1 -= 1
                
            else:
                out.append(A[p2]**2)
                p2 += 1
                
        while p1 >= 0:
            out.append(A[p1]**2)
            p1 -= 1
        
        while p2 < len(A):
            out.append(A[p2]**2)
            p2 += 1
            
        return out        
    
    
# Complexity Analysis

# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N).