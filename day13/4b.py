# --------------------------
# Notes:
# This code demonstrates the use of the Walrus Operator (:=) introduced in Python 3.8.
# The Walrus Operator allows you to assign a value to a variable as part of an expression.
# It helps reduce redundancy by:
#   - Avoiding the need to call a function multiple times
#   - Combining assignment and condition checking in a single line
# --------------------------

# Traditional approach: assign input to 'data', then use it in a loop
# data = input("Enter a value (or 'quit' to exit): ")
# while data != 'quit':
#     print(f"You entered: {data}")
#     data = input("Enter a value (or 'quit' to exit): ")

# Walrus operator version:
# Assigns input to 'data' AND checks the condition in the same line
while (data := input("Enter a value (or 'quit' to exit): ")):
    print(f"You entered: {data}")
    if data == 'quit':
        break

# Summary:
# - The expression (data := input(...)) assigns the input to 'data'
# - Then it checks if 'data' is truthy (non-empty string)
# - This helps make code shorter and avoids repeating the input() function