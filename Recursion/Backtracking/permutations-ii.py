# 47. Permutations II
# Medium

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        def _helper(S, slate):
            # Base Case
            if not S:
                result.append(slate[:])
                return
            
            # Recursive Case
            for i in range(len(S)):
                if i > 0 and S[i] == S[i-1]:
                    continue
                slate.append(S[i])
                _helper(S[:i]+S[i+1:], slate)
                slate.pop()

                
        _helper(nums,[])
        return result