# 665. Non-decreasing Array
# Medium

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        breach = False
        for i in range(n-1):
            # Find a breach if next number is decreasing
            if nums[i] > nums[i+1]:
                # Is this the first breach?
                if breach:  # No
                    return False
                # Now we have 2 options
                # Modify nums[i] to be in the range nums[i-1] and nums[i+1]
                elif i-1 < 0 or nums[i-1] <= nums[i+1]:
                    # We can modify nums[i]
                    pass
                # Modify nums[i+1] to be in the range nums[i] and nums[i+2]
                elif i+2 >= n or nums[i] <= nums[i+2]:
                    # We can modify nums[i+1]
                    pass
                # No option, return False
                else:
                    return False
                # Mark this as a breach
                breach = True
        return True
