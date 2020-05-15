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
        res = []
        def helper(S, slate, slate_sum):
            if slate_sum > target:
                return
            if slate_sum == target:
                res.append(slate[:])
                return
            
            for index in range(len(S)):
                if index > 0 and S[index-1] == S[index]:
                    continue
                slate.append(S[index])
                helper(S[index+1:], slate, slate_sum+S[index])
                slate.pop()
                
        if candidates:
            helper(candidates,[],0)
            return res
        return []