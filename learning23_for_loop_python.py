"""for loop"""

# pass keyword does not show error
for i in range(5):
    pass

# loop starts from 0 by default (if not specified)
# and ends, ending number - 1
# range() method determines the loops range for iterating
for i in range(5):
    print(i)


"""Step skipping"""
# range(start, end, skip) is the step skipping. (..., ..., 2)
# skips by one. Meaning 1 to 3 instead of 2
for i in range(1, 20, 2):
    print(i)


"""continue"""
# skips iteration and does not send the 'i' value to code. It's
# like steps but condition is implemented
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9


"""break"""
# stops the loop when condition is met and throws the value of 'i'
# outside
for i in range(1, 11):
    if i == 5:
        break
    print(i)  # 1, 2, 3, 4


"""Loop else"""
# When 'i' range end mean when it stops iterating. It prints done.
# this only works in python
for i in range(5):
    print(i)
else:
    print("Done")


"""for loop with string"""
# Here for-loop automatically iterates over the string from
# left to right. In the for-loop every character in string
# is given in each iteration (ch)
var_str = "Hello!"
for ch in var_str:
    print(ch)


"""for loop with list"""
# Here for-loop automatically iterates over the list from
# left to right. In the for-loop every element or item in the
# list is given in each iteration (ch)
var_list9 = ["a", "b", "c", "d", "e"]
for i in var_list9:
    print(i)


"""loop with dictionary"""
# 'i' stores each dictionary keys and prints them in a new line
stu_info = {"name": "Nazmul", "batch": 47, "dept": "CSE", "passing_year": 2027}
for i in stu_info:
    print(i)

# Here, "i" stores keys and "j" stores values in each iteration.
# They print keys and values in table like manner
for i, j in stu_info.items():
    print(i, "\t", j)
