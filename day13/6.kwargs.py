# --------------------------
# Notes:
# This function demonstrates the use of **kwargs in Python.
# **kwargs lets you pass any number of keyword arguments to a function.
# These arguments are automatically stored as key-value pairs in a dictionary.
# This is useful when you don't know ahead of time how many named arguments will be passed.
# --------------------------
def marks(**kwargs):
    # Loop through each key-value pair in the kwargs dictionary and print the student's name and marks
    for item in kwargs.keys():
        print(f" The marks of {item} is {kwargs[item]}")

marks(shubham = 34 , vikrant= 56 , jack=90 , marie = 78 , priya = 45 )


