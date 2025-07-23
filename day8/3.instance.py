class Employee :
    company = "Asus" #this is a class attribute
    
    def __init__(self , salary , name , bond  , company):
        self.salary = salary 
        self.name = name
        self.bond = bond 
        self.company=company
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the  employee is {self.name}. Salary is {self.salary} and the bond is for {self.bond} years . He works in {self.company}")

e1= Employee(45000 , "john" ,  4 , "Tesla")
print(e1.company) #will always print instance attribute whenever present


print(Employee.company) #this will always print the class attribute

# Object Intrispection - 

print(dir(e1)) # tells about all the attributes and  methods that are present for e1