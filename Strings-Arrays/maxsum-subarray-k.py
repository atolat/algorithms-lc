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