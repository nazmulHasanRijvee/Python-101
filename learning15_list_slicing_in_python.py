"""list slicing (like string)"""
# Just like string slicing list can be sliced too in Python using
# [ : ]. Always count +1 cause it stops before that like for loop
var_list = [1, 2, 3, 4, 5]
print(var_list[2: 5]) # [3, 4, 5]


# Not specifying the start, it automatically starts from 0 index
# and prints till end. Also, not specifying the end, finishes
# printing till the last element after start index
print(var_list[:4]) # [1, 2, 3, 4]
print(var_list[2:]) # [3, 4, 5]


# Negative indexing. It starts from the -1 which is the last element,
# increases negative value as it goes to first element. By default,
# it prints till the last element
#  1  2  3  4  5 -> elements
# -5 -4 -3 -2 -1 -> index
print(var_list[-4:]) # [2, 3, 4, 5]


# In here [ : : 2] is step it means after printing an element next one
# is skipped (counts as 1), 3 means skipping by 2
print(var_list[:5:2]) # [1, 3, 5]