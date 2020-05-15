# 39. Combination Sum
# Medium

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def helper(S, slate, i):
            if sum(slate) > target:
                return
            if sum(slate) == target:
                
                res.append(slate[:])
                return
            
            for index in range(i, len(S)):
                slate.append(S[index])
                helper(S, slate, index)
                slate.pop()
                
        if candidates:
            helper(candidates,[],0)
            return res
        return []