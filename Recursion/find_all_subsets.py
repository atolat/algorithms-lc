# 78. Subsets
# Medium

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(S, i, slate):
            # Base Case
            if len(S) == i:
                result.append(slate[:])
                return
            
            # Inner Nodes
            # Inclusion
            slate.append(S[i])
            helper(S, i+1, slate)
            slate.pop()
    
            # Exclusion
            helper(S, i+1, slate)
        
        result = []
        helper(nums, 0, [])
        return result

# Cleaner, using backtracking
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(S, slate):
            
            res.append(slate[:])
            
            for index in range(len(S)):
                slate.append(S[index])
                helper(S[index+1:], slate)
                slate.pop()
        
        if nums:
            helper(nums,[])
            return res
        return []
    
