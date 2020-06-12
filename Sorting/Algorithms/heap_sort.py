import heapq

def heap_sort(nums):
    result = []
    heapq.heapify(nums)

    while len(nums) != 0:
        result.append(heapq.heappop(nums))
    return result

print(heap_sort([8,8,1,2,3,4,5,6,7,7,8,8,7,6,9,1]))

# T(n) = O(n log n)
# IN-PLACE
# NOT STABLE