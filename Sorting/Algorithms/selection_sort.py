def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] <= arr[min]:
                arr[j], arr[min] = arr[min], arr[j]
    return arr


print(selection_sort([3, 4, 6, 5, 4, 1, 2, 0, 8]))

# T(n) = O(n**2)
# S(n) = O(1)
# NOT STABLE
