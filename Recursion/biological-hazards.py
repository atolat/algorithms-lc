# I/P
# m = [1,2,3]
# n = [3,3,1]

# [1],[2],[3],[1,2]

def findUniqueSubsets(m,n):
    def helper(S, i, slate):
        # Back tracking case, return when you see items that are in the invalid list
        for item in invalid:
            if set(item).issubset(set(slate)):
                return

        # Base Case
        if len(S) == i:
            if len(slate) != 0:
                results.append(slate[:])
            return
        # Inner Nodes
        # Inclusion
        slate.append(S[i])
        helper(S, i+1, slate)
        slate.pop()
    
        # Exclusion
        helper(S, i+1, slate)

    # Join Arrays
    mapping = {}
    invalid = []

    # Prepare a map of invalid combinations
    for i in range(len(m)):
        mapping[m[i]] = n[i]
    
    # Append key value pairs from map to a list
    for x in mapping.items():
        invalid.append(list(x))

    # Join the two input arrays, sort and remove duplicates
    arr = m + n
    arr.sort()
    arr = list(set(arr))

    # Global array for results
    results = []

    # Call helper with empty slate
    helper(arr, 0, [])

    return results


print(findUniqueSubsets([1,2,3],[3,3,1]))