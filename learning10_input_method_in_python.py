"""input() function"""
# input() function is used to take inputs. Takes a string as a parameter
# to display while taking input
# # NOTE, always remember that
# python takes input as a string. If we type 31, it will be a string '31'
# In order to take an integer input use data type convertion int(). This is called cast
var1 = input("Type: ")
var2 = int(input("Type: "))
print(type(var1), type(var2)) # <class 'str'> <class 'int'>
