"""Print Variations in Python"""
# f is a string called f-string that lets write variable in quotation
# using {} curly brackets. It prints the value of variable.
variable = "Nazmul"
print("Hello World")
print(f"This is {variable}")


"""Header alignment"""
# In f string functions { } by writing in this format { :>{10}}
# we can align it.
print(f"{'Key' :>{10}}")
print("-"*20)
# Output:
#        Key
# ------------------
# In this pattern, aligns text or strings with multiple
# variables, with 10 spaces in between
print(f"{'Key':<{10}}{'Value':<{10}}")
print('-'*20)
# Output:
# Key       Value
# --------------------


"""Improved f-string Python 3.12"""
# Debug f-strings (VERY useful) like f"{x=}". It's super helpful for debugging
# (no need to type variable name manually)
x = 10
print(f"{x = }") # x = 10

# Before, f-strings had limitations but now complex expressions can be written
# directly inside third parentheses {}
user = "Nazmul"
print(f"{user.upper() = }") # user.upper() = "NAZMUL"

# Multi-line and cleaner formatting using f"""..."""
name = "Nazmul"
age = 22
text = f"""
Name: {name}
Age: {age}
"""
print(f"{text}") # Name: Nazmul
                 # Age: 22


"""Use modern f-string features when"""
# Debugging -> f"{var=}"
# Cleaner logs -> f"{value=:.2f}"
# inline logic -> f"{x*2}"


"""Extra things like f-string"""
# Raw strings using r"..."
print(r"C:\new_folder")

# Byte strings using b"..."
data = b"hello"
print(data)