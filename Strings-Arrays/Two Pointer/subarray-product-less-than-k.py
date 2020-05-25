# 713. Subarray Product Less Than K
# Medium

# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        start = 0
        product = 1
        count = 0
        result = []
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and start < len(nums):
                product /= nums[start]
                start += 1
                            
            count += end - start + 1
                
            # Collect sub-arrays - Follow up - return the subarrays?
            temp = collections.deque()
            for i in range(end, start - 1, -1):
                temp.appendleft(nums[i])
                result.append(temp)


        return count
    
# Time complexity # -- SOURCE - https://www.educative.io/courses/grokking-the-coding-interview/RMV1GV1yPYz#time-complexity
# The main for-loop managing the sliding window takes O(N) but creating subarrays can take up to O(N^2)
# in the worst case. Therefore overall, our algorithm will take O(N^3)

# Space complexity #
# Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.
# Can you try estimating how much space will be required for the output list?
# The worst case will happen when every subarray has a product less than the target!
# So the question will be, how many contiguous subarray an array can have?

# It is definately not all Permutations of the given array, is it all Combinations of the given array?

# It is not all the Combinations of all elements of the array!

# For an array with distinct elements, finding all of its contiguous subarrays is like finding the number of ways to choose two indices i and j in the array such that i <= j.

# If there are a total of n elements in the array, here is how we can count all the contiguous subarrays:

# When i = 0, j can have any value from ‘0’ to ‘n-1’, giving a total of ‘n’ choices.
# When i = 1, j can have any value from ‘1’ to ‘n-1’, giving a total of ‘n-1’ choices.
# Similarly, when i = 2, j can have ‘n-2’ choices.
# …
# …
# When i = n-1, j can only have ‘1’ choice.
# Let’s combine all the choices:

#     n + (n-1) + (n-2) + ... 3 + 2 + 1
# Which gives us a total of: n*(n+1)/2n∗(n+1)/2

# So, at the most, we need a space of O(n^2) for all the output lists.