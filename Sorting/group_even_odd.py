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

<<<<<<< HEAD
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
=======
def solve(arr):
    orange = -1  # Track even elements
    green = -1  # Track odd elements

    for green in range(len(arr)):
        if arr[green] % 2 == 0:  # Even
            orange += 1
            arr[orange], arr[green] = arr[green], arr[orange]
    return arr
>>>>>>> 65c006708053d9f0dc45cb38e3dda64130e3fef9
