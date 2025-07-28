# --------------------------
# Notes:
# This code demonstrates how the 'filter()' function works in Python.
# 'filter()' is used to select elements from a list based on a condition.
# It takes two arguments:
#   1. A function that returns True or False
#   2. An iterable (like a list)
# It returns only those elements for which the function returns True.
# The result is a filter object, which we convert into a list using list().
# --------------------------

def is_greater_than_9(x):
    if (x>9):
        return True 
    else:
        return False
a= [ 1, 3, 5 , 234 , 76 , 8533 , 5 , 89 , 23, 64]

# Using filter() with a named function
# This will keep only elements greater than 9 from the list 'a'
new = list(filter(is_greater_than_9 , a ))

# Using filter() with a lambda (anonymous) function for the same logic
new = list(filter(lambda x : x>9 , a ))

# Print the filtered list containing only elements > 9
print (new)