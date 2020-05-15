def towers_of_hanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk from "+ str(src) + " to " + str(dest))
        results.append((src, dest))
    else:
        towers_of_hanoi(n-1, src, aux, dest)
        print("Move disk from "+ str(src) + " to " + str(dest))
        results.append((src, dest))
        towers_of_hanoi(n-1, aux, dest, src)

results = []
towers_of_hanoi(4, 1, 3, 2)
print(results)