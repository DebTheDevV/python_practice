#find average of 3 numbers


# defining the function:

def average (a , b,  c):
    d = (a+b+c)/3.0
    print(d)
    #this function returns Nothing , ie. None

# calling the function
average(3, 4, 5)  
average (4 , 2 , 1)

#  now , let's say we want to save the value of averages to a new variable

o1=average(3, 4, 5)  
o2=average (4 , 2 , 1) #

print(o1)   # returns None
print(o2) #returns None -> we dont  have anything as value of average (4 , 2 , 1) 



# so instead of printing it in the function , i will ask to return

def averages (a , b,  c):
    d = (a+b+c)/3.0
    return d 

o1= averages( 3 , 4, 5 )
print(o1) # now , it returns a value



