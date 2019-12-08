def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1,i,-1):
            if arr[j-1] > arr[j]:
                swap(arr, j-1, j)
    return arr

def swap(arr, firstIndex, secondIndex):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp


print(bubble_sort([1,2,1,1,11,6,5,4,3]))