"""Global keyword with function"""

# global keyword is used for accessing a top-level variable (outside
# any class or function) locally in a class or method
# We can use this for shared or variable value across different
# classe and methods

# global keyword allows a class or function to modify that variable
# rather than creating a new local one. It can also be used inside
# a class or function to create a new variable in the global scope
# if it does not already exist
img_path = None


def get_path():

    global img_path
    # Code ...
    return img_path


def set_img_path(path):

    global img_path
    # Code ...
    img_path = path


# NOTE: but this not in methods inside classes because self. already
# gives access to the outside variables of the method
