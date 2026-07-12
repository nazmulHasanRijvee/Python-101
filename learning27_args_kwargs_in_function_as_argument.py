"""*args and **kwargs arguments in function"""
# - *args -> collects extra positional arguments or parameters
# - **kwargs -> collects extra keyword (named) arguments or parameters


"""*args"""
# Normally, a function expects a fixed number of arguments but
# *args lets a function accept any number of positional arguments
# args is a tuple
def add(*args):
    total = 0

    for num in args: # iterate like a list
        total += num

    return total

print(add(1,2)) # 3
print(add(1,2,3)) # 6
print(add(1,2,3,4)) # 10


"""**kwargs"""
# Used when we need to pass any number of named arguments
# kwargs is a dictionary.
def person(**kwargs):

    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])

person(name="Nazmul", age= 22)
# Output:
# {
#  'name': 'Nazmul',
#  'age': 22
# }
# Nazmul
# 22


"""Using Both Together"""
def example(*args, **kwargs):

    print(args)
    print(kwargs)

example(1, 2, 3, name="Nazmul", age=22)
# Output:
# (1, 2, 3)
# {
#  'name': 'Nazmul',
#  'age': 22
# }


"""Argument Unpacking"""
# The * and ** operators are also used when calling functions
# * operator unpacks a list/tuple.
# Like add(*numbers) equivalent to add(10, 20)
numbers = [10, 20]

def add(a, b):
    print(a + b)

add(*numbers) # 30

# ** operator unpacks a dictionary
# equivalent to intro(name="Nazmul", age= 22)
person = {
    "name": "Nazmul",
    "age": 22
}

def intro(name, age):
    print(name, age)

intro(**person)