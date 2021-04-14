def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)



def fib_memoization(n):
    fib_cache = [-1]*51
    if n == 0 or n == 1:
        return 1
    else:
        if fib_cache[n] != -1:
            return fib_cache[n]
        else:
            fib_cache[n] = fib_memoization(n-1) + fib_memoization(n-2)
            return fib_cache[n]

def fib_additive(n,b1,b2):
    if n == 0 or n == 1:
        return b1
    else:
        return fib_additive(n-1, b2, b1+b2)


print(fib(0)) 
print(fib_memoization(1))
print(fib_additive(50,1,1))

