def rec_mult(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = rec_mult(a,c)
        z1 = rec_mult(a,d)
        z2 = rec_mult(b,c)
        z3 = rec_mult(b,d)

        return (z0 * 10**(2*m2)) + (10**m2 * (z1 + z2)) + z3