# 739. Daily Temperatures
# Medium

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        # Initialize a stack to hold index of temperatures
        stack = []

        # initialize a resdult array with 0's
        res = [0 for _ in range(n)]

        # iterate over the array
        for i in range(n):
            # if the current number is greater than the number at index stack.peek() - we have found the next highest temp
            # pop from stack to get the index, update the result with current index - popped index -> number of elements in between curr and highest
            # repeat this till the current number is greater than every number that appears on the top of the stack
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            # Add the indedx of current number to the stack
            stack.append(i)

        return res
