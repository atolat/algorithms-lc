def merge_sort(arr):

    return helper(arr, 0, len(arr)-1)


def helper(arr, startIndex, endIndex):
    # Base Case
    if startIndex >= endIndex:
        return arr, 0
    # Recursive Case
    # Split
    mid = (startIndex + endIndex)//2
    a, ai = helper(arr, startIndex, mid)
    b, bi = helper(arr, mid+1, endIndex)
    
    inversions = 0 + ai + bi

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
            inversions += (mid - i + 1)
            j += 1

    while i <= mid:
        aux.append(arr[i])
        i += 1

    while j <= endIndex:
        aux.append(arr[j])
        j += 1
    arr[startIndex:endIndex+1] = aux
    return arr, inversions

def main():
    int_list = open('./integer_array.txt', 'r')
    arr = [int(line) for line in int_list]
    arr, inv = merge_sort(arr)
    print(inv)
    
main()

# T(n) = O(n * log n)
# S(n) = O(n)
# STABLE