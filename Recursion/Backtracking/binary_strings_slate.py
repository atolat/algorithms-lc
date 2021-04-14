def binarystrings(slate, i):
    # Base Case
    if i == n:
        print(slate)
        return
    
    slate.append(0)
    binarystrings(slate, i + 1)
    slate.pop()
    
    slate.append(1)
    binarystrings(slate, i + 1)
    slate.pop()
    
n = 5
binarystrings([], 0)