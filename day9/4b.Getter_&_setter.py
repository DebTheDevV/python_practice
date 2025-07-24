# to do  it with setter
class Employee :
    def __init__(self , name , salary):
        self.name= name
        self.salary=salary


    @property #built-in decorator  , turns a methos into a read-only attribute... basically python's way to define getter
    def first_name(self):
        return self.name.split(" ")[0]
    
    @first_name.setter
    def first_name(self , first ):
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name=new_name

        
e=Employee("Jack Doe" , 345555)

print(e.first_name) #e.first_name is actually a function but here it is acting like an property
e.first_name="John"
print(e.name)