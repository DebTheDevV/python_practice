# --------------------------
# Notes:
# The 'reduce()' function is used to apply a rolling computation to a sequence.
# It processes the list from left to right and reduces it to a single cumulative value.
# You need to import it from the 'functools' module.
# --------------------------

from functools import reduce

def sum(a, b):
    return a+b 

numbers =[1, 2, 3 , 45 , 4 , 21 ]

# Apply the sum() function cumulatively to the elements of the 'numbers' list
c= reduce(sum , numbers )
print(c) 

# How reduce works here:
# Step 1: 1 + 2 = 3
# Step 2: 3 + 3 = 6
# Step 3: 6 + 45 = 51
# Step 4: 51 + 4 = 55
# Step 5: 55 + 21 = 76