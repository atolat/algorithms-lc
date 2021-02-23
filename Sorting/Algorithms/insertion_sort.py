def insertionSort(array):
    # Write your code here.
	helper(array, len(array))
	print(array)

def helper(arr,n):
	# Base Case
	if n <= 1:
		return
	# Recursive Case
	helper(arr,n-1)
	n_th = arr[n-1]
	j = n-2
	while j >= 0 and arr[j] > n_th:
		arr[j+1] = arr[j]
		j = j-1
	arr[j+1] = n_th
 
insertionSort([8, 5, 2, 9, 5, 6, 3])

# Decrease and Conquer approach
# T(n) = O(n**2)
# S(n) = O(1)
# STABLE