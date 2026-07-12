"""list is an array of elements stored in square brackets"""

"""list() method (or cast)"""
# It can be used to convert or declare a list
var_string = '123'
var_converted_list = list(var_string) # converted string to list -> ['1', '2', '3']
var_list9 = list() # Defined a list
print(type(var_converted_list), var_list9)

# Elements can be accessed using index
var_list1= [7 , 9, 'Nazmul']
print(var_list1[0], var_list1[2]) # 7 Nazmul


""".sort() method"""
# Organizes the elements in ascending order
var_list1 = [1, 8, 7, 2, 21, 15]
var_list1.sort()
print(var_list1) # [1, 2, 7, 8, 15, 21]


""".reverse() method"""
# reverses the elements organized order form ascending
# to descend.
var_list2 = [1, 8, 7, 2, 21, 15]
var_list2.reverse()
print(var_list2) # [21, 15, 8, 7, 2, 1]


""".append() method"""
# adds an element at the end of the list
var_list2.append(8)
print(var_list2) # [1, 8, 7, 2, 21, 15, 8]


""".insert() method"""
# will add  a new element (8) at 3 index and
# the element (8) present there will be moved to 4 index
var_list3 = [1, 8, 7, 2, 21, 15]
var_list3.insert(3, 8)
print(var_list3) # [1, 2, 7, 8, 8, 21, 15]


""".pop() method"""
# pops the last element (if not specified) or deletes the
# valued stored at 2 specified index and can store it in
# a variable
var_list4 = [1, 8, 7, 2, 21, 15]
var_list4.pop()
popped_value = var_list4.pop()
print(var_list4, popped_value) # [ 1, 8, 2, 21, 15]  7


""".remove() method"""
# directly deletes the element (finds it in the list O(n))
# which is written in () parentheses
var_list5 = [1, 8, 7, 2, 21, 15]
var_list5.remove(21)
print(var_list5) # [1, 8, 7, 2, 15]


""".count() method"""
# counts how many times an element is repeating
var_list6 = [1, 8, 7, 2, 21, 15]
var1 = var_list6.count(1)
print(var1) # 2


""".index() method"""
# finds the index number of 5, where 5 is stored. If the value
# or element is not present in the list it will throw run-time error
var_list7 = [1, 1, 2, 5]
var2 = var_list7.index(5)
print(var2) # 3


""".join() method"""
# list() function or method can convert string to list,
# and we can convert that list back to string using ' '.join() method
var_str = 'String'
var_list8 = list(var_str)
print(var_list8) # ['S', 't', 'r', 'i', 'n', 'g']
var_str = ''.join(var_list8)
print(var_str) # String


"""for loop with list"""
# Here for-loop automatically iterates over the list from
# left to right. In the for-loop every element or item in the
# list is given in each iteration (ch)
var_list9 = ['a', 'b', 'c', 'd', 'e']
for i in var_list9:
    print(i)


""".__contains__() method"""
# checks if the specified parameter is present in the lists elements
# If it's present returns True if not False
my_list = ['a', 'b', 'c', 'd']
result = my_list.__contains__('d')
print(result) # True
result = my_list.__contains__('e')
print(result) # False


""".sum() method"""
# Takes a list and calculates the sum of all items and returns it.
# The second parameter is start which is by default 0, the number
# specified here will be added too with the total value
nums = [1, 2, 3, 4, 5]
print(sum(nums)) # 15
print(sum(nums, 3)) # 15 + 3 = 18


"""max() and min() methods"""
# takes a list and returns the largest item in the list
nums2 = [5, 3, 1, 8, 4]
print(max(nums2)) # 8
print(min(nums2)) # 1


"""list unpacking"""
# * unpacks list in the serial order. list() solves pointing
# to same memory address problem (DSA)
def total(a, b, c):
    return a + b + c
var_list10 = [2, 3, 5]
print(total(*var_list10)) # 10
copied_list = list(var_list10)
print(copied_list)