"""Python automatically identifies the data"""
# and determines the data type. If we don't want to assign a value for now,
# we can just declare it with None to assign value later
# In Python double data type is float

var_int = 2 # identifies integer
var_float = 2.5	# identifies float/double
var_string = 'Hello'	# identifies string
var_bool = True	# identifies bool

var_none = None	# identifies nothing or none
print(var_none)
var_none = True
print(var_none)

"""type() function"""
# type() method is used to find out the data type of the variable
print(type(var_float)) # <class 'float'>
print(type(var_bool)) # <class 'bool'>
