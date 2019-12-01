import random
def quick_sort(a):
    return helper(a,0,len(a)-1)

def helper(a,start,end):
    # Base Case
    if start >= end:
        return

    # Pick a random pivot index
    rand_pivot_index = random.randint(start,end)
    # Lomuto Partition
    # Swap pivot element with start element
    a[rand_pivot_index],a[start] = a[start], a[rand_pivot_index]
    # Assign pivot element to element at start index, pivot is not the start element
    pivot = a[start]
    # Initialize orange and green pointers
    orange = start
    green = start
    # Traverse array with green pointer
    for green in range(start+1, end+1):
        if a[green] <= pivot:
            orange += 1
            a[orange], a[green] = a[green], a[orange]
    
    # Place pivot in the right spot
    a[start], a[orange] = a[orange], a[start]

    # Recursive Case 
    helper(a, start, orange - 1)
    helper(a, orange + 1, end)

    return a

print(quick_sort([8,8,1,2,3,4,5,6,7,7,8,8,7,6,9,1]))

