# 1060. Missing Element in Sorted Array
# Medium

# 413

# 20

# Add to List

# Share
# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

# Example 1:

# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.
# Example 2:

# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
# Example 3:

# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Use Binary Search Template
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            predicted = nums[0] + mid
            missing = nums[mid] - predicted
            
            if missing < k:
                start = mid + 1
            else:
                end = mid - 1
        
        missing = nums[end] - (nums[0] + end)
        
        return nums[end] + (k - missing)