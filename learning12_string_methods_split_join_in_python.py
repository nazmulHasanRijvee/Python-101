"""String methods in python"""

""".capitalize()"""
# .capitalize() makes the first word 'my' in sentence capital
var1 = "my name is Nazmul"
print(var1.capitalize())  # My ...


""".lower() and .upper()"""
# These methods convert all letters into small or capital letters/case
var2 = input("Enter a string: ").lower()
var3 = input("Enter a string: ").upper()
print(var2, var3)  # boat RICe


""".title()"""
# makes the first letter capital of every word
var4 = "my name is Nazmul"
print(var4.title())  # My Name Is Nazmul


"""len() method"""
# prints how many elements are in the string or list. Simpy the length
var5 = "Hello"
print(len(var5))  # 5


""".endswith()"""
# method matches with the strings ending letters such as 'hello's 'lo' part
# If it matches the output then true otherwise false
var6 = "Hello"
print(var6.endswith("lo"))  # True


""".count()"""
# method counts a letter such as 'l' is repeating how many times in 'hello'
var7 = "Hello"
print(var7.count("l"))  # 2


""".find()"""
# method finds the element 'a' in the string and shows it's index value.
# The first one it finds it displays it
var8 = "watermark"
print(var8.find("watermark"))


""".replace()"""
# method replaces the first letter in replace('r', 'l') with second letter
# 'l'. We can also replace only one 'r' if there are multiple same elements
# using replace('r', 'l', 1)
var9 = "Harry"
print(var9.replace("r", "l"))  # Hally
print(var9.replace("r", "l", 1))  # Halry


""".split()"""
# method by default splits the words in a string at space (_)
# and returns a list of words.
var10 = "Welcome to the jungle"
var10 = var10.split()
print(var10)  # ['Welcome, 'to', 'the', 'jungle']

# We can also customize it so it splits the string at '*'
var11 = "Welcome*to*the*jungle"
var11 = var11.split("*")
print(var11)


""".strip() method"""
# method removes unnecessary spaces or tabs in front or after a string
# (\t or \n)
var12 = "Welcome "
print(var12.strip())  # Welcome

# we can also filter out empty lines or elements by using .strip()
# method in if statement
list1 = ["\n", "Hi"]
for i in list1:
    if i.strip():
        print(i)  # Hi

# And .strip() method can also be used for removing any extra spaces
# after string slicing
string = "a b"
string = string[:3].strip()
print(string)  # a


""".join()"""
# method allows to join the split words into one or tuples into one.
# " " in quotation whatever is written will be in between the joints
var_list = ["Welcome", "to", "the", "jungle"]
tuple_var = ("Welcome", "to", "the", "tuple")
var13 = " ".join(var_list)
var14 = " ".join(tuple_var)
print(var14)  # Welcome to the jungle, Welcome to the tuple


"""for loop with string"""
# Here for-loop automatically iterates over the string from
# left to right. In the for-loop every character in string
# is given in each iteration (ch)
var_str = "Hello!"
for ch in var_str:
    print(ch)
