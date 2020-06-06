## Tips & Tricks

#### Flip Bits
To flip all bits, XOR with 1<<(size of num)  
To flip certain bits - use a bitmask and XOR   
Flip first and last bit in a 5 bit number  
```python
num ^ (1 << 5 | 1)
```

#### Get and Set Bits
```python
def getBit(i, num):
    return num >> i & 1

def setBit(i, val, num):
    if val == 1:
        return (1 << i) | n
    else:
        return ~(1 << i) & n
```

#### Swap Bits
```python
def swapBits(x, i, j):
    # Extract i-th and j-th bit and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 >> i) | (i >> j)
        x ^= bit_mask
    return x
```

https://catonmat.net/low-level-bit-hacks
