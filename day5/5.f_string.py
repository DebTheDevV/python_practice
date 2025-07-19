#string formatting-
# template = " Dear Harry , You are awesome . Take this 1000$ bag"

template = " Dear {}, You are awesome . Take this {}$ bag"

# now , let's say for different people(with different name) , we have different money , so baar baar likhne se aacha , hum ek template likhe , aur usme values change krte jaye 

a="John"
a1=10000
b="Jack"
b1=1000
c="Marie"
c1=300

s1=template.format(a , a1)
print(s1)


#f-string - a way to simply put variables inside a string
print(f"{a} , you are awesome . So , take this {a1} dollar bag")


name=input("Enter Your name : ")
age = int(input("Enter your age : "))
print(f"Hey {name} , nice to know that you are {age}")
