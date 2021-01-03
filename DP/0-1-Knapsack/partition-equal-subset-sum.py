# 416. Partition Equal Subset Sum
# Medium

# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Recursive Solution - TLE
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Edge Case, if sum is odd, return False
        if not nums or sum(nums) % 2 == 1:
            return False

        # Target sum is sum of nums divided by 2
        s = sum(nums)//2

        def helper(s, index):
            # Base Cases
            # If target sum is reached, return True
            if s == 0:
                return True
            if index == 0:
                return False
            pick = False
            # 2 options - either pick the current number or don't pick current number
            if s - nums[index] >= 0:  # Can pick only if adding current number doesn't exceed the sum
                pick = helper(s - nums[index], index - 1)
            dont_pick = helper(s, index - 1)
            return pick or dont_pick

        return helper(s, len(nums) - 1)

# Bottom Up DP
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        n = len(nums)

        # Edge Case - if the sum is odd, we cannot for subsets with equal sums
        if total % 2 == 1:
            return False

        s = int(total/2)

        # Initialize 2D dp table
        dp = [[False for _ in range(1+s)] for _ in range(n)]

        # 0 can be achieved by excluding all numbers - mark the first column as True
        for i in range(0, n):
            dp[i][0] = True

        # with only one number, we can form a subset only when the required sum is equal to its value
        for j in range(1+s):
            dp[0][j] = nums[0] == j

        # Tabulate
        for numindex in range(1, n):
            for target in range(1, 1+s):
                pick = False
                # Include number at current index
                if target - nums[numindex] >= 0:
                    pick = dp[numindex-1][target - nums[numindex]]
                # Exclude number at current index
                dont_pick = dp[numindex-1][target]
                dp[numindex][target] = pick or dont_pick

        return dp[n-1][s]
