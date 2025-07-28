# --------------------------
# Notes:
# This script demonstrates the use of *args in Python.
# *args allows a function to accept any number of positional arguments.
# It collects them into a tuple, which can be looped through and processed.
# Useful when you're not sure how many arguments will be passed to the function.
# --------------------------

# def sum (a , b):
#     return a +b 

# print(sum(342 , 2, 7)) #  put 3 args  instead of 2 


def sum(*args):
    # 'args' is a tuple containing all the arguments passed to the function
    print(args) # here , we will get all the arguments as a tuple
    total = 0 
    # Loop through each number in the tuple and add it to the total
    for item in args :
        total+= item
    return total

print(sum(342 , 3 , 7))
print(sum(342 , 3 , 7 , 670 , 98))
print(sum(1 , 2 , 3 , 5 , 6 , 7))

# *args collects all positional arguments into a tuple, allowing flexibility in function input
