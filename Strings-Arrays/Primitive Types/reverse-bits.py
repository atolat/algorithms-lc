# 190. Reverse Bits
# Easy

# Mask & Shift

class Solution:
    def reverseBits(self, n):
        res, mask = 0, 1
        for _ in range(32):
            res <<= 1
            res |= n & mask
            n >>= 1
        return res

# EPI - Caching, 64 bit
# https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python_solutions/reverse_bits.py
def reverse_bits(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    PRECOMPUTED_REVERSE = [] # => Array cache with precomputed reverse of 16 bit integers
    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size)
            | PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] <<
            (2 * mask_size) |
            PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << mask_size
            | PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask])

