# Generate All Possible Expressions That Evaluate To The Given Target Value
# Given a string s that consists of digits (“0”..”9”) and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.
# When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: “join” or “*” or “+”. 
# For example, by inserting different operators between the two characters of string “12” we can get either 12 (1 joined with 2) or 2 (1*2) or 3 (1+2).
# Other operators such as “-” or “÷” are NOT supported.
# Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.
# Precedence of the operators is conventional: “join” has the highest precedence, “*” – medium and “+” has the lowest precedence. For example, 1+2*34=(1+(2*(34)))=1+68=69.
# You have to return ALL expressions that can be built from string s and evaluate to the target.

# Input:
# s="222", target=24.

# Output:
# ["22+2", "2+22"] and ["2+22", "22+2"] are both correct outputs.
# 22+2=24: we inserted the “join” operator between the first two characters and the “+” operator between the last two characters of s.
# 2+22=24: we inserted the “+” operator between the first two characters and the “join” operator between the last two characters of s.


# Input: s="1234", target=11.
# Output: ["1+2*3+4"]

# Input:
# s="99", target=1.
# Output:
# []

# Constraints:

# 1 <= length of s <= 13
# 0 <= target < 10^13

# Complete the function below.

def generate_all_expressions(s, target):
    res = []
    def generate(S, slate, i, evaluated, prev):
        if not S:
            if evaluated == target:
                res.append(slate[:])
            return
        
        for index in range(1,len(S)+1):
            current = S[:index]
            curr_int = int(current)
            if i == 0:
                generate(S[index:], slate + current, i+1, curr_int, curr_int)
            else:
                # we need to give precedence to multiplication, e.g. if we have a+b*c,
                # we really want a+(b*c), not (a+b)*c.
                # For prev addition; ev = (a + b), prev = b, curr = c; so current calculation
                #   (ev - prev) + (prev * curr) will give us (a + b - b) + (b * c) = a + (b * c)
                # For prev multiplication; ev = (a * b), prev = a * b, curr = c; so current calculation
                #   (ev - prev) + (prev * curr) will give us (a * b - a * b) + (a * b * c) = a * b * c
                generate(S[index:], slate + '+' + current , i+1, evaluated + curr_int, curr_int)
                generate(S[index:], slate + '*' + current, i+1, (evaluated - prev) + (prev * curr_int), prev*curr_int)
    if s:           
        generate(s, '',0,0,0)
        return res
    return []