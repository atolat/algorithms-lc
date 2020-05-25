# 18. 4Sum
# Medium

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# FindPairs Template 

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        def findPairs(nums, target, first, second):
            start = second + 1
            end = len(nums) - 1
            while start < end:
                current_sum = nums[first] + nums[second] + nums[start] + nums[end]
                if target == current_sum:
                    results.append([nums[start], nums[first], nums[second], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif current_sum < target:
                    start += 1
                else:
                    end -= 1
                    
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                findPairs(nums, target, i, j)
                
        return results
    
# Time complexity #
# Sorting the array will take O(N*logN). Overall searchQuadruplets() will take O(N * logN + N^3),
# which is asymptotically equivalent to O(N^3)

# Space complexity #
# The space complexity of the above algorithm will be O(N) which is required for sorting.