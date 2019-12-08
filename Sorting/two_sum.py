# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Using extra space - dictionary O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        k = 0
        
        for i in range(len(nums)):
            num = nums[i]
            k = target - num
            if k not in seen:
                seen[num] = [num,i]
            else:
                return [seen[k][1],i]

    # Sort and solve - in - place - O(n log n)
    def twoSumInPlace(self, nums, target):
        # Sort input array
        nums.sort()

        # Two pointers start & end
        start = 0
        end = len(nums)-1

        while start <= end:
            k = nums[start] + nums[end]
            if k == target:
                return [start,end]
            elif k > target:
                end -= 1
            elif k < target:
                start +=1
        return None
            
