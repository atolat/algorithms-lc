def merge_sort(arr):
    return helper(arr, 0, len(arr) - 1)


def helper(arr, start_index, end_index):
    # Base Case
    if start_index >= end_index:
        return arr, 0
    # Recursive Case
    # Split
    mid = (start_index + end_index) // 2
    helper(arr, start_index, mid)
    helper(arr, mid + 1, end_index)

    # Merge
    i = start_index
    j = mid + 1
    aux = []

    while i <= mid and j <= end_index:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1

        elif arr[j] < arr[i]:
            aux.append(arr[j])
            j += 1

    while i <= mid:
        aux.append(arr[i])
        i += 1

    while j <= end_index:
        aux.append(arr[j])
        j += 1
    arr[start_index:end_index + 1] = aux
    return arr


def main():
    arr = [1, 4, 3, 2, 8, 11, 4, 6]
    res = merge_sort(arr)
    print(res)


main()

# T(n) = O(n * log n)
# S(n) = O(n)
# STABLE
