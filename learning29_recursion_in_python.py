"""Recursion"""

# Syntax. recursion() is a function that calls itself. In here,
# in return recursion is returning a value and recalls itself
# with that value
# def recursion():
#     return recursion()


# This recursion calculates variable if condition fails it recalls
# itself and returns the n * n – 1 value and recalls with
# the n - 1 value.
def factorial(n):

    # Base case responsible for stopping the recursion
    if n == 1:
        return n

    # Recursive case for calling the function
    return n * factorial(n - 1)


if __name__ == "__main__":

    num = 4

    if num < 0:
        print("Invalid")

    else:
        print(factorial(num))  # 24
