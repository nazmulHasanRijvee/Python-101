"""function in python"""

# function() calls the function and runs it. def keyword is used
# to define functions
# def function(parameters):
#       code
# function()


# Here, total is defined by def and when called prints 5 + 6 = 11
def total():

    print(5 + 6)


total()  # 11


"""defining parameters in function"""


# var1 and var2 is written in total2() as parameters. return is used
# to return one or multiple values that can be stored and printed
# on in python functions
# By default, python parameters are positional
def total2(var1, var2):

    return var1 + var2


var3 = total2(1, 2)
print(var3)  # 30


"""returning multiple values"""


# return keyword can return multiple value when stored to a single
# variable as a tuple but if multiple variables using coma then stores
# individually
def math(var1, var2):

    return var1 + var2, var1 - var2


var4 = math(20, 10)
print(var4)  # (30, 10)
var4, var5 = math(15, 10)
print(var4, var5)  # 25 5


"""named parameters in function"""


# By default, python supports positional parameters.
# Just by typing parameter= it becomes named parameters
# and position order doesn't order
def intro(name, age):

    print(f"Name: {name}")
    print(f"Age: {age}")


intro(age=20, name="Nazmul")


"""required named parameters in function"""


# Just by adding * at the very front of the parameters. They
# become required and named or keyword only (parameter=) parameters.
# And positioned parameters order doesn't work anymore
def intro2(*, name, age):

    print(f"Name: {name}")
    print(f"Age: {age}")


intro2(name="Nazmul", age=20)


"""Optional parameters, arguments for default values and specifying type"""


# argument is a parameter that is used to set a default string or data type
# if parameter is not assigned. If it is assigned the default, one
# will not show
# and by adding argument that parameter becomes optional
def greet(name="Stranger"):

    print("Hello, " + name + "!")


# Optional
greet()  # Hello, Stranger!
greet("Nazmul")  # Hello, Nazmul!


"""required + optional (argument) parameters in function"""


def intro3(*, name, city="Unknown"):

    print(f"Name: {name}")
    print(f"City: {city}")


intro3(name="Nazmul")
intro3(name="Nazmul", city="Dhaka")


"""main() method in Python"""
# By writing  if __name__ == "__main__"
# # we can create a main function like C/C++


def main():
    x, y = 20 + 10, 20 - 10
    print(x, y)  # 30, 10


if __name__ == "__main__":
    main()
