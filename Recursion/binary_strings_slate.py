def binarystrings(slate, n):
    if n == 0:
        print(slate)
    else:
        binarystrings(slate + "0", n-1)
        binarystrings(slate + "1", n-1)

binarystrings("", 4)