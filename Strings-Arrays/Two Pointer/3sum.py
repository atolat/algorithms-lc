# 15. 3Sum
# Medium

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Using Find Pairs Approach
 
class Solution(object):
    	def threeSum(self, nums):            
            def findPairs(nums, first, target):
                """
                This function will find three numbers that add up to the target
                nums - sorted array
                first - index of the first number 
                target - 3 nums should add up to this number
                """
                start = first + 1
                end = len(nums) - 1
                
                while start < end:
                    current_sum = nums[start] + nums[end] + nums[first]
                    
                    if current_sum == target:
                        triplets.append([nums[first], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        # Remember to add these checks to avoid duplicates
                        # Keep incrementing start or decrementing end till 
                        # there are no duplicates
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif current_sum < target:
                        start += 1
                    else:
                        end -= 1
                        
            nums.sort()
            triplets = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                findPairs(nums, i, 0)
                
            return triplets

# Complexity Analysis
# Time Complexity: O(n^2). 
# findPairs is O(n), and we call it n times.
# Sorting the array takes O(nlogn), so overall complexity is O(nlog n) + O(n^2)
# This is asymptotically equivalent to O(n^2)

# Space Complexity: O(logn) to O(n), depending on the implementation of the sorting algorithm. 
# For the purpose of complexity analysis, we ignore the memory required for the output.