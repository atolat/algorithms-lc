# 560. Subarray Sum Equals K
# Medium

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        prefix_map = collections.defaultdict(int)
        prefix_sum = 0
        out = 0
        prefix_map[0] = 1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if (prefix_sum - k) in prefix_map:
                out += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return out
    
# **Complexity Analysis**
# Time complexity : O(n). The entire numsnums array is traversed only once.

# Space complexity : O(n). Hashmap mapmap can contain upto nn distinct entries in the worst case.