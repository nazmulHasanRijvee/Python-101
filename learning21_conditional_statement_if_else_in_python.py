"""Conditional Expressions if, elif and else"""

# if condition is true that block executes. If and elif fails
# then else executes
var_num = 7

if var_num >= 10:
    print("Greater than  or equal to 10")
elif var_num >= 5:
    print("Greater than  or equal to 5")
else:
    print("less than 5")


# Ladder of elif will stop if an elif or if condition is met.
# else only executes when all if and elif fails
var_fruit = "apple"
if var_fruit == "banana":
    print("It's a banana")
elif var_fruit == "orange":
    print("It's a orange")
elif var_fruit == "apple":
    print("It's a grape")
else:
    print("It's not a fruit")


"""Ternary Operator ... if condition else ... keywords"""
# if instead of ? and else instead of :
# And condition is written in the middle after if
# instead at the first
var_day = True
var_result = "Day" if var_day else "Night"
print(var_result)  # Day


"""Single line if condition"""
var_str = "apple"
if var_str == "apple":
    print("It's a apple")
