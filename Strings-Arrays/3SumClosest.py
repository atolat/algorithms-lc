# 16. 3Sum Closest
# Medium

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Follow same template as 3Sum with some modifications!
class Solution(object):
    	def threeSumClosest(self, nums, target):
            # Sort numbers
            nums.sort()
            
            # Initialize Results
            min_diff = float('+inf')
            result = -1
            
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
                    diff = abs(target - targetSum)
                    
                    if diff == 0:
                        return targetSum
                    
                    if diff < min_diff:
                        min_diff = diff
                        result = targetSum
                        
                    # If the sum is < 0, we want to move the left pointer forward
                    # Increase the sum
                    if targetSum < target:
                        l += 1
                    # If sum is > 0, decrease the sum by moving right pointer inwards
                    elif targetSum > target:
                        r -= 1
                    else: # Sum is now 0, append result to triplets
					    while l<r and nums[l]==nums[l+1]:
					        l+=1
					    while l<r and nums[r]==nums[r-1]:
					        r-=1
					    l+=1
					    r-=1
                        
            return result