def rabin_karp(t, s):
    # if length of substring > len string, return
    if len(s) > len(t):
        return -1
    
    # Pick a base = # of symbols
    base = 26
    
    # Hash is computed by continually multiplying base with hash of previous char
    h_lambda = lambda h, c: h*base + ord(c)
    
    t_hash = reduce(h_lambda, t[:len(s)], 0)
    s_hash = reduce(h_lambda, s, 0)
    
    # base ^ |s - 1|
    power = base ** max(len(s) - 1, 0)
    
    for i in range(len(s), len(t)):
        # Check if two substrings are actually equal to protect against collisions
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)
        
        # Compute rolling hash
        t_hash -= ord(t[i-len(s)]) * power
        t_hash = t_hash * base + ord(t[i])
        
    # Try to match the pattern with last substring 
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    
    # No match found
    return -1

# Time Complexity
# O(m+n) -> Average case, for a good hash function
# O(mn) -> Worst case, multiple spurious hits/collisions