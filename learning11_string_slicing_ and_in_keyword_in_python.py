"""in keyword in string"""

# Detects if character or string is present in a string
var_str4 = "Hi,"
var_str5 = "Hi, Python"
print(var_str4 in var_str5)  # True
print("H" in var_str4)  # True


"""String Slicing in Python"""
# String stores each character as an element like an array
# so we can slice it using [ : ] indexing. Always count +1
# cause it stops before that like for loop.
var_slice1 = "Hello World"
print(var_slice1[6:11])

# Not specifying the start, it automatically starts from 0 index
# and prints till end. Also, not specifying the end, finishes
# printing till the last element after start index
print(var_slice1[:8])
print(var_slice1[2:])

# Negative indexing. It starts from the -1 which is the last element,
# increases negative value as it goes to first element. By default,
# it prints till the last element
#  W  a  t  e  r
# -5 -4 -3 -2 -1
print(var_slice1[-4:])  # mark

# In here [ : : 2] is step it means after printing an element next one
# is skipped (counts as 1), 3 means skipping by 2
var_slice2 = "Amazing"
print(var_slice2[:7:2])  # Aaig
