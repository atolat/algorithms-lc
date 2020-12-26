# 986. Interval List Intersections
# Medium

# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
# The intersection of two closed intervals is a set of real numbers that is either empty, 
# or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# Example 1:

# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        start, end = 0, 1
        intersection  = []
        
        while i < len(A) and j < len(B):
            A_start = A[i][start]
            A_end = A[i][end]
            B_start =  B[j][start]
            B_end = B[j][end]
            
            a_overlaps_b = B_start <= A_start <= B_end
            b_overlaps_a = A_start <= B_start <= A_end
            
            if a_overlaps_b or b_overlaps_a:
                new_start = max(A_start, B_start)
                new_end = min(A_end, B_end)
                intersection.append([new_start, new_end])
                
            if A_end < B_end:
                i += 1
            else:
                j += 1
        return intersection