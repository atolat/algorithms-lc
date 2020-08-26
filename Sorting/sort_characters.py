# Sort All Characters

# Problem Statement:
# You have to sort an array of characters containing alphanumeric characters along with some other characters - ‘!’, ’@’, ’#’, ’$’, ’%’, ’^’, ’&’, ’*’, ’(‘, ’)’.
# You are given a character array named arr.

#
# Complete the 'sort_array' function below.
#
# The function accepts Character Array arr as parameter.
#

def sort_array(arr):
    # Write your code here
    freq = [0 for _ in range(128)]
    out = []
    for c in arr:
        index = ord(c)
        freq[index] += 1

    for i in range(128):
        for j in range(0, freq[i]):
            out.append(chr(i))
    return out
