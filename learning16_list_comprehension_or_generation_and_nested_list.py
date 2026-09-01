"""list comprehension or generation"""

# This copies the var_list1 to var_new. Beginning is the stored items;
# middle is the loop and condition is written at last
var_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var_new = [i for i in var_list1]
print(var_new)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""With condition (if)"""
# Stores and prints even numbers from var_list2. First are stored
# elements, middle is loop and last is condition
var_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var_new2 = [i for i in var_list2 if i % 2 == 0]
print(var_new2)  # [2, 4, 6, 8, 10]


"""Another Example"""
# Stores the double of every element in var_list3
var_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var_new3 = [i * 2 for i in var_list3]
print(var_new3)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


"""Using inverse condition (if not)"""
# Here, if not skips the numbers in  10 to 20, 40 to 50, 70 to 80
var_list4 = [
    i for i in range(1, 101) if not (10 <= i <= 20 or 40 <= i <= 50 or 70 <= i <= 80)
]
print(var_list4)
# NOTE: [ i for ... if not (condition or condition)] this syntax might come in handy


"""Nested list"""
# We can define a nested list just by writing another
# list as the element of the first list. We can repeat
# this process to further nest it (Remember, it's not optimal
# and not efficient use dictionary or class and object)
var_list5 = [5, [10, 6, [3, 6], 8], 9]
print(var_list5)
# We can access the values of elements of nested list using indexing
# like double [][] square parentheses. When we get to the element where
# second sub-list is stored, we access it using a second [] and so on
var_list6 = [5, [10, 6, [3, 6], 8], 9]
print(var_list6[1])  # [10, 6, [3, 6], 8]
# noinspection PyUnresolvedReferences
print(var_list6[1][2])  # [3, 6]
# noinspection PyUnresolvedReferences
print(var_list6[1][2][0])  # 3
# noinspection PyUnresolvedReferences
print(var_list6[1][2][1])  # 6
