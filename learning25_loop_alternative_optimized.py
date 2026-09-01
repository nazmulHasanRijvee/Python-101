"""map() method is the for loop alternative like Dart and optimized"""

# It's a built-in python function that applies a function to
# every element of an iterable (like a list or list of dictionaries,
# tuple or set). It takes two parameters:
# - function -> What we want to do to each item of the list
# - iterable -> The list of collection we want to process
# map(function, iterable)


# Here, map() method iterates over each element of the list and
# squares the element. And returns a map object (an iterator),
# not a list. Convert it to a list using list() method
def square(x):
    return x * x


numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(result)  # <map object at 0x000001A82ECEA180>
result = list(map(square, numbers))
print(result)  # [1, 4, 9, 16]


"""Using lambda function with map()"""
# Most of the time, people don't create a separate function.
# Instead, uses a lambda function.
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * x, numbers))
print(result)  # [1, 4, 9, 16]


# Here, lambda x: x * x means
def square(x):
    return x * x


"""Mapping Strings"""
# str.upper (.upper())is a function that is applied to every string.
names = ["alice", "bob", "charlie"]
result = list(map(str.upper, names))
print(result)  # ['ALICE', 'BOB', 'CHARLIE']


"""Multiple Iterables (list)"""
# map() can process more than one iterable or list. Python takes:
# 1 + 4
# 2 + 5
# 3 + 6
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # [5, 7, 9]


"""Best Practices:"""
# •	Use map() when we're applying the same transformation to every element.
# •	Use lambda function for short, simple transformations.
# •	If the transformation is complex, define a regular function with def.
# •	Remember that map() returns an iterator, so wrap it with list() if we need a list.
