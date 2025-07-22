marks = [5, 2, 21, 5, 7]
print(marks[3])
extra_marks = [6, 18, 20]

# Copying lists properly
a = marks.copy() #Returns a copy
b = marks.copy()
c = marks.copy()
d = marks.copy()
e = marks.copy()
f = marks.copy()
g = marks.copy()

marks.append(63) #adds at the end of list
print("append:", marks)

marks.pop() #takes index at argument , and deletes the  value at that argument ... ; deletes item at last if no index is given 
print("pop:", marks)

marks.extend(extra_marks) #extends the table
print("extend:", marks)

a.clear() #returns a empty list
print("clear:", a)

copied_list = b.copy() #shallow copy
print("copy:", copied_list)

index_of_21 = c.index(21) #returns the index of the value
print("index:", index_of_21)

d.insert(0, 23) #  u need to tell at what index , u r inserting what
print("insert:", d)

e.remove(21) #removes the object from the list
print("remove:", e)

f.reverse() #reverses the list
print("reverse:", f)

g.sort()#it sorts the list in ascending order
print("sort:", g)

