# --------------------------
# Notes:
# This script demonstrates how to use the Walrus Operator (:=) in Python.
# The Walrus Operator allows assignment and condition checking in a single line.
# It is useful for avoiding redundant function calls or repetitive code.
# Introduced in Python 3.8.
# --------------------------

# Define a function that simulates a time-consuming task
def very_slow_func():
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    return 70

# ❌ This would call the slow function twice (uncommenting would run it twice):
# if(very_slow_func() > 10):
#     print(very_slow_func())
# else:
#     print("It is not greater than 10")

# ✅ Instead, we assign the result to a variable first to avoid duplicate calls
a = very_slow_func()
if a > 10:
    print(a)
else:
    print("It is not greater than 10")

# ✅ Using the Walrus Operator to do assignment and comparison in one line
# This calls the function only once and stores its result in 'a'
if (a := very_slow_func()) > 10:
    print(a)
else:
    print("It is not greater than 10")
