# 16. 3Sum Closest
# Medium

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = float('+inf')
        result = -1
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                current_sum = nums[start] + nums[end] + nums[i]
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    start += 1
                else:
                    end -= 1
                
                diff = abs(target-current_sum)
                
                if diff < min_diff:
                    min_diff = diff
                    result = current_sum
            
        return result
    
# Complexity Analysis
# Time Complexity: O(n^2). 
# findPairs is O(n), and we call it n times.
# Sorting the array takes O(nlogn), so overall complexity is O(nlog n) + O(n^2)
# This is asymptotically equivalent to O(n^2)

# Space Complexity: O(logn) to O(n), depending on the implementation of the sorting algorithm. 
# For the purpose of complexity analysis, we ignore the memory required for the output.