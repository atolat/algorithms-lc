# 213. House Robber II
# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Same as house robber 1, two cases -
        # rob house 1
        # don't rob house 1

        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        if len(nums) == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])

        table = [0 for _ in range(len(nums))]

        # Case 1: suppose house 0 was robbed
        # In that case, house 1 cannot be robbed
        table[2] = nums[2]
        table[3] = max(nums[2], nums[3])

        for i in range(4, len(nums)-1):
            table[i] = max(table[i-1], table[i-2]+nums[i])

        case1 = nums[0] + table[-2]

        # Case 2: house 0 is not robbed
        # This means house 1 can be robbed
        table[1] = nums[1]
        table[2] = max(nums[1], nums[2])
        for i in range(2, len(nums)):
            table[i] = max(table[i-1], table[i-2]+nums[i])
        case2 = table[-1]

        return max(case1, case2)
