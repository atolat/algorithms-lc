def print_perm_no_rep(inputs, slate):
    if len(inputs) == 0:
        print(slate)
    else:
        for i in range(len(inputs)):
            print_perm_no_rep(inputs[:i] + inputs[i+1:], slate + str(inputs[i]))

print_perm_no_rep(["a","b","c"], "")