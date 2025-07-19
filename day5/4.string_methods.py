name = "Harry"
# strings are immutable ,ie if we use some function to change the string, it actually forms a new string . The actual string remains unchanged in memory

# name[0] ="R"  
#you cannot do this  , here we will get a runtime error 


a=len(name) # shows the length of the string
print(a)

s="hellO wOrld" 
a = len(s)
print(a)
print(s.upper() , s) 
# here - output- HELLO WORLD hello world
# this is inmutability in action. , the original string remains unchanged , but the s.upper() did it's work
print(s.lower()) # sabko lower mei kr do
print(s.capitalize()) #convert the first char of string to uppercase , ie . just H
print(s.title()) # first char of every word will be changed to upper case

text=" hello world "
print(text.strip())#output:"hello world" ie , removes leading and trailing whitespaces from a string
print(text.lstrip())#output:"hello world "  , removes leading whitespace(left of the string)
print(text.rstrip())#output:" hello world"  , removes tailing whitespace(write of the string)

#removes whitespace , \n , \t , \r , \f , \v... also u can specify , for eg ....  s.strip(/) , this will remove all / from the string

s = " \n\t hello world \n"
print(s.strip())   # "hello world"
print(s.lstrip())  # "hello world \n"
print(s.rstrip())  # " \n\t hello world"

s = "//hello// "
print(s.strip("/"))

texts= "Python is fun and fun and fun"
#       01234567
print(texts.find("is")) #output is 7  
print(texts.replace('fun' , 'awesome'))

fruits = "Apples,Bananas,Pineapples"
print(fruits.split(","))  #output is a list..
print(",".join([' Apples', 'Bananas', 'Pineapples ']))

python="Python123"
print(python.isalpha())#kya is mei saare alphabets h ?? - False
print(python.isdigit())#kya is mei saare numbers h ?? - False
print(python.isalnum())#kya is mei saare alphabets  and numbers h ?? - True
print(python.isspace())#kya is mei saare space h ?? - False






