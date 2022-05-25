# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

# Example 1:

# Input: x = 4
# Output: 2
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.



import math  

def mySqrt(x: int) -> int:    
    # Find MSB(Most significant Bit) of N
    msb = int(math.log(x, 2))

    # (a = 2 ^ msb)
    a = 1 << msb
    result = 0
    while a != 0:
        # Check whether the current value of 'a' can be added or not
        if (result + a) * (result + a) <= x :
            result += a
        # (a = a / 2)
        a >>= 1

    # Return the result
    return result


print(mySqrt(36))