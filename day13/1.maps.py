# --------------------------
# Notes:
# This script demonstrates how to use the 'map()' function in Python.
# - 'map()' takes a function and an iterable (like a list).
# - It applies the function to each element of the iterable.
# - The result is a map object, which we convert to a list to view the results.
# Two examples are shown:
#   1. Using a named function called 'square'
#   2. Using a lambda (anonymous) function
# --------------------------
numbers =[1, 2, 3 , 45 , 4 , 21 ]

def square (x):
    return x*x ;

# 'map()' applies a function to every element in the list.
# By default, it returns a map object, so we convert it to a list using 'list()'.
new= list(map(square , numbers)) # map by default returns a map object , so for changing it , we need to type cast it
print(new)

# Instead of defining a separate function, we can use a lambda (anonymous) function.
# This version is shorter and more readable for simple one-line operations.
new= list(map(lambda x : x*x  , numbers))  #readable and usinf less lines of code