def sum ( a , b):
    #a and b are local variables , ie. only access them inside function
    c=a+b 
    z=1 # creates a local variable , called z , which is destroyed after this function returns  Therefore this will not change the value of global variable  z
    return c

def greet():
    z=32 #local variable
    print("hello world")
    
z=8  #global variable
print(sum(4 , 6))
# print(c)
print(z)

