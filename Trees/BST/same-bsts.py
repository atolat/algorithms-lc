# Given two arrays representing order of insertion of elements in BSTs, return if the two arrays represent the same BST

def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

	
    leftSubtreeOne = findSmaller(arrayOne)
    leftSubtreeTwo = findSmaller(arrayTwo)
    rightSubtreeOne = findLarger(arrayOne)
    rightSubtreeTwo = findLarger(arrayTwo)

    return sameBsts(leftSubtreeOne, leftSubtreeTwo) and sameBsts(rightSubtreeOne, rightSubtreeTwo)

def findSmaller(array):
	out = []
	for x in array[1:]:
		if x < array[0]:
			out.append(x)
	return out

def findLarger(array):
	out = []
	for x in array[1:]:
		if x >= array[0]:
			out.append(x)
	return out
