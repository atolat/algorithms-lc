# Group the numbers

# Problem Statement:

# You are given an integer array arr, of size n. Group and rearrange them (in-place) into evens and odds in such a way that group of all even integers appears on the left side and group of all odd integers appears on the right side.




# Constraints:

# 1 <= n <= 10^5
# arr contains only positive integers.
# arr may contains duplicate numbers.
# Solution with linear time complexity and constant auxiliary space is expected.


# Sample Test Case:



# Sample Input:



# [1, 2, 3, 4]



# Sample Output:

# [4, 2, 1, 3]

import heapq
def topK(arr, k):
    k_heap = []
    track_set = set()
    
    for x in arr:
        if x in track_set:
            continue
        if len(k_heap) < k:
            heapq.heappush(k_heap, x)
            track_set.add(x)
        else:
            if x > k_heap[0]:
                popped = heapq.heappop(k_heap)
                track_set.remove(popped)
                heapq.heappush(k_heap,x)
                track_set.add(x)
    return k_heap

print(topK([1,2,6,4,8,6,4,5,6],3))