"""Dictionary"""
# It is unordered, changeable and does not allow duplicates (has map)
# syntax:
#   dictionary_name = {
#       "key1" : value,
#       "key2" : value,
#   }
# Example, name stu_indo, _ underscore is needed for gap in python.
# Keys are written in quotation (Single or double) and values are assigned
# by : (semicolon) and keys are separated by coma
# prints all the keys and values side by side like this as a list
stu_info = {
    'name' : 'Nazmul',
    'batch' : 47,
    'dept': 'CSE',
    'passing_year': 2027
}
print(stu_info) #  {'name': 'Nazmul', 'batch': 47, ...}

# The key written in [] third bracket will print its value
print(stu_info['batch']) # 47
# 'passing_year' keys value will be printed
print(stu_info['passing_year']) # 2027


"""Changing values of an item or updating it"""
# It changes the value of key 'name' from Nazmul to Sami
stu_info['name'] = 'Sami'


""".update() method"""
# changes the value of keys, or it can add a new key with value
# at the end like appending (if not present)
stu_info.update({
    'dept' : 'BBA',
    'passing_year' : 2024
})
print(stu_info)

# adds a new 'gender' key with value 'male' and appends it
stu_info.update({
    'gender' : 'male'
})
print(stu_info)


""".get() method"""
# used to get a value safely using a Key that might not exist in the
# dictionary and by using the second parameter we can get an initial value
# like 0 and create the Key for later access
dictionary1 = {}
value = dictionary1.get('age', 0) # Key missing, create it with 0
print(value) # 0
dictionary1['age'] = 5
print(dictionary1['age']) # 5

# Otherwise if the Key doesn't exist, and we access it like the traditional
# way it will throw error


""".pop() method (removing value)"""
# removes a key and its value which can be stored in a variable
var_popped = stu_info.pop('name')
print(stu_info) # { 'batch' : 47, 'dept' : 'BBA', ...}
print(var_popped) # Sami


""".popitem() method"""
# automatically deletes the last key and its value and returns which
# can be stored as a tuple in a variable like var_popped
var_popped = stu_info.popitem()
print(var_popped) # ('gender', 'male')


"""del"""
# deletes the key and its value. Simply removes them
del stu_info['batch']
print(stu_info) # {'dept': 'BBA', 'passing_year': 2024}


""".values() method (extra methods)"""
# only prints the values of the keys as a list
print(stu_info.values()) # dict_values(['BBA', 2024])


""".keys() method"""
# prints the keys of the dictionary as a list
print(stu_info.keys()) # dict_keys(['dept', 'passing_year'])


""".items() method"""
# stores or prints keys with their values as a tuple in a list
print(stu_info.items()) # dict_items([('dept', 'BBA'), ('passing_year', 2024)])


"""** operator (dictionary unpacking)"""
# ** operator unpacks dictionary in the serial order
var_dict = {
    "name" : "Nazmul",
    "age" : 23
}
copied_dict = {**var_dict}
print(copied_dict)

# unpacking dictionary for function for parameters or arguments
def info(var_1, var_2):
    print(var_1, var_2)

info(**var_dict)


"""loop with dictionary"""
# 'i' stores each dictionary keys and prints them in a new line
for i in stu_info:
    print(i)

# Here, "i" stores keys and "j" stores values in each iteration.
# They print keys and values in table like manner
for i, j in stu_info.items():
    print(i, '\t', j)


"""Nested dictionary"""
# This works like having a Sub-Key under a Key.
contacts = {
    'name': {
    'phone': '01991407207',
    'email': 'nhasanr18@gmail.com'
    }
}
print(contacts) # {'name': {'phone': '01991407207', 'email': 'nhasanr18@gmail.com'}}

# Using .items() method which returns the Key and Values.
# In this case, Key and Sub-Key is returned, where
# Sub-Key name is used to access the Value like
# dictionary[‘name’][‘email’]
contacts = {
    'name': {
    'phone': '01991407207',
    'email': 'nhasanr18@gmail.com'
    }
}
for name, info in contacts.items():
    print('\nname', name)
    print('Phone', info['phone'])
    print('Email', info['email'])
