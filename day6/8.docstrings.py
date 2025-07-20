def sum(a , b):
    """ This will sum two numbers """
    return a+b


# this might look like a regular comment , but when it is written in triple quotes just after the def function name then it is also considered as a docstring , and can be accessed as follows

print(sum.__doc__)


def add (a , b) :
    """
    Returns the sum of two numbers

    Paramters:
    a(int) : The first number 
    b(int) : The second number

    returns:
    int: The sum of Two numbers
    """
    return a+b

print(add(3+4))
print(add.__doc__)

