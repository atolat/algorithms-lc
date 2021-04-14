# 90. Subsets II
# Medium

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        def helper(S, slate):
            res.append(slate[:])
            
            for i in range(len(S)):
                if i > 0 and S[i-1] == S[i]:
                    continue
                slate.append(S[i])
                helper(S[i+1:], slate)
                slate.pop()
                    
        helper(nums,[])
        return res
            