def decorator(func):
    def wrapper():
        print("I am about to print hello ...")
        func()
        print("I have executed the function")
    return wrapper

@decorator # using this does the same work as decorator(say_hello)

def say_hello():
    print("Hello")

say_hello()



