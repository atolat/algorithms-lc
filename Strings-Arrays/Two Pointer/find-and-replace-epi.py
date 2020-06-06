# Given a string s and it's size:
# Replace each 'a' by 'dd'
# Delete each entry containing 'b'
# Return the final size
# *Assume there is extra space in the list to hold final string 
import pytest
from typing import List

def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    # First pass - Remove b's
    write_index = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count += 1
            
    # Second Pass - Backwards, replace a with dd
    curr_index = write_index - 1 # End of array with b's removed
    write_index = write_index + a_count - 1 # End of array after adding the d's
    final_size = write_index + 1
    while curr_index >= 0:
        if s[curr_index] == 'a': # Write 'dd'
            s[write_index - 1:write_index + 1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[curr_index]
            write_index -= 1
        curr_index -= 1
        
    return final_size

def test_replace_and_remove():
    s = ["d", "a", "d", "a", "b", "d", "a", "d", "a", "c", "d", "d", "c", "d", "a", "d", "d", "d", "b", "c", "d", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    res = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "c", "d", "d", "c", "d", "d", "d", "d", "d", "d", "c", "d"]
    size = 21
    assert len(replace_and_remove(size, s)) == len(res)