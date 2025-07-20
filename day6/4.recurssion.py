'''
a function calls itself -> we shud use recursion as sometimes it directly solves the problem
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 ..... index

fib(0)=0
fib(1)=1
fib(2)=fib(0)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)
fib(5)=fib(3)+fib(4)

fib(n)=fib(n-2)+fib(n-1)

'''

def fib(n):
    # base case of recurssion - manually define for n= 0 , 1

    if(n==0 or n==1):
        return n 
    
    return fib(n-2)+ fib(n-1)

print(fib(5))   #output= 5
print(fib(6))   #output= 8
print(fib(7))   #output= 13

