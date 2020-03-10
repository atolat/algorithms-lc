# 40. Combination Sum II
# Medium

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def helper(S, i, slate, slatesum, target):
            # Backtracking Case
            if slatesum == target:
                result.append(slate[:])
                return
            
            # Base Case
            if slatesum > target:
                return
            
            for j in range(i, len(S)):
                if j == i or S[j] != S[j-1]:
                    slate.append(S[j])
                    helper(S, j+1, slate, slatesum + S[j], target)
                    slate.pop()
            
        helper(candidates, 0, [], 0, target)
        return result