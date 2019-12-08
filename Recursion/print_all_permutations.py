def printpermutations(slate,n):
    if n == 0:
        print(slate)
    else:
        for i in range(0,10):
            printpermutations(slate+str(i), n-1)

printpermutations("",10)