# Maximum Sum Increasing Subsequence
# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

# Example 1:

# Input: {4,1,2,6,10,1,12}
# Output: 32
# Explanation: The increaseing sequence is {4,6,10,12}.
# Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
# Example 2:

# Input: {-4,10,3,7,15}
# Output: 25
# Explanation: The increasing sequences are {10, 15} and {3,7,15}.

def find_MSIS(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]

    maxSum = nums[0]
    for i in range(1, n):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
                maxSum = max(maxSum, dp[i])

    return maxSum


def main():
    print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS([-4, 10, 3, 7, 15]))


main()
