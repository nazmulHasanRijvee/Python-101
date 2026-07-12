"""Assigning and Swapping Values in Python"""
# Multiple variables can be assigned using coma but
# the values need to ordered like variables
var1, var2 = 21, 'Hi'
print(var2, var1) # Hi 21

# Swapping, just changing the positions in coma, we can swap values
# between variables

var1 = 'Hello'
var2 = 32
var1, var2 = var2, var1
print(var1, var2) # 32 Hello


"""Operators in Python"""
# Math -> We have +, -, *, /, ** (for to the power x^n), // (for only
# displaying answer as integer after division), % (for remainder)
a = 20
b = 4

print(a + b) # 24
print(a - b) # 16
print(a * b) # 80
print(a / b) # 5.0 (float)
print(a // b) # 5 (int)
print(a % b) # 0 (remainder)
print(2 ** b) # 16


"""Assigning"""
# We have =, += (addition with self), -= (subtraction with self)
a += 1
print(a) # 21
b -= 1
print(b) # 3


"""Comparison"""
# we have == (equal to), !=(not equal to), > (greater than), < (lesser than)
# , <= (greater than or equal), >= (less than or equal)
# Returns a bool always
print(a == b) # False
print(a != b) # True
print(a < b) # False
print(a <= b) # False
print(a > b) # True
print(a >= b) # True



"""Logic"""
# We have and (both condition needs to be true), or (one condition needs to be true),
# not (if condition true returns false), is (do they have the same data or same object in memory),
# in (detects if item is present in string or list)
print(a == 21 and b == 3) # True
print(a != 21 or b != 3) # False
print(not a == 20) # True
print(a is b) # False (== alternative)

var_ch = 'Hi'
print(var_ch in 'Hi, I am Nazmul') # True


"""& and | bits"""
# 101  101
# 100  100
# ---  ---
# 101  100
print(5 & 4) # 4
print(5 | 4) # 5
