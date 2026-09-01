"""Lambda or Anonymous Function"""

# A lambda function is a small, anonymous (unnamed) function that
# can have any number of parentheses but only one expression
# - lambda -> Keyword to create the anonymous function
# - parameters -> inputs to the function
# - expression -> The value that is automatically returned
# Syntax:
# lambda parameters : expression


"""Basic Usage"""


# Normal function
def square(x):

    return x * x


print(square(5))  # 25

# Lambda function, both do the same thing
lambda_square = lambda x: x * x

print(lambda_square(5))  # 25


"""Multiple Lambda Usage"""
# Just using coma, we can pass multiple parameters in the lambda
# function
add = lambda a, b: a + b
print(add(10, 20))  # 30


"""Using Lambda with map() Function"""


# This is where lambda is used most often. Instead of writing:
def double(x):

    return x * 2


numbers = [1, 2, 3, 4]
result = list(map(double, numbers))
print(result)  # [2, 4, 6, 8]

# we can write it in one line using lambda
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [2, 4, 6, 8]


"""Using Lambda with sorted() function"""
# Suppose we have a list of tuples
students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
# Sort by marks. Here, lambda student : student[1] means "Use
# the second element (marks) as the sorting key"
students = sorted(students, key=lambda student: student[1])
print(students)  # [ ('Bob', 75), ('Charlie', 85), ('Alice', 90)]


"""Use Cases"""
# Use a lambda when:
# - The function is short and simple
# - We only need it once
# - We're passing a function to another function like map(), filter(), reduce()
# or sorted()
