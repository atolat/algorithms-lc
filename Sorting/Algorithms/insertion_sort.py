def insertion_sort(arr):
    return helper(arr, len(arr)-1)

def helper(arr,n):
    # Base Case
    if n <= 1:
        return
    # Recursive Case
    else:
        helper(arr,n-1)
        j = n-1
        while j >= 1 and arr[j] > arr[j+1]:
            swap(arr,j+1,j)
            j = j-1
    return arr

def swap(arr, firstIndex, secondIndex):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp

print(insertion_sort([1,2,1,1,11,6,5,4,3]))