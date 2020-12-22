# 503. Next Greater Element II
# Medium

# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize result array with -1
        n = len(nums)
        result = [-1 for _ in range(len(nums))]

        # Initialize empty stack
        stack = []

        # Traverse over the array 2*- circular array
        for i in range(n*2):
            # If the current number is > the number on top of the stack, this is the next greater number
            # Update the result with the number at the corresponding index(stack.pop() gives this index)
            while stack and nums[i % n] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i % n]

            # Push numbers on the stack only if the next greater element is not found
            if result[i % n] == -1:
                stack.append(i % n)

        return result
