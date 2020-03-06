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

class Solution(object):
    	def threeSum(self, nums):
            # Sort numbers
            nums.sort()
            
            # Initialize Results
            triplets=[]
            
            for i in range(len(nums)-2):
                # Initialize left and right pointers
                # Left starts from i+1 because i starts from 0, so the 
                # case for nums[0] is already covered!
                
                l = i + 1
                r = len(nums) - 1
                
                # Duplicate numbers eg: [1,1,1...] continue
                if i > 0 and nums[i]==nums[i-1]: continue
                
                while l < r:
                    targetSum = nums[i] + nums[l] + nums[r]
                    # If the sum is < 0, we want to move the left pointer forward
                    # Increase the sum
                    if targetSum < 0:
                        l += 1
                    # If sum is > 0, decrease the sum by moving right pointer inwards
                    elif targetSum > 0:
                        r -= 1
                    else: # Sum is now 0, append result to triplets
					    triplets.append([nums[i], nums[l], nums[r]])
                        # Check if there are duplicates on left and right
                        # Increase/Decrease left and right pointers accordingly
					    while l<r and nums[l]==nums[l+1]:
						    l+=1
					    while l<r and nums[r]==nums[r-1]:
						    r-=1
                        # After the result is found and duplicates are bypassed
                        # Increase left by 1, Decrease right by one
					    l+=1
					    r-=1
                        
            return triplets