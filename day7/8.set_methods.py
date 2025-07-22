s={34 , 23 , 2 , 4  , 22}
print(s)

s.add(32)
print(s)
s.remove(2)
print(s)
# s.remove(43234) ## will give keyerror
s.discard(43234) # dont thru an error if the value is not present, otherwise will remove
s.pop() #removes random element