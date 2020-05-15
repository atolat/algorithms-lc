def minSwap(s):
    
    consecutiveCount = 0
    previousChar = None
    totalSwaps = 0
    for each_char in s:
        if each_char is previousChar:
            consecutiveCount += 1
        else:
            totalSwaps += consecutiveCount//3
            consecutiveCount = 0
        previousChar = each_char
    return totalSwaps
        
print(minSwap('abbbbbbbbbba'))