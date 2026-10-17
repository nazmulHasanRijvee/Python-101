"""format() method"""

# fortmat() and ".2f" lets us print only two digits after decimal point.
# Useful with double data type.
variable = 12.123
print(format(variable, ".2f"))  # 12.12

"""f-string"""
# Using f function :.2f lets us  print the digits
print(f"{variable:.2f}")  # 12.12
