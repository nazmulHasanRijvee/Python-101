"""Converting Data types in Python"""

# Use str(), int(), float(), set(), list(), dic() methods
# for converting to that data type or define (initialize)

var1 = "31"
var2 = 2
var3 = "2.5"


converted1 = int(var1)
converted2 = str(var2)
converted3 = float(var3)

print(type(converted1))  # <class 'int'>
print(type(converted2))  # <class 'str'>
print(type(converted3))  # <class 'float'>

# set(), list(), dict()
set1 = set(var1)
list1 = list(var1)
dict1 = dict()

print(set1)  # {'3', '1'}
print(list1)  # ['3', '1']
print(dict1)  # {}
