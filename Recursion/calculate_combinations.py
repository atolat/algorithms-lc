def c(n,k):
    # Base Case
    if n <= 1 or k == 0 or k == n:
        return 1
    else:
        return c(n-1,k) + c(n-1,k-1) # Pascal's Triangle

print(c(4,3))