# What id filr i/o and why do we need files in python , // f is a file object
f= open("harry.txt" , 'r')
# also we can do rt(in text files)and rb(binary files read)

content= f.read()
print(content)

f.close()
#Flush and close the IO object.

# This method has no effect if the file is already closed.

# // here we will get filenot found error if we dont have the file from behorehand