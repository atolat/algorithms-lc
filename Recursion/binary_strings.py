# Iterative implementation - Print all binary strings of length n
def binarystrings(n):
    result = ["0","1"]
    for iter in range(2,n+1):
        newresult = []
        for s in result:
            newresult.append(s+"0")
            newresult.append(s+"1")
        result = newresult
    return result

b_result = binarystrings(4)
print(b_result)