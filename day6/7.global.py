#excesive use of global variable is discouraged
def sum(a,b):
    print("hey I am adding")
    c = a+b 
    global z #please modify global z , this will refer to the gloval variable z , and not the local variable
    z=0
    return c 

z=3
print("before:"  , z)

print(sum(3 , 12))
print(f"After calling function , z is {z}")