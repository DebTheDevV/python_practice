numbers = [1 ,2 , 3,  4, 5]

# def square(x):
#     return x*x 


# new= list(map(square , numbers))
# print(new)


new= list(map(lambda x : x*x  ))
print(new)
# --------------------------
# Notes:
# This script demonstrates how to use the `map()` function in Python.
# `map()` applies a function to each element in an iterable (like a list).
# It returns a map object, which can be converted to a list to view results.
# This example shows how to use `map()` with both a named function and a lambda.
# --------------------------

numbers = [1, 2, 3, 4, 5]

# Using map with a named function
def square(x):
    return x * x

squared_list = list(map(square, numbers))
print("Squares using named function:", squared_list)

# Using map with a lambda function (inline, anonymous function)
squared_list_lambda = list(map(lambda x: x * x, numbers))
print("Squares using lambda function:", squared_list_lambda)