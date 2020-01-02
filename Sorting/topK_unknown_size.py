# Top K

# Problem Statement:

# You are given an array of integers arr, of size n, which is analogous to a continuous stream of integers input. Your task is to find K largest elements from a given stream of numbers.
# By definition, we don't know the size of the input stream. Hence, produce K largest elements seen so far, at any given time. For repeated numbers, return them only once.
# If there are less than K distinct elements in arr, return all of them.

# Note:

# Don't rely on size of input array arr.
# Feel free to use built-in functions if you need a specific data-structure.

# Return an integer array res, containing K largest elements. If there are less than K unique elements, return all of them.

# Order of elements in res does not matter.

# Constraints:

# 1 <= n <= 10^5
# 1 <= K <= 10^5
# arr may contains duplicate numbers.
# arr may or may not be sorted

# Complete the function below.
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
                heapq.heappush(k_heap, x)
                track_set.add(x)
    return k_heap
