"""set and its properties in python"""

# It is an array with curly brackets {}. Where no element can
# repeat in it (no duplicates) and elements cannot be accessed
# index
s = {1, 2, "Harry"}
print(s)  # {1, 2, 'Harry'}


"""set() method (or cast)"""
# can be used to declare a set variable or convert something to
# set just by passing it as the parameter
var_set1 = set()
var_list = [1, 2, 3]
var_set2 = set(var_list)
print(var_set1, var_set2)


""".add() method"""
# adds elements in the set
var_set3 = set()
var_set3.add(1)
var_set3.add(2)
var_set3.add(2)
print(var_set3)  # {1, 2}


""".clear() method"""
# clears the set and empties it. All elements are deleted
var_set4 = {1, 2, "Harry"}
var_set4.clear()
print(var_set4)  # set()


""".union() method"""
# returns all elements from both sets. if an element is
# repeated it will not be added (Duplicate is not allowed)
var_set5 = {1, 8, 2, 3}
var_set5 = var_set5.union({8, 11})
print(var_set5)  # {1, 2, 3, 8, 11}


""".intersection() method"""
# returns elements that are common or present in both sets
var_set6 = {1, 8, 2, 3}
var_set6 = var_set6.intersection({8, 11})
print(var_set6)  # {8}


"""for loop with set"""
# for-loop automatically iterates over the set from left to right
# and in each iterating every element of the set is given as "i"
var_set7 = {1, 8, 2, 3}
for i in var_set7:
    print(i)


"""Subset & Superset"""
# a set A is a subset of set B if every element of A is also in B
# A ⊆ B. We can check it using .issubset() method
A = {1, 2}
B = {1, 2, 3}
print(A.issubset(B))  # True

# a set B is a superset of A if it contains all elements of A
# B ⊇ A
print(A.issuperset(B))  # True

# SHORTCUT. Instead of methods we can use operators for finding
# subset/superset using <= / >=
print(A <= B)  # True (subset)
print(A >= B)  # True (superset)
