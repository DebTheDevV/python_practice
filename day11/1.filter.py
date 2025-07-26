def is_greater_than_9(x):
    if x>9 :
        return True
    else: 
        return False
    
a=[1 ,3 ,5 , 234 , 34 , 32,6543 , 23 , 6 ,7. ,43]

new=list(filter(is_greater_than_9 , a))
print(new)
new= list(filter(lambda x: x>9 , a))
# --------------------------
# Notes:
# This script demonstrates how to use the `filter()` function in Python.
# `filter()` is used to extract elements from a list that satisfy a certain condition.
# It takes two arguments: a function and an iterable.
# The function should return True for elements you want to keep.
# --------------------------

# Function that returns True if the input is greater than 9
def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False

# Original list
a = [1, 3, 5, 234, 34, 32, 6543, 23, 6, 7, 43]

# Using filter with a named function
new = list(filter(is_greater_than_9, a))
print("Filtered using named function:", new)

# Using filter with a lambda function (more concise)
new = list(filter(lambda x: x > 9, a))
print("Filtered using lambda function:", new)