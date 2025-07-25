a= int(input("enter number 1: "))
b= int(input("enter number 2: "))

if (b==0):
    raise ValueError("please dont divide by 0")

print(f'the division is {a/b}')
# --------------------------
# Notes:
# This code demonstrates how to raise a custom error using `raise`.
# It manually raises a ValueError when attempting to divide by 0.
# Helps in preventing runtime crashes by proactively handling invalid inputs.
# --------------------------

a = int(input("enter number 1: "))  # Take first integer input from user
b = int(input("enter number 2: "))  # Take second integer input from user

if (b == 0):
    raise ValueError("please dont divide by 0")  # Manually raise error if denominator is zero

print(f'the division is {a/b}')  # Perform and print the division if safe