a={ 3 , 23 , 1 , 56 }
b={23 , 3 , 4 , 2 , 55 , 1}

c=a.union(b) # create a set with all the eelements of a and b
print(c)


d=a.intersection(b)
print(d)

e=b.intersection(a)
print(e)

f=a.difference(b)
print(f)