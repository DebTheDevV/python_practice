def repeat(n): # n is the no. of times i want to repeat that function
    def decorator(func):
        def wrapper(a): #a is nothing but function's argument
            for i in range(n): # since i want it to repeat n times
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f'Hello {a}')

"""
what this decorator actually does:
    for i in range(7): 
        say_hello("harry")

"""

say_hello("harry")



