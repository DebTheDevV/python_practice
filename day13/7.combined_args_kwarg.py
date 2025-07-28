# --------------------------
# Notes:
# This function demonstrates how to use both *args and **kwargs together.
# - *args collects extra positional arguments into a tuple.
# - **kwargs collects extra keyword arguments into a dictionary.
# Order matters: *args must come before **kwargs in the function definition.
# --------------------------

# Define a function that accepts any number of positional and keyword arguments
def func(*args , ** kwargs):
    # Print the tuple of all positional arguments passed
    print(args)
    # Print the dictionary of all keyword arguments passed
    print(kwargs)

# Call the function with both positional and keyword arguments
func( 1, 2, 3 , 4, 5, joe = 45 ,  smith = 98)
