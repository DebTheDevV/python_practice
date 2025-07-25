n=int(input("Enter n : "))
try:
    a=345/n
except Exception as e:
    print(e)
else:
    print("hey , i am good ") # gets executed when there is no error in the try block
    


# --------------------------
# Notes:
# This code demonstrates the use of `try-except-else` in Python.
# If the division succeeds, the `else` block runs.
# If there's a division error (like dividing by 0), the `except` block handles it.
# --------------------------

n = int(input("Enter n : "))  # Prompt user to enter a number

try:
    a = 345 / n  # Attempt division
except Exception as e:
    print(e)  # Handle any exception and print the error message
else:
    print("hey , i am good ")  # Executed only if no exception occurs in try block