"""Constants, Placeholder variables and Rounding numbers in python"""

"""constants in Python"""
# constant is a variable which is assigned in compile-time and whose
# value isn't supposed to change after its assigned

# Python has no built-in "const" keyword like Dart
# Instead Python programmers follow a naming convention. Writing
# variable names in ALL-CAPS tells other developers "Treat it as a const"
PI = 3.14159
MAX_USERS = 100
API_URL = "https://example.com"
print(PI, MAX_USERS, API_URL)

# But python won't stop us from modifying them
PI = 5
print(PI)


"""Placeholder Variables"""
# Sometimes we need a variable, but we don't care about its value
# Python uses the underscore (_) as a placeholder
# Example, Ignoring a value
name, _, age = ("Nazmul", "Bangladesh", 22)
print(name, age)

# Example-2, Loop variable not used. "i" is not needed
for _ in range(5):
    print("Hello")

# Example-3, Throwing away a value. Everything in the middle is ignored
first, *_, last = [10, 20, 30, 30]
print(first, last)  # 10 30


"""Rounding Numbers"""
# round() function
x = 3.7
print(round(x))  # 4

# Specify decimal places in round(..., 2)
pi = 3.145926
print(round(pi, 2))  # 3.15

# math.ceil() always rounds up
import math

print(math.ceil(3.1))  # 4

# math.floor() always rounds down
print(math.floor(3.1))  # 3

# int() but its not rounding, (Be careful)
# it simply removes the decimal part (truncates)
print(int(3.9))  # 3


"""Comparison of Round methods"""
#   Function        3.2     3.8
#   round()         3       4
#   math.floow()    3       3
#   math.ceil()     4       4
#   int()           3       3
