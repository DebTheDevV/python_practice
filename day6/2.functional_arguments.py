#positional arguments-
def addition (a , b) :
    return a+b
c= addition(3 , 5)
print(c) # output- 8

#default arguments -

#here the function will run , because the default plus = 0 is htere , if it was an positional argument , it wud have through a error as it wud have expected you to pass an argument
def add (a , b , plus = 0) :
    return a+b+plus
c= add(3 , 5)
print(f"c = {c}")
d= add(3 , 5 , 2) # default value got overridden
print(f"d = {d}")


#now , let's say we want to pass b pehele and a later ...here 
#keyword argument comes in

e=add(b=5 , a= 3) # we r specifying a ayr b kya h
print(f"e = {e}")
   