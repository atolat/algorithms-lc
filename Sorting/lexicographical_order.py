# Lexicographical Order
# Given a bunch of key-value pairs, for each unique key find 1) the number of values and 2) the lexicographically greatest value.

# Example One
# Input is an array of strings, each with a key and a value separated by a space:

# ["key1 abcd",
#  "key2 zzz",
#  "key1 hello",
#  "key3 world",
#  "key1 hello"]

# Output is an array of strings with unique keys followed by a colon, the total number of values, a comma, and the lexicographically greatest of the values associated with that key in the input:
# ["key1:3,hello",
#  "key2:1,zzz",
#  "key3:1,world"]

# The order or strings in the output is insignificant; these same strings in a different order are also a correct output.

# Notes
# Order of strings in the output does not matter.

#
# Complete the solve function below.
#
from collections import defaultdict, namedtuple
from typing import NamedTuple


class Entry:
    val: str = ''
    count: int = 0


def solve(arr):
    #
    # Write your code here.
    #
    hmap = defaultdict(lambda: Entry())

    op = []
    for x in arr:
        key = x.split(' ')[0]
        value = x.split(' ')[1]
        if key in hmap:
            if value > hmap[key].val:
                hmap[key].val = value
                hmap[key].count += 1
            else:
                hmap[key].count += 1
        else:
            hmap[key].val = value
            hmap[key].count = 1

    for k, v in hmap.items():
        op.append(k + ':' + str(v.count) + ',' + v.val)

    return op
