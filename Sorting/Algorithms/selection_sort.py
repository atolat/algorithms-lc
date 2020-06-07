def selection_sort(arr):
    for i in range(0,len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] <= arr[min]:
                swap(arr,j,min)
    return arr



def swap(arr, firstIndex, secondIndex):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp


print(selection_sort([3,4,6,5,4,1,2,0,8]))