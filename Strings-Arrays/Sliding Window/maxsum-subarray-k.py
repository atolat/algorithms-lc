# Problem Statement #
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].


def maxSum(arr,k):
    currentRunningSum = 0
    maxVal = float('-inf')
    for i in range(len(arr)):
        currentRunningSum += arr[i]
        if i >= k-1:
            maxVal = max(currentRunningSum,maxVal)
            currentRunningSum -= arr[i-(k-1)]
            print(arr[i],arr[i-(k-1)])
            
    return maxVal
    
print(maxSum([4,2,1,7,8,1,2,8,1,0],3))