# 300. Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# DP Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize a dp array with 1's - dp[i] indicates the length of the longest subsequence at index i
        dp = [1 for _ in range(len(nums))]
        # initial maxlen = 1
        maxlen = 1

        # For every number at index i, scan numbers from 0 to i-1 and see if they form an increasing subsequence with the number at index i
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    # the number at index j forms an increasing subsequence with i
                    # update dp[i] to include the number at j if it results in a better/longer subsequence
                    dp[i] = max(dp[i], dp[j]+1)
                    # Update maxlen
                    maxlen = max(maxlen, dp[i])

        return maxlen

# Binary Search Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize auxillary array to save longest subsequence so far
        aux = [nums[0]]

        # For every number in nums
        for i in range(len(nums)):
            # if num > last element of aux, append it to aux
            if nums[i] > aux[-1]:
                aux.append(nums[i])
            # else find the index of number that is just greater than nums[i] in the aux array and insert nums[i] at that index
            else:
                idx = bisect.bisect_left(aux, nums[i], 0, len(aux)-1)
                aux[idx] = nums[i]

        return len(aux)
