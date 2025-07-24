# used to enhance or modify existing functions

# decorator is a function that takes a function , it creates a new function inside it's body(wrapper) using the function . Then it returns the new function

def decorator(func):
    def wrapper():
        print("I am about to print hello ...")
        func()
        print("I have executed the function")
    return wrapper

def say_hello():
    print("Hello")

# say_hello()

# here u wont write f=decorator(say_hello()) , take a close look on the paranthesis.. if u write the function with paranthesis , then it  prints hello and returns none , so f basically becomed f=decorator(None) which will return nothing and might give error

""" f will look something like this -
def f():
        print("I am about to print hello ...")
        print("Hello")
        print("I have executed the function")

"""
f=decorator(say_hello)
f()


