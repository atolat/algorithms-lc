def insertion_sort(arr):
    return helper(arr, len(arr)-1)

def helper(arr,n):
    # Base Case
    if n <= 1:
        return
    # Recursive Case
    else:
        helper(arr,n-1)
        n_th = arr[n]
        j = n-1
        while j >= 1 and arr[j] > n_th:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = n_th
    return arr

print(insertion_sort([1,2,1,1,11,6,5,4,3]))

# Decrease and Conquer approach
# T(n) = O(n**2)
# S(n) = O(1)
# STABLE