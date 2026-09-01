"""Callback Methods in Python"""

# Functions are first-class objects in Python (No need for special
# type like Dart's VoidCallback)
# This means we can:
# - Store a function in a variable
# - Pass a function as an argument
# - Return a function from another function

"""Python Callback"""


# Here greet() function takes the done function itself as a
# parameter and can be called in the greet() function
def greet(callback):
    print("Hello")
    callback()


def done():
    print("Done")


greet(callback=done)  # passed as a callback
# Output:
#   Hello
#   Done


"""Using lambda function as a Callback"""


# Instead of defining a separate function
def greet(callback):
    print("Hello")
    callback()


# Do this (very similar to passing anonymous () {} function in Dart)
greet(callback=lambda: print("Done"))
# Output:
#   Hello
#   Done


"""Passing Parameters to a Callback"""


def calculate(a, b, operation):
    return operation(a, b)


result = calculate(10, 20, lambda a, b: a + b)
print(result)  # 30


"""Type Hinting (Optional)"""
# Python doesn't require types, but we can document callbacks
# using the typing module
# Callable[[], None] means:
# - [] -> takes no arguments
# - None -> returns nothing
# This is the closest equivalent to Dart's VoidCallback callback
from typing import Callable


def greet(callback: Callable[[], None]):
    print("Hello")
    callback()


greet(callback=lambda: print("Done"))
# Output:
#   Hello
#   Done


# Another Example. Here:
# - Takes two int arguments
# - Returns an int
def calculate(var1, var2, operation: Callable[[int, int], int]):
    return operation(var1, var2)


result = calculate(var1=10, var2=20, operation=lambda a, b: a + b)
print(result)  # 30
