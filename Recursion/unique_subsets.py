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
        def helper(S, i, slate):
            # Base Case
            if len(S) == i:
                results.append(slate[:])
                return

            # Count occurances of elements
            count = 1
            j = i + 1

            while j <= len(S) - 1 and S[j] == S[i]:
                count += 1
                j += 1
            # count holds the number of duplicates
            # Recursive Cases
            # Exclusion Case
            helper(S, i + count, slate)

            # Inclusion
            # Include the element in slate 'count' # of times
            for _ in range(count):
                slate.append(S[i])
                helper(S, i + count, slate)
            
            # Pop element from slate 'count' # of times
            for _ in range(count):
                slate.pop()

        results = []
        nums.sort()
        helper(nums, 0, [])
