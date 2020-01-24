# Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal to the sum of their lengths. This process is repeated until n ropes are connected into a single rope. Find the min possible cost required to connect all ropes.

# Example 1:

# Input: ropes = [8, 4, 6, 12]
# Output: 58
# Explanation: The optimal way to connect ropes is as follows
# 1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
# 2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
# 3. Connect the ropes of length 18 and 12 (cost is 30).
# Total cost to connect the ropes is 10 + 18 + 30 = 58
# Example 2:

# Input: ropes = [20, 4, 8, 2]
# Output: 54
# Example 3:

# Input: ropes = [1, 2, 5, 10, 35, 89]
# Output: 224
# Example 4:

# Input: ropes = [2, 2, 3, 3]
# Output: 20

import heapq
def connectRopes(ropes):
    if not ropes: return 0
    if len(ropes) == 1: return ropes[0]
    heapq.heapify(ropes)
    result = 0
    while len(ropes) > 1:
        x,y = heapq.heappop(ropes),heapq.heappop(ropes)
        result += x + y
        heapq.heappush(ropes,x+y)
        
    return result

ropes = [1, 2, 5, 10, 35, 89]
print(connectRopes(ropes))

# Analysis:
# Time: O(nlogn), space: O(n), where n = sticks.length.

### LEETCODE DISCUSS ###
# What is the wrong thing that you are pointing! Mathematically log(N!) < NlogN and not at all equal. 
# But when using PQ it becomes 4*log(N!) > Nlog(N). 
# The increase in execution time is more when using a PQ since the popping and pushing on a PQ takes logN time where as the suggested solution takes constant time. 
# In simple words increase the size of N and still the getMin function takes same time but in case of a PQ, 
# the time to push and pop increases. Coming to the part of removing constant, 
# it is basically how O notation works (read the note above).