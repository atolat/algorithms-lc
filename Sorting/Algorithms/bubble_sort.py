def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1,i,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

print(bubble_sort([1,2,1,1,11,6,5,4,3]))

# T(n) = O(n**2)
# S(n) = O(1)
# STABLE