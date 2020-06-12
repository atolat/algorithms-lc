# countingSort(array, size)
#   max <- find largest element in array
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique element and 
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1

def counting_sort(arr):
    max_size = max(arr)
    count = [0 for _ in range(max_size+1)]
    out = [0 for _ in range(len(arr))]
    
    for i in range(len(arr)):
        count[arr[i]] += 1
                
    for i in range(1, max_size+1):
        count[i] += count[i-1]
        
    for i in reversed(range(len(arr))):
        print(arr[i])
        index = count[arr[i]] - 1
        out[index] = arr[i]
        count[arr[i]] -= 1
        
    return out

print(counting_sort([5,6,1,1,1,0,9,10,8,7,100]))