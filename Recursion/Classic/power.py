
# Power
# The problem statement is straight forward. Given a base ‘a’ and an exponent ‘b’. 
# Your task is to find a^b. The value could be large enough. So, calculate a^b % 1000000007.
#  Complete the calculate_power function below.
#  @param a: base
#  @param b: exponent
#
def calculate_power(a,b):
    MOD = 1000000007
    # Write your code here
    if b == 0:
        return 1
        
    elif b < 0:
        return calculate_power(a,-b)
        
    v = calculate_power(a, b//2) % MOD
    
    if b % 2 == 0:
        return v*v % MOD
    else:
        return v*v*a % MOD
