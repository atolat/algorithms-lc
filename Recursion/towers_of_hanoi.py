def towers_of_hanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk from "+ str(src) + " to " + str(dest))
    else:
        towers_of_hanoi(n-1, src, aux, dest)
        print("Move disk from "+ str(src) + " to " + str(dest))
        towers_of_hanoi(n-1, aux, dest, src)

towers_of_hanoi(7, 1, 3, 2)