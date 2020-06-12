def merge_sort(arr):
    return helper(arr, 0, len(arr)-1)


def helper(arr, startIndex, endIndex):
    # Base Case
    if startIndex >= endIndex:
        return
    # Recursive Case
    # Split
    mid = (startIndex + endIndex)//2
    helper(arr, startIndex, mid)
    helper(arr, mid+1, endIndex)

    # Merge
    i = startIndex
    j = mid + 1
    aux = []

    while i <= mid and j <= endIndex:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1

        elif arr[j] < arr[i]:
            aux.append(arr[j])
            j += 1

    while i <= mid:
        aux.append(arr[i])
        i += 1

    while j <= endIndex:
        aux.append(arr[j])
        j += 1
    arr[startIndex:endIndex+1] = aux
    return arr


print(merge_sort([5, 3, 4, 5, 6, 7]))

# T(n) = O(n * log n)
# S(n) = O(n)
# STABLE