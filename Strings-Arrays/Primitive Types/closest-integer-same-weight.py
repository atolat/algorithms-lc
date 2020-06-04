def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    num_unsigned_bits = 64
    for i in range(num_unsigned_bits-1):
        # Check if i th bit and i+1 th bit differ
        if (x >> i & 1) != (x >> i+1 & 1):
            # Swap i and i+1
            x ^= (1 << i)|(1 << (i+1))
            return x
    raise ValueError('All bits are 0 or 1') 