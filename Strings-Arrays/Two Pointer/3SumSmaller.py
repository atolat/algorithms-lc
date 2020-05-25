# 259. 3Sum Smaller 
# Medium
# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example:

# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 
# Explanation: Because there are two triplets which sums are less than 2:
#              [-2,0,1]
#              [-2,0,3]
# Follow up: Could you solve it in O(n2) runtime?

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        
        def findPairs(nums, first, target):
            count = 0
            start = first + 1
            end = len(nums)-1
            
            while start < end:
                current_sum = nums[first] + nums[start] + nums[end]
                if current_sum < target: # Found Triplet
                # since nums[end] >= arr[start], therefore, we can replace nums[end] by any number between
                # start and end to get a sum less than the target sum 
                    count += (end - start)
                    start += 1
                else: # Reduce sum by moving end in-wards
                    end -= 1
            return count
        
        count = 0
        for i in range(len(nums)):
            count += findPairs(nums,i, target)

        return count
    
# Complexity Analysis
# Time Complexity: O(n^2). 
# findPairs is O(n), and we call it n times.
# Sorting the array takes O(nlogn), so overall complexity is O(nlog n) + O(n^2)
# This is asymptotically equivalent to O(n^2)

# Space Complexity: O(logn) to O(n), depending on the implementation of the sorting algorithm. 
# For the purpose of complexity analysis, we ignore the memory required for the output.