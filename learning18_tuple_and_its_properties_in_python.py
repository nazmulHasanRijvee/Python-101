"""tuple and it's properties"""
# Tuple is a constant array which can't be added with elements
# or removed. It is defined ore enclosed by round brackets/parentheses
# ()
t = (1, 2, 3)
print(t) # (1, 2, 3)
print(t[0]) # 1


"""tuple() method (or cast)"""
# can be used to declare a tuple variable or convert to tuple,
# from a list or set
var_tuple1 = tuple()
var_list = [1, 2, 2, 3]
var_tuple2 = tuple(var_list)
print(var_tuple2) # (1, 2, 2, 3)


""".count() method"""
# counts how many times an element is repeating in the tuple
var_tuple3 = (1, 7, 2, 1)
var_count = var_tuple3.count(1)
print(var_count) # 2


""".index() method"""
# finds the index value of element 2. if the value or element is
# not present in the list, it will throw run-time error
var_tuple4 = (1, 7, 2, 1)
var_index = var_tuple4.index(2)
print(var_index) # 2
