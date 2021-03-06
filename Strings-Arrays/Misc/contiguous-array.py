# 525. Contiguous Array
# Medium

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Time Complexity - O(n)
# Space Complexity - O(n)
# Did it run on leetcode - Yes
# Did you face any problems - No
# Approach:
# This follows the prefix sum approach wherein we maintain a record (in a map) of a running sum and array index for that sum -
# 0's can be treated as -1 (subtract 1 from the running count if the element is 0)
# While iterating over the array, there are two cases:
# 1. The current running sum is present in the map - the subarray from the old index(stored in the map) to the current index add up to 0
# 2. if the current running sum is 0, all the elements uptil this index add up to 0
# For both cases mentioned above, update the max len of the subarray.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cnt_map = collections.defaultdict(int)
        cnt_map[0] = -1
        max_len = 0
        for i in xrange(len(nums)):
            count = count + 1 if nums[i] == 1 else count - 1
            if count in cnt_map:
                max_len = max(max_len, i - cnt_map[count])
            else:
                cnt_map[count] = i
        return max_len
